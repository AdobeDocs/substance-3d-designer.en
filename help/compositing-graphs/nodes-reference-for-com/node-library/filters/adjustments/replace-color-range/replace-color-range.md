---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/replace-color-range.html"
breadcrumb-title: ""
description: Use the Replace Color Range node to replace colors within a specified range with new colors for color correction.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Replace Color Range
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Replace Color Range
user-guide-description: ""
user-guide-title: ""
---

# Replace Color Range

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](replace-color-range.resources/replace-color-range-01.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Replaces Source Color by Target Color, with additional controls. Can for example be used to re-color parts of a Material ID map (bake).

For a more advanced version, see [Color Match.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/color-match/color-match.md)

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Source Color</b> <i>(Color value)</i> | Color to replace. |
| <b>Target Color</b> <i>(Color value)</i> | Color to replace with. |
| <b>Source Range</b> <i>0.0 - 1.0</i> | Range or tolerance of the picked Source. Can be increased so further neighbouring colours are also hue-shifted. |
| <b>Threshold</b> <i>0.0 - 1.0</i> | Falloff/contrast for range. Set low to replace only Source color, set higher to replace colors blending into Source as well. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="replace-color-range.resources/replace-color-range-02.png" />
        </td>
    </tr>
</table>
