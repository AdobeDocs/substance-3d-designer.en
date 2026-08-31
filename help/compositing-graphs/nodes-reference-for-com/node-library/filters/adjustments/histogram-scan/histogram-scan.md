---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/histogram-scan.html"
breadcrumb-title: ""
description: Use the Histogram Scan node to scan and analyze texture histograms for color correction and adjustments.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Histogram Scan
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Histogram Scan
user-guide-description: ""
user-guide-title: ""
---

# Histogram Scan

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](histogram-scan.resources/histogram-scan-01.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Very simple yet useful node that provides an intuitive way to remap the contrast and brightness of input grayscale images. Can be used to "grow" and "shrink" masks in dynamic ways.

[Click here to watch a Substance Academy video on Histogram operations.](https://www.youtube.com/watch?v=p9wcmJBFyGA&t=427s)

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Position</b> <i>0.0 - 1.0</i> | Similar to a brightness control, shifts the midpoint of the result. When used on a gradient input, this expands and shrinks the transition point.<br><br>Important: a default value of 0 means the end result is always black, so try starting with 0.5! |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the result. Can be used to set the hardness of the transition. |
| <b>Invert Position</b> <i>False/True</i> | Inverts the final result. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="histogram-scan.resources/histogram-scan-02.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="histogram-scan.resources/histogram-scan-03.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="histogram-scan.resources/histogram-scan-04.gif" />
        </td>
    </tr>
</table>
