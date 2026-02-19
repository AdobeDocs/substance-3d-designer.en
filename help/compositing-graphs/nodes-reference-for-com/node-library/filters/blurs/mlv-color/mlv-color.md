---
title: "MLV color"
description: "Use the MLV Color blur filter to apply motion blur effects to color textures for dynamic visual looks."
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blurs > MLV color"
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blurs/mlv-color.html"
---

# MLV color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![MLV color: icon](MLV_Color_Icon.png "MLV color: icon")

<b>In:</b> Filters &gt; Blurs

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

MLV stands for <b>&#39;Mean of Least Variance&#39;</b>. This filter enhances edges and smoothes out noise in an image.

The filter finds structuring areas in an image and uses them to both sharpen and flatten it. In some cases, this may result in steps along gradients wider than the structuring areas.

</td>
</tr>
</table>

>[!NOTE]
>
> See also [MLV grayscale](../mlv-grayscale/mlv-grayscale.md).

## Input connectors

<b>Input </b>*Color*The color image which should be processed.

## Output connectors

<b>Output</b> *Color*The filtered color image.

## Parameters

<b>Intensity</b> *Float*The strength of the filtering applied to the image.  
Higher values results in more smoothing of details and noise into flatter areas.

<b>Smoothness</b> *Float*The intensity of the smoothing applied to the structuring areas, which results in rounder areas and lessens the stepping effect which may occur at higher filtering intensities.

<b>Criterion</b> *Integer*The criterion used to select the values that will define the structuring areas in the image.  
In other words, how pixels should be *grouped* into areas that should be smoothed out.  
*- Variance:* Select values with the lowest dispersion around the mean, which results in clusters of pixels similar to each other  
*- Coefficient of variation:* Select values while taking the mean into account, which results in less variation in brighter areas inversely

<b>Gaussian</b> *Boolean*Use a Gaussian distribution for grouping pixels into structuring areas.  
When 'True', this results in smoother areas and a reduced flattening effect.

<b>Affect alpha</b> *Boolean*When 'True', filtering is also applied on the alpha channel of the image.  
When 'False', the alpha channel is ignored entirely and left as is in the output.

<b>Iterations</b> *Integer*The number of times the filter is run, where each iteration is applies on the result of the previous one.  
More iterations result in flatter and sharper structuring areas.

## Examples

<table>
  <tr>
    <td>
      <img src="MLV_Variant4A.png" alt="MLV_Variant4A">
      <br><i>Before</i>
    </td>
    <td>
      <img src="MLV_Variant4B.png" alt="MLV_Variant4B">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="MLV_Variant5A.png" alt="MLV_Variant5A">
      <br><i>Before</i>
    </td>
    <td>
      <img src="MLV_Variant5B.png" alt="MLV_Variant5B">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="MLV_Variant3A.png" alt="MLV_Variant3A">
      <br><i>Before</i>
    </td>
    <td>
      <img src="MLV_Variant3B.png" alt="MLV_Variant3B">
      <br><i>After</i>
    </td>
  </tr>
</table>
