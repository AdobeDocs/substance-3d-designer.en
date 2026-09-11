---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/flood-fill-to-gradient.html"
breadcrumb-title: ""
description: Use the Flood Fill to Gradient node to fill regions with gradient values for creating smooth color transitions.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to Gradient
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Flood Fill to Gradient
user-guide-description: ""
user-guide-title: ""
---

# Flood Fill to Gradient

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](flood-fill-to-gradient.resources/floodfill-to-gradient.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Transforms a [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md) base into (randomly oriented) gradients. Very useful for creating a Heightmap where tiles are randomly tilted and sloped.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Flood Fill</b> <i>Color Input</i> | Base Flood fill data. |
| <b>Angle Input</b> <i>Grayscale Input</i> | Opttional map to determine per-cell angle with an external map. |
| <b>Slope Input</b> <i>Grayscale Input</i> | Optional map to determine per-cell gradient slope-strength. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Angle</b> <i>0.0 - 1.0</i> | Sets uniform, global angle/direction for all tiles. |
| <b>Angle Variation</b> <i>0.0 - 1.0</i> | Randomises the angle for each tile individually. This is the most useful and powerful parameter! |
| <b>Multiply by Bounding Box Size</b> <i>0.0 - 1.0</i> | Scales the entire linear effect by the tile's individual bounding box size. This means smaller tiles will end up being darker than larger ones. |
| <b>Angle Image Input Multiplier</b> <i>0.0 - 1.0</i> | Set influence of optional Angle Input map on generated gradient directions |
| <b>Slope Image Input Multiplier</b> <i>0.0 - 1.0</i> | Set influence of optional Slope Input map on generated gradient slope strength. |
| <b>Multiply by Slope Intensity</b> <i>0.0 - 1.0</i> |  |
| <b>Flat Slope Color</b> <i>(Grayscale value)</i> | Allows setting of solid value for flat slopes. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="flood-fill-to-gradient.resources/floodgradient-ex2.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="flood-fill-to-gradient.resources/floodgradient-ex1.png" />
        </td>
    </tr>
</table>
