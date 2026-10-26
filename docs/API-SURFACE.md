# CODESYS scripting API surface

Generated from the shipped type stubs by `tools/api_inventory.py` (`D:\Program Files\CODESYS 3.5.22.20\CODESYS\ScriptLib\Stubs\scriptengine`).

**50 modules / 260 classes / 636 plain methods / 733 property accessors**

Cross-check against the raw text: 262 `class` lines, 1395 `def` lines, 737 `@property`
(a `def` under `@property` is an accessor, so callables = methods + accessors).

Every row below is a real signature found in a `.pyi` file; nothing here is inferred.
The machine-readable version is `recon/api_catalog.json`.

## Modules by size

| module | classes | methods | properties | notable methods |
| --- | --- | --- | --- | --- |
| `ScriptApplicationComposer` | 29 | 36 | 154 |  |
| `dotNETs` | 25 | 9 | 1 |  |
| `ScriptOnline` | 19 | 67 | 44 | `ScriptOnlineApplication.login`, `ScriptOnlineApplication.logout`, `ScriptOnlineApplication.start`, `ScriptOnlineApplication.stop` |
| `ScriptProject` | 14 | 43 | 16 | `ScriptProject.save_as`, `ScriptProject.save_archive`, `ScriptProject.export_xml`, `ScriptProject.export_native` |
| `ScriptDeviceParameters` | 14 | 30 | 62 |  |
| `ScriptUserManagement` | 13 | 32 | 35 | `ScriptUserManagement.login`, `ScriptUserManagement.logout`, `ScriptUser.remove`, `ScriptUser.rename` |
| `ScriptDeviceObject` | 12 | 38 | 25 |  |
| `ScriptLibManObject` | 12 | 34 | 40 |  |
| `ScriptSystem` | 12 | 29 | 37 |  |
| `ScriptSymbolConfigObject` | 12 | 21 | 31 | `ScriptSymbolConfigSignatureCollection.find` |
| `ScriptTaskConfigObject` | 7 | 19 | 18 | `ScriptTaskConfigObject.create_task`, `ScriptPouObjectCollection.remove` |
| `ScriptDeviceUserManagement` | 6 | 27 | 12 | `ScriptDeviceUserManagement.upload`, `ScriptDeviceUserManagement.download`, `ScriptDeviceUserList.remove`, `ScriptDeviceGroupList.remove` |
| `ScriptImagePoolObject` | 6 | 15 | 10 | `ScriptImagePoolItems.remove`, `ScriptImagePoolItems.move` |
| `ScriptIecLanguageObjectContainer` | 6 | 12 | 8 | `ScriptIecLanguageObjectContainer.create_pou` |
| `ScriptDeviceDescription` | 6 | 2 | 27 |  |
| `ScriptObject` | 5 | 26 | 36 | `ScriptObject.rename`, `ScriptObject.remove`, `ScriptObject.move`, `ScriptObject.move` |
| `ScriptTextListObject` | 5 | 20 | 5 | `ScriptTextListItemsCollection.remove` |
| `ScriptLiveDeviceUserManagement` | 5 | 17 | 11 | `ScriptLiveDeviceUserManagement.upload` |
| `ScriptExternalFileObject` | 5 | 7 | 7 |  |
| `ScriptProjects` | 5 | 5 | 20 |  |
| `ScriptDeviceRepository` | 4 | 28 | 8 | `ScriptDeviceRepository.import_device`, `ScriptDeviceRepository.import_vendor_description`, `ScriptDeviceRepository.get_all_devices`, `ScriptDeviceRepository.get_all_devices` |
| `ScriptTextualObject` | 3 | 6 | 5 | `ScriptTextDocument.remove` |
| `ScriptCasScriptProjectExtension` | 3 | 5 | 9 |  |
| `ScriptCasEdgeGatewayManager` | 2 | 13 | 33 |  |
| `ScriptDriverInfo` | 2 | 12 | 11 |  |
| `ScriptApplication` | 2 | 7 | 4 | `ScriptApplication.build`, `ScriptApplication.create_task_configuration` |
| `ScriptExplicitConnectorObjects` | 2 | 7 | 2 |  |
| `ScriptCasEnums` | 2 | 0 | 0 |  |
| `ScriptTraceEditorObject` | 1 | 12 | 3 | `ScriptTraceEditorObject.download`, `ScriptTraceEditorObject.start`, `ScriptTraceEditorObject.stop` |
| `ScriptTraceVariableList` | 1 | 12 | 0 | `ScriptTraceVariableList.remove`, `ScriptTraceVariableList.remove`, `ScriptTraceVariableList.remove` |
| `ScriptTraceDiagramVariableCollection` | 1 | 12 | 0 | `ScriptTraceDiagramVariableCollection.remove`, `ScriptTraceDiagramVariableCollection.remove`, `ScriptTraceDiagramVariableCollection.remove` |
| `ScriptTraceDiagramCollection` | 1 | 12 | 0 | `ScriptTraceDiagramCollection.remove`, `ScriptTraceDiagramCollection.remove`, `ScriptTraceDiagramCollection.remove` |
| `ScriptAutomationServer` | 1 | 7 | 4 |  |
| `ScriptCasCredentialsManager` | 1 | 5 | 0 |  |
| `ScriptTreeObject` | 1 | 3 | 3 | `ScriptTreeObject.find` |
| `ScriptTraceObject` | 1 | 2 | 16 |  |
| `ScriptAxisSettings` | 1 | 1 | 13 |  |
| `ScriptTraceDiagram` | 1 | 1 | 7 |  |
| `ScriptCasOptionsManager` | 1 | 1 | 2 |  |
| `ScriptDriverTraceImpl` | 1 | 1 | 0 |  |
| `ScriptTraceVariable` | 1 | 0 | 10 |  |
| `ScriptFontDesc` | 1 | 0 | 2 |  |
| `ScriptTraceDiagramVariable` | 1 | 0 | 1 |  |
| `IScriptTraceObjectMarker` | 1 | 0 | 1 |  |
| `TriggerState` | 1 | 0 | 0 |  |
| `TriggerEdge` | 1 | 0 | 0 |  |
| `Resolution` | 1 | 0 | 0 |  |
| `PacketState` | 1 | 0 | 0 |  |
| `GraphType` | 1 | 0 | 0 |  |
| `AxisScaleMode` | 1 | 0 | 0 |  |

## Method index

### `AxisScaleMode`

> | The axis range is determined based on the range of the data | (For the time axis: the latest content of the runtime system | buffer, for y-axes: a range that is large enough to show all | values.)

- **AxisScaleMode** (Enum)
  - | The possible scale modes of an axis.

### `GraphType`

> | None.

- **GraphType** (Enum)
  - | Used for ScriptTraceVariable.graph_type. Defines the appearence of a variable in the diagram.

### `IScriptTraceObjectMarker`

- **IScriptTraceObjectMarker** (object)
  - | This is added to every IScriptObject, | so the check wether it is a valid trace object can be executed on every IScriptObject.
  - `is_trace_object` *(property)* — | Wether the object is a valid trace object.

### `PacketState`

> | The trace packet is currently disabled

- **PacketState** (Enum)
  - | The configuration of a trace packet is incomplete

### `Resolution`

- **Resolution** (Enum)
  - | This enumeration is used to identify the resolution of the trace.

### `ScriptApplication`

- **ScriptApplicationMarker** (object)
  - Marker object to check whether a ScriptObject is an application object. :version added: 3.5.2.0
  - `is_application` *(property)* — Gets a value indicating whether this :class:`ScriptApplicationMarker` is an application. :rtype: bool :returns: ``True`` if it is an application; otherwise, ``F
- **ScriptApplication** (ScriptApplicationMarker)
  - ScriptObjects which are an application object are extended with this interface. :version added: 3.5.2.0
  - `build(self)` — Builds the application. You can use the :meth:`.System.get_messages` and :meth:`.System.get_message_objects` calls to check whether any messages were added. Thi
  - `clean(self)` — Cleans the application. You can use the :meth:`.System.get_messages` and :meth:`.System.get_message_objects` calls to check whether any messages were added. Thi
  - `generate_code(self)` — Generates the code for the application. You can use the :meth:`.System.get_messages` and :meth:`.System.get_message_objects` calls to check whether any messages
  - `rebuild(self)` — Rebuilds the application. You can use the :meth:`.System.get_messages` and :meth:`.System.get_message_objects` calls to check whether any messages were added. T
  - `create_boot_application(self, output_filename)` — Creates the offline boot project at the specified outputpath. Relative output filenames are interpreted relative to the location of the project. If you pass Non
  - `create_boot_application(self, output_filename, update_compile_info=False, write_visu_files=False)` — Creates the offline boot project at the specified outputpath. If the project was changed since the last download or online change to a PLC, and you create a boo
  - `create_task_configuration(self)` — Add the task configuration object to an application. :version added: 3.5.10.0 :rtype: :class:`.ScriptTaskConfigObject` :returns: Script object of the task confi
  - `is_active_application` *(property)* — Gets a value indicating whether this. :class:`ScriptApplication` is the active application. The active application is always in the primary project, so this pro
  - `is_uptodate` *(property)* — Gets a value indicating whether this application is the same running on the PLC. :version added: 3.5.10.0 :rtype: bool :returns: ``True`` if it is the same; oth
  - `is_online_change_possible` *(property)* — Gets a value indicating whether an online change is possible or not. :version added: 3.5.10.0 :rtype: bool :returns: ``True`` if online change is possible; othe

### `ScriptApplicationComposer`

- **ScriptModuleRepository** (object)
  - An instance of an object implementing this interface is injected into the scriptengine scope under the name "modulerepository".
  - `get_toplevel_instances(self)` — Gets all Toplevel-Module-Instances of the primary project. :rtype: list :returns: Returns all Toplevel-Module-Instances of the primary project.
  - `get_all_instances(self)` — Gets all Module-Instances of the primary project. :rtype: list :returns: Returns all Module-Instances of the primary project.
  - `get_toplevel_modules(self)` — Gets all Toplevel-Modules available in the primary project. :rtype: list :returns: Returns all Toplevel-Modules available in the primary project.
  - `get_all_modules(self)` — Gets all Modules available in the primary project. :rtype: list :returns: Returns all Modules available in the primary project.
  - `find_module(self, stQualifiedName)` — Finds the module with its declaration at the given qualified path (namespace.modulename). :type stQualifiedName: str :param stQualifiedName: The qualified path 
  - `get_compatible_modules(self, slot)` — Gets all modules which are compatible to a specified slot. :type slot: ScriptModuleSlot :param slot: The slot for which comaptible modules shall be searched. :r
  - `add_toplevel_instance(self, stInstanceName, scriptMd)` — Adds a toplevel instance to the module tree. :type stInstanceName: str :param stInstanceName: The desired name for the toplevel instance. :type scriptMd: Script
  - `add_submodule_instance(self, stInstanceName, scriptMd, scriptSlot, index)` — Adds a submodule instance to the module tree under the specified slot. The slot has to have an ownership of type submodule, otherwise the operation will return 
  - `add_reference_instance(self, scriptObj, scriptSlot, index)` — Adds a reference instance to the module tree under the specified slot. The slot has to have an ownership of type reference, otherwise the operation will return 
  - `set_generator(self, stGenGuid, bEnable)` — Enables generators in the generator settings. :type stGenGuid: str :param stGenGuid: The string representation of Guid of the generator, which shall be enabled.
  - `load_wildcard_setting(self, stFileName)` — Loads a specific XML file into the wildcard options dialog. :type stFileName: str :param stFileName: The file to be loaded into the wildcard dialogs settings. I
  - `create_module_declaration_object(self, stDeclObjectName, stDeclObjectText)` — Adds a module declaration object to the POU-Pool. :type stDeclObjectName: str :param stDeclObjectName: The name of the module declaration object. :type stDeclOb
  - `generate(self)` — Generate an IEC-Application from configured module instance tree. :rtype: bool :returns: Returns ``True`` in case of success.
  - `scan_all_modules(self)` — Scans all available module declarations. :rtype: bool :returns: Returns ``True`` in case of no error.
  - `generate_and_login(self)` — Generates the IEC-Application from the module tree. It then uploads this application and logs on. :rtype: bool
  - `update_all_module_instances(self)` — Update all module instances to the current version of the module descriptions.
- **ScriptApplicationComposerObjectMarker** (object)
  - Every ScriptObject instance will be extended using this interface.
  - `is_module_instance_object` *(property)* — Gets a bool indicating whether this ScriptObject is a ModuleInstanceObject object. :rtype: bool
  - `is_module_reference_object` *(property)* — Gets a bool indicating whether this ScriptObject is a ModuleReference object. :rtype: bool
  - `is_module_declaration_object` *(property)* — Gets a bool indicating whether this ScriptObject is a ModuleDeclObject object. :rtype: bool
- **ScriptModuleInstanceObject** (ScriptApplicationComposerObjectMarker)
  - Functionality for manipulating ModuleInstanceObject-Objects. All Objects implementing ModuleInstanceObject will be extended with this methods.
  - `name` *(property)* — Gets the Instance-Name of the ModuleInstanceObject-Object. :rtype: str
  - `module` *(property)* — Gets the Module this instance is type of. :rtype: :class:`ScriptModule`
  - `parameters` *(property)* — Gets the Parameters of the Instance (see ScriptModule). :rtype: list
  - `ios` *(property)* — Gets the IOs of the Instance (see ScriptModule). :rtype: list
  - `slots` *(property)* — Gets the Slots of the Instance (see ScriptModule). :rtype: list
  - `inst_refs` *(property)* — Gets the InstanceReferences of the Instance (see ScriptModule). :rtype: list
  - `toplevel_info` *(property)* — Gets the ToplevelInfo of the Instance (see ScriptModule). Returns ``None`` if the instance is not toplevel. :rtype: :class:`ScriptModuleToplevelInfoInstance`
  - `parent_instance` *(property)* — Gets the parent module instance or ``None`` if this instance is toplevel. :rtype: :class:`.ScriptObject`
  - `parent_slot` *(property)* — Gets the slot this module instance is connected to or ``None`` if this instance is toplevel. :rtype: :class:`ScriptModuleSlotInstance`
  - `is_submodule` *(property)* — Whether this module instance is a submodule or not. :rtype: bool
- **ScriptModuleReferenceObject** (ScriptApplicationComposerObjectMarker)
  - Functionality for manipulating ModuleReferenceObjects. All Objects implementing ModuleReferenceObject will be extended with this methods.
  - `target` *(property)* — Returns the referenced module instance object or ``None`` if the referenced instance does not exit. :rtype: :class:`.ScriptObject`
  - `target_path` *(property)* — Returns the (relative) instance path of the referenced object. The components of the path are separated by "/" characters, the parent path is denoted by the spe
- **ScriptModule** (object)
  - Interface providing necessary information and functionalities dealing with Modules in Python. Equalling the type Module in the application composer interface collection.
  - `name` *(property)* — Gets the name of the Module. :rtype: str
  - `qualified_name` *(property)* — Gets the fully qualified Name (namespace.modulename) of the Module. :rtype: str
  - `parameters` *(property)* — Gets all Module-Parameters. :rtype: list
  - `ios` *(property)* — Gets all Module-IOs. :rtype: list
  - `slots` *(property)* — Gets all Module-Slots. :rtype: list
  - `inst_refs` *(property)* — Gets all Module-InstanceReferences. :rtype: list
  - `var_arrays` *(property)* — Gets all Module-VarArrays. :rtype: list
  - `toplevel_info` *(property)* — Gets the Module-ToplevelInfo. Returns ``None`` if module is not toplevel. :rtype: :class:`ScriptModuleToplevelInfo`
  - `meta_data` *(property)* — Gets the Module-MetaData. Returns ``None`` if module is not toplevel. :rtype: :class:`ScriptModuleMetaData`
  - `proxies` *(property)* — Gets all Module-Proxies. :rtype: list
  - `iec_declaration` *(property)* — Gets the declaration of the corresponding Module-IEC-FB. :rtype: :class:`ScriptModuleIECDecl`
  - `is_param_page_disabled` *(property)* — Whether the Editors Parameters-Page is dissabled or not. :rtype: bool
  - `is_toplevel_page_disabled` *(property)* — Whether the Editors Toplevel-Page is dissabled or not. :rtype: bool
  - `device_generator_data` *(property)* — Returns the data provided for the device generator. :rtype: :class:`ScriptModuleDeviceGeneratorData`
  - `alarm_generator_data` *(property)* — Returns the data provided for the alarm generator. :rtype: :class:`ScriptModuleAlarmGeneratorData`
- **ScriptModuleParameter** (object)
  - Interface providing necessary information and functionalities for dealing with Module-Parameters in Python.
  - `get_value(self)` — The current value of the Parameter. If no value is set, default or initial values that are actually used are returned. If this parameter does not belong to a Mo
  - `name` *(property)* — Localized (multi-lingual) name of the Parameter. :rtype: str
  - `description` *(property)* — Localized (multi-lingual) description of the Parameter. :rtype: str
  - `id` *(property)* — Id of the Parameter. The Id is unique among all Parameters of one module. :rtype: str
  - `type` *(property)* — The IEC-Type of the Parameter. :rtype: str
  - `var_path` *(property)* — Gets the instance path of the Parameters variable relative to the instance FB of the module. :rtype: str
  - `minimum` *(property)* — Gets the minimum value, that is defined for the parameter. :rtype: str
  - `maximum` *(property)* — Gets the maximum value, that is defined for the parameter. :rtype: str
  - `group_id` *(property)* — The GroupID of the parameter or an empty string if the parameter does not belong to a group. :version added: 3.5.13.0 :rtype: str
  - `group_name` *(property)* — The localized GroupName of the parameter or an empty string if the parameter does not belong to a group. :version added: 3.5.13.0 :rtype: str
- **ScriptModuleParameterInstance** (ScriptModuleParameter)
  - Interface providing necessary information and functionalities for dealing with Module-Parameter-Instances in Python.
  - `set_value(self, value)` — Sets the current value of the Parameter. By setting a parameter its standard initial or default values are no longer used. :type value: str :param value: The va
  - `get_initial_value(self)` — Gets the initial value of the parameter as string. Never returns ``None``. :version added: 3.5.13.0 :rtype: str
- **ScriptModuleIo** (object)
  - Interface providing necessary information and functionallities for dealing with Module-IOs in Python.
  - `get_display_name(self)` — The current representation of the current IO-Channels mapping meant for display. If not mapped, a value indicating "missing" is returned. If this IO does not be
  - `name` *(property)* — Localized (multi-lingual) name of the IO. :rtype: str
  - `description` *(property)* — Localized (multi-lingual) description of the IO. :rtype: str
  - `id` *(property)* — Id of the IO. The Id is unique among all IOs of one module. :rtype: str
  - `is_output` *(property)* — Returns whether the IO is output or not. :rtype: bool
  - `is_input` *(property)* — Returns whether the IO is input or not. :rtype: bool
  - `type` *(property)* — The IEC-Type of the IO-Channel. :rtype: str
  - `var_path` *(property)* — Gets the instance path of the IO-Channels variable relative to the instance FB of the module. :rtype: str
- **ScriptModuleIoInstance** (ScriptModuleIo)
  - Interface providing necessary information and functionallities for dealing with Module-IO-Instances in Python.
  - `set_void_mapping(self)` — Sets a void mapping, which equals an IO-Channel with no connection.
  - `set_missing_mapping(self)` — Sets a missing mapping. This indicates that this io channel has no connections (as for void), but remembers the user to set a mapping whenever code is generated
  - `set_direct_mapping(self, other)` — Sets a direct mapping to another IOChannel. :type other: ScriptModuleIoInstance :param other: The IO-Channel this channel shall be connected to. Note that Input
  - `set_io_channel_mapping(self, channel)` — Sets a channel mapping, which connects this IO to a physical IO-Channel. A possible example for a valid string used for this type of mapping is "param::Device.E
  - `set_expression_mapping(self, expression)` — Sets a channel mapping to an ST-Expression. :type expression: str :param expression: String holding the ST-Expression.
- **ScriptModuleSlot** (object)
  - Interface providing necessary information and functionallities for dealing with Module-Slots in Python.
  - `role` *(property)* — Localized (multi-lingual) description of the slot role. :rtype: str
  - `id` *(property)* — Id of the Slot. The Id is unique among all Slots of a module. :rtype: str
  - `is_submodule_slot` *(property)* — Returns whether the Slot is meant to hold submodules or not. :rtype: bool
  - `is_reference_slot` *(property)* — Returns whether the Slot is meant to hold references to modules or not. :rtype: bool
  - `is_single` *(property)* — Returns whether the Slot is a Single-Slot, which only can hold one instance, or not. :rtype: bool
  - `is_multi` *(property)* — Returns whether the Slot is a Multi-Slot, which can hold multiple instances, or not. :rtype: bool
  - `max_connections` *(property)* — Gets the number of the maximum of submodules or references, that can be connected to this Slot. :rtype: int
  - `min_connections` *(property)* — Gets the number of the minimum of submodules or references, that have to be connected to this Slot. :rtype: int
  - `default_inst_name` *(property)* — Gets the default name for module instances, which are connected to this Slot. If no default name is defined an empty string is returned. :rtype: str
  - `type` *(property)* — Gets the interface type of this Slot. Slot is corresponding to the interface, that FBs have to implement, when they shall be connectable to this slot. :rtype: s
  - `var_path` *(property)* — The IEC instance path of the slot variable relative to the FB instance of the module. :rtype: str
  - `var_array_size_path` *(property)* — Returns instance path. For Multi-Slots the instance path of the variable, which holds the number of connected submodules or references, relative to the FB insta
  - `inst_prefix` *(property)* — Gets the optional prefix, that is prepended to the name of the FB instance variables of submodules. This string can either have a value or is empty, what indica
  - `pragmas` *(property)* — Returns the compiler-pragmas, that are to be inserted before instances of submodule function blocks. :rtype: list
- **ScriptModuleSlotInstance** (ScriptModuleSlot)
  - Interface providing necessary information and functionalities for dealing with Module-Slot-Instances in Python.
  - `connected_sub_modules` *(property)* — Returns a List of connected ModuleInstanceObject-Objects to this Slot. When there are no submodules connected an empty list is returned. :rtype: list
  - `connected_ref_modules` *(property)* — Returns a List of connected ModuleReferenceObject-Objects to this Slot. When there are no references connected an empty list is returned. :rtype: list
- **ScriptModuleInstRef** (object)
  - Interface providing necessary information and functionalities for dealing with Module-InstanceReferences in Python.
  - `get_connected_instances(self)` — Return a list of connected instances. If there are no instances connected an empty list is returned. :rtype: list
  - `description` *(property)* — Localized (multi-lingual) description of the InstanceReference role. :rtype: str
  - `is_single` *(property)* — Returns whether the InstanceReference can only hold a single instance or not. :rtype: bool
  - `is_multi` *(property)* — Returns whether the InstanceReference can hold multiple instances or not. :rtype: bool
  - `max_connections` *(property)* — Maximum number of connectable instances. :rtype: int
  - `min_connections` *(property)* — Minimal number of connectable instances. :rtype: int
  - `type` *(property)* — Gets the interface type of the InstanceReference. Only FB instances which implement this interface can be connected to this InstanceReference. :rtype: str
  - `is_interface_type` *(property)* — Returns whether the reference type is an interface. :rtype: bool
  - `array_size_var_path` *(property)* — Returns instance path. Only defined if the InstanceReference is able to hold multiple instances (see "is_multi"). The IEC instance path of the variable, which h
- **ScriptModuleInstRefInstance** (ScriptModuleInstRef)
  - Interface providing necessary information and functionalities for dealing with Module-InstanceReference-Instances in Python.
  - `set_connected_instances(self, listInstances)` — Replaces the current list of instances of the InstanceReference instance by the given list of strings describing FB instances. :type listInstances: list :param 
- **ScriptModuleVarArray** (object)
  - Interface providing information and functionalities for dealing with Module-VarArrays.
  - `id` *(property)* — Id of the VarArray. The Id is unique among the VarArrays of a module. :rtype: str
  - `type` *(property)* — The IEC-Type of the array elements. :rtype: str
  - `var_path` *(property)* — The IEC instance path of the array variable, relative to the module FB instance. :rtype: str
  - `array_size_var_path` *(property)* — The IEC instance path of the variable, which holds the size of the array, relative to the module FB instance. :rtype: str
  - `instance_name` *(property)* — The optional instance name of the array variable. :rtype: str
  - `pragmas` *(property)* — Returns the compiler-pragmas that are to be inserted before the created array variables. :rtype: list
- **ScriptModuleMetaData** (object)
  - Interface providing necessary information and functionalities for dealing with Module-MetaData in Python.
  - `description` *(property)* — Localized (multi-lingual) description of the module. :rtype: str
  - `category` *(property)* — The hierarchic category of the module. The components are separated by '|'. :rtype: str
  - `inst_prefix` *(property)* — An optional, default instance prefix that is prepended to the name of the FB-instance variables of submodules and to the names of VarArray variables. "" is a po
  - `default_inst_name` *(property)* — Returns the default name for instances of this module type. :rtype: str
- **ScriptModuleAlarmGeneratorData** (object)
  - Interface providing necessary information and functionalities for dealing with the Alarm-Generator in Python.
  - `set_alarms` *(property)* — Returns a list of all alarms generated for a module. :rtype: list
- **ScriptModuleSetAlarm** (object)
  - Interface providing necessary information for a alarm, which is generated by the alarm generator.
  - `alarm_id` *(property)* — Returns the internal id of the module alarm. :rtype: str
  - `module_call_flags` *(property)* — Returns the type of module calls for alarming. :rtype: int
  - `message` *(property)* — Returns the message of the module alarm. :rtype: str
  - `alarm_class` *(property)* — Returns the alarm class of the module alarm. :rtype: str
  - `latch_var_1` *(property)* — Returns the latch variable 1 of the module alarm. :rtype: str
  - `latch_var_2` *(property)* — Returns the latch variable 2 of the module alarm. :rtype: str
  - `deactivation` *(property)* — Returns the deactivation variable of the module alarm. :rtype: str
  - `pending_time` *(property)* — Returns the pending time of the module alarm. :rtype: str
  - `higher_prio_alarm_id` *(property)* — Returns the id of the higher priority alarm of the current module alarm. :rtype: str
  - `expression` *(property)* — Returns the expression being alarm watched. :rtype: str
  - `comparer` *(property)* — Returns the type of comparison for UpperLimit, LowerLimit and Equality alarms. :rtype: str
  - `limit_expression_1` *(property)* — Returns the limiting expression for UpperLimit and LowerLimit alarms, the equality expression for Equality alarms, the lower area expression for InsideRange and
  - `limit_expression_2` *(property)* — Returns the higher area expression for InsideRange and OutsideRange alarms. :rtype: str
  - `inclide_limit_1` *(property)* — Returns whether the lower area expression (limit_expression_1) is includes in the defined area. :rtype: bool
  - `inclide_limit_2` *(property)* — Returns whether the higher area expression (limit_expression_2) is includes in the defined area. :rtype: bool
  - `inside_range` *(property)* — Returns whether a InsideRange or OutsideRange alarm is used. :rtype: bool
  - `hysteresis` *(property)* — Returns the alarm hysteresis for UpperLimit, LowerLimit, Equality, InsideRange and OutsideRange expressions. :rtype: double
  - `latch_vars` *(property)* — Returns all latch variables of the module alarm. :rtype: Dictionary(int, string)
- **ScriptModuleDeviceGeneratorData** (object)
  - Interface providing necessary information and functionalities for dealing with Module-DeviceGenerator-Data in Python.
  - `generated_devices` *(property)* — Returns a list of objects corresponding to the generated devices of the module. :rtype: list
  - `generated_ios` *(property)* — Returns a list of objects corresponding to the generated ios of the module. :rtype: list
  - `generated_inst_refs` *(property)* — Returns a list of objects corresponding to the generated instance references of the module. :rtype: list
  - `generated_device_parameters` *(property)* — Returns a list of objects corresponding to the gerenrated device parameters of the module. :rtype: list
- **ScriptModuleGeneratedDevice** (object)
  - Interface providing necessary information and functionalitties for dealing with Module-DeviceGenerator-Generated-Devices in Python.
  - `device_id` *(property)* — Returns the internal identification of the (generated) device. :rtype: str
  - `parent_device_id` *(property)* — Returns the internal identification of the parent (generated) device if available. :rtype: str
  - `device_type` *(property)* — Returns the Device-Identification-Type of the generated device if available. :rtype: str
  - `device_identification_id` *(property)* — Returns the Device-Identification-Id of the generated device if available. :rtype: str
  - `device_version` *(property)* — Returns the Device-Identification-Version of the generated device if available. :rtype: str
  - `device_module_id` *(property)* — Returns the Device-Identification-Module-Id of the generated device if available. :rtype: str
  - `wildcard_type` *(property)* — Returns the Wildcard-Device-Type of the generated device if available. :rtype: str
  - `wildcard_description` *(property)* — Return the Wildcard-Description of the generated device if available. :rtype: str
  - `flexible_wildcard_maximum` *(property)* — Returns the maximum number of flexible Wildcard-Devices if available. :rtype: str
