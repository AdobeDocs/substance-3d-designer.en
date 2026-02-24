---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/technical-issues/baking-issues.html"
breadcrumb-title: ""
description: Find troubleshooting steps for technical issues related to baking textures in Substance 3D Designer.
helpx_creative_field: ""
helpx_description: Designer > Technical issues > Baking issues
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Baking issues
user-guide-description: ""
user-guide-title: ""
---



# Baking issues

This page lists technical issues related to [baking textures](../../help/bakers/bakers.md) in Substance 3D Designer, and offer troubleshooting steps for each.

## In this page

'Match by name' does not work

## 'Match by name' does not work

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<b>!&#91;(error)&#93;(error.svg) Issue</b>

When the 'Match' option is set to 'By mesh name', the matching does not appear to be applied, or not consistently across all scene objects.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

In Designer versions 14.1 and lower, low poly and high poly objects were matched using the name of their *parent* objects – in most cases, their parent transform.

Since Designer 15.0, the name of the *geometry* objects are used directly.

</td>
<td style="border: 0;" valign="top">

![Geometry object and its parent in the scene tree](sceneTree_objectsName.png "Geometry object and its parent in the scene tree"){zoomable="yes"}

</td>
</tr>
</table>

There are two paths you may take to get the expected macthing:

* Adjust the name of the geometry objects to apply matching names.
* Revert to the behaviour or previous Designer versions, by ajusting the ['Name filtering mode' option](../../help/interface/preferences-window/project-settings/project-settings.md) in the Project settings:
  1. Go to Edit &gt; Preferences &gt; Projects
  1. Select the last project file in the list
  1. Below the list of project files, select the 'Bakers' tab
  1. Set the 'Name filtering mode' to 'Parent name (Legacy)
