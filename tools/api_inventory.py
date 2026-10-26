"""Inventory the CODESYS scripting API from the shipped type stubs.

The engine documents itself: ``<install>\\CODESYS\\ScriptLib\\Stubs\\scriptengine\\*.pyi`` holds one
stub per module with signatures **and** docstrings. This tool turns them into machine-readable
JSON plus a readable summary, so the kit (and an agent) can answer "what else can be automated?"
without guessing.

    python tools/api_inventory.py                  # default install path
    python tools/api_inventory.py --stubs <dir> --out recon

Outputs:
    recon/api_catalog.json   every module / class / method / property with its doc summary
    docs/API-SURFACE.md      grouped summary + counts, regenerated each run
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_STUBS = r"D:\Program Files\CODESYS 3.5.22.20\CODESYS\ScriptLib\Stubs\scriptengine"

CLASS_RE = re.compile(r"^class\s+([A-Za-z_]\w*)\s*(?:\((.*?)\))?\s*:")
DEF_RE = re.compile(r"^def\s+([A-Za-z_]\w*)\s*\((.*)\)\s*(?:->\s*(.*?))?\s*:$")
ATTR_RE = re.compile(r"^([A-Za-z_]\w*)\s*:\s*(.+?)\s*$")
DOC_QUOTES = ('"""', "'''")

NOTABLE = (
    "login", "logout", "download", "upload", "start", "stop", "reset", "read_value",
    "read_values", "set_prepared_value", "write_prepared_values", "create_pou", "build",
    "create_task_configuration", "create_task", "export_xml", "import_xml", "export_native",
    "import_native", "save_archive", "save_as", "save_as_compiled_library", "compare_to",
    "generate_runtime_system_files", "import_device", "import_vendor_description",
    "get_all_devices", "create_symbol_configuration", "find", "remove", "rename", "move",
)


def read_docstring(lines, index):
    """Return (text, next_index) for a docstring starting at ``lines[index]``."""
    line = lines[index].strip()
    quote = line[:3]
    body = line[3:]
    parts = []
    if body.endswith(quote) and len(body) >= 3:
        parts.append(body[:-3])
        return " ".join(parts).strip(), index + 1
    parts.append(body)
    index += 1
    while index < len(lines):
        inner = lines[index]
        if inner.strip().endswith(quote):
            parts.append(inner.strip()[:-3])
            index += 1
            break
        parts.append(inner)
        index += 1
    text = " ".join(part.strip() for part in parts if part.strip())
    return re.sub(r"\s+", " ", text).strip(), index


def parse_stub(path):
    with open(path, encoding="utf-8", errors="replace") as handle:
        lines = handle.read().splitlines()

    classes = []
    module_doc = ""
    current_class = None
    current_member = None
    index = 0

    def attach_doc(text):
        """Docstrings follow the definition they describe, so attach to the newest target."""
        nonlocal module_doc
        if current_member is not None and not current_member.get("doc"):
            current_member["doc"] = text
        elif current_class is not None and not current_class.get("doc"):
            current_class["doc"] = text
        elif not module_doc:
            module_doc = text

    while index < len(lines):
        raw = lines[index]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            index += 1
            continue
        if stripped.startswith(DOC_QUOTES):
            text, index = read_docstring(lines, index)
            attach_doc(text)
            continue

        match = CLASS_RE.match(stripped)
        if match:
            current_class = {"name": match.group(1), "bases": (match.group(2) or "").strip(),
                             "doc": "", "methods": [], "properties": [], "attributes": []}
            classes.append(current_class)
            current_member = None
            index += 1
            continue

        if current_class is not None and stripped == "@property":
            current_member = {"kind": "property", "name": None, "signature": "",
                              "returns": "", "doc": ""}
            index += 1
            continue

        if current_class is not None and stripped.startswith("def "):
            signature_lines = [stripped]
            # a signature may wrap over several lines until the closing ':' at depth 0
            while not (signature_lines[-1].endswith(":")
                       and signature_lines[-1].count("(") == signature_lines[-1].count(")")):
                index += 1
                if index >= len(lines):
                    break
                signature_lines.append(lines[index].strip())
                if len(signature_lines) > 40:      # safety valve
                    break
            signature = " ".join(signature_lines)
            match = DEF_RE.match(signature)
            if match:
                name, params, returns = match.groups()
                entry = {"name": name, "signature": params.strip(),
                         "returns": (returns or "").strip(), "doc": ""}
                if current_member is not None and current_member.get("kind") == "property":
                    current_class["properties"].append(entry)
                else:
                    current_class["methods"].append(entry)
                current_member = entry
            index += 1
            continue

        if current_class is not None:
            match = ATTR_RE.match(stripped)
            if match and not stripped.startswith(("pass", "return")):
                name, type_text = match.groups()
                current_class["attributes"].append({"name": name, "type": type_text,
                                                    "doc": ""})
                current_member = current_class["attributes"][-1]
                index += 1
                continue

        index += 1

    return {"classes": classes, "doc": module_doc}


