---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/histogram-equalize.html"
breadcrumb-title: ""
description: Use the Histogram Equalize node to redistribute pixel intensities for improved contrast and brightness.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Histogram equalize
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Histogram equalize
user-guide-description: ""
user-guide-title: ""
---

# Histogram equalize

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Histogram equalize: icon](../../../../../../assets/histogram_equalize.png "Histogram equalize: icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Equalizes the histogram for a grayscale image, effectively adjusting the grayscale values aiming for an equal distribution.

</td>
</tr>
</table>

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
| <b>Input</b> *Grayscale* PRIMARY | The image for which the histogram should be equalized. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* | The result image with histogram equalization applied. |

## Parameters

|  |  |
| --- | --- |
| <b>Histogram resolution</b> *Integer* | The width of the histogram. A higher value allows for a finer value distribution.   Available resolutions are, in pixels:  256, 512, 1024, 2048, 4096 |
| <b>Histogram smoothing</b> *Float* | The histogram may be smoothed by redistributing the grayscale values in the image to equalize the *difference* between each value.   This parameter adjusts the intensity of that smoothing. |

## Examples

<table>
  <tr>
    <td>
      <img src="histogram_equalize_example_1_before.jpg" alt="histogram_equalize_example_1_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="histogram_equalize_example_1_after.jpg" alt="histogram_equalize_example_1_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Histogram equalize: Example 1](../../../../../../assets/histogram_equalize_example_3.png "Histogram equalize: Example 1"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="histogram_equalize_example_2_before.jpg" alt="histogram_equalize_example_2_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="histogram_equalize_example_2_after.jpg" alt="histogram_equalize_example_2_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Histogram equalize: Example 2](../../../../../../assets/histogram_equalize_example_5.png "Histogram equalize: Example 2"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="histogram_equalize_example_4_before.jpg" alt="histogram_equalize_example_4_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="histogram_equalize_example_4_after.jpg" alt="histogram_equalize_example_4_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Histogram equalize: Example 3](../../../../../../assets/histogram_equalize_example_6.png "Histogram equalize: Example 3"){zoomable="yes"}
