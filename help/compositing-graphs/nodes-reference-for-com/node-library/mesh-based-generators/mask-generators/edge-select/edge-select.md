---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/edge-select.html"
breadcrumb-title: ""
description: Use the Edge Select node to generate masks selecting mesh edges for creating edge-based weathering and wear effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Edge Select
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Edge Select
user-guide-description: ""
user-guide-title: ""
---

# Edge Select

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/edge-select.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask is the best way to select any kind of edge based on the curvature. Convex, Concave at any level or contrast can be isolated, providing an excellent shortcut to avoid manually doing this through a [Levels node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/levels/levels.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Curvature</b> <i>Grayscale Input</i> | Baked map used for highlighting edges. Required! |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Sets the total amount of edge highlighting for both Convex and Concave. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the highlighting for both Convex and Concave. |
| <b>Convex</b> |  |
| <b>Convex Edges Width</b> <i>0.0 - 1.0</i> | Sets width of the highlighting for Convex edges. Keep in mind that increasing Softness slightly can lead to thinner edges. |
| <b>Convex Softness</b> <i>0.0 - 1.0</i> | Set softness of the transition for Convex edges. |
| <b>Convex Intensity</b> <i>0.0 - 1.0</i> | Sets the maximum intensity of the Edge highlighting for Convex edges. Set to 0 for no highlighting. |
| <b>Concave</b> |  |
| <b>Concave Edges Width</b> <i>0.0 - 1.0</i> | Set width of the highlighting for Concave edges. Keep in mind that increasing Softness slightly can lead to thinner edges. |
| <b>Concave Softness</b> <i>0.0 - 1.0</i> | Set softness of the transition for Concave edges. |
| <b>Concave Intensity</b> <i>0.0 - 1.0</i> | Set the maximum intensity of the Edge highlighting for Concave edges. Set to 0 for no highlighting. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/edge-select-ex.gif" />
        </td>
    </tr>
</table>
