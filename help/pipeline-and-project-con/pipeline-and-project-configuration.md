---
title: "Pipeline and Project Configuration"
description: ""
helpx_description: "Designer > Pipeline and Project Configuration"
---

# Pipeline and Project Configuration

Substance 3D Designer has a powerful system to configure the application for pipeline usage. Through an advanced system of hierarchical "**Project**" files the application can be instantly configured to Studio or Project standards, with all configurations and Library content being under version control. The main goal of the system is to centralize all pipeline-relevant settings, yet still allow multiple configurations to override and expand each other.

>[!WARNING]
>
> This system is not intended for single users with simpler requirements, but rather for *studios with large projects and teams* and a higher need for organization. To make full use of this system, a fair amount of planning and preparation, as well as a certain degree of automated set-up is recommended!

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Configuration files hierarchy

Designer has 3 tiers or Configuration files, each with a different purpose. For Windows all files are located in *~User\AppData\Local\Adobe\Adobe Substance 3D Designer.*

The image illustrates the relation between the different files in Designer's default setup, after a fresh install.

</td>
<td style="border: 0;" valign="top">

![Configuration files hierarchy](filestructureoverview.png "Configuration files hierarchy")

</td>
</tr>
</table>

* <b>&#91;User\_Preferences.XML&#93;(user-preferences-aut/user-preferences-automating-setup.md)</b> contains general program settings, of which all but one are not relevant to project pipelines. This file is unique and can not be swapped out, Designer is hardcoded to utilize this exact file.  
  It contains one single reference to a Configuration file.
* <b>&#91;Default\_Configuration.SBSCFG&#93;(configuration-list-sbscfg/configuration-list-sbscfg.md)</b> can be swapped out for other SBSCFG files with different names, but only one SBSCFG file can be used at the same time.  
  It contains multiple references to Project files. *Note that for the default configuration these files are not explicitly defined, but are hard-coded!*
* <b>&#91;Project.SBSPRJ&#93;(project-configuration-fil/project-configuration-files-sbsprj.md)</b> files contain project/pipeline relevant settings. Multiple Projects can be defined in a hierarchy, overriding or expanding on the previously defined project.

## Designer pipeline setup

Every type of file is explained with more detail on child pages of this page, but the short overview of how to ideally define a custom setup for Designer is as follows:

1. <b>Identify and group what settings to add into your Project files.</b> This is different for every studio and requires a certain amount of planning!  
   In almost every case at least 2 Projects should be defined: one for global, studio-wide defaults (like standard templates, shader files, baking settings), and one with more specific content such as Library content. If you have different projects running simultaneously you might want to create multiple project configurations for each (so 3 or more total).
1. <b>Create the relevant &#91;SBSPRJ files&#93;(project-configuration-fil/project-configuration-files-sbsprj.md) and place them and their content under version control.</b> It is strongly recommended to separate Designer pipeline and library content from your actual project content and resources (3D models, textures, code) by creating a *separate repository* for it.
1. <b>Create an&#91; SBSCFG configuration&#93;(configuration-list-sbscfg/configuration-list-sbscfg.md) file listing all project files, place it under version control</b>. If you have multiple projects, you can create a Config for every project.
1. <b>Set up every user&#39;s &#91;User\_Preferences.xml&#93;(user-preferences-aut/user-preferences-automating-setup.md) to reference their relevant configuration file.</b>  
   You can have every user do this manually, or you can script this by injecting lines into their XML file. [More info on the relevant page](user-preferences-aut/user-preferences-automating-setup.md).
