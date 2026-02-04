---
title: "Plugin search paths"
description: ""
helpx_description: "Designer > Scripting > Plugin search paths"
---

# Plugin search paths

Designer will look for plugins in specific directories (i.e. search paths). This page explains how to configure these paths.

Users can *add custom directories* manually in the software preferences, or specify them using environment variables.

## Manually adding plugin search paths

1. Go to <b>Edit &gt; Preferences...</b>
1. Select the <b>Projects</b> category
1. Select the <b>Project File</b> you want to edit
1. In the <b>Python</b> tab, click on the *<b>+</b>*button to add the directory that contains the plugins
1. Click <b>OK</b> to validate

![Settings up Python plugins search paths Project settings](image-70.png "Settings up Python plugins search paths Project settings")

## Using environment variables

The application will look for plugins in all paths specified using the <b>SBS\_DESIGNER\_PYTHON\_PATH </b>environment variable.
