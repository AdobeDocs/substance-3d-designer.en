---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/flood-fill-to-grayscale-color.html"
breadcrumb-title: ""
description: Use the Flood Fill to Grayscale Color node to fill connected regions with grayscale colors for creating monochrome patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to GrayscaleColor
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Flood Fill to GrayscaleColor
user-guide-description: ""
user-guide-title: ""
---

# Flood Fill to Grayscale/Color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](flood-fill-to-grayscale-color.resources/flood-fill-to-grayscale-color-01.png){width="128px"}

![](flood-fill-to-grayscale-color.resources/flood-fill-to-grayscale-color-02.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Uses Flood Fill data to generate grayscale or color value swatches. Unlike [Flood Fill to Random Grayscale](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-random-gra/flood-fill-to-random-grayscale.md), these two nodes allow more control to set the exact variation and tones, with an additional extra input map to determine the base value to randomize on a per-cell basis.

It's a powerfull system to give every cell a unique value or color, yet still retain control and base it off of a pre-determined input.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Flood Fill</b> <i>Color Input</i> |  |
| <b>Grayscale/Color Input</b> <i>Grayscale/Color Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Luminance/Color Adjustment</b> <i>-1.0 - 1.0</i> | Set the bias or base value for the node. When a Grayscale or Color input is used, this is used to change that initial value as a starting point. |
| <b>Luminance/Color Random</b> <i>-1.0 - 1.0</i> | Set the amount of variation. |
