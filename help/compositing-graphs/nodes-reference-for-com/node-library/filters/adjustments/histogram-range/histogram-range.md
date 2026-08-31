---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/histogram-range.html"
breadcrumb-title: ""
description: Use the Histogram Range node to remap texture values based on histogram ranges for color correction and adjustments.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Histogram Range
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Histogram Range
user-guide-description: ""
user-guide-title: ""
---

# Histogram Range

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](histogram-range.resources/histogram-range-01.png){width="128px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Reduce and/or move the range of a grayscale input. Can be used to remap transitions, similar to [Contrast Luminosity](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/contrast-luminosity/contrast-luminosity.md), but with different controls that might make more sense for some situations.  
Also see [Histogram Scan](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-scan/histogram-scan.md) for another, more useful way to remap the range.

[Click here to watch a Substance Academy video on Histogram Range.](https://www.youtube.com/watch?v=p9wcmJBFyGA&t=517s)

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Range</b> <i>0.0 - 1.0</i> | How much to reduce the range down from. This is similar to moving both Levels min and Max sliders inwards. |
| <b>Position</b> <i>0.0 - 1.0</i> | Offset for the range reduction, setting a different midpoint for the range reduction. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="histogram-range.resources/histogram-range-02.gif" />
        </td>
    </tr>
</table>
