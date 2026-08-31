---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/hald-clut.html"
breadcrumb-title: ""
description: Use the Hald CLUT node to apply color lookup tables using Hald CLUT format for color grading and correction.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Hald CLUT
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Hald CLUT
user-guide-description: ""
user-guide-title: ""
---

# Hald CLUT

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](hald-clut.resources/hald-clut-01.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Applies a LUT on the input image. The LUT has to be in the Hald format in 4096\*4096 resolution. See <http://www.quelsolaar.com/technology/clut.html> for more information.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>input</b> <i>Color Input</i> | Image onto which to apply the LUT. |
| <b>lut</b> <i>Color Input</i> | Lut input slot. Must be 4096x4096. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>LUT Intensity by Alpha</b> <i>False/True</i> | Defines if the LUT effect is weighted by the alpha channel. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="hald-clut.resources/hald-clut-02.jpg" />
        </td>
    </tr>
</table>
