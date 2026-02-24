---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/working-with-3d-scenes/exporting-scenes.html"
breadcrumb-title: ""
description: Export 3D scenes with all edits made in Designer using the Export scene action in the 3D View Scene menu.
helpx_creative_field: ""
helpx_description: Designer > Working with 3D scenes > Exporting scenes
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Exporting scenes
user-guide-description: ""
user-guide-title: ""
---


# Exporting scenes

When you need to export the scene with all edits made in Designer, use the 'Export scene...' actions in the [3D View](../../interface/3d-view/3d-view.md)'s 'Scene' menu.

For exports to USD formats, the contents of the scene will match the tree displayed in the [Scene browser](../../interface/3d-view/scene-browser/scene-browser.md).

For other formats, the contents of the scene and its internal structure will depend on the features supported by the selected file format.

>[!NOTE]
>
> All items added to the scene by Designer will be included in the exported scene: the default camera, the default environment, all material copies any additional lights.

![Scene export actions](exportActions.png "Scene export actions"){zoomable="yes"}

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Export scene

</td>
<td style="border: 0;" valign="top">

### Export scene as layers

</td>
<td style="border: 0;" valign="top">

### Textures

</td>
</tr>
</table>

## Export scene

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

The ‘Export scene…’ action in the ‘Scene’ menu exports edited 3D scenes destructively: the scene is *flattened* and any reference to the original is lost.

This means edits to the original scene do not impact the exported scene at all.

</td>
<td style="border: 0;" valign="top">

![Exported scene files - Flattened](exportFlattened.png "Exported scene files - Flattened"){zoomable="yes"}

</td>
</tr>
</table>

## Export scene as layers

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

The ‘Export scene as layers…’ action exports to <b>USD</b> formats (.usd, .usda, .usdc, .usdz) and is *non-destructive*: the main exported file helms a *chain of references* where all the edited aspects of the new scene are stored into separate USD files.

This means edits to the original scene carry over to the exported scene.

</td>
<td style="border: 0;" valign="top">

![Exported scene files - Layered](exportLayered.png "Exported scene files - Layered"){zoomable="yes"}

</td>
</tr>
</table>

The exported files follow this structure:

* <b>Main file</b>
  * <b>.layers</b>: References the sublayers below and declares the material overrides, which bind of geometry to the material copies created by Designer.
    * <b>.assembly</b>: References the .scene# file and declares the geometry overrides, which bring the data recomputed by Designer of the geometry impacted by overridden materials.
      * <b>.scene&#35;</b>: References the original scene.
    * <b>.camera</b>: Declares the camera added by Designer to the scene.
    * <b>.light</b>: Declares the lights added by Designer to the scene.
    * <b>.material</b>: Declares the materials copies added by Designer to the scene, which use the exported textures.

## Textures

Textures are exported in a directory next to the exported file and named after it, with a ‘<b>\_textures</b>’ suffix.

They use the <b>PNG</b> format, except HDR textures (floating-point) which use the <b>EXR</b> format.