def build_catalog(stubs_dir):
    modules = {}
    for name in sorted(os.listdir(stubs_dir)):
        if not name.endswith(".pyi"):
            continue
        try:
            modules[name[:-4]] = parse_stub(os.path.join(stubs_dir, name))
        except Exception as exc:  # noqa: BLE001 - one bad stub must not stop the inventory
            modules[name[:-4]] = {"error": str(exc), "classes": [], "doc": ""}

    totals = {"modules": len(modules), "classes": 0, "methods": 0, "properties": 0,
              "attributes": 0}
    # cross-check against the raw text: stubs contain 1395 ``def`` lines, of which the ones
    # below an ``@property`` are accessors rather than plain methods.
    raw = {"classes": 0, "defs": 0, "property_markers": 0}
    for name in sorted(os.listdir(stubs_dir)):
        if not name.endswith(".pyi"):
            continue
        text = open(os.path.join(stubs_dir, name), encoding="utf-8", errors="replace").read()
        raw["classes"] += len(re.findall(r"^class\s+[A-Za-z_]\w*", text, re.M))
        raw["defs"] += len(re.findall(r"^\s+def\s+[A-Za-z_]\w*\s*\(", text, re.M))
        raw["property_markers"] += len(re.findall(r"^\s+@property", text, re.M))
    for module in modules.values():
        for cls in module.get("classes", []):
            totals["classes"] += 1
            totals["methods"] += len(cls.get("methods", []))
            totals["properties"] += len(cls.get("properties", []))
            totals["attributes"] += len(cls.get("attributes", []))
    return {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "stubs_dir": stubs_dir,
        "totals": totals,
        "raw_text_totals": raw,
        "modules": modules,
    }


def render_markdown(catalog, out_path):
    totals = catalog["totals"]
    lines = [
        "# CODESYS scripting API surface",
        "",
        "Generated from the shipped type stubs by `tools/api_inventory.py` "
        "(`%s`)." % catalog["stubs_dir"],
        "",
        "**%d modules / %d classes / %d plain methods / %d property accessors**"
        % (totals["modules"], totals["classes"], totals["methods"],
           totals["properties"]),
        "",
        "Cross-check against the raw text: %d `class` lines, %d `def` lines, %d `@property`"
        % (catalog.get("raw_text_totals", {}).get("classes", 0),
           catalog.get("raw_text_totals", {}).get("defs", 0),
           catalog.get("raw_text_totals", {}).get("property_markers", 0)),
        "(a `def` under `@property` is an accessor, so callables = methods + accessors).",
        "",
        "Every row below is a real signature found in a `.pyi` file; nothing here is inferred.",
        "The machine-readable version is `recon/api_catalog.json`.",
        "",
        "## Modules by size",
        "",
        "| module | classes | methods | properties | notable methods |",
        "| --- | --- | --- | --- | --- |",
    ]
    rows = []
    for name, module in catalog["modules"].items():
        classes = module.get("classes", [])
        method_count = sum(len(c.get("methods", [])) for c in classes)
        prop_count = sum(len(c.get("properties", [])) for c in classes)
        notable = []
        for cls in classes:
            for method in cls.get("methods", []):
                if method["name"] in NOTABLE:
                    notable.append("%s.%s" % (cls["name"], method["name"]))
        rows.append((len(classes), method_count, prop_count, name, notable[:4]))
    rows.sort(reverse=True)
    for class_count, method_count, prop_count, name, notable in rows:
        lines.append("| `%s` | %d | %d | %d | %s |"
                     % (name, class_count, method_count, prop_count,
                        ", ".join("`%s`" % item for item in notable) or ""))

    lines += ["", "## Method index", ""]
    for name in sorted(catalog["modules"]):
        module = catalog["modules"][name]
        classes = module.get("classes", [])
        if not classes:
            continue
        lines.append("### `%s`" % name)
        if module.get("doc"):
            lines += ["", "> %s" % module["doc"][:300]]
        lines.append("")
        for cls in classes:
            header = "**%s**" % cls["name"]
            if cls.get("bases"):
                header += " (%s)" % cls["bases"]
            lines.append("- %s" % header)
            if cls.get("doc"):
                lines.append("  - %s" % cls["doc"][:280])
            for method in cls.get("methods", []):
                signature = "%s(%s)" % (method["name"], method["signature"])
                doc = method.get("doc", "")
                lines.append("  - `%s`%s" % (signature, (" — " + doc[:160]) if doc else ""))
            for prop in cls.get("properties", []):
                lines.append("  - `%s` *(property)*%s"
                             % (prop["name"], (" — " + prop["doc"][:160]) if prop.get("doc")
                                else ""))
        lines.append("")

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")
    return out_path


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--stubs", default=os.environ.get("CODESYSKIT_STUBS", DEFAULT_STUBS))
    parser.add_argument("--out", default=os.path.join(ROOT, "recon"))
    args = parser.parse_args(argv)

    if not os.path.isdir(args.stubs):
        print("stubs not found: %s" % args.stubs)
        return 2
    os.makedirs(args.out, exist_ok=True)
    catalog = build_catalog(args.stubs)
    json_path = os.path.join(args.out, "api_catalog.json")
    with open(json_path, "w", encoding="utf-8") as handle:
        json.dump(catalog, handle, ensure_ascii=False, indent=1)
    md_path = render_markdown(catalog, os.path.join(ROOT, "docs", "API-SURFACE.md"))
    totals = catalog["totals"]
    print("wrote %s" % json_path)
    print("wrote %s" % md_path)
    print("%d modules / %d classes / %d methods / %d properties / %d attributes"
          % (totals["modules"], totals["classes"], totals["methods"],
             totals["properties"], totals["attributes"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
