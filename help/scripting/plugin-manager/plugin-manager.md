---
title: "Plugin Manager"
description: ""
helpx_description: "Designer > Scripting > Plugin Manager"
---

# Plugin Manager

The <b>Plugin manager</b> dialog is accessible from the <b>Tools</b> menu in the main menu bar. It lets you see which plugins are *active*, as well as *load and unload* plugins.

![Plugin manager](pluginmgr.png "Plugin manager")

It is also possible to *manually* load plugins, by using the <b>Browse</b> button and choosing a Python file.

The <b>Refresh</b> button can be used to *update* the plugin list. This is useful when plugins are loaded using the Python API.

>[!NOTE]
>
> If the plugin is a *module* (I.e., a directory), it can be loaded by choosing the <b>\_\_init\_\_.py</b> file inside the module.
