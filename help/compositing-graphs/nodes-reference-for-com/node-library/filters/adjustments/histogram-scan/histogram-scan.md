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
<td style="border: 0;" valign="top">

![](histogram-scan-1.png){width="128px"}

## Histogram Scan

**In:** *Filters/Adjustments*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Very simple yet useful node that provides an intuitive way to remap the contrast and brightness of input grayscale images. Can be used to "grow" and "shrink" masks in dynamic ways.

[Click here to watch a Substance Academy video on Histogram operations.](https://www.youtube.com/watch?v=p9wcmJBFyGA&amp;t=427s)

## Parameters

* **Position**: *0.0 - 1.0*Similar to a brightness control, shifts the midpoint of the result. When used on a gradient input, this expands and shrinks the transition point.  
  Important: a default value of 0 means the end result is always black, so try starting with 0.5!
* **Contrast**: *0.0 - 1.0*  
  Adjusts the contrast of the result. Can be used to set the hardness of the transition.
* **Invert Position**: *False/True*Inverts the final result.

## Example Images

![](histogram-scan.gif)

![](histogram-scan2.gif)

![](histogram-scan3.gif)

</td>
</tr>
</table>
