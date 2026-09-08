---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/bottom-to-top.html"
breadcrumb-title: ""
description: Use the Bottom To Top node to generate gradient masks from bottom to top based on mesh world position.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Bottom To Top
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Bottom To Top
user-guide-description: ""
user-guide-title: ""
---

# Bottom To Top

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](bottom-to-top.resources/bottom-to-top.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Mask Generators

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/features/smart-materials-and-masks) in [Painter](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/home).

This generates a white to black transition from the bottom to the top of a model, useful for making geometry-based falloffs and selections.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Position</b> <i>Color Input</i> | Baked Position map. Required! |
| <b>Roughness</b> <i>Grayscale Input</i> | This has nothing to do with PBR roughness, but is an (optional) variation map to break up the transition. Only appears when Roughness is set higher than 0. |
| <b>Mask (optional)</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Level</b> <i>0.0 - 1.0</i> | Shifts the average level of the result between black or white, like a brightness adjustment. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the transition. |
| <b>Roughness_Variation</b> <i>0.0 - 1.0</i> | Determines amount of the Roughness map to blend in for variation. Increasing this over 0 reveals the map slot. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="bottom-to-top.resources/bottom-to-top-ex.gif" />
        </td>
    </tr>
</table>
