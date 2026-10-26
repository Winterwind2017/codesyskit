"""Compiler-log judging: the engine reports to stderr, so the kit parses that."""

import pytest

from codesyskit.service import Service

SAMPLE = """编译: Text: C0: ------ 开始构建应用程序 PLC.Application -------
编译: Text: C0: 代码典型化...
编译: Error: C189: 应该用';' 替换'IS'
编译: Warning: C139: 代码'THIS;\\n'不可能执行到.这是有目的的吗？
编译: Error: C9: 发现非预期的记号'NOT'
附加代码检查: Text: SA0: 其他代码检查...
编译: Text: C0: 编译完成--12错误,2警告
"""

CLEAN = """编译: Text: C0: ------ 开始构建应用程序 PLC.Application -------
编译: Text: C0: 代码典型化...
编译: Text: C0: 编译完成 -- 0错误,0警告
"""


def test_parses_errors_and_warnings():
    parsed = Service.parse_engine_log(SAMPLE)
    assert parsed["ok"] is False
    assert parsed["errors"] == 12          # the summary is authoritative
    assert parsed["warnings"] == 2
    codes = [item["code"] for item in parsed["messages"]]
    assert "C189" in codes and "C9" in codes
    assert parsed["summary"] == {"errors": 12, "warnings": 2}


def test_clean_build_is_ok():
    parsed = Service.parse_engine_log(CLEAN)
    assert parsed["ok"] is True
    assert parsed["errors"] == 0 and parsed["warnings"] == 0
    assert parsed["messages"] == []


def test_empty_log_is_ok_but_silent():
    parsed = Service.parse_engine_log("")
    assert parsed["ok"] is True
    assert parsed["summary"] is None


def test_message_shape():
    parsed = Service.parse_engine_log(SAMPLE)
    first = parsed["messages"][0]
    assert set(first) == {"category", "severity", "code", "text"}
    assert first["category"] == "编译"
    assert first["severity"] == "Error"
    assert first["text"].startswith("应该用")


def test_summary_without_spaces():
    parsed = Service.parse_engine_log("编译: Text: C0: 编译完成--3错误,0警告")
    assert parsed["errors"] == 3 and parsed["ok"] is False
