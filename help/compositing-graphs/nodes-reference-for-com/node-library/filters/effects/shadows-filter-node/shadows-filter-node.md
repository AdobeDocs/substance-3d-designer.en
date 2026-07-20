---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/shadows-filter-node.html"
breadcrumb-title: ""
description: Use the Shadows filter node to generate shadow effects from input textures for adding depth and realism to materials.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Shadows (Filter Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shadows (Filter Node)
user-guide-description: ""
user-guide-title: ""
---

# Shadows (Filter Node)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/shadows-1.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A raw, grayscale-only version of the [Shape Drop Shadow](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/shape-drop-shadow/shape-drop-shadow.md) node. It only takes a black and white, binary shapes as input and returns only the shadow.

Can be useful if you're just after the shadow and do not want to work with a more complete node, for example when building your own material or baked lighting.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Shadow Distance</b> <i>0.0 - 1.0</i> | Controls how far away the shadow should fall. |
| <b>Light Angle</b> <i>0.0 - 1.0</i> | Controls the incidence angle of the light. |
| <b>Edges Softness</b> <i>0.0 - 1.0</i> | Determines how hard or soft the shadows edges are. |
| <b>Samples</b> <i>1 - 16</i> | Sets quality for the Edges Softness setting. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/shadow-ex.png" />
        </td>
    </tr>
</table>