- **ScriptModuleGeneratedIO** (object)
  - Interface providing necessary information and functionalities for dealing with Module-DeviceGenerator-Generated-IOs in Python.
  - `io_id` *(property)* — Returns the internal id of the Generated-IO. :rtype: str
  - `parent_id` *(property)* — Returns the parent (generated) device id of the Generated-IO. :rtype: str
  - `connected_parameter_id` *(property)* — Returns the Device-Parameter-ID of the connected Generated-IO if available. :rtype: str
  - `connected_connector_id` *(property)* — Returns the Device-Connector-ID of the connected Generated-IO if available. :rtype: str
  - `connected_element_path` *(property)* — Returns the Device-Element-Path of the connected Generated-IO if available. :rtype: str
  - `demanded_description` *(property)* — Returns the description of the demanded Generated-IO if available. :rtype: str
  - `demanded_properties` *(property)* — Returns the demanded properties of the demanded Generated-IO if available. :rtype: list
- **ScriptModuleGeneratedInstRef** (object)
  - Interface providing necessary information and functionalitties for dealing with Module-DeviceGenerator-Generated-InstRefs in Python.
  - `inst_ref_id` *(property)* — Returns the internal id of the demanded Generated-InstRef if available. :rtype: str
  - `parent_id` *(property)* — Returns the demanded id of the Instance reference. :rtype: str
  - `demanded_description` *(property)* — Returns the description of the demanded Generated-InstRef if available. :rtype: str
  - `demanded_properties` *(property)* — Returns the demanded properties of the demanded Generated-InstRef if available. :rtype: list
- **ScriptModuleGeneratedDeviceParameter** (object)
  - Interface providing necessary information and functionalities for dealing with Module-DeviceGenerator-Generated-Device-Parameters in Python.
  - `target_id` *(property)* — Returns the (generated) device id for which a parameter is set/added. :rtype: str
  - `internal_id` *(property)* — Returns the internal id of the Generated-Device-Parameter. :rtype: str
  - `connected_parameter_id` *(property)* — connected_parameter_id. :rtype: str
  - `connected_connector_id` *(property)* — Returns the Device-Connector-ID of the Generated-Device-Parameter if available. :rtype: str
  - `connected_element_path` *(property)* — Returns the Device-Element-Path of the Generated-Device-Parameter if available. :rtype: str
  - `add_parameter_name` *(property)* — Returns the parameter name of the added Generated-Device-Parameter. :rtype: str
  - `add_parameter_type` *(property)* — Returns the parameter type of the added Generated-Device-Parameter. :rtype: str
  - `set_parameter_value` *(property)* — Returns the parameter value of the set Generated-Device-Parameter. :rtype: str
- **ScriptModuleToplevelInfo** (object)
  - Interface providing all neccessary information and functionalities for dealing with Module-ToplevelInfo.
  - `get_home(self)` — Gets the home location of a toplevel module where the composer generates the applications. It has the form "Device.AppName" or holds the special string "POU Poo
  - `get_standard_task_high(self)` — Returns the standard task info for the high priority task, or `None`` if this task was not enabled. :rtype: :class:`ScriptModuleStdTaskInfo`
  - `get_standard_task_medium(self)` — Returns the standard task info for the medium priority task, or ``None`` if this task was not enabled. :rtype: :class:`ScriptModuleStdTaskInfo`
  - `get_standard_task_low(self)` — Returns the standard task info for the low priority task, or ``None`` if this task was not enabled. :rtype: :class:`ScriptModuleStdTaskInfo`
  - `gvl_name` *(property)* — Gets the name of the global variable list where the module instances will be declared. :rtype: str
  - `custom_tasks` *(property)* — Returns all defined custom tasks. :rtype: str
  - `pragmas` *(property)* — Returns the compiler pragmas that are to be inserted before instances of the module function block. :rtype: list
- **ScriptModuleToplevelInfoInstance** (ScriptModuleToplevelInfo)
  - Interface providing all neccessary information and functionalities for dealing with Module-ToplevelInfo-Instances.
  - `set_home(self, stHome)` — Sets the home location of a toplevel module. :type stHome: str :param stHome: String describing the home location in the form "Device.AppName" or by the special
  - `set_standard_task_high(self, stTaskName)` — Sets the Name of the standard high priority task. :type stTastName: str :param stTastName: The desired task name.
  - `set_standard_task_medium(self, stTaskName)` — Sets the Name of the standard medium priority task. :type stTastName: str :param stTastName: The desired task name.
  - `set_standard_task_low(self, stTaskName)` — Sets the Name of the standard low priority task. :type stTastName: str :param stTastName: The desired task name.
- **ScriptModuleStdTaskInfo** (object)
  - Interface providing all necessary information and functionallities for dealing with a StandardTaskInfo.
  - `name` *(property)* — The name of the task. :rtype: str
  - `description` *(property)* — Localized (multi-lingual) description of the task. :rtype: str
  - `is_update_ios` *(property)* — Whether module IOs that are directly mapped (i.e. not mapped to physical IOs) are read and written in this task or not. :rtype: str
  - `is_create_if_missing` *(property)* — Whether the task is created, if it did not exist yet, or not. :rtype: str
  - `is_readonly` *(property)* — Whether the name can be changed by the user or not. :rtype: str
- **ScriptModuleCustomTaskInfo** (object)
  - Interface providing all necessary information and functionalities for dealing with a CustomTaskInfo.
  - `method_name` *(property)* — The name of the method that will be called from this task. :rtype: str
  - `priority` *(property)* — The priority of the task (0 (lowest) to 31 (highest)). :rtype: int
  - `interval` *(property)* — The task interval in milliseconds. :rtype: int
  - `is_shared` *(property)* — Whether several custom tasks may share one method or not. :rtype: bool
  - `is_update_ios` *(property)* — Whether module IOs that are directly mapped (i.e. not to physical IOs) are read an written in this task or not. :rtype: bool
- **ScriptModuleProxy** (object)
  - Interface providing necessary information and functionallities for dealing with Module-Proxies in Python.
  - `id` *(property)* — The Id of the proxy. The Id is unique among all proxies of a module. :rtype: str
  - `iec_declaration` *(property)* — Gets the FB declaration of this proxy (i.o.w. the Proxy-FB). :rtype: :class:`ScriptModuleIECDecl`
- **ScriptModuleIECDecl** (object)
  - Interface providing necessary information and functionallities for dealing with module-bound Declarations in Python.
  - `name` *(property)* — Gets the name of the declaration object. :rtype: str
  - `is_fb` *(property)* — Whether this declaration is an FB or not. :rtype: bool
  - `is_interface` *(property)* — Whether this declaration is an interface or not. :rtype: bool
  - `is_struct` *(property)* — Whether this declaration is a struct or not. :rtype: bool
  - `is_method` *(property)* — Whether this declaration is a method or not. :rtype: bool
  - `is_union` *(property)* — Whether this declaration is an union or not. :rtype: bool
  - `is_other` *(property)* — Whether this declaration is of an other type or not. :rtype: bool
- **ScriptModuleDeclaration** (ScriptApplicationComposerObjectMarker)
  - Interface providing necessary information and functionalities dealing with Modules Declarations in Python. This interface is equalling the type ModuleDeclObject in the application composer interface collection.
  - `decltext(self, value)`
  - `decltext` *(property)* — Set or Gets the declaration text of the corresponding ModuleDeclObject. :rtype: str

### `ScriptAutomationServer`

- **AutomationServer** (object)
  - Scripting functionality for the "CODESYS Automation Server Connector" plugin. An instance of this interface is injected into the default namespace under the name "cas". .. note:: Only available if the "CODESYS Automation Server Connector" Plugin and the "CODESYS Script Engine" pa
  - `connect_edge_to_server(self, gateway: str, server_url: str, name: str, description: str = "", proxy_url: str = None, proxy_user: str = None, proxy_password: str = None)` — Connects the specified edge gateway to the automation server. May be called on a not-yet configured edge gateway with config mode enabled. :type gateway: str :p
  - `replace_edge_gateway(self, gateway: str, server_url: str, edge_id: int, proxy_url: str = None, proxy_user: str = None, proxy_password: str = None)` — Connects the specified edge gateway to the specified automation server, taking the role of an already existing gateway. Should be called on a not-yet configured
  - `provide_encryption_password_for_checkout(self, encryption_password: str)` — Provide a password for project encryption to be used for the ``checkout`` method. If the project you want to check out is password encrypted, use this method to
  - `checkout(self, server_url, project_id: int, commit_id: int, project_path: str, overwrite : bool = False)` — Checkout of a project from the server. :type server_url: str | Uri :param server_url: The server URL or hostname. :type project_id: int :param project_id: The p
  - `synchronize_gateways(self, server_url = None)` — Synchronize the list of remote gateways. :type server_url: str | Uri :param server_url: The server we should synchronize to. If omitted, and the primary project
  - `find_gateway_guid(self, server_url, gateway_id: int)` — Finds the Gateway guid for a given server and id, if it is registered in the current CODESYS installation. :type server_url: str | Uri :param server_url: The se
  - `calculate_plc_address(self, plc_id: int)` — Returns the CODESYS address to use with ``ScriptDeviceObject.set_gateway_and_address(...)`` for a given PLC id on the server. :type plc_id: int :param plc_id: T
  - `credentials` *(property)* — Gets the credentials manager to manage the stored server credentials. :rtype: :class:`CasCredentialsManager` :returns: The credentials manager instance responsi
  - `proxy_credentials` *(property)* — Gets the credentials manager to manage the stored proxy credentials. :rtype: :class:`CasCredentialsManager` :returns: The credentials manager instance responsib
  - `options` *(property)* — Gets the CasOptionsManager to manage options and settings for the cas connector plugin. :rtype: :class:`CasOptionsManager` :returns: The CasOptionsManager to ma
  - `edge_gateway` *(property)* — Gets the CasEdgeGatewayManager to inspect and connect edge gateways. :rtype: :class:`CasEdgeGatewayManager` :returns: The CasEdgeGatewayManager to inspect and c

### `ScriptAxisSettings`

- **ScriptAxisSettings** (object)
  - | Bundles settings of the x-axis of a traceObject or the y-axis of a diagram.
  - `copy_from(self, source: ScriptAxisSettings)` — | Convenient method for copying all properties, accessable by scripting, from the source to this ScriptAxisSettings.
  - `mode` *(property)* — | Scale mode of the axis. Possible values and their behaviours are: | Auto: the axis range is determined based on the range of the data. | FixedLength: the leng
  - `min_val` *(property)* — | Gets or sets the minimum value of the axis range. | This is only used, if mode == Fixed. | For the time axis, the resolution is ms.
  - `max_val` *(property)* — | Gets or sets the maximum value of the axis range. | This is only used, if mode == Fixed. | For the time axis, the resolution is ms.
  - `range` *(property)* — | Gets or sets the range of the axis. | This is only used, if mode == FixedLength. | For the time axis, the resolution is ms.
  - `draw_description` *(property)* — | Gets or sets wether the description text is drawn.
  - `description` *(property)* — | Gets or sets the description text.
  - `color` *(property)* — | Gets or sets the 32bit-ARGB representation of the color, used to draw the axis, tick marks, and labels.
  - `font` *(property)* — | Contains settings for font, used for the label and axis descriptions.
  - `draw_grid` *(property)* — | Gets or sets, wether the grid is drawn.
  - `grid_color` *(property)* — | Gets or sets the 32bit-ARGB representation of the color, used to draw the grid lines of the major tick.
  - `tickmark_fixed_spacing` *(property)* — | Gets or sets, wether a fixed spacing is used for the tick marks.
  - `tickmark_fixed_distance` *(property)* — | Gets or sets the distance of major tick marks, if tickmark_fixed_spacing is true. | For the time axis, the resolution is ms.
  - `tickmark_fixed_subdivisions` *(property)* — | Gets or sets the number of subdivisions of a major tick mark, if tickmark_fixed_spacing is true.

### `ScriptCasCredentialsManager`

- **CasCredentialsManager** (object)
  - Operations on stored credentials for servers or proxies. Use ``cas.credentials`` to manage server credentials, and ``cas.proxy_credentials`` to manage proxy credentials for the connector accessing the server. .. note:: The credentials are stored using the windows credentials api,
  - `exists_for(self, server_url)` — Checks whether we have credentials for a specific server (or proxy). :type server_url: str | Uri :param server_url: The server (or proxy) URL or hostname :rtype
  - `store(self, server_url, username: str, password: str, overwrite: bool = True)` — Adds or replaces credentials for a specific server (or proxy). :type server_url: str | Uri :param server_url: The server (or proxy) URL or hostname :type userna
  - `delete(self, server_url)` — Deletes any credentials for a specific server (or proxy), if there are some. :type server_url: str | Uri :param server_url: The server (or proxy) URL or hostnam
  - `delete_all(self)` — Deletes any credentials we have for servers (or proxies).
  - `get_urls_and_users(self)` — Assembles a dictionary of known server (or proxy) URLs and usernames. :rtype: dict[str, str] :returns: A ``dict`` with the server urls as keys, and the username

### `ScriptCasEdgeGatewayManager`

- **CasEdgeInfo** (object)
  - Information about an edge gateway on the server
  - `name` *(property)* — The name of the edge gateway, as configured in the server.
  - `id` *(property)* — The ID of the edge gateway on the server.
  - `cert_thumbprint` *(property)* — The primary certificate thumbprint used by the server to verify the connection to the edge gateway.
  - `secondary_cert` *(property)* — The secondary certificate thumbprint, or ``None`` if not present. :rtype: str | None .. Note:: When a certificate is refreshed before it expires, there is a sma
  - `description` *(property)* — The description of the edge gateway on the server, if the user configured one. :rtype: str | None
- **CasEdgeGatewayManager** (object)
  - Methods and properties to investigate and configure an edge gateway for the CODESYS Automation Server. .. note:: Being familiar with the "Configure Edge Gateway" view in either CODESYS or the Service Tool will help understanding this API. See https://help.codesys.com/webapp/_casc
  - `check_edge_gateway(self, gateway: str, port: int = 1217, verify_server: bool = True)` — Connects to the specified edge gateway, and checks its state, setting/refreshing the properties of this class. :type gateway: str :param gateway: The IP address
  - `check_server(self, server_url)` — Checks the specified Server and refreshes the list of available edge gateways ``server_known_edge_gateways``. :type server_url: str | Uri :param server_url: The
  - `connect_to_server(self, server_url, name: str, description: str = "", proxy_url = None, proxy_user: str = None, proxy_password: str = None): """Connects the current edge gateway to the automation server.  May be called after``check_edge_gateway()`` was executed successfully on a not-yet configured edge gateway, and ``edge_config_mode==True``;  :type server_url: str | Uri :param server_url: The url or hostname of the automation server the edge gateway should be connected to.  :type name: str :param name: The name the edge gateway should have on the server.  :type description: str :param description: Optional description of the gateway on the server.  :type proxy_url: str | Uri | None :param proxy_url: Proxy url if the edge gateway needs to connect through an explicit proxy to the server.  :type proxy_user: str | None :param proxy_user: Proxy user if the proxy at ``proxy_url`` needs authentication.  :type proxy_password: str | None :param proxy_password: Proxy password if the proxy at ``proxy_url`` needs authentication. """ pass  def replace_edge_gateway(self, edge_info, proxy_url = None, proxy_user: str = None, proxy_password: str = None)` — Connects the current edge gateway to the current automation server, taking the role of an already existing gateway. May be called after ``check_edge_gateway`` w
  - `renew_certificate(self)` — Renews and replaces the certificate currently used to authenticate the edge gateway to the server. .. note:: This method may be used to repair a connection when
  - `disable_communication(self)` — Disables the edge communication to the server by setting the ``edge_communication_state`` setting to 0, but keeps the configuration intact. .. note:: Communicat
  - `enable_communication(self)` — Re-activates the edge communication to the server by setting the ``edge_communication_state`` setting to 1, this requires a correct configuration. .. note: Use 
  - `repair_reconnect(self)` — Reconnects the specified edge gateway to the already configured automation server. This will repair mismatching certificates etc. To be called on an already con
  - `repair_reconnect(self, proxy_url = None, proxy_user: str = None, proxy_password: str = None)` — Reconnects the specified edge gateway to the already configured automation server, updating the proxy configuration. This will repair mismatching certificates e
  - `change_proxy_settings(self, proxy_url = None, proxy_user: str = None, proxy_password: str = None, disable_config_mode: bool = True)` — Sets, updates or deletes the proxy configuration. To be called on an already configured edge gateway with activated config mode. :type proxy_url: str | Uri | No
  - `disconnect(self)` — Disconnects the current edge gateway from the automation server, and deletes the configuration. .. note:: This operation will only affect the edge gateway confi
  - `disable_config_mode(self)` — Just disables the config mode on this edge gateway.
  - `craft_edge_webapp_url(self, info : CasEdgeInfo = None, start_scan : bool = False)` — Crafts the URL of the edge gateway within the CAS WebApp. :type info: CasEdgeInfo | None :param info: The edge to craft the URL for, or ``None`` to use ``server
  - `open_edge_webapp_url(self, info : CasEdgeInfo = None, start_scan : bool = False)` — Opens the URL of the given edge gateway in the system default browser. :type info: CasEdgeInfo | None :param info: The edge to open in the browser, or ``None`` 
  - `edge_error_message` *(property)* — Any error messages (human-readable) regarding the edge configuration. :rtype: str
  - `edge_gateway_address` *(property)* — The IP address or DNS host name of the edge gateway. :rtype: str
  - `edge_gateway_port` *(property)* — The TCP port of the edge gateway, or ``None`` if not initialized yet. :rtype: int
  - `edge_server_url` *(property)* — The server url configured for the edge gateway, or ``None`` if nothing is set yet. :rtype: str
  - `edge_config_mode` *(property)* — Edge configuration can only be written if this property returns <c>True</c>. For security reasons, the configuration mode has to be explicitly enabled on the ed
  - `edge_communication_state` *(property)* — Reflects whether the edge communication plugin is enabled in the edge gateway. If it is disabled, the edge gateway will not connect to the server, but the confi
  - `edge_cert_info` *(property)* — Information about the current certificate used by the edge gateway to connect to the server. :rtype: str .. note:: The "scenario" id for the certificate store i
  - `edge_cert_problems` *(property)* — Human readable description of any problems identified with the edge gateway certificate. Is ``None`` or empty if no problems were detected. :rtype: str
  - `edge_cert_thumbprint` *(property)* — The thumb print of the current certificate used by the edge gateway to connect to the server. :rtype: str
  - `edge_device_name` *(property)* — The device name announced by the edge gateway. :rtype: str
  - `edge_vendor_name` *(property)* — The vendor name announced by the edge gateway. :rtype: str
  - `edge_version_info` *(property)* — The version information announced by the edge gateway, human readable formatted. :rtype: str .. note:: This contains both ``edge_version`` and ``edge_core_versi
  - `edge_version` *(property)* — The product / firmware version announced by the edge gateway. :rtype: :class:`Version` .. note:: This version is freely assigned by the device vendor, and may d
  - `edge_core_version` *(property)* — The core version of the edge gateway component built into the edge gateway. :rtype: :class:`Version`
  - `edge_node_name` *(property)* — The node name announced by the edge gateway. :rtype: str
  - `edge_target_info` *(property)* — The target id and device type information (human readable). :rtype: str .. note:: This contains both ``edge_device_type`` and ``edge_target_id``.
  - `edge_device_type` *(property)* — The device type of the edge gateway. This is usually ``CasDeviceType.Communication`` for standalone gateways, and ``CasDeviceType.Programmable`` for runtimes wi
  - `edge_target_id` *(property)* — The target id of the gateway. This is 32 bit, the upper 16 bits are Vendor ID, lower 16 bits are Device ID. :rtype: int
  - `edge_proxy_url` *(property)* — The proxy url configured for the edge gateway, or ``None`` if no proxy is set. :rtype: str
  - `edge_proxy_user` *(property)* — The proxy auth username configured for the edge gateway, or ``None`` if no proxy user is set. :rtype: str
  - `edge_proxy_password` *(property)* — The proxy auth password configured for the edge gateway, or ``None`` if no proxy password is set. :rtype: str
  - `server_checked_url` *(property)* — The server url we checked, either implicitly with ``check_edge_gateway`` when a server is already configured, or explicitly with ``check_server()``. :rtype: str
  - `server_known_edge_gateways` *(property)* — Contains the list of known edge gateways in the server, or an empty list if no edge gateways are known. :rtype: list[CasEdgeInfo]
  - `server_edge_match` *(property)* — The information about the edge gateway entry on the server matching the configuration of the edge gateway, this is filled by ``check_edge_gateway`` when execute
  - `server_cert_info` *(property)* — Human-readable state about the certificate, e. G. whether ``edge_cert_thumbprint`` matches ``CasEdgeInfo.cert_thumbprint`` or ``CasEdgeInfo.secondary_cert``. :r
  - `server_cert_error` *(property)* — Any information about errors with the certificate (or configuration) on the server side, for example, when the certificate thumbprints known to the server do no
  - `server_check_error` *(property)* — Any errors which occurred when the server was checked. :rtype: str
  - `possible_actions` *(property)* — Flags bitfield of possible actions for the ``CasEdgeGatewayManager``. Which operations are allowed depends on the current state, any other operations will most 

### `ScriptCasEnums`

> No actions possible in the current state.

- **CasEdgeConfigActions** (Enum)
  - Possible actions for the ``CasEdgeGatewayManager`` in the current state. This enum may be extended in future versions. .. note:: The returned value will be a bit-wise combination of the possible actions.
- **CasDeviceType** (Enum)
  - The device / target type. .. note:: Correspond to SYSTARGET_TYPE_XXX defines in the runtime.

### `ScriptCasOptionsManager`

- **CasOptionsManager** (object)
  - Represents information stored by the CAS Connector plugin in the CODESYS options storage .. note:: Only available if the "CODESYS Automation Server Connector" Plugin and the "CODESYS Script Engine" packages are installed! .. note:
  - `auto_assign_boot_applications_on_download(self, value: bool)`
  - `auto_assign_boot_applications_on_download` *(property)* — When this setting is ``True``, and a new boot application is downloaded to a /// PLC in a CAS debug session, this application is also uploaded to the server, an
  - `recent_server_urls` *(property)* — Gets the recent server urls, approximately ordered by least recent usage first. :rtype: list[str] :returns: A python list containing the recent server URLs as s

### `ScriptCasScriptProjectExtension`

- **CasScriptProjectExtension** (ScriptProject)
  - All :class:`ScriptProject` instances are extended with this member, to provide access to the cas connector functionality. .. note:: Only available if the "CODESYS Automation Server Connector" Plugin and the "CODESYS Script Engine" package including the "Projects" script driver ar
  - `cas` *(property)* — Provides access to the Automation Server specific functionality for :class:`ScriptProject` instances, provided by ``CasScriptProjectImplementation``. :rtype: bo
- **CasReferenceInfo** (object)
  - Information about the project connection to the automation server
  - `server_url` *(property)* — The Url this project is connected to. :rtype: str
  - `project_id` *(property)* — Gets the project identifier (primary key of the project on the server database.) :rtype: int
  - `project_name` *(property)* — Gets the name of the project on the server, optional, for informative purposes. :rtype: str
  - `commit_id` *(property)* — Gets the ID of the base commit. This is the last commit from checkout, update or created during synchronization. (Primary key of the commit entity in the databa
  - `commit_message` *(property)* — Gets the commit message of the base commit, optional, for informative purposes. :rtype: str
  - `project_file_hash` *(property)* — Gets a hash of the project file in the base commit on the server. :rtype: str
- **CasScriptProjectImplementation** (object)
  - Automation Server specific functionality for :class:`ScriptProject` instances, can be accessed via the ``.cas`` property added by ``CasScriptProjectExtension``. .. note:: Only available if the "CODESYS Automation Server Connector" Plugin and the "CODESYS Script Engine" package in
  - `disconnect(self)` — Disconnects the project from the CAS server.
  - `connect(self, server_url, commit_message: str, project_name: str)` — Connects the current project to the automation server. :type server_url: str | Uri :param server_url: The server URL or hostname :type commit_message: str :para
  - `reconnect(self, server_url, commit_message: str, existing_project_id: int)` — Connects the current project to the automation server. :type server_url: str | Uri :param server_url: The server URL or hostname :type commit_message: str :para
  - `synchronize(self, commit_message: str)` — Synchronizes a connected project to the server. :type commit_message: str :param commit_message: The commit message for the project on the server. :rtype: :clas
  - `update(self)` — Updates a Project by fetching the newest commit available for this project on the server. Will close replace the primary project if an actual update is performe
  - `is_connected` *(property)* — Checks whether the project is connected to the automation server. :rtype: bool :returns: ``True`` if the project is connected to the cas, and ``False`` if the p
  - `cas_reference_info` *(property)* — Returns the CAS server reference information :rtype: :class:`CasReferenceInfo` | None :returns: The ``CasReferenceInfo`` or ``None`` if ``is_connected==False``.

### `ScriptDeviceDescription`

- **ScriptDeviceCollection** (list)
  - A collection of :class:`ScriptDeviceDescription` objects.
  - `get_devices_of_vendor(self, vendor)` — Get all devices in the list which match the specified vendor. :type vendor: str :param vendor: Vendor name. :rtype: ScriptDeviceCollection :returns: A collectio
  - `__len__` *(property)* — Gets the length (number of device descriptions). :rtype: int :returns: The number of device descriptions.
  - `vendors` *(property)* — Gets the list of all vendors in the collection. :rtype: tuple[int]
- **ScriptDeviceDescription** (object)
  - Description of a device.
  - `device_id` *(property)* — Get the identification object of the device. :rtype: :class:`DeviceID` :returns: DeviceID
  - `device_info` *(property)* — Get information about the device. :rtype: :class:`ScriptDeviceInfo` :returns: DeviceInfo
  - `connectors` *(property)* — Gets the connectors. :rtype: :class:`ScriptDeviceConnectorSet` :returns: DeviceConnectorSet
- **ScriptDeviceInfo** (object)
  - Provides information about a device..
  - `name` *(property)* — Internationalized name of the device. :rtype: str
  - `description` *(property)* — Internationalized description of the device. :rtype: str
  - `vendor` *(property)* — Internationalized vendor of the device vendor. :rtype: str
  - `categories` *(property)* — Gets a list of categories this device belongs to. :rtype: tuple[int]
  - `families` *(property)* — Gets a list of vendor-specific families this device belongs to. Each string has got the format ``VendorId:FamilyId``. :rtype: tuple[str]
  - `custom` *(property)*
  - `default_instance_name` *(property)* — The default intance name for this device. :version added: 3.5.11.0 :rtype: str
- **ScriptVendorDescription** (object)
  - Vendor description.
  - `get_family(self, family_id)` — Get the family with the specified family Id. :type family_id: int :param family_id: Family Id. :rtype: :class:`ScriptDeviceFamily` :returns: Device family objec
  - `vendor_id` *(property)* — Id of the vendor. :rtype: int
  - `version` *(property)* — Version. :rtype: str
  - `vendor_info` *(property)* — Vendor information. :rtype: :class:`ScriptVendorInfo`
  - `families` *(property)* — Get all families of the vendor. :rtype: tuple[ScriptDeviceFamily]
- **ScriptVendorInfo** (object)
  - Vendor information.
  - `name` *(property)* — Vendor name. :rtype: str
  - `addresses` *(property)* — Address of the vendor. :rtype: tuple[str]
  - `phones` *(property)* — Phone number(s). :rtype: tuple[str]
  - `faxes` *(property)* — Fax number(s). :rtype: tuple[str]
  - `mail_addresses` *(property)* — eMail address(es). :rtype: tuple[str]
  - `web_addresses` *(property)* — Web address(es). :rtype: tuple[str]
- **ScriptDeviceFamily** (object)
  - Family Id.
  - `family_id` *(property)* — Family Id. :rtype: int
  - `parent_family` *(property)* — Parent family. :rtype: str
  - `name` *(property)* — Family name. :rtype: str
  - `description` *(property)* — Description of the family. :rtype: str
  - `sub_families` *(property)* — Sub families of the family. :rtype: tuple[ScriptDeviceFamily]

### `ScriptDeviceObject`

> Tracked by name (e.g. 'MyPlc').

- **DeviceTrackingMode** (Enum)
  - Enumeration that defines how a device is tracked on the network.
- **StopResetBehaviour** (Enum)
  - The outputs keep the last current values.
- **ConnectorRole** (Enum)
  - Describes the role of a connector
- **AccessRight** (Enum)
  - Defines access rights on a parameter.
- **ChannelType** (Enum)
  - Defines the types of a channel.
- **DiagType** (Enum)
  - Describes the function of a parameter in respect to module diagnosis.
- **ScriptDeviceObjectMarker** (object)
  - Every ScriptObject instance will be extended with this method.
  - `is_device` *(property)* — Gets a value indicating whether this instance is a device object. :rtype: bool
- **ScriptDeviceObject** (ScriptDeviceObjectMarker)
  - Functionality for manipulating device objects. All device objects implementing DeviceObject will be extended with this methods.
  - `get_device_identification(self)` — Gets the device identification. :rtype: :class:`DeviceId`
  - `enable(self)` — Marks this device as enabled during download.
  - `disable(self)` — Marks this device as disabled during download.
  - `is_enabled(self)` — Determines whether this instance is enabled during download. :rtype: bool :returns: ``True`` if this instance is enabled during download; otherwise, ``False``.
  - `update(self, device: DeviceId, module: str = None)` — Updates the specified device. :type device: :class:`DeviceId` :param device: The device Id. :type module: str :param module: The module ID. (This parameter is o
  - `update(self, type: int, id: str, version: str, module: str = None)` — Updates the specified device. :type type: int :param type: The device type. :type id: str :param id: The device identification. :type version: str :param versio
  - `plug(self, name: str, device: DeviceId, module: str = None)` — Plugs the specified device. :type name: str :param name: Name of the device. :type device: :class:`DeviceId` :param device: The device Id. :type module: str :pa
  - `plug(self, name: str, type: int, id: str, version: str, module: str = None)` — Plugs the specified device. :type name: str :param name: Name of the device. :type type: int :param type: The device type. :type id: str :param id: The device i
  - `add(self, name: str, device: DeviceId, module: str = None)` — Adds the specified device. :type name: str :param name: Name of the device. :type device: :class:`DeviceId` :param device: The device Id. :type module: str :par
  - `add(self, name: str, type: int, id: str, version: str, module: str = None)` — Adds the specified device. :type name: str :param name: Name of the device. :type type: int :param type: The device type. :type id: str :param id: The device id
  - `insert(self, name: str, index: int, device: DeviceId, module: str = None)` — Inserts the specified device at the specified index. :type name: str :param name: Name of the device. :type index: int :param index: Index where to insert the d
  - `insert(self, name: str, index: int, type: int, id: str, version: str, module: str = None)` — Inserts the specified device at the specified index. :type name: str :param name: Name of the device. :type index: int :param index: Index where to insert the d
  - `unplug(self)` — Unplugs the specified device.
  - `get_simulation_mode(self)` — Gets the simulation mode. :returns: ``True`` if simulation is enabled.
  - `set_simulation_mode(self, simulation)` — Sets the simulation mode. :type simulation: bool :param simulation: if set to ``True``, simulation is enabled.
  - `get_gateway(self)` — Gets the gateway. See also: :attr:`ScriptDeviceObject.get_device_communication_settings` :rtype: Guid :returns: The guid of the gateway.
  - `get_address(self)` — Gets the address of the device. See also: :attr:`ScriptDeviceObject.get_device_communication_settings` :rtype: str :returns: The device address in the bus indep
  - `set_gateway_and_address(self, gateway: Guid, address: str)` — Sets the gateway and address. If you pass the empty gateway and an empty address, the gateway address will be cleared. You can use :meth:`ScriptGateway.find_add
  - `set_gateway_and_address(self, gateway: str, address: str)` — Sets the gateway and address. If you pass the empty gateway and an empty address, the gateway address will be cleared. You can use :meth:`ScriptGateway.find_add
  - `set_gateway_and_address(self, gateway: ScriptGateway, address: str)` — Sets the gateway and address. If you pass the empty gateway and an empty address, the gateway address will be cleared. You can use :meth:`ScriptGateway.find_add
  - `get_module_identification(self)` — Returns the unique identification of a module. A module is a special type of device, that is only available within the context of a certain device. The module i
  - `allow_interfaces_at(self, index)` — Get the name of the child interfaces that this device object can accept at the specified insert position. :version added: 3.5.4.0 :type index: int :param index:
  - `set_gateway_and_device_name(self, gateway: ScriptGateway, device_name: str)` — Sets the gateway and device name for communication. If you pass the empty guid and an empty address, the gateway address will be cleared. The device will be tra
  - `set_gateway_and_device_name(self, gateway: Guid, device_name: str)` — Sets the gateway and device name for communication. If you pass the empty guid and an empty address, the gateway address will be cleared. The device will be tra
  - `set_gateway_and_device_name(self, gateway: str, device_name: str)` — Sets the gateway and device name for communication. If you pass the empty guid and an empty address, the gateway address will be cleared. The device will be tra
  - `set_gateway_and_ip_address(self, gateway: ScriptGateway, ip_address: str, port: int = 11740)` — Sets the gateway and IP address for communication. :version added: 3.5.8.0 :type gateway::class:`ScriptGateway` :param gateway: The gateway. :type ip_address: s
  - `set_gateway_and_ip_address(self, gateway: ScriptGateway, ip_address: IPAddress, port: int = 11740)` — Sets the gateway and IP address for communication. :version added: 3.5.8.0 :type gateway: :class:`ScriptGateway` :param gateway: The gateway. :type ip_address: 
  - `set_gateway_and_ip_address(self, gateway: Guid, ip_address: str, port: int = 11740)` — Sets the gateway and IP address for communication. :version added: 3.5.8.0 :type gateway: Guid :param gateway: The gateway's Guid. :type ip_address: str :param 
  - `set_gateway_and_ip_address(self, gateway: Guid, ip_address: IPAddress, port: int = 11740)` — Sets the gateway and IP address for communication. :version added: 3.5.8.0 :type gateway: Guid, str or :class:`ScriptGateway` :param gateway: The gateway's' Gui
  - `set_gateway_and_ip_address(self, gateway: str, ip_address: str, port: int = 11740)` — Sets the gateway and IP address for communication. :version added: 3.5.8.0 :type gateway: str :param gateway: The gateway guid (as string) or name. :type ip_add
  - `set_gateway_and_ip_address(self, gateway: str, ip_address: IPAddress, port: int = 11740)` — Sets the gateway and IP address for communication. :version added: 3.5.8.0 :type gateway: str :param gateway: The gateway guid (as string) or name. :type ip_add
  - `get_device_communication_settings(self)` — Gets the communication settings of the device. :rtype: :class:`ScriptCommunicationSettings`
  - `export_io_mappings_as_csv(self, file_path)` — Export the io mappings as a CSV file to the specified absolute path. :version added: 3.5.8.0 :type file_path: str :param file_path: The absolute path of the fil
  - `import_io_mappings_from_csv(self, file_path)` — Imports the io mappings from a CSV file at the specified absolute path. :version added: 3.5.8.0 :type file_path: str :param file_path: The absolute path of the 
  - `allow_symbolic_var_access_in_sync_with_iec_cycle(self, value)`
  - `device_parameters` *(property)* — Gets the set of device parameters. Since V3.5.8.0, this actually is a :class:`ScriptMappableDeviceParameterSet`. :version added: 3.5.4.0 :rtype: :class:`ScriptD
  - `connectors` *(property)* — Gets the connectors. :rtype: :class:`ScriptDeviceConnectorSet`
  - `driver_info` *(property)* — Get the driver info of the device. :version added: 3.5.9.0 :rtype: :class:`ScriptDriverInfo`
  - `allow_symbolic_var_access_in_sync_with_iec_cycle` *(property)* — Property used by the symbol configuration to determine if symbolic variable access is allowed to be synchronized with the IEC cycle. The default is False and sh
- **ScriptProjectDeviceExtension** (object)
  - Functionality to add top-level devices (e. G. SPS) to projects. ScriptProject instances are amended with these objects. :version added: 3.4.3.0
  - `add(self, name: str, device: DeviceId, module: str = None)` — Adds the specified device. :type name: str :param name: Name of the device. :type device: :class:`DeviceId` :param device: The device Id. :type module: str :par
  - `add(self, name: str, type: int, id: str, version: str, module: str = None)` — Adds the specified device. :type name: str :param name: Name of the device. :type type: int :param type: The device type. :type id: str :param id: The device id
- **DeviceId** (object)
  - Represents a Device ID. An implementation class of this interface is injected under the name "DeviceID" into the python scope, so python code can create device IDs without the need to subclass that interface. The constructor signature is: DeviceID(int iType, string stId, string s
  - `type` *(property)* — Type of the device. :rtype: int
  - `id` *(property)* — Id of the device. The format for this id is specified for each type. The id is unique within the class of devices of one type. :rtype: str
  - `version` *(property)* — The version of the device. The format for the version string is specified for each type. :rtype: str
- **ModuleId** (DeviceId)
  - Unique identification for a module. A module is a special type of device, that is only available within the context of a certain device. The module is identified by the same values as each owning device, with an additional module id, to distinguish it from other modules of the sa
  - `module_id` *(property)* — Id of the module. The format for this id is specified for each type. The id is unique within the class of devices of one type. :rtype: str
- **ScriptCommunicationSettings** (object)
  - Provides access to the communication settings of the device.
  - `is_communication_encrypted(self, value)`
  - `gateway_guid` *(property)* — The guid of the gateway. :rtype: Guid
  - `device_address` *(property)* — The address of the device. :rtype: str
  - `prompt_at_login` *(property)* — Whether there's a prompt at login. :rtype: bool
  - `secure_online_mode` *(property)* — Gets a boolean value indicating whether secure online mode is activated for the corresponding devices. If set, user interfaces should prompt the user before an 
  - `device_name` *(property)* — Gets the name of the device as entered on the communication settings page. :rtype: str
  - `monitoring_interval_msec` *(property)* — The interval for status and variable monitoring measured in milliseconds. Default = 200ms, Minimum = 10ms, Maximum = 1000ms, Increment 10ms. Invalid values will
  - `monitoring_interval` *(property)* — The interval for status and variable monitoring measured in milliseconds. Default = 200ms, Minimum = 10ms, Maximum = 1000ms, Increment 10ms. Invalid values will
  - `TrackingMode` *(property)* — Property to get the mode used to track a device on the network - whether the device is tracked via CODESYS address, ip address or name. :rtype: DeviceTrackingMo
  - `scanned_device_name` *(property)* — The name of the physical device (E.g. "MyPlc"), as seen in the network scan. :rtype: str
  - `scanned_ip_address_and_port` *(property)* — Device IP Address and Port if block driver TCP is used for connection. Format: "192.168.101.109:11740", as seen in the network scan. This may return the emtpy s
  - `scanned_target_id` *(property)* — Target ID. Format: "1234 ABCD" (=hexadecimal), same as in device description, as seen in the network scan. This may return the emtpy string if it's not availabl
  - `scanned_target_name` *(property)* — The name of the target (E.g. "CODESYS PLC Win NT"), as seen in the network scan. This may return the emtpy string if it's not available. Even if some network sc
  - `scanned_target_type` *(property)* — Target Type (Format: "4096" (=decimal), same as in device description), as seen in the network scan. This may return the emtpy string if it's not available. Eve
  - `scanned_target_vendor` *(property)* — The vendor of the target, as seen in the network scan. This may return the emtpy string if it's not available. Even if some network scan members are set, this d
  - `scanned_target_version` *(property)* — The version of the target, as seen in the network scan. This may return the emtpy string if it's not available. Even if some network scan members are set, this 
  - `is_communication_encrypted` *(property)* — Get or set if encrypted communication should be used with the device. :version added: 3.5.16.10 :rtype: bool

### `ScriptDeviceParameters`

- **ScriptDeviceConnectorSet** (list)
  - The readonly list of connectors for a specific device object.
  - `get_device_object(self)` — Gets the device object associated with this connector set. :rtype: :class:`ScriptDeviceObject`
  - `by_id(self, id)` — Gets the specific connector by its id. :type id: int :param id: The id. :rtype: :class:`ScriptDeviceConnector` :returns: The connector
  - `__contains__(self, id: int)` — Determines whether the list contains an element with the specified id. :type id: int :param id: The id. :rtype: bool :returns: ``True`` if the list contains an 
  - `__contains__(self, visible_name)` — Determines whether the list contains this element or an element with the specified id or name. :type visible_name: str :param visible_name: The visible name. :r
  - `__contains__(self, element: ScriptDeviceConnector)` — Determines whether the list contains this element or an element with the specified id or name. :type element: :class:`ScriptDeviceConnector` :param element: The
  - `__getitem__(self, visible_name)` — Gets the :class:`ScriptDeviceConnector` with the specified ``visible_name``. :type visible_name: str :rtype: :class:`ScriptDeviceConnector`
- **ScriptConnector** (object)
  - A connector. This is implemented by the :class:`ScriptDeviceConnector` instances returned by the :class:`ScriptDeviceConnectorSet` as well as by :class:`ScriptExplicitConnectorObject`.
  - `get_device_object(self)` — Get an instance of the device object this connector belongs to. :rtype: :class:`ScriptDeviceObject` :returns: The device object.
  - `module_type` *(property)* — Id of the connector. This id is used by the driver on the runtime system. The Id's of matching parent and child connectors are different. Therefore in order to 
  - `interface` *(property)* — The unique typename of a connector, eg. "Common.PCI". A parent connector may be connected to a child connector, if this connector type matches. :rtype: str
  - `interface_name` *(property)* — Get an internationalized version of the interface name for presentation purposes. :rtype: str
  - `connector_id` *(property)* — The unique connector id. :rtype: int
  - `host_path` *(property)* — Get the id of the next connector towards the host. ``-1``, if the attached device is the controlling host. :rtype: int
  - `connector_role` *(property)* — Get whether this connector is a parent or child connector. :rtype: ConnectorRole
  - `is_explicit` *(property)* — Get whether a separate node should be shown in the user interface for this connector. :rtype: bool
  - `host_parameters` *(property)* — Get the host parameter set of this connector. The returned list is read-only which means you can't add, insert or remove parameters or clear it. The list of ava
  - `additional_interfaces` *(property)* — Gets the additional interfaces of the connector. This may be useful to find out which child connector of the current parent connector is actually valid. :versio
- **ScriptDeviceConnector** (ScriptConnector)
  - A device connector as contained in the :class:`ScriptDeviceConnectorSet`.
  - `io_always_mapping(self, value: bool)`
  - `parent` *(property)* — Gets the :class:`ScriptDeviceConnectorSet` defining this connector. :rtype: :class:`ScriptDeviceConnectorSet`
  - `io_always_mapping` *(property)* — Gets a value indicating whether this ScriptDeviceConnector is always mapping the I/Os belonging to this connector, even if they're not used in the IEC code. By 
  - `driver_info` *(property)* — Get the driver info of the device connector. :version added: 3.5.15.0 :rtype: :class:`ScriptDriverInfo`
- **ScriptDeviceParameterSet** (list)
  - A device parameter set. The list is read-only which means you can't add, insert or remove parameters or clear it. The list of available parameters is defined in the device description.
  - `get_device_object(self)` — Gets the device object or explicit connector object defining this parameter set. :rtype: :class:`ScriptDeviceObject`
  - `__getitem__(self, name)` — Gets the :class:`ScriptDeviceParameter` with the specified name. :type name: str :rtype: :class:`ScriptDeviceParameter`
  - `__contains__(self, id: int)` — Determines wether it contains the specified ScriptDeviceParameter or one with the specified id or name. :type id: int :param id: The id. :rtype: bool :returns: 
  - `__contains__(self, name)` — Determines wether it contains the specified ScriptDeviceParameter or one with the specified id or name. :type name: str :param name: The name. :rtype: bool :ret
  - `__contains__(self, parameter: ScriptDeviceParameter)` — Determines wether it contains the specified ScriptDeviceParameter or one with the specified id or name. :type parameter: :class:`ScriptDeviceParameter` :param p
  - `by_id(self, id: int)` — Gets the :class:`ScriptDeviceParameter` with the specified id. :type id: int :rtype: :class:`ScriptDeviceParameter`
  - `parent` *(property)* — Gets the parent. This is either a :class:`ScriptDeviceObject`, a :class:`ScriptConnector`, or a :class:`ScriptExplicitConnectorObject`. :rtype: obj
- **ScriptMappableDeviceParameterSet** (ScriptDeviceParameterSet)
  - Extension interface for the :class:`ScriptDeviceParameterSet` returned by :meth:`ScriptDeviceObject.device_parameters`.
  - `io_always_mapping(self, value: bool)`
  - `io_always_mapping` *(property)* — Gets a value indicating whether this ScriptMappableDeviceParameterSet is always mapping the I/Os belonging to device parameter set (not part of any connectors),
- **ScriptDataElement** (object)
  - A data element of an online parameter. Notice that instances of this interface usually also implement at least one of the related interfaces :class:`ScriptCompoundDataElement`, :class:`ScriptValueDataElement`, :class:`ScriptDeviceParameter`, :class:`ScriptCompoundDataElement`, :c
  - `user_comment(self, value: str)`
  - `parent` *(property)* — Gets the parent. This property returns either the parent :class:`ScriptDataElement` (which may be the :class:`ScriptDeviceParameter`), or the :class:`ScriptDevi
  - `parameter` *(property)* — Gets the parameter defining this data element. This will return the same instance if called on the :class:`ScriptDeviceParameter`. :rtype: :class:`ScriptDeviceP
  - `identifier` *(property)* — Unique identifier of this data element within it's parent element. :rtype: str
  - `visible_name` *(property)* — Internationalized name of the data element (this is the name used in the user interface). :rtype: str
  - `description` *(property)* — Internationalized description of the data element. :rtype: str
  - `unit` *(property)* — Internationalized unit of the data element. To be used by the presentation layer. :rtype: str
  - `bit_size` *(property)* — Get the size of this parameters value in bits. :rtype: int
  - `user_comment` *(property)* — Get or set a specified user comment. :rtype: str
  - `has_sub_elements` *(property)* — Get information whether this element is a compound type. True for structs, arrays, bitfields, ... - in this case, the element implements :class:`ScriptCompoundD
  - `is_range_type` *(property)* — True, if the elements value must be within a certain range. If this is true, the element implements the :class:`ScriptRangeDataElement` interface. :rtype: bool
  - `is_enumeration` *(property)* — True if this element is defined as an enumeration. It then also implements :class:`ScriptEnumerationDataElement`. The properties :attr:`is_enumeration` and :att
  - `is_union` *(property)* — Gets a value indicating whether this :class:`ScriptDataElement` is an union. :rtype: bool
  - `can_access_online` *(property)* — Gets a value indicating whether this :class:`ScriptDataElement` can be read online. If this is true, the element additionally implements :class:`ScriptValueData
  - `is_mappable_io` *(property)* — Gets a value indicating whether this :class:`ScriptDataElement` is a mappable input or output. :version added: 3.5.8.0 :rtype: bool :returns: ``True`` if is a m
  - `io_mapping` *(property)* — Gets the io mapping of this data element. :version added: 3.5.8.0 :rtype: :class:`ScriptIoMapping` :returns: The mapping, or ``None`` if no mapping exists (e. G
- **ScriptCompoundDataElement** (list)
  - Data element representing compound values which cannot be read or written, but they have subelements which can be modified (if they're not ScriptCompoundDataElements themselves). Implementations of this interface also implement :class:`ScriptDataElement` and sometimes also :class
  - `__getitem__(self, identifier)` — Return the element with the specified identifier. :type identifier: str :param identifier: :attr:`DataElement.Identifier` of the requested DataElement :raises A
  - `__contains__(self, identifier: str)` — Return ``True`` if a ScriptDataElement with this identifier exists in the collection. :type identifier: str :param identifier: :attr:`ScriptDataElement.Identifi
  - `__contains__(self, sub_element: ScriptDataElement)` — Return ``True`` if a ScriptDataElement with this identifier exists in the collection. :type sub_element: str or :class:`ScriptDataElement` :param sub_element: :
