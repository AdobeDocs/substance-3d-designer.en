---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/surface-brush.html"
breadcrumb-title: ""
description: Use the Surface Brush node to generate masks based on surface orientation for creating directional weathering and wear effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Surface Brush
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Surface Brush
user-guide-description: ""
user-guide-title: ""
---

# Surface Brush

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](surface-brush.resources/surface-brush-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents an interesting effect of metal-brushing on an object surface, occluded by object geometry and AO.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>World Space Normal</b> <i>Color Input</i> |  |
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Ambient Occlusion</b> <i>Grayscale Input</i> | Baked map used for internal effects and masking. |
| <b>Position</b> <i>Grayscale Input</i> |  |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets global effect level, gradually revealing. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. |
| <b>Scratches Lenght</b> <i>0.0 - 8.0</i> | Sets the length of scratches. Smaller values are more like dots, higher values are long streaks. |
| <b>Occlude Axis</b> <i>X, Y, Z, none</i> | Axis of the object that should receive scratches. Does not alter direction of the scratches. |
| <b>Occlude Axis Intensity</b> <i>0.0 - 1.0</i> | Strength of the axis occlusion effect. |
| <b>Occlusion</b> <i>0.0 - 1.0</i> | Strength of the AO on occluding scratches. |
| <b>Sharpen Intensity</b> <i>0.0 - 1.0</i> | Set amount of post-sharpening to apply to the scratches. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="surface-brush.resources/surface-brush-02.gif" />
        </td>
    </tr>
</table>
