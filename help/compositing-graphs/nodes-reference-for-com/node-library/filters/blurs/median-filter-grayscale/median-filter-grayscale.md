---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blurs/median-filter-grayscale.html"
breadcrumb-title: ""
description: Use the Median Filter Grayscale node to reduce noise and preserve edges in grayscale textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blurs > Median filter grayscale
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Median filter grayscale
user-guide-description: ""
user-guide-title: ""
---

# Median filter grayscale

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Median filter grayscale: icon](../../../../../../assets/MedianFilter_Icon_Grayscale.png "Median filter grayscale: icon")

<b>In:</b> Filters &gt; Blurs

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This filter smoothes out noise in an image while preserving edges.

For every pixel, the node computes a grayscale value according to the median value of the pixel's neighbours.

</td>
</tr>
</table>

>[!NOTE]
>
> See also [Median filter color](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blurs/median-filter-color/median-filter-color.md).

## Input connectors

<b>Input </b>*Grayscale*The grayscale image that the filter should be applied to.

## Output connectors

<b>Output</b>*Grayscale*The grayscale image computed by applying the filter to the input grayscale image.

## Parameters

<b>Kernel size</b> *Integer*A kernel is a specific group of values used in a filter’s computations. In this context, it is the values of the neighbouring pixels.  
For every pixel, the filter takes all neighbors around that pixel in a square kernel and computes the median value of all neighbors.  
This parameter controls the size of that square kernel, in pixels. A larger kernel results in a stronger, farther-reaching smoothing effect at the cost of some detail.  
*- 3x3:* a kernel 3 pixels wide and 3 pixels tall, totalling 8 neighbor pixels.  
*- 5x5:* a kernel 5 pixels wide and 5 pixels tall, totalling 24 neighbor pixels.

<b>Filter type</b> *Integer*The computation applied to the neighbors sampled in the kernel.  
*- Median:* Use the median value of all neighbors directly.  
*- MLMAD:* Stands for 'Median Of Least Median Absolute Deviation'. The deviation accounts for how different a value is from the median. Instead of using the median value directly which may be skewed by an outlier pixel with high deviation, the MLMAD method uses the median of all deviations. This method results in a stronger smoothing effect that may flatten areas according to the kernel size.

## Examples

<table>
  <tr>
    <td>
      <img src="MedianFilter_Variant2A.png" alt="MedianFilter_Variant2A">
      <br><i>Before</i>
    </td>
    <td>
      <img src="MedianFilter_Variant2B.png" alt="MedianFilter_Variant2B">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="MedianFilter_Variant4A.png" alt="MedianFilter_Variant4A">
      <br><i>Before</i>
    </td>
    <td>
      <img src="MedianFilter_Variant4B.png" alt="MedianFilter_Variant4B">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="MedianFilter_Variant1A.png" alt="MedianFilter_Variant1A">
      <br><i>Before</i>
    </td>
    <td>
      <img src="MedianFilter_Variant1B.png" alt="MedianFilter_Variant1B">
      <br><i>After</i>
    </td>
  </tr>
</table>
