---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/multi-color-equalizer.html"
breadcrumb-title: ""
description: Use the Multi Color Equalizer node to equalize colors across multiple texture channels for consistent scanned material processing.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi Color Equalizer
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi Color Equalizer
user-guide-description: ""
user-guide-title: ""
---

# Multi Color Equalizer

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/color-equalizer-multi.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is the multi-input version of [Color Equalizer](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/color-equalizer/color-equalizer.md). It evens out color differences and removes unwanted tints at a user-selectable scale. It is mainly intended for use with multi-angle photos, which are then combined with [Multi-Angle to Albedo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-albedo/multi-angle-to-albedo.md) or [Multi-Angle to Normal](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-normal/multi-angle-to-normal.md).

>[!NOTE]
>
> See the original [Color Equalizer](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/color-equalizer/color-equalizer.md) for more info.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input 1-8</b> <i>Color Input</i> | Multiple inputs to process. |
| <b>Mask Input</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Input Count</b> <i>1 - 8</i> | Sets the number of inputs to process in parallel. |
| <b>Input Tiled</b> <i>False/True</i> | Optionally preserves tiling on edges. |
| <b>Radius</b> <i>0.0 - 50.0</i> | Sets equalising radius. A larger radius will only remove large color differences. This requires tweaking for every image. |
| <b>Bright/Dark Balance</b> <i>0.0 - 1.0</i> | Bias setting to leave or remove darker tints. |
| <b>Custom Color Variation</b> <i>False/True</i> | Allows you to vary the effect towards a user-specified color. |
| <b>Color Variation</b> | Only active if Custom Color Variation is enabled. Settings allow you to select a tint offset to equalise towards. |
| <b>Hue</b> <i>0.0 - 360.0</i> |  |
| <b>Chroma</b> <i>0.0 - 1.0</i> |  |
| <b>Luma</b> <i>0.0 - 1.0</i> |  |
| <b>Mask Source</b> <i>None, Image Average, Color Parameter, Input</i> | Sets whether any masking should happen. Color Parameter enables additional settings below, Input switches to a user-defined mask input. |
| <b>Mask</b> | Only active with Color Parameter masking. Contains additional masking parameters to determine the mask based on the image itself. The below parameters allow you to precisely convert a tint to a binary mask on which the equalisation is applied. Note that the Radius parameter's effects can become much less pronounced when using these settings. |
| <b>Color</b> <i>(Color value)</i> |  |
| <b>Hue Range</b> <i>0.0 - 360.0</i> |  |
| <b>Chroma Range</b> <i>0.0 - 1.0</i> |  |
| <b>Luma Range</b> <i>0.0 - 1.0</i> |  |
| <b>Blur</b> <i>0.0 - 2.0</i> |  |
| <b>Smoothness</b> <i>0.0 - 2.0</i> |  |
