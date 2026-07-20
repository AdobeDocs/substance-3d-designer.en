---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/color-match.html"
breadcrumb-title: ""
description: Use the Color Match node to match colors between textures for creating consistent color palettes and harmonizing textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Color Match
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Color Match
user-guide-description: ""
user-guide-title: ""
---

# Color Match

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/color-match-3.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Tries to match the defined *Source Color* range to a *Target Color* range, with support for input slots to define Source and Target.

For simpler versions, see [Replace Color Range](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/replace-color-range/replace-color-range.md) or [Replace Color](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/replace-color/replace-color.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Color Input</i> | Main input to modify for result. |
| <b>Source Color</b> <i>Color Input</i> | Input slot for Source color, only used when 'Source Color Mode' is set to *Input*. |
| <b>Target Color</b> <i>Color Input</i> | Input slot for Target color, only used when 'Target Color Mode' is set to *Input*. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Source Color Mode</b> <i>Average, Parameter, Input</i> | Sets whether Source Color is defined by averaging the input image, by setting a parameter, or by using an input slot. |
| <b>Source Color</b> <i>(Color value)</i> | If Source Color Mode is set to *Parameter*, this parameter determines the Source Color. |
| <b>Target Color Mode</b> <i>Parameter, Image Input</i> | Sets whether Source Color is defined by averaging the input image, by setting a parameter, or using an input slot. |
| <b>Target Color</b> <i>(Color value)</i> | If Target Color Mode is set to *Parameter*, this parameter determines the Target Color. |
| <b>Custom Color Variation</b> <i>False/True</i> | Enables an additional color variation. |
| <b>Color Variation</b> | Sets Hue, Chrominance or Luminance variations to the result if enabled. |
| <b>Use Mask</b> <i>False/True</i> | Toggles usage of either Mask Input or Output, depending on the Mask Mode below. |
| <b>Mask Mode</b> <i>Parameter, Input</i> | Parameter mode outputs a mask detailing how color where changed. Input mode enables a mask to control the strength of the Color Matching effect. |
| <b>Mask</b> | Outputs a mask showing where exactly the Color Matching effect was applied, with additional controls for smoothing and blurring out the resulting mask. |
