---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/pipeline-and-project-configuration/environment-variables.html"
breadcrumb-title: ""
description: Learn how to use environment variables in Substance 3D Designer for configuring paths and system settings.
helpx_creative_field: ""
helpx_description: Designer > Pipeline and Project Configuration > Environment variables
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Environment variables
user-guide-description: ""
user-guide-title: ""
---


# Environment variables

This page list environment variables that can be used to override the default behavior of the application.

| Variable | Description |
| --- | --- |
| **SBS\_DESIGNER\_PYTHON\_PATH** | The path from which Designer will load [Python plugins](../../scripting/plugin-basics/plugin-basics.md). |
| **SUBSTANCE\_DESIGNER\_LICENSE** | The location of the license file (*license.key*) which should be used by Designer.   Overrides the path set in Designer's [Activation Wizard](../../getting-started/activation-and-licenses/activation-and-licenses.md).  **Note:**  Old versions may need to use an alternate variable name:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>SUBSTANCE&#95;DESIGNER&#95;6&#95;LICENSE</strong></li><li data-preserve-html="true"><strong>SUBSTANCE&#95;DESIGNER&#95;5&#95;LICENSE</strong></li></ul> |
| <b>OCIO</b> | The path to the OCIO configuration file which should be used when using OpenColorIO [color management](../../color-management/color-management.md).   Overrides the path set in Designer's color management settings in the [Project settings](../../interface/preferences-window/project-settings/project-settings.md). |
| **ALLEGO\_LICENSE\_IDLE\_DELAY** | The delay in seconds before releasing a license seat in case of a multi-user configuration   Default is 7200 seconds (2 hours). |
