---
title: "Auto Crop | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Auto Crop"
---

# Auto Crop

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](autocropgrayscale.png){width="200px"}

</td>
<td style="border: 0;" valign="top">

![](autocropcolor.png){width="200px"}

</td>
</tr>
</table>

**In:** Filters*/Transforms*

**Simple**

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

The **Auto Crop** node adjusts the **Input** so that its content is either placed at the *center* of the image without being resized, or *resized to the span* of the image.

The content of the image is defined by a box fitted to the *first and last pixels* on **X** and **Y** which values are *higher than 0* (i.e. non-black). The **Color** version lets you choose from the RGB and Alpha channels for defining that box.

</td>
</tr>
</table>

## Parameters

* **Mode** *Integer*Set the cropping method which should be applied:  
  * *Crop square*: the image is cropped so that the shape is at the center of the smallest *square* image which can fully include it  
  * *Crop auto*: The image is cropped so that the shape is at the center of the smallest *square or non-square* image which can fully include it  
  * *Fit (Keep ratio)*: The image is resized to the *full span* of the image while keeping its *proportions* (i.e. width to length ratio)  
  * *Fill (Stretch)*: The image is resized to the *full span* of the image
* **Use alpha** *Boolean*Use the alpha channel of the **Input** to determine the image content's *bounds* for cropping. When set to *False*, black pixels are used instead.  
  *Note*: This parameter is only available in the **Color** version of the node.
* **Filtering Mode** *Integer*Defines how to treat the sampled results when *interpolating* between pixels:  
  * *Nearest*: will sample exactly the *same* value (faster)  
  * *Bilinear*: will apply a bilinear filter on the result for a *smoother* look  
  * *Auto*: Uses the most appropriate of the two modes above depending on the selected **Mode** for cropping

## Example Images

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](autocrop-demo-01-resized.gif){width="768px"}

</td>
<td style="border: 0;" valign="top">

![](autocrop-variant2.jpg){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](autocrop-variant.jpg){width="128px"}

</td>
<td style="border: 0;" valign="top">

![](autocrop-variant4.png){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](autocrop-variant3.png){width="256px"}

</td>
<td style="border: 0;" valign="top">

![](autocrop-node.png){width="420px"}

</td>
</tr>
</table>
