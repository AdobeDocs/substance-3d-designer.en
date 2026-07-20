---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/luminance-highpass.html"
breadcrumb-title: ""
description: Use the Luminance Highpass node to extract high-frequency luminance details from textures for enhancing surface details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Luminance Highpass
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Luminance Highpass
user-guide-description: ""
user-guide-title: ""
---

# Luminance Highpass

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/luminance-highpass.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Cancels out lighting information by performing a [highpass ](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/highpass/highpass.md)on the input's Luminance value. Useful for fixing photographed textures with lighting information. Can be combined in  [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) with multiple passes to remove different frequencies of lighting details.

Does a slightly better job at preserving colors than [Lighting Cancel Low Frequencies.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/lighting-cancel-low-fre/lighting-cancel-low-frequencies.md)

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Radius</b> <i>0.0 - 64.0</i> | Radius of the highpass effect. A smaller radius cancels smaller lighting, adjust to match the input images. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/luminance-highpass-example.png" />
        </td>
    </tr>
</table>
