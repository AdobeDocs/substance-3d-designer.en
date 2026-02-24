---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/packaging-plugins.html"
breadcrumb-title: ""
description: Learn how to package Python plugins for Substance 3D Designer for distribution and installation.
helpx_creative_field: ""
helpx_description: Designer > Scripting > Packaging plugins
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Packaging plugins
user-guide-description: ""
user-guide-title: ""
---



# Packaging plugins

## Plugin package contents

Packages are a single file, internally a zip archive, containing a **pluginInfo.json** file with metadata about the plugin,

the plugin code, and any other files or resources needed by the plugin to work.

**PluginInfo.json entries:**

| Entry | Description | Default Value | Notes |
| --- | --- | --- | --- |
| metadata\_format\_version | The format of the metadata file. | 1 | Required.Currently must be set to 1. |
| name | The plugin name. |  | Required.Must match the name of the Python module containing the plugin code |
| version | The plugin version. |  | Optional. |
| author | The plugin author. |  | Optional. |
| email | The plugin author email. |  | Optional. |
| min\_designer\_version | Minimum version of the application required by the plugin to work. | 2019.2 | Optional. |
| platform | Platform the plugin runs on. | any | Optional.For plugins containing compiled code, this entry can be used to disable the plugin in non-supported platforms.Possible values: win, linux, osx, any. |

## Creating a new plugin package project

We provide a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template project to simplify the creation of plugin package projects.

You can use it directly or modify it for you own needs.

The template can be found in the application directory, under <b>plugins/tools/pkgplugintemplate</b>.

1. <b>Install Python if it is not already installed in your system</b>

   Cookiecutter is compatible with both Python 2 and Python 3
1. <b>Install Cookiecutter if you don&#39;t have it already</b>

   Usually this can be done by using pip:

   ```

   pip install cookiecutter
   ```


   For alternative ways to install Cookiecutter or for more information about Cookiecutter you can check the documentation at <https://cookiecutter.readthedocs.io/en/latest/installation.html>
1. <b>Create a new plugin package project</b>

   In a terminal window run:

   ```

   cookiecutter path/to/pkgplugintemplate -o path/to/new/project
   ```


   Fill the information required. The new project will be created in the specified directory.
1. <b>Package your plugin once development is complete</b>

   In a terminal window run:

   ```

   python makepackage.py
   ```

1. The plugin package will be generated in the build directory
