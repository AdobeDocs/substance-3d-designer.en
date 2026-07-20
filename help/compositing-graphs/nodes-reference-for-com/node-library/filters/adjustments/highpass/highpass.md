---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/highpass.html"
breadcrumb-title: ""
description: Use the Highpass node to extract high-frequency details from textures for creating sharpening and detail enhancement effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Highpass
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Highpass
user-guide-description: ""
user-guide-title: ""
---

# Highpass

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/high-pass-greyscale.png){width="128px"}

![](../../../../../../assets/high-pass.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs a highpass filter, available in color as well as in a grayscale version. Similar to the Photoshop action with the same name.  
Useful for removing large Luminance differences in images, such as when cleaning up textures for tiling.

Important: make sure to use the appropriate version for your input! Use "Highpass" for Color inputs, "Highpass Grayscale" for Grayscale inputs.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Radius</b> <i>0.0 - 64.0</i> | Filter radius: a small radius removes small differences, a bigger radius removes large areas. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/highpass.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/highpass-example.png" />
        </td>
    </tr>
</table>