- **ScriptValueDataElement** (ScriptDataElement)
  - Data element representing values of basic member elements which can be read and written.
  - `value(self, value: str)`
  - `read_online_value(self, nTimeOut=1000)` — Get the online value with the specified timeout. You need to check :attr:`ScriptDataElement.can_access_online` before using this property. :type nTimeOut: int :
  - `write_online_value(self, value)` — Writes the specified value to the device. You need to check :attr:`ScriptDataElement.can_access_online` before using this property. :type value: str :param valu
  - `default_value` *(property)* — Get the default value for this data element. If the string is empty, then no explicit defaultvalue has been set. :rtype: str
  - `value` *(property)* — Set/get the value for this element as a string representation. Invalid values are accepted, but cause the error flag to be set. :raises InvalidOperationExceptio
  - `base_type` *(property)* — Gets the base type of this data element, or None if the type is a compound type. :rtype: str
- **ScriptRangeDataElement** (ScriptValueDataElement)
  - Data element representing values with a limited range.
  - `min_value` *(property)* — Get the minimal value for this element as a string representation. :raises InvalidOperationException: Thrown if this element is not a range type element (equiva
  - `max_value` *(property)* — Get the maximum value for this element as a string representation. :raises InvalidOperationException: Thrown if this element is not a range type element (equiva
- **ScriptEnumerationDataElement** (ScriptValueDataElement)
  - Data element representing enumeration values.
  - `enum_value(self, value: ScriptEnumerationValue)`
  - `value_index(self, value: int)`
  - `read_online_enum_value(self, nTimeout=1000)` — Get_online_enum_values the specified n timeout. You need to check :attr:`ScriptDataElement.can_access_online` before using this property. :type nTimeout: int :p
  - `write_online_value(self, value)` — Writes the specified value to the device. You need to check :attr:`ScriptDataElement.can_access_online` before using this property. :type value: :class:`ScriptE
  - `enum_value` *(property)* — Set/get the current value for this element as an enumeration value. :raises InvalidOperationException: Thrown if this element is not a valid enumeration element
  - `allowed_values` *(property)* — Set/get the current value for this element as an enumeration value. Invalid values are accepted, but cause the error flag to be set. :raises InvalidOperationExc
  - `value_index` *(property)* — Gets or sets the index of the current value within the :attr:`allowed_values` array. :rtype: int :returns: ``-1`` if the current value is not a valid enumeratio
- **ScriptEnumerationValue** (object)
  - Defines one element of an enumeration.
  - `parent` *(property)* — Gets the defining :class:`ScriptEnumerationDataElement`. :rtype: :class:`ScriptEnumerationDataElement`
  - `identifier` *(property)* — Unique identifier of this enumeration value within its enumeration element. This is the value to use with the :attr:`ScriptValueDataElement.value` property. :rt
  - `visible_name` *(property)* — Internationalized name of the enumeration value. To be used by the presentation layer. :rtype: str
  - `description` *(property)* — Internationalized description of the enumeration value. To be used by the presentation layer. :rtype: str
  - `value` *(property)* — Gets the value. :rtype: str
  - `index` *(property)* — Gets the index of this value within the :attr:`ScriptEnumerationDataElement.allowed_values` list. :rtype: str
- **ScriptDeviceParameter** (ScriptDataElement)
  - A device parameter.
  - `get_device_object(self)` — Gets the device object associated with this parameter. :rtype: :class:`ScriptDeviceObject`
  - `id` *(property)* — Each parameter has a unique id within it's parameter list. This is also returned as the identifier in the underlying DataElement. :rtype: int
  - `name` *(property)* — Internationalized name of the data element. To be used by the presentation layer. :rtype: str
  - `offline_access_rights` *(property)* — Get the allowed access to this parameter in offline mode. :rtype: AccessRight
  - `online_access_rights` *(property)* — Get the allowed access to this parameter in online mode. :rtype: AccessRight
  - `downloaded_with_ioconfig` *(property)* — Get whether this parameter will be downloaded with the IO-Config. :rtype: bool
  - `channel_type` *(property)* — If this parameter represents an IO channel, returns whether it is an input or an output channel. Otherwise this property returns ChannelType.None. :rtype: Chann
  - `diagnostic_type` *(property)* — Get or set the diagnostic type of this parameter. :rtype: DiagType
  - `type_string` *(property)* — Returns a string which fully describes the type. :rtype: str
  - `section` *(property)* — Gets the section of the parameter. The sections are purely informative and help to structure the device parameters in user interfaces. :rtype: str
  - `iec_type` *(property)* — Gets the iec type of this parameter, or ``None`` if none is defined. :rtype: str
  - `param_type` *(property)* — get information about the original paramtype (e.g. "std:uint" or "localtypes:struct"). Usually, this is the best method to describe the type of an parameter - h
  - `disable_mapping` *(property)* — Get whether this parameter will be in the task mapping list for the io drivers. :version added: 3.5.12.20 :rtype: bool
- **ScriptIoVariableMapping** (object)
  - Represents a single variable mapping.
  - `variable(self, value: str)`
  - `Id` *(property)* — Gets the identifier. :rtype: int
  - `variable` *(property)* — Gets or sets the variable for the mapping. The string must be a valid IEC variable expression. If it's an unqualified expression, a new variable with the given 
  - `default_variable` *(property)* — Gets the default variable, if defined in the device description. The default variable, if existing, is defined in the device description. :rtype: str
  - `mapping_creates_variable` *(property)* — Gets a value indicating whether this :class:`ScriptIoVariableMapping` creates a new variable. This is the opposite of :attr:`maps_to_existing_variable`. :rtype:
  - `maps_to_existing_variable` *(property)* — Gets a value indicating whether this :class:`ScriptIoVariableMapping` maps to an existing variable. This is the opposite of :attr:`mapping_creates_variable`. :r
- **ScriptIoMapping** (ScriptIoVariableMapping)
  - Describing the I/O Mapping options. This object also represents the first actual mapping for the variable. Currently the device IO mapping editor UI allows only a single mapping to be configured, so we'll implicitly handle this mapping similar to what the device IO mapping editor
  - `automatic_iec_address(self, value: bool)`
  - `manual_iec_address(self, value: str)`
  - `automatic_iec_address` *(property)* — Gets or sets a value indicating whether this :class:`ScriptIoMapping` has automatically assigned IEC addresses. :rtype: bool :returns: ``True`` if the IEC addre
  - `manual_iec_address` *(property)* — Gets or sets the manually assigned IEC address. Setting this to ``None`` will set :attr:`automatic_iec_address` to ``True``, setting this to an address will set

### `ScriptDeviceRepository`

> pass def import_vendor_description(self, stream: Stream, source: ScriptRepositorySource, source_path: str): """Import a device description file into a repository. .. warning:: The original C# function that is called with this method contains 2 overloads. It is strongly advised to pass *all* argument

- **ScriptDeviceRepository** (object)
  - Device respository.
  - `create_device_identification(self, type, id, version)` — Factory method for a :class:`DeviceId` object. :type type: int :param type: The device type. :type id: str :param id: The device id. :type version: str :rtype: 
  - `create_module_identification(self, type, id, version, module_id)` — Factory method for a :class:`ModuleId` object. :type type: int :param type: The device type. :type id: str :param id: The device id. :type version: str :type mo
  - `import_device(self, stream: Stream, source: ScriptRepositorySource, source_path: str, save_device_cache: bool = True): """Import a device description file into a repository.  .. warning:: The original C# function that is called with this method contains 3 overloads. It is strongly advised to pass *all* arguments with their respective keywords. ``stream``, ``path``, and ``source_path`` are not actually optional, they just aren't required in every overload. Pass them if your overload needs them!  :type stream: Stream :param stream: The System.IO.Stream that contains the device description. This must be a valid device description file. Other types of device descriptions must be imported by special plug-ins.  :type source: :class:`ScriptRepositorySource` :param source: The repository source where the device should be stored. This parameter may be ``None``, in which case the default repository source is used. The repository source must be one of the sources defined in :attr:`sources`.  :type source_path: str :param source_path: Sourcepath for the import. Relative file references inside the device description are resolved relative to this source path. May be empty, if the device description contains only absolute file references.  :type save_device_cache: bool :param save_device_cache: If ``True``, after removing the device the device cache is also written. If ``False``, the device cache is not written. If many devices are removed, this is much faster.  :rtype: :class:`DeviceId` :returns: The ID of the imported device description.  """ pass  def import_device(self, path: str, source: ScriptRepositorySource, save_device_cache: bool = True)` — Import a device description file into a repository. .. warning:: The original C# function that is called with this method contains 3 overloads. It is strongly a
  - `import_vendor_description(self, path: str, source: ScriptRepositorySource)` — Import a device description file into a repository. .. warning:: The original C# function that is called with this method contains 2 overloads. It is strongly a
  - `remove_device(self, device_id, source, save_device_cache=True)` — Remove a device from the specified repository source. :type device_id: :class:`DeviceId` :param device_id: Defines the device to remove. :type source: :class:`S
  - `remove_vendor_description(self, vendor_id, source)` — Remove a vendor description from the specified repository source. :type vendor_id: int :param vendor_id: The vendor id. :type source: :class:`ScriptRepositorySo
  - `save_device_cache(self)` — Saves the current devices in the device cache. Could be used to force it after adding or removing many devices.
  - `rebuild_device_cache(self)` — Rebuild the device cache. The device cache is deleted, initialized and saved.
  - `get_device_category(self, category_id: int)` — This overload is called when ``category_id`` is of type *int*. Get the device category with the specified device category ID. :type category_id: int :param cate
  - `get_device_category(self, category: Guid)` — This overload is called when ``category_id`` is of type *int*. Get the device category with the specified type GUID. :type category_id: Guid :param category_id:
  - `get_device_family(self, family)` — Device family. :type family: str :param family: ``VendorID:FamilyID``. :rtype: :class:`ScriptDeviceFamily`
  - `get_all_devices(self)` — Get a collection containing all devices in the repository. .. warning:: The original C# function that is called with this method contains 5 overloads. It is str
  - `get_all_devices(self, device_id: DeviceId)` — Get a collection containing all devices in the repository. .. warning:: The original C# function that is called with this method contains 5 overloads. It is str
  - `get_all_devices(self, source: ScriptRepositorySource)` — Get a collection containing all devices in the repository. .. warning:: The original C# function that is called with this method contains 5 overloads. It is str
  - `get_all_devices(self, device_id: DeviceId, source: ScriptRepositorySource)` — Get a collection containing all devices in the repository. .. warning:: The original C# function that is called with this method contains 5 overloads. It is str
  - `get_all_devices(self, name: str, source: ScriptRepositorySource)` — Get a collection containing all devices in the repository. .. warning:: The original C# function that is called with this method contains 5 overloads. It is str
  - `get_device(self, device_id)` — Get the device description with the specified device identification. :type device_id: :class:`DeviceId` :param device_id: Device identification. :rtype: :class:
  - `get_all_vendor_descriptions(self)` — Get a collection of all vendor descriptions in the repository. .. warning:: The original C# function that is called with this method contains 2 overloads. It is
  - `get_all_vendor_descriptions(self, source: ScriptRepositorySource)` — Get a collection of all vendor descriptions in the repository. .. warning:: The original C# function that is called with this method contains 2 overloads. It is
  - `get_vendor_description(self, vendor_id)` — Get the vendor description with the specified vendor Id. :type vendor_id: int :param vendor_id: Vendor Id. :rtype: :class:`ScriptVendorDescription` :returns: Th
  - `sources` *(property)* — Get the repository sources of the device repository. :rtype: :class:`ScriptRepositorySourceList`
- **ScriptRepositorySourceList** (list)
  - A collection of :class:`ScriptRepositorySource` objects.
  - `__getitem__(self, index)` — Get the :class:`ScriptRepositorySource` at the specified position or with the specified name. If there is no repository source at the specified position ``None`
  - `__getitem__(self, name)` — Get the :class:`ScriptRepositorySource` at the specified position or with the specified name. If there is no repository source with the specified name ``None`` 
  - `add(self, name, location_url)` — Add a new repository source with the specified name. :type name: str :param name: Name for the new source. :type location_url: str :rtype: :class:`ScriptReposit
  - `remove(self, source)` — Remove an existing repository source. Internal sources cannot be removed. :type source: :class:`ScriptRepositorySource` :param source: The repository source to 
  - `move(self, source, index)` — Move an existing repository source to the specified location in the collection. :type source: :class:`ScriptRepositorySource` :param source: Existing repository
  - `__len__(self)` — Gets the length (number of sources). :rtype: int
- **ScriptRepositorySource** (object)
  - Repository source.
  - `name(self, value: str)`
  - `location_url(self, value: str)`
  - `name` *(property)* — Get or set the name of the repository source. :rtype: str
  - `location_url` *(property)* — Get or set the location URL. :rtype: str
  - `is_internal` *(property)* — Return whether the repository source is internal. If true, then this repository source is an implicit source (like the project internal repository or the instal
- **ScriptDeviceCategory** (object)
  - Category of devices. Devices can be grouped into categories by means of the ``DeviceDescription/Device/DeviceInfo/Category`` tags of the device description file. One can implement a corresponding class of this interface to display these types in a user-friendly way.
  - `category_id` *(property)* — Id of the category. :rtype: int
  - `parent_category` *(property)* — The type GUID of the parent device category implementation, or ``Guid.Empty``, if this device implementation is top-level. :rtype: Guid
  - `name` *(property)* — Gets a user-friendly display name for this device category. This string should be localized. :rtype: str
  - `description` *(property)* — Gets a user-friendly description for this device category. This string should be localized. :rtype: str

### `ScriptDeviceUserManagement`

> If set, the particular _3S.CoDeSys.Core.Online.IDeviceUser or _3S.CoDeSys.Core.Online.IDeviceGroup can be edited.

- **DeviceUserManagementFlags** (Enum)
  - Flags for the entire _3S.CoDeSys.Core.Online.IDeviceUserList, the entire _3S.CoDeSys.Core.Online.IDeviceGroupList, a single _3S.CoDeSys.Core.Online.IDeviceUser, or a single _3S.CoDeSys.Core.Online.IDeviceGroup.
- **ScriptDeviceUserManagement** (object)
  - This object represents the user management on a given device.
  - `reload_from_program(self)` — Reloads the user management contents from the device object in the project.
  - `store_to_project(self)` — Writes the current contents of the user management back to the device object in the project. You should always use this method to persist your changes into the 
  - `upload(self)` — Uploads the user and group information from the device.
  - `download(self)` — Downloads the user and group information to the device.
  - `load(self, xml_or_file_name: str)` — Loads the contents of the given XML element into this user management object. :type xml_or_file_name: str :param xml_or_file_name: The XML document to read. If 
  - `load(self, element: XmlElement)` — Loads the contents of the given XML element into this user management object. :type element: XmlElement :param element: The element.
  - `save(self)` — Saves the contents of this user management object as XML into a string. :rtype: str :returns: A string containing the XML representation of this user management
  - `save(self, file_name)` — Saves the contents of this user management object as XML into a file. :type file_name: str :param file_name: The file name.
  - `save(self, writer=None)` — Saves the contents of this user management object as XML into an ``System.Xml.XmlWriter``. :type writer: XmlWriter :param writer: The writer.
  - `online_device` *(property)* — Gets the online device this user management was created from. :rtype: :class:`ScriptOnlineDevice`
  - `users` *(property)* — Gets the users on the device. Modifications of this list will take place offline and come into effect by downloading the user management to the device. :rtype: 
  - `groups` *(property)* — Gets the groups on the device. Modifications of this list will take place offline and come into effect by downloading the user management to the device. :rtype:
- **ScriptDeviceUserList** (list)
  - Represents a list of script device users.
  - `__len__(self)` — Gets the number of users in this list. :rtype: int
  - `__getitem__(self, index: int)` — Gets the user at the specified index or with the specified name. :type index: int :param index: The zero-based index. :rtype: :class:`ScriptDeviceUser` :returns
  - `__getitem__(self, name: str)` — Gets the user at the specified index or with the specified name. :type name: str :param name: The user name. :rtype: :class:`ScriptDeviceUser` :returns: The use
  - `add(self, name)` — Adds a new user with the specified name. :type name: str :param name: The name of the new user. :raises ArgumentException: A user with the specified name alread
  - `remove(self, name)` — Removes the user with the specified name. :type name: str :param name: The name of the existing user. :raises NotSupportedException: * Deleting existing users i
  - `clear(self)` — Removes all users. :raises NotSupportedException: Deleting existing users is not supported. Check :attr:`ScriptDeviceUser.flags` for the :attr:`DeviceUserManage
  - `flags` *(property)* — Gets flags concerning the entire user list. :rtype: DeviceUserManagementFlags
- **ScriptDeviceGroupList** (list)
  - A list of groups on the device.
  - `__len__(self)` — Gets the number of groups in this list. :rtype: int
  - `__getitem__(self, index)` — Gets the group at the specified index or with the specified name. :type index: int :param index: The zero-based index or the group name. :rtype: :class:`ScriptD
  - `__getitem__(self, name)` — Gets the group at the specified index or with the specified name. :type name: str :param name: The group name. :rtype: :class:`ScriptDeviceGroup` :returns: The 
  - `add(self, name)` — Adds a new group with the specified name. :type name: str :param name: The name of the group. :rtype: :class:`ScriptDeviceGroup` :returns: The newly created gro
  - `remove(self, name)` — Removes the group with the specified name. :type name: str :param name: The name of the existing group. :rtype: bool :returns: ``True`` if the group existed and
  - `clear(self)` — Removes all groups.
  - `flags` *(property)* — Gets flags concerning the entire group list. :rtype: :class:`DeviceUserManagementFlags`
- **ScriptDeviceUser** (object)
  - An user on this device.
  - `name(self, value: str)`
  - `set_password(self, password)` — Sets the password for this user. :type password: str :param password: The password to set.
  - `password_hash(self, value: str)`
  - `set_user_flags(self, flags)` — Sets flags for the user. :type flags: DeviceUserManagementFlags :param flags: The flags to set.
  - `flags` *(property)* — Gets flags concerning this particular user. :rtype: :class:`DeviceUserManagementFlags`
  - `name` *(property)* — Gets or sets the name of the user. :raises NotSupportedException: Editing this user is not supported. Check :attr:`flags` for the :attr:`DeviceUserManagementFla
  - `password_hash` *(property)* — Gets or sets the encrypted password for this user. :raises NotSupportedException: Editing this user is not supported. Check :attr:`flags` for the :attr:`DeviceU
- **ScriptDeviceGroup** (object)
  - A group of users, which have common rights on the device.
  - `name(self, value: str)`
  - `check_cyclic_membership(self, new_group_member)` — Checks whether adding the specified group member would cause a cyclic membership dependency. :type new_group_member: str :param new_group_member: The name of th
  - `flags` *(property)* — Gets flags concerning this particular group. :rtype: :class:`DeviceUserManagementFlags`
  - `name` *(property)* — Gets or sets the name of the group. :raises NotSupportedException: Editing this user is not supported. Check :attr:`flags` for the :attr:`DeviceUserManagementFl
  - `user_members` *(property)* — Gets the list of all user names which are members of this group. This list can be modifed in-place to add or remove users from this group. :rtype: list[string]
  - `group_members` *(property)* — Gets the list of all group names which are members of this group. This list can be modifed in-place to add or remove groups from this group. :rtype: list[str]

### `ScriptDriverInfo`

> Disable the always update of the variables.

- **AlwaysUpdateVariablesMode** (Enum)
  - Defines always mapping modes on a parameter or connectors.
- **ScriptDriverInfo** (object)
  - Provides access to the driver info of the device. Mostly the visible parts of the tab "PLC Settings" in the device editor.
  - `io_application(self, value: Guid)`
  - `set_io_application(self, application)` — Set the application which does the IO handling. :type application: :class:`ScriptApplication` :param application: Script object of the application.
  - `update_ios_while_in_stop(self, value: bool)`
  - `behaviour_for_outputs_on_stop(self, value: StopResetBehaviour)`
  - `user_program_for_stop_reset_behaviour(self, value: str)`
  - `always_update_variables(self, value: AlwaysUpdateVariablesMode)`
  - `set_bus_cycle_task(self, name: str)` — Set the bus cycle task by name or object guid or script object. :type name: str :param name: Name of the task.
  - `set_bus_cycle_task(self, object_guid: Guid)` — Set the bus cycle task by name or object guid or script object. :type guid: Guid :param guid: Object Guid of the task.
  - `set_bus_cycle_task(self, task: ScriptObject)` — Set the bus cycle task by name or object guid or script object. :type task: :class:`ScriptObject` :param task: Script Object of the task.
  - `generate_force_variables(self, value: bool)`
  - `enable_diagnosis(self, value: bool)`
  - `show_io_warnings_as_errors(self, value: bool)`
  - `can_set_io_application` *(property)* — Whether the IO application can be set. :rtype: bool
  - `io_application` *(property)* — Get/set the object Guid of the application which does the IO handling. :rtype: Guid
  - `update_ios_while_in_stop` *(property)* — Update IOs while in stop. :rtype: bool
  - `behaviour_for_outputs_on_stop` *(property)* — Get/set the behaviour for outputs on stop. :rtype: :class:`StopResetBehaviour`
  - `user_program_for_stop_reset_behaviour` *(property)* — Get/set the behaviour program for stop/reset if :attr:`behaviour_for_outputs_on_stop` is set to ``ExecuteProgram``. See also: StopResetBehaviour.ExecuteProgram 
  - `always_update_variables` *(property)* — Set the mode for (always) updating variables. :rtype: :class:`AlwaysUpdateVariablesMode`
  - `bus_cycle_task_by_name` *(property)* — Get the name of the bus cycle task. :rtype: str
  - `bus_cycle_task_by_guid` *(property)* — Get the object guid of the bus cycle task. :rtype: Guid
  - `generate_force_variables` *(property)* — Generate force variables for IO mapping. :rtype: bool
  - `enable_diagnosis` *(property)* — Enable diagnosis for devices. :rtype: bool
  - `show_io_warnings_as_errors` *(property)* — Show IO warnings as errors. :rtype: bool

### `ScriptDriverTraceImpl`

- **ScriptDriverTraceImpl** (object)
  - | Top level "trace" API. Offers actions, independent of concrete trace objects.
  - `create(self, parentObject: ScriptObject, traceName: str, taskName: str="")` — | Creates an empty trace object in the given project/application or project/device. | The Task of the trace object is set, if a task with the given taskname exi

### `ScriptExplicitConnectorObjects`

- **ScriptExplicitConnectorObjectsMarker** (object)
  - Decorator for marking an object as explicit connector or not. All objects within a project are decorated with this marker since V3.5.4.0. :version added: 3.5.4.0
  - `is_explicit_connector` *(property)* — Gets a value indicating whether this instance is a device object. :rtype: bool :returns: ``True`` if this instance is device object; otherwise, ``False``.
- **ScriptExplicitConnectorObject** (ScriptExplicitConnectorObjectsMarker, ScriptConnector)
  - Decorator for explicit connector objects. All objects within a project which are explicit connector objects are extended with this interface (since V3.5.4.0). :version added: 3.5.4.0
  - `allowed_interfaces_at(self, index)` — Get the name of the child interfaces that this device object can accept at the specified insert position. :type index: int :param index: The child index where a
  - `insert(self, name: str, index: int, device: DeviceId, module: str = None)` — Inserts the specified device at the specified index. :type name: str :param name: Name of the device. :type index: int :param index: index where to insert the d
  - `insert(self, name: str, index: int, type: int, id: str, version: str, module: str = None)` — Inserts the specified device at the specified index. :type name: str :param name: Name of the device. :type index: int :param index: index where to insert the d
  - `add(self, name: str, device: DeviceId, module: str = None)` — Adds the specified device. :type name: str :param name: Name of the device. :type device: :class:`DeviceId` :param device: The device id. :type module: str :par
  - `add(self, name: str, type: int, id: str, version: str, module: str = None)` — Adds the specified device. :type name: str :param name: Name of the device. :type type: int :param type: The device type. :type id: str :param id: The device id
  - `export_io_mappings_as_csv(self, file_path)` — Export the io mappings as a CSV file to the specified absolute path. :type file_path: str :param file_path: The absolute path of the file to export.
  - `import_io_mappings_from_csv(self, file_path)` — import the io mappings from a CSV file at the specified absolute path. :type file_path: str :param file_path: The absolute path of the file to import.
  - `driver_info` *(property)* — Get the driver info of the explicit connector. :version added: 3.5.15.0 :rtype: :class:`ScriptDriverInfo`

### `ScriptExternalFileObject`

> Changes on the physical file are automatically reflected in the embedded data.

- **ReferenceMode** (Enum)
- **AutoUpdateMode** (Enum)
  - This enumeration is used to control how changes in a physical file are reflected to the embedded data of a _3S.CoDeSys.Core.External.IFileReference.
- **ScriptExternalFileObjectMarker** (object)
  - Determines whether this object is an external file object or can contain them. :version added: 3.5.9.0
  - `is_external_file_object` *(property)* — Gets a value indicating whether this :class:`ScriptObject` is is an external file object. :rtype: bool :returns: ``True`` if it is an external file object; othe
  - `may_contain_external_file_objects` *(property)* — Gets a value indicating whether this :class:`ScriptObject` or :class:`ScriptProject` may contain external file objects. The project root may always contain exte
- **ScriptExternalFileObject** (ScriptExternalFileObjectMarker)
  - Provides the actual functionality of the external file objects. :version added: 3.5.9.0
  - `change_modes(self, reference_mode, auto_update_mode = AutoUpdateMode.Never)` — Changes the modes of the external file object. :type reference_mode: ReferenceMode :param reference_mode: The reference mode. :type auto_update_mode: AutoUpdate
  - `update(self)` — Updates this instance.
  - `calculate_checksum(self)` — Calculates the checksum of the data. :rtype: int :returns: The CRC 32 value of the data.
  - `get_data(self)` — Gets the data as a byte array. :rtype: list[byte]
  - `get_data(self, stream)` — Gets the data by writing it into the given stream. :type stream: Stream :param stream: The stream.
  - `get_data(self, filename)` — Gets the data by writing it to the specified filename. :type filename: str :param filename: The filename.
  - `create_edit_path(self)` — Gets the absolute path where this file reference is edited. This is the absolute path itself if the file reference is linked to a file system object, or a tempo
  - `file_path` *(property)* — Gets the file path. :rtype: str
  - `reference_mode` *(property)* — Gets the reference mode. :rtype: ReferenceMode
  - `auto_update_mode` *(property)* — Gets the auto update mode. :rtype: AutoUpdateMode
  - `last_modification` *(property)* — Gets the last modification date. :rtype: DateTime
  - `length` *(property)* — Gets the length of the data in bytes. :rtype: int
- **ScriptExternalFileObjectContainer** (ScriptExternalFileObjectMarker)
  - This interface is implemented by the project root, and by objects which can contain synchable external file objects. The project root may always contain external file objects, those are not downloaded to the devices. Devices and Applications may contain files which are synchroniz

### `ScriptFontDesc`

- **ScriptFontDesc** (object)
  - | Bundles the modifyable settings for a font.
  - `name` *(property)* — | Gets or sets the name of the font.
  - `size` *(property)* — | Gets or sets the size of the font.

### `ScriptIecLanguageObjectContainer`

> A Program.

- **PouType** (Enum)
  - Defines the type of the POU which is to be created. :version added: 3.5.9.0
- **DutType** (Enum)
  - Defines the type of the DUT which is to be created. :version added: 3.5.9.0
- **SpecialPouType** (Enum)
  - Defines the type of special POUs (with implicit checks) which have to be created. :version added: 3.5.12.10
- **ScriptIecLanguageObjectContainer** (object)
  - This allows objects to create POU like objects, the methods will be available in the project root as well as applications, and folders below them. The extended settings and specializations which are available in the "Add Object" dialog, but not available in this interface, can be
  - `create_pou(self, name: str, type: PouType = PouType.FunctionBlock, language: Guid = None, return_type: str = None, base_type: str = None, interfaces: str = None): """ Creates a POU with the specified name and type.  .. warning:: The original C# function that is called with this method contains 2 overloads. It is strongly advised to pass *all* arguments with their respective keywords.  :type name: str :param name: The name.  :type type: :class:`PouType` :param type: The type. Optional, the default is a function block.  :type language: Guid :param language: The language. Optional, the default is structured text.  :type return_type: str :param return_type: The return type. This is required for :attr:`PouType.Function`, and not allowed for other POU types.  :type base_type: str :param base_type: The base type. This is optional and only allowed for :attr:`PouType.FunctionBlock`.  :type interfaces: str :param interfaces: The implemented interface(s). This is optional and only allowed for :attr:`PouType.FunctionBlock`.  :raises Exception: Any exception which might occur (e. G. if the name is not an IEC identifier, or an object with the same name already exists within the same namespace, or the language guid is not valid, or the object cannot be created under this parent.  :rtype: :class:`ScriptObject` :returns: The ScriptObject of the newly created POU.  """ pass  def create_pou(self, type: SpecialPouType)` — Creates a POU with implicit checks according to the specified type. Adding a check function will provoke a full recompile and prohibit an online change. :versio
  - `create_function(self, name: str, return_type: str, language: Guid = None)` — Creates a function with the given name. :type name: str :param name: The name. :type return_type: str :param return_type: The return type :type language: Guid :
  - `create_function_block(self, name: str, language: Guid = None, base_type: str = None, interfaces: str = None)` — Creates a function block with the given name. :type name: str :param name: The name. :type language: Guid :param language: The language. Optional, the default i
  - `create_program(self, name: str, language: Guid = None)` — Creates a function block with the given name. :type name: str :param name: The name. :type language: Guid :param language: The language. Optional, the default i
  - `create_gvl(self, name)` — Creates a GVL with the specified name. :type name: str :param name: The name. :raises Exception: Any exception which might occur (e. G. if the name is not an IE
  - `create_dut(self, name, type=DutType.Structure, baseType=None)` — Creates a DUT with the specified name and type. As with manual object creation in the UI, enums will get the attribute 'strict' with compiler versions >= 3.5.7.
  - `create_interface(self, name, baseInterfaces="__System.IQueryInterface")` — Creates an interface with the specified name. :type name: str :param name: The name. :type baseInterfaces: str :param baseInterfaces: The base interfaces (comma
  - `create_persistentvars(self, name)` — Creates a persistent GVL with the specified name. :type name: str :param name: The name. :raises Exception: Any exception which might occur (e. G. if the name i
- **ScriptIecLanguageMemberContainer** (object)
  - This allows objects to create POU like member objects, the methods will be available on POUs, Interfaces, GVLs, and folders below them. The extended settings and specializations which are available in the "Add Object" dialog, but not available in this interface, can be implemente
  - `create_property(self, name, return_type="int", language=None)` — Creates a property with the specified name and type. :type name: str :param name: The name. :type return_type: str :param return_type: The return type. :type la
  - `create_method(self, name, return_type=None, language=None)` — Creates a method with the specified name and type. Methods cannot be added to GVLs or Functions. :type name: str :param name: The name. :type return_type: str :
  - `create_action(self, name, language=None)` — Creates an action with the specified name and type. Actions cannot be added to GVLs or Functions. :type name: str :param name: The name. :type language: Guid or
  - `create_transition(self, name, language=None)` — Creates an transition with the specified name and type. Transitions cannot be added to GVLs or Functions. :type name: str :param name: The name. :type language:
- **ScriptImplementationLanguage** (object)
  - Defines the Guids for the standard IEC 61131-3 languages and those available as CODESYS extensions. An instance of this interface will be injected with the name "ImplementationLanguages". :version added: 3.5.9.0
  - `st` *(property)* — Gets the language guid for ST / Structured Text. :rtype: Guid
  - `cfc` *(property)* — Gets the language guid for CFC / Continous Flow Chart (free layout FUP). :rtype: Guid
  - `page_oriented_cfc` *(property)* — Gets the language guid for Page oriented CFC / Continous Flow Chart (free layout FUP). :rtype: Guid
  - `fbd` *(property)* — Gets the language guid for FBD / Function Block Diagram (FBS). :rtype: Guid
  - `instruction_list` *(property)* — Gets the language guid for IL / Instruction List (AWL). :rtype: Guid
  - `ladder` *(property)* — Gets the language guid for LD / Ladder Diagram (KOP). :rtype: Guid
  - `sfc` *(property)* — Gets the language guid for SFC / Secuential Function Chart (AS). Currently, SFC cannot be used for :meth:`ScriptIecLanguageObjectContainer.create_pou` with :att
  - `uml_statechart` *(property)* — Gets the language guid for the uml statechart. The UML AddOn needs to be installed for this language. See also: http://store.codesys.com/codesys-uml.html :rtype

### `ScriptImagePoolObject`

> This value means that the image is linked from the project only.

- **ImageLinkType** (Enum)
  - This enumeration represents the way an image is embedded or linked into a project. :version added: 3.5.9.0
- **ScriptImagePoolMarker** (object)
  - Marker object to check whether an ScriptObject is an imagepool object. :version added: 3.5.9.0
  - `is_imagepool` *(property)* — Gets a value indicating whether this ScriptApplicationMarker is an imagepool. :rtype: bool :returns: ``True`` if it is an imagepool; otherwise, ``False``
- **ScriptImagePoolObject** (ScriptImagePoolMarker)
  - ScriptObjects which are an imagepool object are extended with this interface. :version added: 3.5.9.0
  - `download_only_used_images(self, value: bool)`
  - `imagepool_is_internal(self, value: bool)`
  - `symboltextlist(self, value: str)`
  - `images` *(property)* — Gets the collection of the items currently configured within this imagepool. :rtype: :class:`ScriptImagePoolItems`
  - `download_only_used_images` *(property)* — Gets or sets a value whether all images or only the explicitly referenced ones should be downloaded to PLCs. :rtype: bool
  - `imagepool_is_internal` *(property)* — Gets or sets a value whether this image pool is visible for projects embedding the current one as a library. This is not relevant when working on a project itse
  - `symboltextlist` *(property)* — Gets and sets the name of the text list for translation of the symbols in this image pool. :rtype: str
- **ScriptImagePoolItems** (list)
  - Gets the current number of items in this image pool. :version added: 3.5.9.0
  - `__len__(self)` — Gets the current number of items in this image pool. :rtype: int
  - `__getitem__(self, index: int)` — Returns the item with the given index or id. :type index: int :param index: The index of the item to return or the id to search for. :raises ArgumentOutOfRangeE
  - `__getitem__(self, id: str)` — Returns the item with the given index or id. :type id: str :param id: The id to search for. :raises KeyNotFoundException: Thrown when the given id is not contai
  - `add(self, id, path, linktype, updateMode=None)` — Adds a new image to the current image pool. :type id: str :param id: The id to assign to the newly inserted image. Must not yet be existing. :type path: str :pa
  - `remove(self, id)` — Removes the :class:`ScriptImagePoolItem` with the given ``id``. :type id: str :param id: description :raises KeyNotFoundException: Thrown when no entry with the
  - `move(self, indexSrc, indexDst)` — Moves a :class:`ScriptImagePoolItem` in the list of items. :type indexSrc: int :param indexSrc: The index of the item that should be moved. :type indexDst: int 
- **ScriptImagePoolItem** (object)
  - An item (in fact like a line) within a :class:`ScriptImagePoolObject`. :version added: 3.5.9.0
  - `id(self, value: str)`
  - `filepath(self, value: str)`
  - `linktype(self, value: ImageLinkType)`
  - `updatemode(self, value: AutoUpdateMode)`
  - `id` *(property)* — The identification of the image that can be accessed in the visualization too. :raises ArgumentException: Thrown when the id is being set and the new id is alre
  - `filepath` *(property)* — The path of the referenced image. Relevant only if :attr:`linktype` yields :attr:`ImageLinkType.Linked` or :attr:`ImageLinkType.EmbeddedAndLinked`. :rtype: str
  - `linktype` *(property)* — The way the image is referenced. :rtype: :class:`ImageLinkType`
  - `updatemode` *(property)* — The way the image is updated automatically while the project is open. Relevant only if :attr:`linktype` yields :attr:`ImageLinkType.EmbeddedAndLinked`. :rtype: 
- **ScriptImagePoolObjectContainer** (object)
  - Projects and Application Objects are extended with this interface since CoDeSys V3.5.9.0. :version added: 3.5.9.0
  - `create_imagepool(self, name=None)` — Creates a new image pool object in the current context (either application or project global). :type name: str :param name: The name of the new imagepool object
  - `get_global_imagepool(self)` — Returns the global image pool object or creates a new one if not yet existing. Typically this method can be called on projects only. Only in case of special cus
  - `has_global_imagepool` *(property)* — Checks whether there is already a globalimagepool in the current location. Only in case of special customizations of the programming system, it is allowed to ca

### `ScriptLibManObject`

- **LibManager** (object)
  - An instance implementing this interface is injected into the scriptengine scope under the name library manager.
  - `insert_repository(self, rootfolder, name, index=-1)` — Creates a new library repository. :type rootfolder: str :param rootfolder: The rootfolder for the repository (this must be the full path to an existing director
  - `move_repository(self, repository, new_index)` — Move_repositories the specified repository to a new position in the list. Use this to manipulate the search order. :type repository: :class:`LibRepository` :par
  - `remove_repository(self, repository, delete_on_disk=False)` — Removes the specified repository. :type repository: :class:`LibRepository` :param repository: The repository. :type delete_on_disk: bool :param delete_on_disk: 
  - `update_repository(self, repository, new_name=None, new_location=None, copy_libraries=False)` — Update the specified repository. :type repository: :class:`LibRepository` :param repository: The repository. :type new_name: str :param new_name: The new name. 
  - `get_file_path(self, library)` — Gets the file path of the specified library in the library repository. :type library: :class:`ManagedLib` :param library: The library. :rtype: str :returns: The
  - `get_category(self, guid)` — Gets the category with the specified GUID. :type guid: Guid :param guid: The GUID. :rtype: :class:`LibCategory` :returns: The library category.
  - `install_library(self, filepath, repository=None, overwrite=False)` — Installs the library with the specified filepath. :type filepath: str :param filepath: The filepath of the library to install. :type repository: :class:`LibRepo
  - `uninstall_library(self, repository, library)` — Uninstalls a library from the specified repository. :type repository: :class:`LibRepository` :param repository: The repository. :type library: :class:`ManagedLi
  - `get_library(self, name, repository)` — Gets all libraries with the specified name. :type name: str :param name: The name. :type repository: :class:`LibRepository` :param repository: The repository. I
  - `get_all_libraries(self, repository: LibRepository)` — This override is used when parameter is of type *LibRepository*. Gets all libraries. :type repository: :class:`LibRepository` :param repository: The repository.
  - `get_all_libraries(self, exclude_shadowed_libs: bool = True)` — This override is used when parameter is of type *bool*. Gets all libraries. :type exclude_shadowed_libs: bool :param exclude_shadowed_libs: If set to ``True``, 
  - `find_library(self, display_name)` — Finds the library with the specified display_name. :type display_name: str :param display_name: The display name to search for. :rtype: tuple [:class:`ManagedLi
  - `repositories` *(property)* — Gets the list of available library repositories. The order of those repositories is configurable by the user in the dialog and the script. This list is a snapsh
  - `categories` *(property)* — Gets all the known library categories. :rtype: tuple[:class:`LibCategory`] :returns: All the known library categories.
  - `top_level_categories` *(property)* — Gets the all known top level library categories. :rtype: tuple[:class:`LibCategory`] :returns: All known top level library categories.
- **LibRepository** (object)
  - Description class for a library repository.
  - `editable` *(property)* — Gets a value indicating whether this LibRepository is editable. The default system library repository is not editable - that means, it cannot be removed from th
  - `name` *(property)* — Gets the name of the repository. :rtype: str
  - `root_folder` *(property)* — Gets the root folder of the repository. :rtype: str
- **ManagedLib** (object)
  - Description class for a managed library.
  - `displayname` *(property)* — Display name. :rtype: str
  - `company` *(property)* — Company. :rtype: str
  - `title` *(property)* — Title. :rtype: str
  - `version` *(property)* — Version. :rtype: Version
  - `default_namespace` *(property)* — Default namespace. :rtype: str
  - `dependencies` *(property)* — Gets the dependencies as a list of strings. :rtype: tuple[str]
  - `categories` *(property)* — Gets the categories. Gets the list of :class:`LibCategory`. :rtype: tuple[:class:`LibCategory`]
- **LibCategory** (object)
  - Information about a library category.
  - `guid` *(property)* — Gets the guid identifying the category. :rtype: Guid
  - `parent` *(property)* — Gets the parent category, or None if the category is top level. :rtype: :class:`LibCategory`
  - `default_name` *(property)* — Gets the default name. :rtype: str
  - `name` *(property)* — Gets the localized name, or the default name if no localized name is available. :rtype: str
  - `localized_name` *(property)* — Gets the localized name for the current UI culture. :rtype: str
  - `version` *(property)* — Version. :rtype: Version
- **ScriptLibManObjectMarker** (object)
  - Every ScriptObject instance will be extended with this method. :version added: 3.4.3.0
  - `is_libman` *(property)* — Gets a value indicating whether this instance is a lib man object. :rtype: bool :returns: ``True`` if this instance is lib man object, otherwise ``False``.
- **ScriptLibManObject** (ScriptLibManObjectMarker)
  - Functionality for manipulating library managers. All objects implementing LibManObject will be extended with this methods.
  - `get_libraries(self, recursive=False)` — Returns a list of all libraries. :type recursive: bool :param recursive: If set to ``True``, sublibraries are also queried recursively. :rtype: list [str] :retu
  - `add_library(self, name: str)` — Adds the library with the specified name. :type name: str :param name: The name of the library.
  - `add_library(self, library: ManagedLib)` — Adds a reference to the specified library. :type library: :class:`ManagedLib` :param library: The library (since V3.5.5.0).
  - `add_placeholder(self, name: str, default_resolution: str)` — Adds a placeholder for a library with the specified name. :type name: str :param name: The name. :type default_resolution: str :param default_resolution: The de
  - `add_placeholder(self, name: str, default_resolution: ManagedLib)` — Adds a placeholder with the specified default resolution. :type name: str :param name: The name. :type default_resolution: :class:`ManagedLib` :param default_re
  - `remove_library(self, name)` — Removes the librariy with the specified name. :type name: str :param name: The name.
  - `references` *(property)* — Gets the collection of the references currently configured within this library manager. :version added: 3.5.5.0 :rtype: :class:`ScriptLibraryReferences`
- **ScriptLibraryReferences** (list)
  - The references currently managed by the library manager.
  - `__len__(self)` — Gets the current number of items in this library manager. :rtype: int :returns: The number of items.
  - `__getitem__(self, name: str)` — Gets the :class:`ScriptLibraryReference` with the specified name. :type name_or_id: str :rtype: :class:`ScriptLibraryReference`
  - `__getitem__(self, id: int)` — Gets the :class:`ScriptLibraryReference` with the specified id. :type id: int :rtype: :class:`ScriptLibraryReference`
- **ScriptLibraryReference** (object)
  - A library reference in the library manager.
  - `namespace(self, value: str)`
  - `get_dependencies(self)` — Gets the dependencies of this library. For libraries containing cyclic dependencies, this may lead to an endless recursion. :rtype: list[:class:`ScriptLibraryRe
  - `hide_when_referenced_as_dependency(self, value: bool)`
  - `publish_symbols_in_container(self, value: bool)`
  - `qualified_only(self, value: bool)`
  - `optional(self, value: bool)`
  - `id` *(property)* — Id. :rtype: int
  - `is_placeholder` *(property)* — Gets a value indicating whether this ScriptLibraryReference is a placeholder. :rtype: bool :returns: ``True`` if it is a placeholder, otherwise ``False``.
  - `is_managed` *(property)* — Gets a value indicating whether this ScriptLibraryReference is a managed reference to a fixed library version. :rtype: bool
  - `name` *(property)* — Gets the name of this library. For managed items, this follows the pattern "Name, Version (Company)". For placeholder items, this name follows the pattern "#Nam
  - `namespace` *(property)* — Gets or sets the namespace for this library. :rtype: str
  - `system_library` *(property)* — Gets a boolean value indicating whether this library is a system library or not. System libraries have been added implicitly by plug-ins whereas non-system libr
  - `parameters` *(property)* — Gets the library parameter set. If a global variable list containing only constant values has the attribute 'parameterlist', its content may be modified in the 
  - `hide_when_referenced_as_dependency` *(property)* — Gets or sets a value indicating whether this library node should be hidden in the user interface if it a direct or indirect dependency of a top-level library no
  - `publish_symbols_in_container` *(property)* — Gets or sets the qualified-only flag. If set, the name of the library is mandatory for any access to the library content. The default is true. :rtype: bool
  - `qualified_only` *(property)* — Gets or sets the qualified-only flag. If set, the name of the library is mandatory for any access to the library content. Defaults to ``True``. :rtype: bool
  - `optional` *(property)* — Gets or sets the optional flag. Libraries which are optional are not reported to the user as missing if they do not exist. :rtype: bool
- **ScriptManagedLibraryReference** (ScriptLibraryReference)
  - A managed library reference which points to a fixed version of the library. :attr:`ScriptLibraryReference.is_managed` is true for those instances.
  - `managed_library` *(property)* — Gets the managed library. :rtype: :class:`ManagedLib`
- **ScriptPlaceholderReference** (ScriptLibraryReference)
  - A placeholder reference. :class`ScriptLibraryReference` instances with :attr:`ScriptLibraryReference.is_placeholder` == True implement this interface.
  - `default_resolution(self, value: str)`
  - `get_redirection(self)` — Gets the redirection setting for this library. :rtype: str :returns: The redirection.
  - `set_redirection(self, fixed_resolution = "")` — Sets the redirection for this library. :type fixed_resolution: str :param fixed_resolution: The fixed resolution. Use ``None`` or an empty string to delete the 
  - `placeholder_name` *(property)* — Gets the name of the placeholder. In contrast to :attr:`ScriptLibraryReference.name`, this name does not include the leading '#' character. :rtype: str
  - `default_resolution` *(property)* — Gets or sets the default resolution of the library. :rtype: str
  - `effective_resolution` *(property)* — Effective resolution. :rtype: str
  - `is_redirected` *(property)* — Gets a value indicating whether this ScriptPlaceholderReference is redirected. :rtype: bool
  - `resolution_info` *(property)* — Gets a human readable information how this placeholder is resolved. :rtype: str
  - `resolver_guid` *(property)* — Gets a machinable readable information how this placeholder is resolved. :rtype: Guid
- **ScriptLibraryParameters** (list)
  - The library parameters interface. This is a sequence of the parameter names. If a global variable list containing only constant values has the attribute 'parameterlist', its content may be modified in the referencing project using this mechanism.
  - `__len__(self)` — Gets the length (number of parameters). :rtype: int
  - `__getitem__(self, name)` — Gets the parameter with the specified name. :type name: str :rtype: str
  - `__setitem__(self, name, expression: str)` — Sets the parameter with the specified name to an valid IEC expression. :type name: str :rtype: str
- **ScriptLibManObjectContainer** (object)
  - Projects and Application Objects are extended with this interface. :version added: 3.5.2.0
  - `get_library_manager(self)` — Gets the library manager for this application or project, implicitly creating one if none is existing yet. :rtype: :class:`ScriptObject` :returns: The library m
  - `has_library_manager` *(property)* — Gets a value indicating whether this ScriptLibManObjectContainer has a library manager. :rtype: bool :returns: ``True`` if there is a library manager, otherwise

### `ScriptLiveDeviceUserManagement`

- **ScriptLiveDeviceUserManagement** (object)
  - This object represents the live user management on a given device. :version added: 3.5.16.0
  - `upload(self)` — Uploads the user and group information from the device.
  - `backup(self, directory, password)` — Backups the user management from the device. Don't change the name of the backup file because the device uses a fixed file name. Use different directories to st
  - `restore(self, path, password)` — Restores the user management to the device. .. note:: After the restore of the user management it is possible to get an authentication exception during the next
  - `add_user(self, name, password, can_change_password=True, must_change_password=False)` — Adds a new user with the specified name. :type name: str :param name: The name of the new user. :type password: str :param password: Password for the new user. 
  - `remove_user(self, name)` — Removes the user with the specified name. :type name: str :param name: The name of the existing user.
  - `set_user_password(self, name, password)` — Sets the password for this user. :type name: str :param name: The name of the user. :type password: str :param password: The password to set.
  - `set_user_flags(self, name, flags)` — Sets flags for the user. :type name: str :param name: The name of the user. :type flags: :class:`DeviceUserManagementFlags` :param flags: The flags to set.
  - `add_group(self, name, group_members, user_members)` — Adds a new group with the specified name. :type name: str :param name: The name of the new group. :type group_members: list[str] :param group_members: The group
  - `remove_group(self, name)` — Removes the group with the specified name. :type name: str :param name: The name of the existing group.
  - `set_members_of_group(self, name, group_members, user_members)` — Sets the members of groups and users which shall be in the group. :type name: str :param name: The name of the group. :type group_members: list[str] :param grou
  - `online_device` *(property)* — Gets the online device this user management is using. :rtype: :class:`ScriptOnlineDevice`
  - `users` *(property)* — Gets the users on the device. :rtype: :class:`ScriptLiveDeviceUserList`
  - `groups` *(property)* — Gets the groups on the device. :rtype: :class:`ScriptLiveDeviceGroupList`
- **ScriptLiveDeviceUserList** (list)
  - Represents a list of script device users. :version added: 3.5.16.0
  - `__getitem__(self, index)` — Gets the user at the specified index or with the specfied name. :type index: int :param index: The zero-based index. :rtype: :class:`ScriptLiveDeviceUser` :retu
  - `__getitem__(self, name)` — Gets the user at the specified index or with the specfied name. :type name: str :param name: The name of the user. :rtype: :class:`ScriptLiveDeviceUser` :return
  - `__len__(self)` — Gets the number of users in this list. :rtype: int
  - `flags` *(property)* — Gets flags concerning the entire user list. :rtype: :class:`DeviceUserManagementFlags`
- **ScriptLiveDeviceGroupList** (list)
  - A list of groups on the device. :version added: 3.5.16.0
  - `__getitem__(self, index)` — Gets the group at the specified index or with the specfied name. :type index: int :param index: The zero-based index. :rtype: :class:`ScriptLiveDeviceGroup` :re
  - `__getitem__(self, name)` — Gets the group at the specified index or with the specfied name. :type name: str :param name: The name of the group. :rtype: :class:`ScriptLiveDeviceGroup` :ret
  - `__len__(self)` — Gets the number of groups in this list. :rtype: int
  - `flags` *(property)* — Gets flags concerning the entire group list. :rtype: :class:`DeviceUserManagementFlags`
- **ScriptLiveDeviceUser** (object)
  - An user on the device. :version added: 3.5.16.0
  - `flags` *(property)* — Gets flags concerning this particular user. :rtype: :class:`DeviceUserManagementFlags`
  - `name` *(property)* — Gets the name of the user. :rtype: str
- **ScriptLiveDeviceGroup** (object)
  - A group of users, which have common rights on the device. :version added: 3.5.16.0
  - `check_cyclic_membership(self, new_group_member)` — Checks whether adding the specified group member would cause a cyclic membership dependency. :type new_group_member: str :param new_group_member: The name of th
  - `flags` *(property)* — Gets flags concerning this particular group. :rtype: :class:`DeviceUserManagementFlags`
  - `name` *(property)* — Gets the name of the group. :rtype: str
  - `user_members` *(property)* — Gets the user names which are member of this group. :rtype: tuple[str]
  - `group_members` *(property)* — Gets the group names which are member of this group. :rtype: tuple[str]

### `ScriptObject`

> pass def import_xml(self, dataOrPath, conflictResolve=None, import_folder_structure=False, reporter=None): """Imports the contents of the specified PLCopenXML file als children of the current object. The heuristics to find out whether the content is a file or directly an XML string currently is as f

- **ScriptObject** (ScriptTreeObject)
  - Modelling of a script object. They compare equal if Guid and ProjectHandle (inherited from ScriptTreeObject) are equal.
  - `get_name(self, resolve_localized_display_name=False)` — Gets the name of the object. :type resolve_localized_display_name: bool :param resolve_localized_display_name: if set to ``True``, the name is localized. :rtype
  - `rename(self, stNewName)` — Renames the object to the new name. :type stNewName: str :param stNewName: New name of the object.
  - `remove(self)` — Removes this instance.
  - `move(self, new_parent: ScriptObject, new_index: int = -1)` — Moves the object to the specified new parent. :type new_parent: :class:`ScriptObject` :param new_parent: The new parent. :type new_index: int :param new_index: 
  - `move(self, new_parent: ScriptProject, new_index: int = -1)` — Moves the object to the specified new parent. :type new_parent: :class:`ScriptProject` :param new_parent: The new parent. :type new_index: int :param new_index:
  - `export_native(self, destination, recursive=True, profile_name=None, reporter=None)` — Export the specified objects in the CoDeSys native export format. :version added: 3.4.4.0 :type destination: str :param destination: The destination file. :type
  - `import_native(self, filenames, filter=None, handler=None)` — Imports the specified files in the native xml format in under the current node. :version added: 3.4.4.0 :type filenames: str or list :param filenames: The filen
  - `create_folder(self, foldername)` — Creates a folder with the specified foldername in the structured view of the parent node. The Modules View currently does not support folders, so creating folde
  - `get_signature_crc(self, application=None, default_value=None)` — Gets the signature CRC of the specified pou. A successful build is needed for this method to work. For POUs which are defined below an application, compile the 
  - `type` *(property)* — Gets the type guid. :rtype: Guid
  - `guid` *(property)* — Gets the GUID of the object. :rtype: Guid
  - `embedded_object_types` *(property)* — Gets the embedded onject types. :rtype: list[Guid]
  - `index` *(property)* — Gets the index. :rtype: int
  - `is_folder` *(property)* — Gets a value indicating whether this instance is a folder. :rtype: bool
  - `parent` *(property)* — Gets the parent ScriptObject, or the Project if we are top-level. You can use the is_root property implemented by objects and projects to distinct between the t
  - `build_properties` *(property)* — Gets the build properties of the object, or None. Not all objects have editable build properties - this method returns None when the object does not have any bu
  - `effectively_excluded_from_build` *(property)* — Gets a boolean indicating whether this object is effectively excluded from the build. An object is effectively excluded if either the object itsself or any of i
  - `exclusion_from_build_is_inherited` *(property)* — Gets a boolean indicating whether the build exclusion is inherited from a parent object. :version added: 3.5.7.0 :rtype: bool
- **ScriptBuildProperties** (object)
  - Defining the build properties of objects contributing to the compiler. Note that some objects do not define all of those properties. For example, folders only allow the :meth:`exclude_from_build` property to be set (which is inherited to POUs below that folder), and devices may o
  - `external(self, value: bool)`
  - `enable_system_call(self, value: bool)`
  - `compiler_defines(self, value: str)`
  - `link_always(self, value: bool)`
  - `exclude_from_build(self, value: bool)`
  - `external` *(property)* — Gets or sets the External-flag. A POU with this flag is supposed to be linked in runtime system. Check the :meth:`external_is_valid` property whether this prope
  - `external_is_valid` *(property)* — Gets wether the :meth:`external` property is valid for this object or not. :rtype: bool
  - `enable_system_call` *(property)* — Gets or sets the Enable system call-flag. A POU with this flag can be called by C-Code out of the runtime system Check the :meth:`enable_system_call_is_valid` p
  - `enable_system_call_is_valid` *(property)* — Gets whether the :meth:`enable_system_call` property is is valid for this object or not. :rtype: bool
  - `compiler_defines` *(property)* — Gets or sets compilerdefines for the object. The defines may be a list of comma seperated defines like this: DEF1, DEF2='value' For simple objects the scope of 
  - `compiler_defines_is_valid` *(property)* — Gets whether the :meth:`compiler_defines` property is valid for this object or not. :rtype: bool
  - `link_always` *(property)* — Gets or sets the flag for linking an object in any case. If ``true`` is assigned, the object will be linked into the application even when it is not referenced 
  - `link_always_is_valid` *(property)* — Gets whether the :meth:`link_always` property is valid for this object or not. :rtype: bool
  - `exclude_from_build` *(property)* — Gets or sets the flag Exclude from build. Objects which are excluded from the build will be ignored by the compiler. In other words, the language model of an ob
  - `exclude_from_build_is_valid` *(property)* — Gets whether the :meth:`exclude_from_build` property is valid for this object or not. :rtype: bool
- **ScriptProjectInfoMarker** (object)
  - The all objects are extended with this interface, since CoDeSys V3.5 SP2. :version added: 3.5.2.0
  - `is_project_info` *(property)* — Gets a value indicating whether this :obj:`ScriptProjectInfoMarker` is the project info object. :rtype: bool
- **ScriptTransientObjectMarker** (object)
  - All script objects are extended with this interface
  - `is_transient_object` *(property)* — Gets a value indicating whether this :obj:`ScriptTransientObjectMarker` is a transient object. :rtype: bool
- **ScriptProjectInfoObject** (ScriptProjectInfoMarker)
  - The project information objects are extended with this interface, since CoDeSys V3.5 SP2. :version added: 3.5.2.0
  - `change_accessor_generation(self, generate_accessors)` — Changes the generate_accessor flag. As changing this flag is potentially expensive (genrating several POUs), it is an explicit function and no property setter. 
  - `company(self, value: str)`
  - `title(self, value: str)`
  - `version(self, value: object)`
  - `released(self, value: bool)`
  - `author(self, value: str)`
  - `description(self, value: str)`
  - `dongle_licencing_active(self, value: bool)`
  - `dongle_licensing_firm_code(self, value: int)`
  - `dongle_licensing_product_code(self, value: int)`
  - `dongle_licensing_activation_url(self, value: str)`
  - `dongle_licensing_activation_mail(self, value: str)`
  - `generate_accessors` *(property)* — Gets a value indicating whether this :obj:`ScriptProjectInfoObject` generates property accessor POU objects or not. :returns: ``true` if accessor functions are 
  - `company` *(property)* — Gets or sets the company. Libraries are uniquely identified by the tuple <:meth:`company`, :meth:`title`, :meth:`version`> :rtype: str
  - `title` *(property)* — Gets or sets the title. Libraries are uniquely identified by the tuple <:meth:`company`, :meth:`title`, :meth:`version`>. :rtype: str
  - `version` *(property)* — Gets or sets the version. remarks :rtype: Version or str or tuple[int] or Sequence[int] :returns: The version. This returns a System.Version instance. For setti
  - `released` *(property)* — Gets or sets a value indicating whether the project containing this :obj:`ScriptProjectInfoObject` is released. Released library projects should not be modified
  - `categories` *(property)* — If the project is used as a library, it appears under the following categories. :rtype: list[LibCategory]
  - `default_namespace` *(property)* — Gets or sets the default namespace when the project is used as a library. :rtype: str
  - `author` *(property)* — Gets or sets the author. :rtype: str
  - `description` *(property)* — Gets or sets the description. This string may be multiline. :rtype: str
  - `dongle_licencing_active` *(property)* — Gets or sets a value indicating whether this library has dongle license protection. If dongle licensing is activated, the user needs to connect a dongle contain
  - `dongle_licensing_firm_code` *(property)* — Gets or sets the dongle licensing firm code. If dongle licensing is activated, the user needs to connect a dongle containing the appropriate license in order to
  - `dongle_licensing_product_code` *(property)* — Gets or sets the dongle licensing product code. If dongle licensing is activated, the user needs to connect a dongle containing the appropriate license in order
  - `dongle_licensing_activation_url` *(property)* — Gets or sets the dongle licensing activation email address. :rtype: str
  - `dongle_licensing_activation_mail` *(property)* — Gets or sets the dongle licensing activation email address. :rtype: str
  - `values` *(property)* — Gets the custom property dictionary. The following types are allowed: ============= ============================================================================

### `ScriptOnline`

> The kinds of authentication allowed for the fallback to the default handler.

- **OnlineChangeOption** (Enum)
  - Online change options used for multiple download.
- **ApplicationState** (Enum)
  - Execution state of an application.
- **OperatingState** (Enum)
  - The global state of an application. Although not defined as such, this enumeration is treated like a flags field, so the effective value may be a combination of more of these values.
- **ResetOption** (Enum)
  - This enum defines the different kinds of reset (warm, cold, origin)
- **BlockDriverType** (Enum)
  - An enumeration to specify the type of Block Driver used on the runtime system
- **ParamType** (Enum)
  - Enumeration defining allowed types for a gateway parameter. The types match the equally named .NET types.
- **AdditionalDirInfo** (Enum)
  - Flags to get additional information about a file or directory.
- **ScriptOnline** (object)
  - Online functionality for the ScriptEngine. Some of the commands may temporarily change the active application.
  - `create_online_application(self, application=None)` — Creates an online application. To prevent resource leaks, script writers should wrap the usage of the online application in a with: block. :type application: :c
  - `create_online_device(selfself, device=None)` — Creates an online device. To prevent resource leaks, script writers should wrap the usage of the online device in a with: block. :type device: ScriptObject :par
  - `set_default_credentials(self, username, password=None)` — Sets the default credentials for login to devices. This setting is in effect until the end of the current script execution. Use None for the username and omit t
  - `set_specific_credentials(self, target, username, password=None)` — Sets the default credentials for login to a specific device. This setting is in effect until the end of the current script execution. Use None for the username 
  - `clear_all_credentials(self)` — Clears all credentials which were set by this script. This only clears the cretentials at the level of the script. The online manager and other components may c
  - `auth_fallback_modes(self, value: CredentialSourceKind)`
  - `register_trusts_certificate(self, device_object, callback, current_node_name=None)` — Register a callback which allows to specify if the certificate of a PLC is trusted for the encrypted communication. :version added: 3.5.17.0 :type device_object
  - `unregister_trusts_certificate(self, device_object, current_node_name=None)` — Unregister a previously registered callback which allowed to specify if the certificate of a PLC is trusted for the encrypted communication. Use the same parame
  - `unregister_all_trusts_certificate(self)` — Unregister all previously registered callbacks which allowed to specify if the certificate of a PLC is trusted for the encrypted communication. :version added: 
  - `UNFORCE` *(property)* — Special value for unforcing a variable. It is returned by :meth:`ScriptOnlineApplication.get_prepared_value` and can be fed to :meth:`ScriptOnlineApplication.se
  - `UNFORCE_RESTORE` *(property)* — Special value for unforcing and restoring a variable. It is returned by :meth:`ScriptOnlineApplication.get_prepared_value` and can be fed to :meth:`ScriptOnline
  - `auth_fallback_modes` *(property)* — Gets or sets the setting how authentication credentials are acquired when no default credentials are set, and no specific credentials match the target. This set
  - `gateways` *(property)* — Gets all currently known gateways. :version added: 3.5.8.0 :rtype: :class:`ScriptGateways` :returns: A python tuple containing the gateways.
  - `gateway_drivers` *(property)* — Gets the gateway drivers. :version added: 3.5.8.0 :rtype: :class:`ScriptGatewayDrivers` :returns: A python tuple containing all gateway drivers.
- **ScriptOnlineApplication** (object)
  - Online application object. Some of the commands may temporarily change the active application. This object keeps an internal connection to the device, so it should be disposed when you don't need it any more: Call the Dispose() method when you're done with it, or - even better - 
  - `login(self, change_option, delete_foreign_apps)` — Performs the application login. If the application was logged in before, it will be logged out and a fresh login will be performed. :type change_option: :class:
  - `logout(self)` — Logs this application out. If the application is not logged in, nothing happens.
  - `start(self)` — Starts this application. :raises TimeoutException: In case of the operation taking to long.
  - `stop(self)` — Stops this application. :raises TimeoutException: In case of the operation taking to long.
  - `create_boot_application(self)` — Creates a boot application for this application on the device. If the current application is not online, a file dialog asks the user for a path to write the boo
  - `source_download(self)` — Downloads the source archive to the device.
  - `write_prepared_values(self)` — Writes the prepared values. :raises ValuesFailedException: If the write of some values fails.
  - `force_prepared_values(self)` — Forces the prepared values. :raises ValuesFailedException: If the force of some values fails.
  - `unforce_all_values(self)` — Unforces all forced values for the current application. :raises ValuesFailedException: If the unforce of some values fails.
  - `get_prepared_value(self, expression)` — Gets the prepared value for a given expression. :type expression: str :param expression: The expression :rtype: str :returns: The prepared value, or ``None`` if
  - `read_value(self, expression)` — Gets the current value for a given expression. Monitoring must be enabled. :type expression: str :param expression: The expression. :rtype: str :returns: The va
  - `read_values(self, expressions)` — Gets the current values for a list of expressions. Monitoring must be enabled. :type expressions: tuple[str] :param expressions: The expressions. :rtype: list[s
  - `get_prepared_expressions(self)` — Gets all expressions for values currently prepared for this application (including those prepared by other scripts, editors etc). :rtype: list[str] :returns: Th
  - `get_forced_expressions(self)` — Gets all expressions for values currently forced for this application (including those prepared by other scripts, editors etc). :rtype: list[str] :returns: The 
  - `set_prepared_value(self, expression, value)` — Prepares values the specified expression. Use None or the empty string to unprepare the value. :type expression: str :param expression: The expression. :type va
  - `set_unforce_value(self, expression, restore=False)` — Prepares the specified forced expression for unforcing. :type expression: str :param expression: The expression. :type restore: bool :param restore: If set to `
  - `timeout(self, value: int)`
  - `reset(self, reset_option=ResetOption.Warm, force_kill=False)` — Resets the online application. This also clears all breakpoints on the application (if any). If the application is currently halted on a breakpoint, and the dev
  - `get_online_device(self)` — Gets the online device for this application. :rtype: :class:`ScriptOnlineDevice`
  - `is_logged_in` *(property)* — Gets a value indicating whether this :class:`ScriptOnlineApplication` is logged in. :rtype: bool :returns: ``True`` if is logged in; otherwise, ``False``.
  - `application_state` *(property)* — Gets the application state. :rtype: :class:`ApplicationState`
  - `operation_state` *(property)* — Gets the operation status. :rtype: :class:`OperatingState`
  - `timeout` *(property)* — Gets or sets the timeout for some operations. Some operations like start() have to wait for defined application states. If those operations take longer than thi
  - `application` *(property)* — Gets the application object for this online application. :rtype: :class:`ScriptObject`
- **ScriptOnlineDevice** (object)
  - Functionality for manipulating online device objects. All device objects for which the online manager returns a IOnlineDevice7 instance are extended with this methods. This object keeps an internal connection to the device, so it should be disposed when you don't need it any more
  - `reset_origin(self)` — Reset the device to the origin (shipping) state. For example, all plc applications, boot applications, and retain and persistent variables are deleted.
  - `connect(self)` — Connects this instance. The connection is a shared connection to the device. Please note that other actions like reset_origin may implicitly connect to the devi
  - `disconnect(self)` — Disconnects this instance. As the connection is shared, the underlying connection may actually stay open, for example when an application is still online. :vers
  - `forced_disconnect(self)` — Forcibly disconnects all shared connections to the device (connections via online applications, as well as other connections), and resets the current login and 
  - `current_logged_on_username(self)` — Gets the name of the user who is currently logged on in the device. If ``None`` or an empty string is returned, nobody is logged on. :version added: 3.5.2.0 :rt
  - `create_user_management(self, load_from_project=True)` — Creates a new user management instance for this device. For the devices with runtime V3.5.16.0 or newer you have to use :meth:`create_live_user_management` beca
  - `download_source(self, bCompact=False, additional_items=None)` — Downloads the source archive to the device. For a definition of the additional items, see :class:`ScriptProjectArchiveCategories`. If you don't pass any ``addit
  - `upload_source(self, archive_path)` — Uploads the source from the device, and saves it under the specified output path. This method will throw various Exceptions on errors. :version added: 3.5.4.0 :
  - `download_file(self, local_file, remote_file, force_overwrite)` — Download a file to the PLC. :version added: 3.5.9.0 :type local_file: str :param local_file: Path of the local file. :type remote_file: str :param remote_file: 
  - `upload_file(self, remote_file, local_file, force_overwrite)` — Upload a file from the PLC. :version added: 3.5.9.0 :type remote_file: str :param remote_file: Path of the remote file. :type local_file: str :param local_file:
  - `rename_file(self, old_name, new_name)` — Rename a file on the PLC. :version added: 3.5.9.0 :type old_name: str :param old_name: Path of the remote file with the old name. :type new_name: str :param new
  - `delete_file(self, remote_file)` — Delete a file on the PLC. :version added: 3.5.9.0 :type remote_file: str :param remote_file: Path of the remote file.
  - `create_directory(self, remote_directory)` — Create a directory on the PLC. :version added: 3.5.9.0 :type remote_directory: str :param remote_directory: Path of the new directory.
  - `get_file_list_of_directory(self, remote_directory)` — Read a directory on the PLC. :version added: 3.5.9.0 :type remote_directory: str :param remote_directory: Path of the directory. :rtype: tuple[:class:`ScriptDir
  - `rename_directory(self, old_name, new_name)` — Rename a directory on the PLC. :version added: 3.5.9.0 :type old_name: str :param old_name: Path of the remote directory with the old name. :type new_name: str 
  - `delete_directory(self, remote_directory, recursive)` — Delete a directory on the PLC. :version added: 3.5.9.0 :type remote_directory: str :param remote_directory: Path of the remote directory. :type recursive: bool 
  - `activate_license(self, ticket, url=None, license_names=None)` — Performs a license activation on a remote device. The first container returned be the device will be used for activation. :version added: 3.5.10.0 :type ticket:
  - `change_user_password(self, user, oldPassword, newPassword)` — Update the passwort of a given user and reset the flag that the user must change the password on next login. :version added: 3.5.14.0 :type user: str :param use
  - `create_live_user_management(self)` — Create a new live user management which is required by PLC runtime V3.5.16.0 or newer. You have to create a connection before calling this method otherwise you 
  - `set_credentials_for_initial_user(self, username, password, can_change_password=True, must_change_password=False)` — Set the username and password for the initial user of the user management if the device requires it or you want one. If the device requires an user management y
  - `device` *(property)* — Gets the underlying device object for this online device. :rtype: :class:`ScriptObject`
  - `connected` *(property)* — Gets a value indicating whether this :class:`ScriptOnlineDevice` is connected. :version added: 3.5.2.0 :rtype: bool
  - `shared_connected` *(property)* — Gets a value indicating whether this ScriptOnlineDevice or anything else has a shared connection to the device. :version added: 3.5.2.0 :rtype: bool :returns: `
- **ValuesFailedException** (Exception)
  - This exception is thrown by :meth:`ScriptOnlineApplication.write_prepared_values` and :meth:`ScriptOnlineApplication.force_prepared_values`.
  - `ValuesFailedException(self, failed_expressions)` — Initializes a new instance of the :class:`ValuesFailedException` class. :type failed_expressions: list[str] :param failed_expressions: The failed expressions. :
  - `failed_expressions` *(property)* — Gets the list of the failedexpressions. :rtype: list[str]
- **ScriptGateway** (object)
  - Script engine representation of a configured gateway for runtime connections. :version added: 3.5.8.0
  - `find_address_by_ip(self, ip_or_name: str, port: int = 11740)` — Finds an CODESYS address by scanning the network by IP or Hostname. Currently, only IPv4 addresses are supported. This method blocks until either the device res
  - `find_address_by_ip(self, address: IPAddress, port: int = 11740)` — Finds an CODESYS address by scanning the network by IP or Hostname. Currently, only IPv4 addresses are supported. This method blocks until either the device res
  - `perform_network_scan(self)` — Performs a network scan on this gateway. This method will block at least for the duration of the network scan timeout period. :version added: 3.5.8.0 :raises Ex
  - `get_cached_network_scan_result(self)` — Gets the cached result of the last network scan on this gateway. :rtype: tuple[:class:`ScriptScanTargetDescription`] :returns: The list of devices which were fo
  - `name` *(property)* — Gets the name of the gateway. For backwards compatibility reasons, the gateway names are not guaranteed to be unique - several gateways with the same name may e
  - `guid` *(property)* — Gets the unique identifier of the gateway. :version added: 3.5.8.0 :rtype: Guid
  - `gateway_driver` *(property)* — Gets the gateway protcol driver used for this gateway. :version added: 3.5.8.0 :rtype: :class:`ScriptGatewayDriver`
  - `config_params` *(property)* — Gets a python dictionary with a copy of the current configuration of the gateway, using the :attr:`ScriptGatewayParameterDescription.id` as keys and the paramet
- **ScriptScanTargetDescription** (object)
  - Description of a scan target found during a device scan. :version added: 3.5.8.0
  - `device_name` *(property)* — Gets the name of the device. Example: "PLCFeeder". If no name has been explicitly assigned to the device, it is derived from the corresponding router address, e
  - `type_name` *(property)* — Gets a string indicating the device type. Example: "Beckhoff CX1000-100" or "BRC Motion Logic Controller". :rtype: str
  - `vendor_name` *(property)* — Gets a string indicating the device vendor. Example: "Beckhoff" or "BRC" :rtype: str
  - `device_id` *(property)* — Gets the ID of the type to be matched with the installed device types (target descriptions). :rtype: :class:`DeviceID`
  - `address` *(property)* — Gets the router address for this device. A hierarchical addressing scheme is used. Example: "123.5". Each component of the router address corresponds to an arra
  - `parent_address` *(property)* — Get the router address of the parent node of this device. Usually this will be the device address without the last address component. Is ``None`` if the parentA
  - `locked_in_cache` *(property)* — If set to true, the devicedescription will stay in the gateways device cache, even during rebuild. So this is not a property of the device itself but a property
  - `block_driver` *(property)* — Property to access the type of block driver used for this target. :rtype: :class:`BlockDriverType`
  - `block_driver_address` *(property)* — Property to store and retrieve the driver-specific address for this target. :rtype: str
- **ScriptGateways** (list)
  - A collection of gateways currently configured in CODESYS. :version added: 3.5.8.0
  - `__getitem__(self, guid: Guid)` — Gets the :class:`ScriptGateway` with the specified unique identifier. :type guid: Guid :param guid: The guid. :raises InvalidOperationException: If several gate
  - `__getitem__(self, name_or_guid: str)` — Gets the :class:`ScriptGateway` with the specified unique identifier. :type name_or_guid: str :param name_or_guid: The name or the guid as string. :raises Inval
  - `find_with_name(self, name)` — Finds all gateways with the name. :type name: str :param name: The name. :rtype: list[:class:`ScriptGateway`] :returns: A (possibly empty) sequence of all gatew
  - `remove_gateway(self, gateway: ScriptGateway)` — Removes the specified gateway. If the specified one is the default one, the next one (if any) will be the new default. :type gateway: :class:`ScriptGateway` :pa
  - `remove_gateway(self, guid: Guid)` — Removes the specified gateway. If the specified one is the default one, the next one (if any) will be the new default. :type guid: Guid :param gateway: The guid
  - `add_new_gateway(self, name, parameters, driver=None, gateway_guid=None)` — Creates and adds a new gateway. The keys of the ``parameters`` dictionary need to be integers corresponding to the :attr:`ScriptGatewayParameterDescription.id`,
  - `convert_gateway_parameter(self, parameter, paramType)` — Converts an object to the specified gateway parameter type. :type parameter: object :param parameter: The parameter. :type paramType: :class:`ParamType` :param 
- **ScriptGatewayDrivers** (list)
  - Represents a list of script gateway drivers. :version added: 3.5.8.0
  - `__getitem__(self, guid)` — Gets the :class:`ScriptGatewayDriver` with the specified name or guid. :type guid: Guid :param guid: The guid. :raises InvalidOperationException: If several gat
  - `__getitem__(self, name_or_guid)` — Gets the :class:`ScriptGatewayDriver` with the specified name or guid. :type name_or_guid: str :param name_or_guid: The name or guid (as string). :raises Invali
  - `find_with_name(self, name)` — Finds all gateway drivers with the name. :type name: str :param name: The name. :rtype: list of :class:`ScriptGatewayDriver` :returns: A (possibly empty) sequen
  - `default_driver` *(property)* — Gets the default gateway driver (currently bound to TCP/IP on standard CODESYS and most derivates). :rtype: :class:`ScriptGatewayDriver`
- **ScriptGatewayDriver** (object)
  - Script engine representation of a gateway driver. :version added: 3.5.8.0
  - `guid` *(property)* — A Guid that uniquely identifies the driver type. Each implementation for a gateway driver is identified by a Guid. :rtype: Guid
  - `name` *(property)* — Get the user-readable name of this gateway driver. :rtype: str
  - `gateway_parameters` *(property)* — Gets the gateway parameter descriptions - those are used when a new gateway with this driver is created. :rtype: ScriptGatewayParameterDescriptions :returns: A 
- **ScriptGatewayParameterDescriptions** (list)
  - A collection of script gateway parameters. :version added: 3.5.8.0
  - `__getitem__(self, id)` — Gets the :class:`ScriptGatewayParameterDescription` with the specified id. :type id: int :param id: The id. :raises InvalidOperationException: If several parame
  - `__getitem__(self, name)` — Gets the :class:`ScriptGatewayParameterDescription` with the specified id. :type name: str :param name: The name. :raises InvalidOperationException: If several 
- **ScriptGatewayParameterDescription** (object)
  - Description of parameters for a gateway driver - those are used when a new gateway with this driver is created. :version added: 3.5.8.0
  - `validate(self, value)` — Check whether the provided object is a valid value for this parameter. You can use the :meth:`ScriptGateways.convert_gateway_parameter` method to convert the pa
  - `id` *(property)* — The id of the parameter. The id is unique for any particular gateway driver. :rtype: long
  - `name` *(property)* — Human readable string, giving the name of the parameter. :rtype: str
  - `description` *(property)* — Human readable string describing the parameter. :rtype: str
  - `parameter_type` *(property)* — The type of the parameter value. The types here have finer granularity than the types available in python. However, users don't need to cast to the correspondin
  - `default_value` *(property)* — Default value of the parameter. May be ``None``. :rtype: object
- **ScriptDirectoryInfo** (object)
  - Describes contents of a remote directory on the PLC. :version added: 3.5.9.0
  - `TrustsCertificateCallback(certificate, chain, node_name)` — This callback allows to specify if the certificate of a PLC should be trusted for the encrypted communcation. :version added: 3.5.17.0 :type certificate: X509Ce
  - `name` *(property)* — Gets the name of the file/directory. :rtype: str
  - `creation_time` *(property)* — Get the creation time of the file/directory. :rtype: DateTime
  - `last_access_time` *(property)* — Get the last access time of the file/directory. :rtype: DateTime
  - `last_modification_time` *(property)* — Get the last modification time of the file/directory. :rtype: DateTime
  - `is_directory` *(property)* — Whether it is a directory. :rtype: bool
  - `is_file` *(property)* — Whether it is a file. :rtype: bool
  - `size` *(property)* — Get the file size in bytes. :rtype: int
  - `additional_dir_info` *(property)* — Get the additional information of the file/directory. :rtype: :class:`AdditionalDirInfo`

### `ScriptProject`

> No flags set.

- **ComparisonFlags** (Enum)
  - Flags controlling the details of the :meth:`ScriptProject.compare_to` method. :version added: 3.5.12.0
- **ObjectDifferences** (Enum)
  - Representing the object differences. :version added: 3.5.12.0
- **NativeImportResult** (Enum)
  - Enum that enumerates the possible results of a native XML import.
- **NativeImportResolve** (Enum)
  - How to resolve a conflict.
- **Formatting** (Enum)
  - DocExport.Formatting
- **ConflictResolve** (Enum)
  - Possible resolvements in the case that importing a specific PLCopenXML object leads to conflicts with an already existing object.
- **ScriptProject** (ScriptTreeObject)
  - Provides project specific functionality to scripts.
  - `close(self)` — Closes this project. The corresponding Object Manager project will also be closed. If this project has got unsaved changes, these changes will be discarded.
  - `save(self)` — Saves this project at its physical location (see path). The encryption settings are not changed.
  - `save_as(self, path, password=None)` — Saves the project under a new filename and with different encryption. If no password is given (None is passed), encryption stays as it is. If the password given
  - `save_archive(self, path, comment=None, additional_files=None, *additional_categories)` — Saves the project as an archive. All additional categories which are selected by default are included, but no extra files. .. note:: For a definition of the add
  - `active_application(self, value)`
  - `document(self, objects)` — Prints the specified database objects, including chapter headings and chapter numbering, a title page and table of contents. The current printer settings as spe
  - `export_xml(self, objects, reporter=None, path=None, recursive=False, export_folder_structure=False, declarations_as_plaintext=False): """Exports the given objects in PLCopenXML format into a string, or a file at the given path.  All non-exportable objects are reported as error, but the export may still continue.  :type objects: tuple[ScriptObject] :param objects: The objects to export.  :type reporter: ExportReporter :param reporter: The ExportReporter instance. None can be passed for no reporting.  :type path: str or None :param path: The path of the file we export into. If omitted, we export into a string and return that string.  :type recursive: bool or None :param recursive: If set to ``True``, all exportable children of the objects are also exported.  :type export_folder_structure: bool :param export_folder_structure: Version added: 3.4.4.0 if set to ``True``, the folder structure of the objects is also exported. This is a proprietary extension to the default schema.  :type declarations_as_plaintext: bool :param declarations_as_plaintext: Version added: 3.5.2.0 if set to ``true``, the declaration parts will be additionally exported as plain text (which is lossless in contrast to the default schema). This is a proprietary extension to the default schema. (Import will automatically recognize and prefer the plain text format if present.)  :rtype: str :returns: The exported XML as string, or None if a filepath is given.  """ pass  def import_xml(self, dataOrPath, reporter=None, import_folder_structure=False)` — Imports the contents of the specified PLCopenXML file into the top level of the project. The heuristics to find out whether the content is a file or directly an
  - `export_native(self, objects, destination, recursive=False, one_file_per_subtree=False, profile_name=None, reporter=None): """Export the specified objects in the CoDeSys native export format.  The parameter ``destination`` must point to a directory if ``one_file_per_subtree`` is set to ``True``, and to a file in the other case.  :version added: 3.4.4.0 :type objects: list :param objects: The objects to export. :type destination: str :param destination: The destination. :type recursive: bool :param recursive: if set to ``true``, the chilren are included recursively. :type one_file_per_subtree: bool :param one_file_per_subtree: if set to ``true``, one file per subtree is generated. :type profile_name: str :param profile_name: The profile_name, or None for the default profile. :type reporter: NativeExportReporter :param reporter: The reporter. You can pass None for no reporting at all.  """ pass  def import_native(self, filename=None, filenames=None, filter=None, handler=None)` — Imports the specified files in the native xml format in the top level of this project. .. warning:: If ``None`` is passed for both ``filename`` and ``filenames`
  - `login(self, username, password)` — Log into the project using the specified credentials. :version added: 3.4.1.10 :type username: str :param username: The username. :type password: str :param pas
  - `logout(self)` — Log out from the project (back to the user "nobody"). :version added: 3.4.1.10
  - `get_project_info(self)` — Gets the project information object, implicitly creating one if not existing yet. :version added: 3.5.2.0 :rtype: ScriptObject :returns: The project information
  - `check_all_pool_objects(self)` — Checks all pool objects. This command only works reliable for libraries, and when called on primary projects. You can use the :meth:`System.get_messages` and :m
  - `generate_runtime_system_files(self, destination_directory, generate_m4=True, generate_c=False)` — Generates the specified destination_directory. At least one of ``generate_m4`` and ``generate_c`` must be set. :version added: 3.5.2.0 :type destination_directo
  - `clean_all(self)` — Performs a "Clean All". :version added: 3.5.2.0
  - `save_as_compiled_library(self, destination_name=None)` — Save the current project as a compiled library. This command currently only works for the primary project. The ``destination_name`` has the following semantics:
  - `create_folder(self, foldername, structured_view=None)` — Creates a folder with the specified folder name. There are three predefined structured views, and the guids are provided as constants: * SV_DEV The device view,
  - `export_doc(self, path=None, ext_path=None, formatting=Formatting.Indented)` — Exports the documentation for primary project in JSON format into a string, or a file at the given path. :version added: 3.5.5.0 :type path: str or None :param 
  - `compare_to(self, right_project, flags=0):   # '0' for ComparisonFlags.None """Compares two script projects.  :version added: 3.5.12.0 :type right_project: ScriptProject :param right_project: The project (base) you want to compare the current project against. :type flags: :class:`ComparisonFlags` :param flags: Flags controlling the detailed behaviour of the comparison. :rtype: ScriptComparisonResult :returns: The comparison result.  """ pass  @property def project_settings(self)` — Returns the management object for :class:`ScriptProjectSettings`. :version added: 3.5.12.10 :rtype: :class:`ScriptProjectSettings`
  - `enable_integrity_check(self)` — Enables the integrity checked project format. :version added: 3.5.13.0
  - `disable_encryption(self)` — Disables password, CodeMeter(TM) dongle and X509 certificate-based encryption or integrity check for the specified project. :version added: 3.5.13.0
  - `is_integrity_check_enabled(self)` — Returns whether the integrity checked project format is is_integrity_check_enabled. :version added: 3.5.13.0 :rtype: bool
  - `dirty` *(property)* — Gets a boolean value indicating whether this project has been changed since the last call to save(). :rtype: bool :returns: ``True`` if this instance is dirty; 
  - `primary` *(property)* — Gets a boolean value indicating whether the primary attribute has been set for this project. The primary project is the one the user is currently working with. 
  - `library` *(property)* — Gets a boolean value indicating whether the project is a background library project. Those projects represent a library which was loaded because it is reference
  - `path` *(property)* — Gets the absolute path where this project is physically stored. To change that path, use save_as(). :rtype: str
  - `active_application` *(property)* — Gets or sets the active application. This is a property. You can read or assign a :class:`ScriptObject` for the application you want to be the active applicatio
  - `user_management` *(property)* — Returns the user management object for this project. :version added: 3.5.1.0 :raises Exception: If no user management is available. :rtype: :class:`ScriptUserMa
  - `has_project_info` *(property)* — Gets a value indicating whether this :class:`ScriptProject` already has a project information object. :version added: 3.5.2.0 :rtype: bool :returns: ``true`` if
- **ScriptProjectSettings** (object)
  - Interface for project settings. :version added: 3.5.12.10
  - `set_sourcedownload(self, timing, content, compact, device)` — Sets the source download settings to the project. :type timing: int :param timing: .. csv-table:: The timing behaviour. :header: "Value", "Behaviour" :widths: 1
  - `set_compilerversion_to_newest(self)` — sets the compiler version of the project to the newest available version. :version added: 4.2.0.0
  - `get_compilerversion(self)` — Returns the current compiler version of the project. :version added: 4.2.0.0 :rtype: str
  - `available_download_content` *(property)* — Gets a list of all available ScriptProjectArchiveCategories that can be used for :meth:`ScriptProjectSettings.set_sourcedownload`. :rtype: list[:class:`ScriptPr
  - `project_defines` *(property)* — Gets or sets the project defines (a comma separated list). This is a property. You can read or assign a string (a comma separated list) containing the project d
- **ScriptComparedObject** (object)
  - Representing the difference of an object.
  - `left_object` *(property)* — The object from the :attr:`ScriptComparison.left_project`, or ``None`` for deleted objects. :rtype: ScriptObject
  - `right_object` *(property)* — The object from the :attr:`ScriptComparisonResult.right_project`, or ``None`` for added objects. :rtype: ScriptObject
  - `differences` *(property)* — The exact object differences. :rtype: :class:`ObjectDifferences`
- **ScriptComparisonResult** (list)
  - Represents the project comparison result. Iterating this returns all changed objects. :version added: 3.5.12.0
  - `__getitem__(self, state_or_object)` — getitem. ``state_or_object`` is of type :class:`ObjectDifferences`. Calls :meth:`get_changed_objects` ``state_or_object`` is of type :class:`ScriptObject` Calls
  - `get_changed_objects(self, state=ObjectDifferences.ANY_CHANGES)` — Returns all changed objects with a matching diff state (any of the given flags have to be set). :type state: :class:`ObjectDifferences` :param state: The diff s
  - `get_diff_state(self, script_object)` — Gets the diff state for a specific object. :type script_object: ScriptObject :rtype: ScriptComparedObject :returns: The diff state for the object.
  - `left_project` *(property)* — The first or left project which was compared. :rtype: :class:`ScriptProject`
  - `right_project` *(property)* — The second or right project which was compared. :rtype: :class:`ScriptProject`
- **ExportReporter** (object)
  - python classes can implement their own export_xml reporter here. This interface(``IExportReporter``) is exposed under the name ExportReporter.
  - `error(self, obj, message)` — This method is called when an error has occurred during export_xml. :type obj: ScriptObject :param obj: The object which caused the error. :type message: str :p
  - `warning(self, obj, message)` — This method is called when a warning has occurred during export_xml. :type obj: ScriptObject :param obj: The object which caused the warning. :type message: str
  - `nonexportable(self, obj)` — This method is called when we find out that a given object is not exportable. This is only called for objects given directly as parameters - non-exportable chil
  - `aborting` *(property)* — This allows abortion when we report non-exportable objects. :rtype: bool
- **ImportReporter** (object)
  - Python classes can implement their own import_xml reporter here. This interface(IImportReporter) is exposed under the name ImportReporter.
  - `error(self, message)` — This method is called when an error has occurred during import_xml. :type message: str :param message: The message describing the problem.
  - `warning(self, message)` — This method is called when a warning has occurred during import_xml. :type message: str :param message: The message describing the problem.
  - `resolve_conflict(self, obj)` — This method is called when an object to import is already existing. :type obj: ScriptObject :param obj: The already existing object. :rtype: ConflictResolve :re
  - `added(self, obj)` — This method is called whenever an object has been successfully added during import. :type obj: ScriptObject :param obj: The newly added object.
  - `replaced(self, obj)` — This method is called whenever an object has been successfully replaced during import. :type obj: ScriptObject :param obj: The replacing object.
  - `skipped(self, objectname)` — This method is called whenever an object has been skipped during import. :type objectname: str :param objectname: The name of the skipped object.
  - `aborting` *(property)* — Gets a boolean value indicating whether importing should be aborted or not. :rtype: bool
- **NativeExportReporter** (object)
  - This reporter is used for the native XML export. This interface is exposed under the name NativeExportReporter.
  - `skipped(self, type_name, serializable_value_name)` — This method is called when data has been effectively skipped during serialization or deserialization. :type type_name: str :param type_name: The typename of the
  - `warn(self, message)` — This method is called when a warning occurs during serialization or deserialization. :type message: str :param message: A message describing the reason of the w
  - `cancel(self, message)` — This method is called when an error occurs during serialization or deserialization. The code that triggered the serialization should discard the resulting strea
  - `NativeImportFilter(self, name, guid, type, path)` — [Delegate]. This method can be used to filter the imported objects. :type name: str :type guid: Guid :type type: string :type path: tuple[object] :param path: A
- **NativeImportHandler** (object)
  - Handler callback for the native XML import. This interface is exposed under the name NativeImportHandler.
  - `conflict(self, name, existingObject, newguid)` — Queries how to resolve a conflict. :type name: str :type existingObject: ScriptObject :type newguid: Guid :rtype: NativeImportResolve :returns: The resolution f
  - `progress(self, name, pastedObject, exception)` — Reports progress of import. :type name: str :type pastedObject: ScriptObject :type exception: Exception
  - `skipped(self, name)` — Informs about skipped objects. :type name: tuple[object] :param name: A python tuple with the names..

### `ScriptProjects`

> The user selected "Yes", which means that the file or item should be overwritten.

- **PromptOverwriteResult** (Enum)
  - Enum that enumerates the possible results for the overwrite handling.
- **VersionUpdateFlags** (Enum)
  - Flags for the _3S.CoDeSys.VersionCompatibilityManager.IVersionCompatibilityManager2.SetVersionUpdateFlags(_3S.CoDeSys.VersionCompatibilityManager.VersionUpdateFlags) method.
- **ScriptProjects** (object)
  - The ScriptDriverProjects uses this interface to provide project handling functionality for the python scripts.
  - `create(self, path, primary=True)` — Creates a new project. :version added: :type path: str :param path: The location where the project content is to be stored. :type primary: bool or None :param p
  - `get_by_path(self, path)` — Gets a Project by the absolute path where the project is physically stored. :type path: str :param path: The path to the project. :rtype: :class:`ScriptProject`
  - `convert(self, path, output_path=None, converter=None, primary=True)` — Converts the specified project. Currently, password and device conversion prompts cannot be caught by the script. .. list-table:: Some converter guids are: :wid
  - `primary` *(property)* — Gets the primary project, or None if no primary project currently exists. The primary project is the one the user usually works with. See :attr:`ScriptProject.p
  - `all` *(property)* — Gets a (possibly empty) List of all currently opened projects. :rtype: list[ScriptProject]
- **ScriptProjectArchiveCategories** (list)
  - The list of available archive categories. Enumerating this object will give all categories available in the current installation. Some often used categories are defined here, but may be unavailable (throw exceptions) in customized environments. An instance of this object is injec
  - `__getitem__(self, guid_or_name)` — Gets the class:`ScriptProjectArchiveCategory` with the specified GUID or name. :type guid_or_name: Guid or str :rtype: ScriptProjectArchiveCategory
  - `default` *(property)* — The default selection of archive categories. See also: :attr:`ScriptProjectArchiveCategory.selected_by_default` :rtype: list[ScriptProjectArchiveCategory]
  - `none` *(property)* — No categories (empty set). This is a special sentinel value, different from passing an arbitrary empty list. :rtype: list[ScriptProjectArchiveCategory]
  - `all` *(property)* — A collection of all categories (returns self).
  - `compileinfo` *(property)* — Gets the category for the compileinfo. This is needed for logins and online changes into an existing application without download. :rtype: ScriptProjectArchiveC
  - `libraries` *(property)* — Gets the category for the libraries referenced by the project. :rtype: ScriptProjectArchiveCategory
  - `devices` *(property)* — Gets the category for the device descriptions of the devices used in the project. :rtype: ScriptProjectArchiveCategory
  - `options` *(property)* — Gets the category for the project, user, and machine specific preferences. :rtype: ScriptProjectArchiveCategory
  - `ftd` *(property)* — Gets the category for the FDT Bulk Data. :rtype: ScriptProjectArchiveCategory
  - `images` *(property)* — Gets the category for the imagepool images of the project. :rtype: ScriptProjectArchiveCategory
  - `bootproject` *(property)* — Gets the category for the files containing offline boot applications, that were generated for the current project. :rtype: ScriptProjectArchiveCategory
  - `libraryprofile` *(property)* — Gets the category for the library profile that is currently in use with this project. :rtype: ScriptProjectArchiveCategory
  - `visualstyles` *(property)* — Gets the category for the visualization styles which are currently referenced by this project. :rtype: ScriptProjectArchiveCategory
  - `visualprofile` *(property)* — Gets the category for the active visualization profile. :rtype: ScriptProjectArchiveCategory
  - `visuextensions` *(property)* — Gets the category for the active visualization extensions. :rtype: ScriptProjectArchiveCategory
- **ScriptProjectArchiveCategory** (object)
  - Represents a category of items which can be included into a project archive.
  - `PromptAbsolutePath(self, path)` — [Delegate]. This method can be used to decide if a project archive item with absolute path should be extracted relatively to the project file or not at all. Or 
  - `guid` *(property)* — Gets the :class:`Guid` for this category. :rtype: Guid
  - `name` *(property)* — Gets a display name for this project category, e.g. "Referenced libraries". This string should be localized. :rtype: str
  - `description` *(property)* — Gets a description for this project category. This string should be localized. :rtype: str
  - `selected_by_default` *(property)* — Gets a boolean value indicating whether this category should be selected for project archive inclusion per default. This is a hint for the presentation layer. :

### `ScriptSymbolConfigObject`

> Direct I/O access is possible.

- **DirectIoAccessObstacles** (Enum)
  - This enum shows the obstacles which prevent the Direct IO access from taking place.
- **SymbolConfigContentFeatureFlags** (Enum)
  - The feature flags describing the contents of the symbol tables and XML files. (Introduced in V3.5.8.30, more broadly supported in V3.5.9.0.) Remark: The "runtime" part of this enum is also defined in the "ContentFeatureFlags" enumeration in the IecVarAccess Interfaces library.
- **SymbolAttributeFilterTypes** (Enum)
  - Definition of the attribute matching type
- **SymbolCommentFilterType** (Enum)
  - Defines which comments are included in the XML file or symbol tables.
- **ScriptSymbolConfigObjectMarker** (object)
  - Every ScriptObject instance will be extended with this method. :version added: 3.5.10.0
  - `is_symbol_config` *(property)* — Gets a value indicating whether this instance is a symbol config object. :rtype: bool :returns: ``True`` if this instance is symbol config object, otherwise ``F
- **ScriptSymbolConfigObject** (ScriptSymbolConfigObjectMarker)
  - Functionality for manipulating symbol configuration objects. :version added: 3.5.10.0
  - `client_side_layout_calculator_guid(self, value: Guid)`
  - `client_side_layout_calculator(self, value: ScriptClientSideLayoutCalculatorDescription)`
  - `enable_direct_io_access(self, value: bool)`
  - `check_effective_direct_io_access(self)` — Checks whether and why the direct Access to the I/O Area is effectively enabled / disabled. Enabling direct access to the I/O area is supported for debugging pu
  - `get_direct_io_obstacle_explanations(self, obstacles)` — Gets user readable, localized messages / explanations of the obstacles. :type obstacles: :class:`DirectIoAccessObstacles` :param obstacles: The obstacles. :rtyp
  - `content_feature_flags(self, value: SymbolConfigContentFeatureFlags)`
  - `get_symbol_configuration_xsd(self)` — Gets the current symbol configuration XML schema, as appropriate for the current symbol config object. The schema is delivered as a byte array, containing the U
  - `symbol_attribute_filter_type(self, value: SymbolAttributeFilterTypes)`
  - `symbol_attribute_filter_data(self, value: str)`
  - `symbol_comment_filter_type(self, value: SymbolCommentFilterType)`
  - `get_all_signatures(self, compile=True)` — Get all signatures (compiler and configured). :type compile: bool :param compile: If True, build the application before generating the list. If the application 
  - `get_all_datatypes(self, compile=True)` — Get all data types (compiler and configured). :type compile: bool :param compile: If True, build the application before generating the list. If the application 
  - `get_only_configured_signatures(self)` — Get only the configured signatures. :rtype: :class:`ScriptSymbolConfigSignatureCollection` :returns: Collection of signatures.
  - `get_only_configured_datatypes(self)` — Get only the configured data types. :rtype: :class:`ScriptSymbolConfigSignatureCollection` :returns: Collection of data types.
  - `client_side_layout_calculator_guid` *(property)* — Gets or sets the Guid denoting the currently configured client side layout calculator. Currently, two different values are allowed: ``Guid.Empty`` to use the Co
  - `client_side_layout_calculator` *(property)* — Gets or sets the calculator object denoting the currently configured client side layout calculator. Currently, two different values are allowed: ``Guid.Empty`` 
  - `available_client_side_layout_calculators` *(property)* — Gets all currently known layout calculators. :rtype: :class:`ScriptClientSideLayoutCalculatorDescriptionCollection`
  - `enable_direct_io_access` *(property)* — Gets or sets a boolean whether direct Access to the I/O Area is configured. Enabling direct access to the I/O area is supported for debugging purposes, e. G. te
  - `content_feature_flags` *(property)* — The configured content feature flags. This is partially redundant with :attr:`SymbolConfigObject.ExportCommentsInXML` and :attr:`SymbolConfigObject.SupportOPCUA
  - `effective_content_feature_flags` *(property)* — The effective content feature flags, considering the :attr:`content_feature_flags` and the compiler version setting. :rtype: :class:`SymbolConfigContentFeatureF
  - `symbol_attribute_filter_type` *(property)* — The configured filter type for the attributes. :rtype: :class:`SymbolAttributeFilterTypes`
  - `effective_symbol_attribute_filter_type` *(property)* — The effective filter type, considering compiler version and other side conditions. :rtype: :class:`SymbolAttributeFilterTypes`
  - `symbol_attribute_filter_data` *(property)* — Describes the filter data for :attr:`SymbolAttributeFilterTypes.Prefix` and :attr:`SymbolAttributeFilterTypes.Regex`. :rtype: str
  - `symbol_comment_filter_type` *(property)* — The configured comment filter type. :rtype: :class:`SymbolCommentFilterType`
  - `effective_symbol_comment_filter_type` *(property)* — The effective comment filter type, considering compiler version and other side conditions. :rtype: :class:`SymbolCommentFilterType`
- **ScriptClientSideLayoutCalculatorDescriptionCollection** (list)
  - Descriptions of the client side layout calculators. :version added: 3.5.10.0
  - `__len__(self)` — Gets the length (number of calculator descriptions). :rtype: int :returns: The number of calculator descriptions.
- **ScriptClientSideLayoutCalculatorDescription** (object)
  - Description of an client side layout calculator. Currently, two different values are allowed: ``Guid.Empty`` to use the Compatibility Offset Calculator which is always available. And "{0141eb75-141b-4ea1-9a8c-75f952b22a6c}" to use the OptimizedOutputOffsetCalculator which is new 
  - `type_guid` *(property)* — The unique ID of the output layout calculator. :rtype: Guid
  - `name` *(property)* — The name of the output layout calculator - human readable and localized. :rtype: str
  - `description` *(property)* — A longer description of the output layout calculator. :rtype: This may be shown in a tooltip, and should give some detailed explanation of the calculator, and e
- **ScriptSymbolConfigSignature** (object)
  - Signature element of the symbol configuration. :version added: 3.5.10.0
  - `name` *(property)* — The name of this element. :rtype: str
  - `full_qualified_name` *(property)* — The full qualified name of this element. :rtype: str
  - `library_id` *(property)* — The identification of the library where this signature is declared. :rtype: str
  - `namespace_path` *(property)* — Namespace path of the library where this signature is declared. :rtype: list <str>
  - `variables` *(property)* — The variables of the signature. :rtype: :class:`ScriptSymbolConfigVariableCollection`
- **ScriptSymbolConfigSignatureCollection** (list)
  - Collection of symbol configuration signatures. :version added: 3.5.10.0
  - `__len__(self)` — Collection of symbol configuration signatures. :rtype: int :returns: The number of signatures.
  - `__getitem__(self, index_or_name)` — Get the :class:`ScriptSymbolConfigSignature` at the specified position or the first :class:`ScriptSymbolConfigSignature` with the specified name which should be
  - `find(self, name, library_id=None)` — Get the first :class:`ScriptSymbolConfigSignature` with the specified name and library ID which should be fully qualified. :type name: str :param name: Name of 
- **ScriptSymbolConfigVariable** (object)
  - Variable element of the symbol configuration. :version added: 3.5.10.0
  - `configured_access(self, value)`
  - `name` *(property)* — The name of this variable. :rtype: str
  - `type` *(property)* — The type of this variable, as the user declared it. :rtype: str
  - `comment` *(property)* — Gets the comment of the signature or variable, or an empty string if no comment is available. This member is only valid for objects parsed from the compiler, no
  - `configured_access` *(property)* — The allowed symbolic access to this variable. :rtype: :class:`SymbolAccess`
  - `maximal_access` *(property)* — The maximal access that is allowed for this variable, decided by the given attributes. :rtype: :class:`SymbolAccess`
  - `effective_access` *(property)* — The effective symbolic access to this variable. :rtype: :class:`SymbolAccess`
  - `exported_via_attribute` *(property)* — Gets a value indicating whether this variable is configured via compiler attribute. :rtype: bool :returns: ``True`` if exported via attribute; otherwise ``False
  - `attribute_access` *(property)* — Gets the attribute access. When :attr:`attribute_access` is false, the result of this member is undefined. :rtype: :class:`SymbolAccess`
  - `type_library_id` *(property)* — Gets the library id, when the type of the member is from a library. This is currently only set for supported data types (userdef and array). :rtype: str
  - `full_qualified_base_type` *(property)* — Gets the full qualified base type of the member. This is currently only set for supported data types (userdef and array). :rtype: str
  - `alias_type` *(property)* — The name of the alias type. For variables with aliased types, the Type, ``SymbolConfigVariable.VariableType`` and ``SymbolConfigVariable2.FullQualifiedBaseType`
- **ScriptApplicationSymbolConfigExtension** (object)
  - Extension provider for ApplicationObject instances. :version added: 3.5.10.0
  - `create_symbol_config(self, export_comments_to_xml, support_opc_ua, client_side_layout_calculator): """Add the symbol configuration object to an application.  :type export_comments_to_xml: bool  :type support_opc_ua: bool  :type client_side_layout_calculator: Guid  :rtype: :class:`ScriptObject` :returns: Script object of the symbol config object.  """ pass   class ScriptSymbolConfigInvalidObjectException(Exception)` — Exception which is thrown when the symbol configuration object is modified externally and so the scripting objects are not valid anymore. :version added: 3.5.10
  - `__init__(self, stMessage)` — init.

### `ScriptSystem`

> Use :attr:`ScriptPromptHandling.SuppressPrompts` instead.

- **PromptHandling** (Enum)
  - This enum is obsolete. Use :class:`ScriptPromptHandling`, :attr:`System.script_prompt_handling`, :attr:`System.process_script_prompts` and :attr:`System.log_prompt_details` instead. For textual prompts in noUI mode please use the command line switch '--textPrompts'.
- **ScriptPromptHandling** (Enum)
  - Definition flags for prompt handling via scripting. Prompts are standard dialog boxes issued by plugins to inform or query the user. For all prompts with a message key a specific handling can be deposited in :attr:`System.prompt_answers`. This enum may be extended in future relea
- **Severity** (Enum)
  - Describes the severity of an _3S.CoDeSys.Core.Messages.IMessage.
- **PromptChoice** (Enum)
  - This enumeration denotes possible prompt options for _3S.CoDeSys.Core.IMessageService methods.
- **PromptResult** (Enum)
  - This enumeration denotes possible prompt results from _3S.CoDeSys.Core.IMessageService methods.
- **System** (object)
  - Access to generic CoDeSys system functionality. An instance of this object is planted into the scriptengine module with the name "system".
  - `exit(self, exitcode=0)` — Exits the application platform by shutting down the engine and exiting the process. If you just want to terminate the script execution without exitting the plat
  - `trace(self, value: bool)`
  - `write_message(self, severity, stMessage, obj=None, position=-1, length=None)` — Writes the message to the Message Store. Position and length are only meaningfull if obj is a ScriptObject and are ignored otherwise. :type severity: :class:`Se
  - `get_messages(self, category="{194B48A9-AB51-43ae-B9A9-51D3EDAADDF3}")` — Gets all messages of a given category which are currently in the store. :type category: str :param category: The category Guid (defaults to the ScriptMessage ca
  - `delay(self, milliseconds)` — Delays the script for the specified amount of milliseconds. The message loop is served during the wait to allow background tasks to be processed. The actual dur
  - `prompt_handling(self, value: PromptHandling)`
  - `get_message_objects(self, category=None, severities=0xFFFFFFFF)` — Gets all messages of a given category and severity which are currently in the store. :version added: 3.5.2.0 :type category: Guid or str :param category: The ca
  - `get_message_categories(self, bActive=True)` — Gets all message categories. :version added: 3.5.2.0 :type bActive: bool :param bActive: If set to ``True`` (the default), only the active ones (those which had
  - `get_message_category_description(self, category)` — Gets a description for the specified message category. :version added: 3.5.2.0 :type category: Guid :param category: The category. :rtype: str :returns: The des
  - `clear_messages(self, category)` — Clears the specified category. :version added: 3.5.2.0 :type category: Guid
  - `abortable(self, value: bool)`
  - `abort_autocheck(self, value: bool)`
  - `progress_start(self, description, items=-1, unit="")` — Starts the progress information for a specific subtask. :version added: 3.5.5.0 :type description: str :param description: The description of the subtask. :type
  - `progress_step(self, item, completed=1)` — Advances the progress of the current subtask. :version added: 3.5.5.0 :type item: str :param item: The item which is currently completed. :type completed: int :
  - `progress_absolute(self, item, absolute_progress)` — Advances the progress of the current subtask. :version added: 3.5.5.0 :type item: str :param item: The item which is currently completed. :type absolute_progres
  - `trace` *(property)* — Gets or sets a value indicating whether trace :class:`System` is active on the current script execution. trace is the replacement for the old "echo" functionali
  - `ui_present` *(property)* — Gets a value indicating whether we have an UI. If this is false, we're running in a console application or background service. :rtype: bool :returns: ``True`` i
  - `prompt_answers` *(property)* — Gets the prompt answers Dictionary for simulating interactive user input. This dictionary is used to intercept the IMessageService interface. It only applies, i
  - `executable_filename` *(property)* — Gets the name of the executable file (the currently running application). :rtype: str
  - `prompt_handling` *(property)* — Gets or sets the way message service prompts are handled. :version added: 3.5.1.0 :rtype: :class:`PromptHandling`
  - `ui` *(property)* — Gets the script ui instance. :version added: 3.5.1.0 :rtype: :class:`ScriptUI`
  - `commands` *(property)* — Gets the commands. :version added: 3.5.1.0 :rtype: :class:`ScriptCommands`
  - `factories` *(property)* — Gets the factories. :version added: 3.5.1.0 :rtype: :class:`ScriptObjectFactories`
  - `abortable` *(property)* — Whether the script is abortable. Since V3.5.5.0, scripts are abortable by default. The user can abort the script by pressing the Cancel button in the progress d
  - `abort_autocheck` *(property)* — Gets or sets a value indicating whether this script execution automatically checks for aborts. If this property is set to True (the default value), the script e
  - `aborting` *(property)* — Gets a value indicating whether this System is aborting. This property gets set to true once the user presses an enabled "Cancel" button on the progress display
  - `background_loading_of_libraries_finished` *(property)* — Is the background loading of libraries finished? :version added: 3.5.15.0 :rtype: bool
  - `script_prompt_handling` *(property)* — Defines how prompts are handled. For textual prompts in noUI mode use the command line switch '--textPrompts'. :version added: 4.2.0.0 :rtype: :class:`ScriptPro
  - `process_script_prompts` *(property)* — If set, prompts issued by the script itself via :attr:`System.ui` are also subject to the :attr:`ISystem6.script_prompt_handling` and :attr:`System.prompt_answe
  - `log_prompt_details` *(property)* — Logs details for all message service calls to the message store. Use this to catch the message keys, options, choices and :class:`PromptChoice` you need for :at
- **ScriptMessage** (object)
  - Represents a message from the message storage.
  - `call_details_handler(self)` — Calls the details handler of this message (this will usually open a popup or similar).
  - `PieceOfCode(self)` — Delegate for a parameterless function without return value.
  - `project` *(property)* — The the project of the message position. If this message does not have a position, None is returned. :rtype: :class:`ScriptProject`
  - `object` *(property)* — The object of the message position. If this message does not have a position, None is returned. :rtype: :class:`ScriptObject`
  - `position` *(property)* — The position within the database object of the message position. The interpretation of this number is handled privately by the object. To get a user-friendly di
  - `position_text` *(property)* — The user-friendly display text for position within the database object of the message position. The interpretation of this number is handled privately by the ob
  - `position_offset` *(property)* — Gets an additional character offset to the position returned by the :attr:`position` property. :rtype: short
  - `length` *(property)* — Gets length of Position. :rtype: int
  - `text` *(property)* — Gets the message text. :rtype: str
  - `severity` *(property)* — Gets the severity of this message. :rtype: Severity
  - `FontColor` *(property)* — Gets the color of the message text, or :attr:`System.Drawing.Color.Empty` if the default color is defined. :rtype: Color
  - `has_details_handler` *(property)* — Gets a value indicating whether this :class:`ScriptMessage` has a details handler. This is visually indicated by a [...]-Button in the message view. :rtype: boo
  - `icon` *(property)* — Specialized Icon. If ``None``, the icon is set according to the severity. :rtype: Icon
  - `number` *(property)* — Unambigous number identifying the message according to its category. Together with the :attr:`prefix`, the number identifies the message. compile, LINT, IO-Conf
  - `prefix` *(property)* — A prefix string identifying the message category (compile, LINT, IO-Config, etc). Together with the :attr:`number`, the message is unambigously identified. None
- **ScriptUI** (object)
  - The script can interact with the user via this instance. Please note that some of the functionalities depend on the currently installed MessageService instance. In --noUI-Mode (console-only mode), a basic, somehow restricted implementation querying the user via text input is prov
  - `error(self, message, message_key="ScriptMessage", arguments=None)` — Reports an error message to the user. This method blocks until the user has acknowledged this message. :type message: str :param message: The message to display
  - `warning(self, message, message_key="ScriptMessage", arguments=None)` — Reports an warning message to the user. This method blocks until the user has acknowledged this message. :type message: str :param message: The message to displ
  - `info(self, message, message_key="ScriptMessage", arguments=None)` — Reports an informational message to the user. This method blocks until the user has acknowledged this message. :type message: str :param message: The message to
  - `choose(self, message, options, initial_selection=0, cancellable=True, message_key="ScriptMessage", *arguments): """Lets the user choose one of several listed items.  :type message: str :param message: The message to display.  :type options: list :param options: A list of options to display. The objects will be converted to string to show them to the user.  :type initial_selection: int :param initial_selection: The index of the initially selected object of the list.  :type cancellable: bool :param cancellable: if set to ``true``, the user can cancel / abort the dialog.  :type message_key: str :param message_key: The message key, for automated filtering / handling by :attr:`System.prompt_answers` or similar mechanism by other plugins (e. G. automated test tools). Most users can leave the default here.  :type arguments: str :param arguments: Optional objects which build the variable part of the message. In other words, if ``message`` is build via a string formatting operation, the arguments of that formatting operation should be passed as ``arguments`` here. This is for advanced usages via automated test tools, most users can ignore it.  :rtype: list :returns: A python tuple containing the index of the selected item, or -1 if ``cancellable`` was set to True and the user cancelled the dialog as the first item, and the selected item or None as the second item.  """ pass  def reset_stored_result(self, store_key)` — Resets any prompt results stored by :meth:`prompt` or :meth:`select_many`. :type store_key: str :param store_key: A non-``None`` caller-specific key with which 
  - `browse_directory_dialog(self, message, path="", root_folder="Environment.SpecialFolder.MyComputer", new_folder_button=True): """Opens a browse directory dialog.  This method is currently not processed by :attr:`System.prompt_answers`.  In --NoUI-Mode, the user simply can enter a path here.  The microsoft documentation for the root folder says: "Only the specified folder and any subfolders that are beneath it will appear in the dialog box and be selectable. The SelectedPath property, along with RootFolder, determines what the selected folder will be when the dialog box is displayed, as long as SelectedPath is an absolute path that is a subfolder of RootFolder (or more accurately, points to a subfolder of the shell namespace represented by RootFolder)."  :type message: str :param message: The message to display.  :type path: str :param path: The path to be preselected when the dialog opens.  :type root_folder: Environment.SpecialFolder :param root_folder: The root folder for the browsing dialog.  :type new_folder_button: bool :param new_folder_button: if set to ``True``, a button which allows the users to create new folders appears in the dialog box.  :rtype: str :returns: The path for the selected directory, or None if the user cancelled the dialog.  """ pass  def query_string(self, message="", text="", multi_line=False, cancellable=False)` — Queries the user to input or edit a text string. This method is currently not processed by :attr:`System.prompt_answers`. :type message: str :param message: The
  - `query_password(self, message="", password="", cancellable=False)` — Queries the user to input a password. This method is currently not processed by :attr:`System.prompt_answers`. :type message: str :param message: The message to
  - `query_credentials(self, message="", username="", password="", cancellable=False)` — Queries the user to input a password. This method is currently not processed by :attr:`System.prompt_answers`. :type message: str :param message: The message to
  - `MultipleChoiceSelector(self, choices)` — Delegate for selecting one of multiple choices for simulating interactive user input via system.promt_answers. Script authors have to cast their delegates to th
  - `PromptCustomControlValueProvider(self, control_id)` — Delegate for providing values for the options of a custom control for simulating interactive user input via system.prompt_answers. Script authors have to cast t
- **ScriptCommand** (object)
  - Represents a CoDeSys command (Menu, Toolbar, Context Menu).
  - `name` *(property)* — Gets the display text of this command. This string is used as menu item label and usually is localized. :rtype: str
  - `description` *(property)* — Gets the description for this command. This string is used as statusbar text and usually is localized. :rtype: str
  - `tokens` *(property)* — Gets the tokens which introduce a corresponding batch instruction. For example, a batch command which opens a project file would probably return the two tokens 
  - `guid` *(property)* — Gets the GUID. :rtype: Guid
- **ScriptCommands** (list)
  - A sequence of all known Commands in CoDeSys.
  - `__getitem__(self, tokens)` — Searches a specific command by its tokens. :type tokens: list[str] :param tokens: The command tokens (either separated by space, or a list of strings containing
- **ScriptObjectFactory** (object)
  - An Object factory.
  - `guid` *(property)* — Gets the GUID of the object factory. :rtype: Guid
  - `object_type` *(property)* — Gets the guid of the produced object type. :rtype: Guid
  - `object_namespace` *(property)* — Gets a GUID identifying the namespace the created object will belong to. :rtype: Guid
  - `name` *(property)* — Gets the display text of this object factory. This string should be localized. :rtype: str
  - `description` *(property)* — Gets the description for this object factory. This string should be localized. :rtype: str
- **ScriptObjectFactories** (list)
  - A sequence of all known object factories.
  - `__getitem__(self, factory_guid)` — Searches for an object factory by its guid. :type factory_guid: Guid :param factory_guid: The factory Guid. :rtype: :class:`ScriptObjectFactory`
  - `search_factories_for(self, typeguid)` — Returns all known object factories for a given object type. The list is ordered, so that perfect matches (which produce exactly the queried type) come before fa

### `ScriptTaskConfigObject`

- **KindOfTask** (Enum)
- **ScriptTaskConfigObjectMarker** (object)
  - Every ScriptObject instance will be extended with this method. :version added: 3.5.10.0
  - `is_task_configuration` *(property)* — Gets a value indicating whether this instance is a task configuration object. :rtype: bool :returns: ``True`` if this instance is task config object; otherwise,
- **ScriptTaskObjectMarker** (object)
  - Every ScriptObject instance will be extended with this method. :version added: 3.5.10.0
  - `is_task` *(property)* — Gets a value indicating whether this instance is a task object. :rtype: bool :returns: ``True`` if this instance is task object; otherwise, ``False``
- **ScriptTaskConfigObject** (ScriptTaskConfigObjectMarker)
  - Functionality for manipulating task configuration objects. :version added: 3.5.10.0
  - `create_task(self, name)` — Add a task object to a task configuration. :type name: str :rtype: :class:`ScriptTaskObject`
- **ScriptTaskObject** (ScriptTaskObjectMarker)
  - Functionality for manipulating task objects. :version added: 3.5.10.0
  - `kind_of_task(self, value: KindOfTask)`
  - `priority(self, value: str)`
  - `interval(self, value: str)`
  - `interval_unit(self, value: str)`
  - `event(self, value: str)`
  - `external_event(self, value: str)`
  - `core_binding(self, value: int)`
  - `parent_synchron_task(self, value: str)`
  - `name` *(property)* — Name of the task. :rtype: str
  - `kind_of_task` *(property)* — Kind of task. :rtype: KindOfTask
  - `event_pou_guid` *(property)* — Guid of POU for event. :rtype: Guid
  - `priority` *(property)* — Priority of the task. :rtype: str
  - `interval` *(property)* — Interval of the task. Requires the property :attr:`kind_of_task` to be set to KindOfTask.Cyclic or KindOfTask.ExternalEvent if the device supports it. :rtype: s
  - `interval_unit` *(property)* — Unit used for the :attr:`interval`. Requires the property :attr:`kind_of_task` to be set to KindOfTask.Cyclic or KindOfTask.ExternalEvent if the device supports
  - `watchdog` *(property)* — Settings for the watchdog of the task. :rtype: :class:`ScriptWatchdog`
  - `event` *(property)* — Use event to trigger the task. Requires the property :attr:`kind_of_task` to be set to KindOfTask.Event or KindOfTask.Status. :rtype: str
  - `external_event` *(property)* — Use external event to trigger the task. Requires the property :attr:`kind_of_task` to be set to KindOfTask.ExternalEvent. :rtype: str
  - `core_binding` *(property)* — Core binding. On multicore deivce each task can have an optional core binding. :rtype: int
  - `parent_synchron_task` *(property)* — Task of the device application which allows synchronous calls to child application in bus cycle. Requires the property :attr:`kind_of_task` to be set to KindOfT
  - `pous` *(property)* — Collection of POUs which are executed by the task. :rtype: :class:`ScriptPouObjectCollection`
- **ScriptWatchdog** (object)
  - A configuration for a watchdog. :version added: 3.5.10.0
  - `enabled(self, value: bool)`
  - `time(self, value: str)`
  - `time_unit(self, value: str)`
  - `sensitivity(self, value: str)`
  - `enabled` *(property)* — Enable the watchdog for a task. :rtype: bool
  - `time` *(property)* — Time monitoring for a task. :rtype: str
  - `time_unit` *(property)* — Unit user for the :attr:`time`. :rtype: str
  - `sensitivity` *(property)* — Sensitivity of the watchdog. :rtype: str
- **ScriptPouObjectCollection** (list)
  - A collection of POUs which are executed by a task. :version added: 3.5.10.0
  - `add(self, pou_name, comment=None)` — Add a POU to the list. :type pou_name: str :param pou_name: Name of the POU. :type comment: str :param comment: Optional comment about this entry
  - `insert(self, index, pou_name, comment)` — Insert a POU to the list at the specified index. :type index: int :param index: Index of a POU at which a new POU should be inserted. :type pou_name: str :param
  - `replace(self, index, pou_name, comment)` — Replace the POU in the list at the specified index. :type index: int :param index: Index of a POU which should be replaced. :type pou_name: str :param pou_name:
  - `remove(self, index_or_name)` — Remove a POU from the list at the specified index OR: Remove the first POU with the specified name from the list. :type index_or_name: int or str :param index_o
  - `__len__(self)` — Gets the length. :rtype: int :returns: The number of POUs.
  - `__getitem__(self, index)` — Gets the name and the comment of the entry at the specifed index as a python tuple. :type index: int :param index: Index of a POU. :rtype: tuple[str, str] :retu

### `ScriptTextListObject`

- **ScriptTextListMarker** (object)
  - Marker object to check whether an ScriptObject is a textlist object. :version added: 3.5.11.0
  - `is_textlist` *(property)* — Gets a value indicating whether this :class:`.ScriptApplicationMarker` is a textlist. :rtype: bool :returns: ``True`` if it is a textlist; otherwise ``False``.
- **ScriptTextListObject** (ScriptTextListMarker)
  - ScriptObjects which are a textlist object are extended with this interface. :version added: 3.5.11.0
  - `addlanguage(self, language)` — Adds a new language to the text list. If the language already exists, it is not added twice.
  - `removelanguage(self, language)` — Removes a new language to the text list.
  - `languagecount(self)` — Gets the current number of languages in this textlist. :rtype: int
  - `getlanguage(self, index)` — Returns the language with the given ``index``. :type index: int :param index: The index of the language to return. :raises ArgumentOutOfRangeException: Thrown w
  - `updatetextids(self)` — Only for global textlist. Calls the command 'Update Visualization Text IDs' for this textlist. This command updates all inconsistent IDs in a static text list.
  - `checkids(self)` — Only for global textlist. Calls the command 'Check Visualization Text IDs' for this textlist. This command checks whether the ID of a text list entry in the pro
  - `removeunusedids(self)` — Only for global textlist. Calls the command 'Remove Unused Text List Entries' for this textlist. This command checks whether a text list entry in the project is
  - `importfile(self, importfile)` — Like in import/export dialog: The file can contain text list entries both for the global text list and for text lists. :type importfile: str
  - `importreplacementfile(self, importfile)` — Like in import/export dialog: The replacement file contains replacements for the global text list. :type importfile: str :param importfile: Name and path of a f
  - `export(self, exportfile)` — Like in import/export dialog: exports all the texts from all the text lists in the current project. :type exportfile: str
  - `rows` *(property)* — Gets the collection of the rows currently configured within this textlist. :rtype: ScriptTextListItemsCollection
- **ScriptTextListRow** (object)
  - A row within an :class:`ScriptTextListObject`. :version added: 3.5.11.0
  - `setlanguagetext(self, language, text)` — Sets the text in the row, for a defined language. :type language: str :param language: The languagename, which defines the language entry, to use. :type text: s
  - `setdefaulttext(self, defaulttext)` — Sets the defaulttext in this row. :type defaulttext: str :param defaulttext: The defaultext to set for this row. :rtype: bool :returns: ``True`` if the text cou
  - `languagetextcount(self)` — Gets the current number of languagetexts in this row. :rtype: int
  - `languagetext(self, index)` — Gets the languagetext. :type index: int :param index: The index of the languagetext to return. :raises ArgumentOutOfRangeException: Thrown when the given index 
  - `id` *(property)* — The identification of the row. :rtype: str
  - `defaulttext` *(property)* — The default text entry in this row. :rtype: str
- **ScriptTextListItemsCollection** (list)
  - The items currently managed by the textlist object. :version added: 3.5.11.0
  - `__len__(self)` — Gets the current number of items(rows) in this textlist. :rtype: int
  - `__getitem__(self, index_or_id)` — Returns the row with the given index or id. :type index_or_id: int or str :param index_or_id: The index of the row to return or the id to search for. :raises Ar
  - `add(self, id, defaulttext)` — Adds a new row to the current textlist. :type id: str :param id: The id to assign to the newly inserted row. Must not yet be existing. :type defaulttext: str :p
  - `remove(self, id)` — Removes the ScriptTextListRow with the given ``id``. :type id: str :param id: The id of the item to remove. :raises KeyNotFoundException: Thrown when no entry w
- **ScriptTextListObjectContainer** (object)
  - Projects and Application Objects are extended with this interface. :version added: 3.5.11.0
  - `create_textlist(self, name=None)` — Creates a new textlist object in the current context (either application or project global). :type name: str :param name: The name of the new textlist object. I
  - `get_global_textlist(self)` — Returns the global textlist object or creates a new one if not yet existing. Typically this method can be called on projects only. Only in case of special custo
  - `has_global_textlist` *(property)* — Checks whether there is already a global textlist in the current location. Only in case of special customizations of the programming system, it is allowed to ca

### `ScriptTextualObject`

> pass class ScriptObjectWithTextualDeclaration(ScriptTextualObjectMarker): """Accessor interface for textual declaration parts. :version added: 3.5.6.0

- **ScriptTextualObjectMarker** (object)
  - All tree objects get amended with this marker. :version added: 3.5.6.0
  - `has_textual_declaration` *(property)* — Gets a value indicating whether this :class:`ScriptObject` has a textual declaration part. :rtype: bool :returns: ``True`` if it has a textual declaration; othe
  - `has_textual_implementation` *(property)* — Gets a value indicating whether this :class:`ScriptObject` has a textual implementation part. :rtype: bool :returns: ``True`` if it has a textual implementation
- **ScriptTextDocument** (object)
  - @property def length(self): """Gets the length of the text document in bytes. :rtype: int
  - `get_line(self, lineno)` — Gets the line with the specified lineno. Lines do not include the line ending character. The first line has lineno 0. :type lineno: int :param lineno: The line 
  - `get_text(self, length, offset=None, lineno=None, lineoffset=None)` — Gets the text. .. warning:: The original C# function that is called with this method contains 2 overloads. It is strongly advised to pass *all* arguments with t
  - `replace_line(self, lineno, line)` — Replaces the complete line with the specified line number with the new text. This method retains the position info of the text lines which are not modified. :ty
  - `append(self, text)` — Appends the specified text at the end of the buffer. This method retains the position info of the text lines which are not modified. :type text: str :param text
  - `insert(self, text, offset=None, lineno=None, lineoffset=None)` — Insert text. .. warning:: The original C# function that is called with this method contains 2 overloads. It is strongly advised to pass *all* arguments with the
  - `remove(self, length, offset=None, lineno=None, lineoffset=None)` — Remove text. .. warning:: The original C# function that is called with this method contains 2 overloads. It is strongly advised to pass *all* arguments with the
  - `linecount` *(property)* — pass @property def text(self): """Gets the complete text as a string. :rtype: str
  - `textual_declaration` *(property)* — Gets the textual declaration. :rtype: :class:`ScriptTextDocument`
- **ScriptObjectWithTextualImplementation** (ScriptTextualObjectMarker)
  - Accessor interface for textual implementation parts. :version added: 3.5.6.0
  - `textual_implementation` *(property)* — Gets the textual implementation. :rtype: :class:`ScriptTextDocument`

### `ScriptTraceDiagram`

- **ScriptTraceDiagram** (object)
  - | Contains the settings for a diagram of the trace.
  - `add_diagram_variable(self, variable: ScriptTraceVariable, visible: bool=True)` — | Adds an existing ScriptTraceVariable with the given visibility to the diagram. :rtype: ScriptTraceDiagramVariable :returns: The created ScriptTraceDiagramVari
  - `background_color` *(property)* — | Gets or sets the 32bit-ARGB representation of the background color.
  - `background_color_sel` *(property)* — | Gets or sets the 32bit-ARGB representation of the background color, used, while the diagram is selected.
  - `y_axis` *(property)* — | Bundled settings for the y axis.
  - `variables` *(property)* — | The variables, used in this diagram.
  - `name` *(property)* — | Gets or sets the name of the diagram.
  - `can_rename` *(property)* — | Gets wether the diagram can be renamed.
  - `visible` *(property)* — | Gets or sets wether die diagram is visible.

### `ScriptTraceDiagramCollection`

- **ScriptTraceDiagramCollection** (list)
  - | Represents the collection of Diagrams in one TraceObject. .. automethod:: __iter__ .. automethod:: __next__ .. automethod:: __len__ .. automethod:: __contains__ .. automethod:: __getitem__
  - `__iter__(self)`
  - `__next__(self)`
  - `add(self)` — | Creates and adds a ScriptTraceDiagram to the collection. Returns the ScriptTraceDiagram. | Not allowed for the ScriptTraceDiagramCollection of the DeviceTrace
  - `__len__(self)` — | Returns the number of ScriptTraceDiagrams in this ScriptTraceDiagramCollection.
  - `remove(self, index: int)` — | Removes the ScriptTraceDiagram at the given index.
  - `remove(self, diagram: ScriptTraceDiagram)` — | Removes the given ScriptTraceDiagram from this ScriptTraceDiagramCollection.
  - `remove(self)` — | Removes the ScriptTraceDiagram at the given index.
  - `clear(self)` — | Removes all ScriptTraceDiagrams from this ScriptTraceDiagramCollection.
  - `index_of(self, diagram: ScriptTraceDiagram)` — | Returns the index of the ScriptTraceDiagram in the collection or -1, if the Variable could not be found.
  - `__contains__(self, diagram: ScriptTraceDiagram)` — | Returns, wether the ScriptTraceDiagramCollection contains the ScriptTraceDiagram. | Allows usage of 'in' and 'not in' operators.
  - `contains(self, diagram: ScriptTraceDiagram)` — | Returns, wether the ScriptTraceDiagramCollection contains the ScriptTraceDiagram.
  - `__getitem__(self, index: int)` — | Gets or sets the diagram at the given index.

### `ScriptTraceDiagramVariable`

- **ScriptTraceDiagramVariable** (object)
  - | Represents the connection between one ScriptTraceVariable and one ScriptTraceDiagram. | One ScriptTraceVariable can be used in multiple diagrams, and a diagram usually consists of multiple variables.
  - `visible` *(property)* — | Gets or sets the visibility of the variable in the diagram.

### `ScriptTraceDiagramVariableCollection`

- **ScriptTraceDiagramVariableCollection** (list)
  - | Represents a collection of ScriptTraceDiagramVariables, used in a diagram. .. automethod:: __iter__ .. automethod:: __next__ .. automethod:: __len__ .. automethod:: __contains__ .. automethod:: __getitem__
  - `__iter__(self)`
  - `__next__(self)`
  - `add(self, variable: ScriptTraceVariable)` — | Creates and adds a ScriptTraceVariable to the diagram. Returns the new ScriptTraceDiagramVariable.
  - `__len__(self)` — | Returns the number of variables, used in this diagram.
  - `remove(self, index: int)` — | Removes the ScriptTraceDiagramVariable at the given index.
  - `remove(self, diagramVariable: ScriptTraceDiagramVariable)` — | Removes the given ScriptTraceDiagramVariable from the diagram.
  - `remove(self)` — | Removes the ScriptTraceDiagramVariable at the given index.
  - `clear(self)` — | Removes all ScriptTraceDiagramVariables from the diagram.
  - `index_of(self, diagramVariable: ScriptTraceDiagramVariable)` — | Returns the index of the ScriptTraceDiagramVariable in the collection or -1, | if the diagramVariable is not part of this diagram.
  - `__contains__(self, diagramVariable: ScriptTraceDiagramVariable)` — | Returns, wether this collection contains the given ScriptTraceDiagramVariable. | Allows usage of 'in' and 'not in' operators.
  - `contains(self, diagramVariable: ScriptTraceDiagramVariable)` — | Returns, wether this collection contains the given ScriptTraceDiagramVariable.
  - `__getitem__(self, index: int)` — | Gets or sets the diagram variable at the given index.

### `ScriptTraceEditorObject`

- **ScriptTraceEditorObject** (object)
  - | Represents a open trace editor, used to perform online actions on a trace.
  - `download(self)` — | Download a trace to the device. After this call the trace will be logged in. :exception: This is exception is throw if the trace can not be downloaded, becaus
  - `start(self)` — | Start the recording of a downloaded trace :exception: This exception is thrown if the trace can not be started, because tt is not logged in, is is already run
  - `stop(self)` — | Stop the recording of a downloaded trace :exception: This exception is thrown if the trace can not be stopped, because it is not logged in, is is not running 
  - `save(self, file_name: str)` — | Save the data of the trace to a file. If the file already exists it is overwriten. | The format of the file depends on the fileextension. :type file_name: str
  - `get_trigger_state(self)` — | Returns information about the trigger while the trace is currently running. :exception: This exception is thrown if the trace has not be downloaded to the dev
  - `get_trigger_timestamp(self)` — | Returns the (absolute) timestamp of the last trigger event. The resolution is ms or µs, depending on the resolution of the trace. :exception: This exception i
  - `get_trigger_startdate(self)` — | Returns the date of the last trigger event in UTC. :exception: This exception is thrown if the trace has not be downloaded to the device,
  - `get_packet_state(self)` — | Returns information about the trace packet in the runtime. :exception: This exception is thrown if the trace has not be downloaded to the device,
  - `get_trace_start_timestamp(self)` — | Returns the (absolute) timestamp when the packet was started.The resolution is ms or µs, depending on the resolution of the trace. :exception: This exception 
  - `reset_trigger(self)` — | Resets the trigger and causes that the trace is running again
  - `get_online_traces(self)` — | Returns a list of strings with the packet names of trace, that are currently online. :rtype: list[str] :returns: See summary
  - `upload_to_device_trace(self, stPacketName: str)` — | Uploads the given trace packet to the currently open device trace editor. :type stPacketName: str :param stPacketName: The name of the trace packet to upload
  - `is_online` *(property)* — | Check if the application for the trace is online.
  - `is_logged_in` *(property)* — | Check if the trace is logged in.
  - `is_running` *(property)* — | Check if the trace is currently running.

### `ScriptTraceObject`

- **ScriptTraceObject** (IScriptTraceObjectMarker)
  - | Represents one TraceObject. .. automethod:: __str__
  - `open_editor(self)` — | Open the trace editor for this trace object. | This is required to perform online operations like starting, stopping and downloading traces. | If the editor i
  - `__str__(self)`
  - `is_trace_object` *(property)* — | Wether the object is a valid trace object.
  - `task_name` *(property)* — | The task in which the data is recorded. | Setting the task name is not allowed for the DeviceTrace.
  - `record_name` *(property)* — | The name of the trace recording in the runtime.
  - `trigger_enabled` *(property)* — | Indicates whether a trigger condition has to be considered in the trace recording.
  - `trigger_variable` *(property)* — | The trace signal that is used as a trigger. A complete instance path is required..
  - `trigger_edge` *(property)* — | Defines the edge detection for triggering.
  - `trigger_level` *(property)* — | Value that is reached to start the triggering. Any numeric types like int, ulong, double | (null represents the absence of a trigger level) are accepted. :exc
  - `post_trigger_samples` *(property)* — | Number of records per trace variable that are buffered after triggering.
  - `resolution` *(property)* — | Unit of measure for the time stamp that is recorded.
  - `record_condition` *(property)* — | At runtime, the application checks the recording condition. If it is fulfilled, then the trace data is buffered.
  - `comment` *(property)* — | The comment of the trace recording.
  - `auto_start` *(property)* — | Persistently saves the trace configuration and the last contents of the runtime buffer to the target device. After the device has been restarted, the trace is
  - `every_n_cycles` *(property)* — | Data is recorded in every n task cycle.
  - `time_axis` *(property)* — | Contains the configuration of the time axis.
  - `diagrams` *(property)* — | Not allowed for the DeviceTrace.
  - `variable_list` *(property)* — | Not allowed for the DeviceTrace.

### `ScriptTraceVariable`

- **ScriptTraceVariable** (object)
  - `variable_name` *(property)* — | Gets or sets the name of the variable. Must only contain ASCII characters.
  - `graph_color` *(property)* — | Gets or sets the color of the graph. Expects the 32bit-ARGB color representation.
  - `graph_type` *(property)* — | Gets or sets the graph type, used to display the values.
  - `max_warning_area` *(property)* — | Gets or sets the limit, above which values can be displayed using max_color, depending on activate_max_warning.
  - `activate_max_warning` *(property)* — | Gets or sets wether values above max_warning_area should be displayed using max_color.
  - `max_color` *(property)* — | Gets or sets the graph color for values greater than max_warning_area. Expects the 32bit-ARGB color representation.
  - `min_warning_area` *(property)* — | Gets or sets the limit, below which values can be displayed using min_color, depending on activate_min_warning.
  - `activate_min_warning` *(property)* — | Gets or sets wether values below min_warning_area should be displayed using min_color.
  - `min_color` *(property)* — | Gets or sets the graph color for values less than min_warning_area. Expects the 32bit-ARGB color representation.
  - `enabled` *(property)* — | Indicates, whether the variable should be included in the trace recording.

### `ScriptTraceVariableList`

- **ScriptTraceVariableList** (list)
  - | Provides functionality for the modification of the list of variables, traced by the corresponding ScriptTraceObject. .. automethod:: __iter__ .. automethod:: __next__ .. automethod:: __len__ .. automethod:: __contains__ .. automethod:: __getitem__
  - `__iter__(self)`
  - `__next__(self)`
  - `add(self)` — | Creates and adds a ScriptTraceVariable to the list. Returns the ScriptTraceVariale. | Not allowed for the variable list of the DeviceTrace.
  - `__len__(self)` — | Returns the number of ScriptTraceVariables in this ScriptTraceVariableList.
  - `remove(self, index: int)`
  - `remove(self, traceVariable: ScriptTraceVariable)` — | Removes the given ScriptTraceVariable from this ScriptTraceVariableList.
  - `remove(self)` — | Removes the given ScriptTraceVariable from this ScriptTraceVariableList.
  - `clear(self)` — | Removes all ScriptTraceVariables from this ScriptTraceVariableList.
  - `index_of(self, variable: ScriptTraceVariable)` — | Returns the index of the ScriptTraceVariable in the list or -1, if the Variable could not be found.
  - `__contains__(self, variable: ScriptTraceVariable)` — | Returns, wether the ScriptTraceVariableList contains the ScriptTraceVariable. | Allows usage of 'in' and 'not in' operators.
  - `contains(self, variable: ScriptTraceVariable)` — | Returns, wether the ScriptTraceVariableList contains the ScriptTraceVariable.
  - `__getitem__(self, index: int)` — | Gets or sets the trace variable at the given index.

### `ScriptTreeObject`

- **ScriptTreeObject** (object)
  - Common base functionality for ScriptObject and ScriptProject.
  - `find(self, name, recursive=False)` — Finds objects matching the given name. Names are not unique in the tree, so several Objects can be delivered. The search is against the nonlocalized name. :type
  - `find_ignore_transient_objects(self, name, recursive=False)` — Finds objects matching the given name. Names are not unique in the tree, so several Objects can be delivered. The search is against the nonlocalized name. Trans
  - `get_children(self, recursive=False)` — Gets the children of our object. :type recursive: bool :param recursive: If set to ``True``, we work recursively. :rtype: list[ScriptObject] :returns: All child
  - `project` *(property)* — Gets the project. This returns "this" rsp. "self" if called on Projects. :rtype: ScriptProject
  - `handle` *(property)* — Gets the internal Automation Platform handle of the Project. This handle is primarily useful for other Atomation Platform plugins which provide functionality fo
  - `is_root` *(property)* — Gets a value indicating whether this instance is the root of the object tree. This returns true for all :class:`.ScriptProject` instances, and false for all :cl

### `ScriptUserManagement`

> The permission to view an object.

- **ObjectPermissionKind** (Enum)
  - This enumeration contains the various possibilites to access an object from the viewpoint of the User Management.
- **PermissionState** (Enum)
  - The permission state, either "granted", "denied", or "default".
- **ScriptUserManagement** (object)
  - UserManagement interface.
  - `login(self, username, password)` — Log into the project using the specified credentials. This is equal to :meth:`ScriptProject.login`. :type username: str :param username: The username. :type pas
  - `logout(self)` — Log out from the project (back to the user "nobody"). This is equal to :meth:`.ScriptProject.logout`.
  - `check_available(self, type)` — Checks whether permission management for the given PermissionType is available in the given CoDeSys installation. :type type: Guid :param type: The type. :rtype
  - `get_user_management_permission(self)` — Gets the permission object for the user management. :rtype: :class:`ScriptPermission`
  - `get_command_permission(self, commandguid)` — Gets the permission object for execution of a specific command. :type commandguid: Guid or :class:`ScriptCommand` :param commandguid: The ScriptCommand or its G
  - `get_factory_permission(self, factory)` — Gets the permission object for accessing a specific object factory. :type factory: Guid or :class:`ScriptObjectFactory` :param factory: The factory or its guid.
  - `get_object_permission(self, obj, kind)` — Gets a Permission object for that specific script object. :type obj: :class:`ScriptObject` :param obj: The object we want the permission for. :type kind: :class
  - `project` *(property)* — Backlink to the project for this user management. :rtype: :class:`ScriptProject`
  - `users` *(property)* — The collection of all defined users for this project. :rtype: :class:`ScriptUserList`
  - `groups` *(property)* — The colleciton of all defined groups for this project. :rtype: :class:`ScriptGroupList`
  - `logged_on_user` *(property)* — Gets the user which is currently logged in, or None if no user is currently logged in. :rtype: :class:`ScriptUser`
  - `login_time` *(property)* — Gets the timestamp since the last successful login, or DateTime.MinValue if no user is currently logged in. :rtype: DateTime
  - `types` *(property)* — Gets all available types. :rtype: :class:`ScriptPermissionTypes`
- **ScriptPermissionTypes** (list)
  - This object represents all available permission types.
  - `usermanagement` *(property)* — The permission type guid for user management, or Guid.Empty if not available in this installation. :rtype: Guid
  - `objectaccess` *(property)* — The permission type guid for object access rights, or Guid.Empty if not available in this installation. :rtype: Guid
  - `objectfactory` *(property)* — The permission type guid for object factory rights (object creation), or Guid.Empty if not available in this installation. :rtype: Guid
  - `commandexecution` *(property)* — The permission type guid for execution of commands, or Guid.Empty if not available in this installation. :rtype: Guid
- **ScriptUserList** (list)
  - Represents the list of all users known to the current project.
  - `create(self, name)` — Creates a new user with the specified name. :type name: str :param name: The name. :rtype: :class:`ScriptUser`
  - `__getitem__(self, id_or_name)` — Gets the :class:`ScriptUser` with the specified id or name. :type id_or_name: Guid or str :rtype: :class:`ScriptUser`
  - `user_management` *(property)* — Back-Link to the project's user management. :rtype: :class:`ScriptUserManagement`
  - `project` *(property)* — Backlink to the project for this user management. :rtype: :class:`ScriptProject`
- **ScriptUserOrGroup** (object)
  - This interface contains the common members of :class:`ScriptUser` and :class:`ScriptGroup`.
  - `description(self, value: str)`
  - `add_to(self, parent)` — Adds this user or group to the specified parent group. :type parent: :class:`ScriptGroup` :param parent: The parent.
  - `remove_from(self, parent)` — Removes this user or group from the specified parent group. :type parent: :class:`ScriptGroup` :param parent: The parent.
  - `project` *(property)* — Backlink to the project for this user management. :rtype: :class:`ScriptProject`
  - `user_management` *(property)* — Back-Link to the project's user management. :rtype: :class:`ScriptUserManagement`
  - `is_user` *(property)* — Gets a value indicating whether this ScriptUserOrGroup is an user. :rtype: bool
  - `is_group` *(property)* — Gets a value indicating whether this ScriptUserOrGroup is a group. :rtype: bool
  - `id` *(property)* — Gets the ID of this user or group. :rtype: Guid
  - `name` *(property)* — Gets the login name of this user or group. :rtype: str
  - `description` *(property)* — Gets or sets the description for this user or group. This is informative only. :rtype: str
- **ScriptUser** (ScriptUserOrGroup)
  - Instances of this interface represent a single user within the user management. A user is uniquely identified by its ID (not by its name), although its name must also be unique within a user list.
  - `fullname(self, value: str)`
  - `active(self, value: bool)`
  - `check_password(self, password)` — Checks the password for an user. :type password: str :param password: The password. :rtype: bool :returns: ``True`` if the password is correct.
  - `change_password(self, old_password, new_password)` — Changes the password for the user. :type old_password: str :param old_password: The old password. :type new_password: str :param new_password: The new password.
  - `remove(self)` — Removes the user with the specified ID from this list. :raises UserNotExistingException: If the user does not exist (e. G. because it was removed before). :rais
  - `rename(self, newname)` — Renames the user. :type newname: str :param newname: The new name.
  - `userlist` *(property)* — Backreference to the user list. :rtype: :class:`ScriptUserList`
  - `fullname` *(property)* — Gets or sets the full name of this user. This is informative only. :rtype: str
  - `active` *(property)* — Gets or sets a boolean which indicates whether this user is currently active. Inactive users cannot login to the user management. :rtype: bool
  - `groups` *(property)* — Gets a python tuple with the groups this user is member of. :rtype: tuple[ScriptGroup]
- **ScriptGroupList** (list)
  - Represents the list of all known groups in this project.
  - `create(self, name)` — Creates a new group with the specified name. :type name: str :param name: The name. :rtype: :class:`ScriptGroup` :returns: The newly created group.
  - `__getitem__(self, id_or_name)` — Gets the :class:`ScriptGroup` with the specified id or name. :type id_or_name: Guid or str :rtype: :class:`ScriptUser` :returns: The ScriptGroup, or ``None`` if
  - `user_management` *(property)* — Back-Link to the project's user management. :rtype: :class:`ScriptUserManagement`
  - `project` *(property)* — Backlink to the project for this user management. :rtype: :class:`ScriptProject`
  - `owner_group` *(property)* — Owner group. :rtype: :class:`ScriptGroup`
  - `everyone_group` *(property)* — Everyone group. :rtype: :class:`ScriptGroup`
- **ScriptGroup** (ScriptUserOrGroup)
  - Instances of this interface represent a single group within the user management. A group is uniquely identified by its ID (not by its name), although its name must also be unique within a group list.
  - `add_member(self, member)` — Adds a member to this group. This might be either a user or another group. If such a user or group does not exist, (e. G. because it was deleted in the meantime
  - `remove_member(self, member)` — Removes a member from this group. :type member: :class:`ScriptUserOrGroup` :param member: The member.
  - `has_member(self, member)` — Checks whether the specified user or group is a member of this group. :type member: :class:`ScriptUserOrGroup` :param member: The member. :rtype: bool :returns:
  - `get_user_members(self, recursive)` — Returns a python tuple of all users which are member of this group, or which are members of group members of this group. :type recursive: bool :param recursive:
  - `get_group_members(self)` — Gets a python tuple of all groups which are member of this group. :rtype: list
  - `rename(self, newname)` — Renames the group. :type newname: str :param newname: The new name.
  - `remove(self)` — Removes this group from the containing grouplist.
  - `grouplist` *(property)* — Backlink to the grouplist. :rtype: :class:`ScriptGroupList`
  - `is_everyone_group` *(property)* — Gets a boolean value indicating whether this group is the "everyone" group. :rtype: bool
  - `is_owner_group` *(property)* — Gets a boolean value indicating whether this group is the "owner" group. :rtype: bool
- **ScriptPermission** (object)
  - Interface for permission objects.
  - `check_permission(self, silent_or_group)` — This overload is used when ``silent_or_group`` is of type *bool*. Checks whether the currently logged in user has a specific permission or not. :type silent: bo
  - `get_permission_state(self, group, resolve_effective=True, resolve_inherited=False)` — Gets the the state of a specific permission. You can use :attr:`.System.commands` to search for a command guid. :type group: :class:`ScriptGroup` :param group: 
  - `set_permission_state(self, group, state)` — Sets the permissions for a specific command. :type group: :class:`ScriptGroup` :param group: The group. :type state: :class:`PermissionState` :param state: The 
  - `check_set_permission_state(self, group, state, silent=True)` — Checks whether our group is allowed to set a specific permission. :type group: :class:`ScriptGroup` :param group: The group. :type state: :class:`PermissionStat
  - `type` *(property)* — Gets the type. :rtype: Guid
- **ScriptObjectPermission** (ScriptPermission)
  - ObjectAccess Permissions come with additional information about which object to access, and the specific kind of object access.
  - `check_permission_extended(self)` — Checks the effective permission the current user has for the given object. This considers permission inheritance along the object tree etc. This method may prom
  - `target_object` *(property)* — Target object. :rtype: :class:`ScriptObject`
  - `access_kind` *(property)* — Access kind. :rtype: :class:`ObjectPermissionKind`
- **ScriptCommandPermission** (ScriptPermission)
  - Permissions for commands come with the command guid.
  - `command_guid` *(property)* — Gets the command guid. :rtype: Guid
- **ScriptFactoryPermission** (ScriptPermission)
  - Permissions for factories come with a guid describing the object factory.
  - `factory_guid` *(property)* — Gets the factory guid. :rtype: Guid

### `TriggerEdge`

> | No trigger edge defined.

- **TriggerEdge** (Enum)
  - | Describes the way of trigger detection.

### `TriggerState`

> | No trigger defined.

- **TriggerState** (Enum)
  - | Flags field defining the state of the trigger of a trace packet in the runtime system.

### `dotNETs`

- **Guid** (object)
  - .Net's type System.Guid
  - `Empty` *(property)* — Empty Guid. :rtype: Guid
- **Version** (object)
  - .Net#s type System.Version
  - `Revision(self)`
  - `Revision(self)`
  - `Build(self)`
  - `Minor(self)`
  - `Major(self)`
  - `MinorRevision(self)`
  - `MajorRevision(self)`
  - `ToString(self)`
- **IPAddress** (object)
  - .Net's type System.Net.IPAddress
- **DateTime** (object)
  - .Net's type System.DateTime
- **TimeSpan** (object)
  - .Net's type System.TimeSpan
  - `ToString(self)`
- **Color** (object)
  - .Net's type System.Drawing.Color
- **Icon** (object)
  - .Net's type System.Drawing.Icon
- **Image** (object)
  - .Net's type System.Drawing.Image
- **Stream** (object)
  - .Net's System.IO.Stream
- **Uri** (object)
  - .Net's System.Uri
- **XmlElement** (object)
  - .Net's System.Xml.XmlElement
- **XmlWriter** (object)
  - .Net's System.Xml.XmlWriter
- **X509Certificate2** (object)
  - .Net's System.Security.Cryptography.X509Certificates.X509Certificate2
- **X509Chain** (object)
  - .Net's System.Security.Cryptography.X509Certificates.X509Chain
- **Win32Window** (object)
  - .Net's System.Windows.Forms.IWin32Window
- **EventArgs** (object)
  - .Net's System.EventArgs
- **CancelEventArgs** (EventArgs)
  - .Net's System.ComponentModel.CancelEventArgs
- **HandledEventArgs** (EventArgs)
  - .Net's System.ComponentModel.HandledEventArgs
- **DialogResult** (Enum)
  - System.Windows.Forms.DialogResult
- **PSNode** (object)
  - _3S.CoDeSys.Core.Objects.IPSNode
- **ProgressCallback** (object)
  - _3S.CoDeSys.Core.IProgressCallback
- **ProjectStructure** (object)
  - _3S.CoDeSys.Core.Objects.IProjectStructure4
- **RcsSelectionVerificationArgs** (object)
  - _3S.CoDeSys.RevisionControlHooks.RcsSelectionVerificationArgs
- **RcsVirtualProject** (object)
  - _3S.CoDeSys.RevisionControlHooks.IRcsVirtualProject
- **RcsVirtualProjectNode** (object)
  - _3S.CoDeSys.RevisionControlHooks.RcsVirtualProjectNode

