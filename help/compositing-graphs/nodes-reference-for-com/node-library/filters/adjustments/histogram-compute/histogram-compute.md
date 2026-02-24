---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/histogram-compute.html"
breadcrumb-title: ""
description: Use the Histogram Compute node to calculate histogram data from textures for analysis and processing.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Histogram compute
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Histogram compute
user-guide-description: ""
user-guide-title: ""
---


# Histogram compute

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Histogram compute: icon](histogram_compute.png "Histogram compute: icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Computes the histogram for a grayscale image.

The histogram is encoded as a row of pixels in an image, where each pixel value is the *population* of the color value matching the pixel position on the X-axis.  
E.g., a pixel value of 75 at (0.25, 0) means there are 75 pixels which have the 0.25 color value in the image.

</td>
</tr>
</table>

The node also outputs the *cumulative distribution function* (CDF) computed for the image.

Custom tools can be created using the data computed by the node, such as custom masks, as shown below in the 'Examples' section.

>[!IMPORTANT]
>
> All values out of the &#91;0,1&#93; range are clamped, therefore the histogram may not be accurate for HDR images.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">

### Output connectors

</td>
<td style="border: 0;" valign="top">

### Parameters

</td>
</tr>
</table>

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale* PRIMARY | The image for which the histogram should be computed. |

## Output connectors

|  |  |
| --- | --- |
| <b>Histogram</b> *Grayscale* | The histogram computed for the input image, encoded as a row of pixels where each pixel value is the *population* of the color value matching the pixel position on the X-axis.   E.g., a pixel value of 75 at (0.25, 0) means there are 75 pixels which have the 0.25 color value in the image. |
| <b>CDF</b> *Grayscale* | The result of the *cumulative distribution function* (CDF) computed for the image, encoded in a row of pixels where each pixel is the sum of all pixel values to its left.   That sum is then *normalized* against the total number of pixels in the image. |

## Parameters

|  |  |
| --- | --- |
| <b>Histogram resolution</b> *Integer* | The width of the histogram. A higher value allows for a finer value distribution.   Available resolutions are, in pixels:  256, 512, 1024, 2048, 4096 |

## Examples

![Histogram compute: Example 1](histogram_compute_example_1.jpg "Histogram compute: Example 1"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="histogram_compute_example_2_before.jpg" alt="histogram_compute_example_2_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="histogram_compute_example_2_after.jpg" alt="histogram_compute_example_2_after">
      <br><i>After</i>
    </td>
  </tr>
</table>
