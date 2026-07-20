---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/utilities-mesh-based-generators/3d-planar-projection.html"
breadcrumb-title: ""
description: Use the 3D Planar Projection node to project textures onto mesh surfaces using planar projection for texture mapping.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Utilities (Mesh Based Generators) > 3D Planar Projection
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Planar Projection
user-guide-description: ""
user-guide-title: ""
---

# 3D Planar Projection

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/3d-planar-gray.png)![](../../../../../../assets/3d-planar.png)

<b>In:</b> Mesh Based Generators &gt; Utilities

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs a planar projection based on baked mesh data (Position and World Normal Maps). Allows you to project and place decals across seams, independent of original UV-mapping.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Position Map</b> <i>Color Input</i> | Baked Position Map |
| <b>World Space Normal</b> <i>Color Input</i> | Baked World Space Normal Map |
| <b>Projected Texture</b> <i>Color Input</i> | Input texture to project onto target. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Positioning</b> |  |
| <b>Project Input</b> <i>UV Position, World Space Position</i> | Choose whether the projection position is set in 2D/UV or in 3D/World space. |
| <b>Target UV Position</b> | Only with UV Position Input, best used to pick a point in the 2D view on the Position map. |
| <b>Target Position</b> <i>(Color value)</i> | Only with World Space Position Input, lets you define an exact 3D coordinate. |
| <b>Target Normal</b> <i>(Color value)</i> |  |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Rotates the projected texture along it' normal axis. |
| <b>Scale</b> <i>0.0 - 1.0</i> | Set the global scale for the projected texture. |
| <b>Size</b> <i>0.0 - 2.0</i> | Perform non-uniform scaling on the projected texture. |
| <b>Masking</b> |  |
| <b>Maximum Depth</b> <i>0.0 - 1.0</i> | Controls how deep the projected texture will appear, when it will cut-off. |
| <b>Depth Fade</b> <i>0.0 - 1.0</i> | Set the transition for the cut-off depth to be sudden or faded. |
| <b>Normal Threshold</b> <i>-1.0 - 1.0</i> | Set the treshold for surfaces not exactly aligned with the projection normal. |
| <b>Normal Fade</b> <i>0.0 - 1.0</i> | Set the transition for surfaces not aligned to sudden or fade. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3d-planar-projection-ex.gif" />
        </td>
    </tr>
</table>
