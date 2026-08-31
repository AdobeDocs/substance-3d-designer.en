---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/histogram-render.html"
breadcrumb-title: ""
description: Use the Histogram Render node to visualize histogram data as a texture for analysis and debugging.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Histogram render
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Histogram render
user-guide-description: ""
user-guide-title: ""
---

# Histogram render

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Anisotropic Kuwahara Grayscale icon](histogram-render.resources/histogram-render-01.png "Anisotropic Kuwahara Grayscale icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Draws the histogram for a grayscale image.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Grayscale</i> PRIMARY | The image for which the histogram should be drawn. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The histogram visualization computed out of the input image. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Histogram resolution</b> *Integer* | The width of the histogram. A higher value allows for a finer value distribution.   Available resolutions are, in pixels:  256, 512, 1024, 2048, 4096 |
| <b>Automatic scale</b> *Boolean* | When 'True', remaps the histogram to use the full height of the image.   When 'False', each column uses as many pixels in height as there are occurrences of a value in the input image. |
| <b>Scale</b> *Float* | Scales the histogram vertically, where a value of 1 is the full height of the histogram. |
| <b>Sampling</b> *Integer* | The method of filtering the histogram image, which impacts the result when the histogram resolution and render resolution mismatch:<ul data-preserve-html="true"> <li data-preserve-html="true"><b>Bilinear:</b> applies bilinear filtering to the histogram, resulting in interpolated points</li> <li data-preserve-html="true"><b>Nearest:</b> samples the nearest pixel with no filtering, resulting in flat steps</li> </ul> |
| <b>Flip Y axis</b> *Boolean* | When 'True', mirrors the histogram vertically. |

## Examples

![Histogram render: Example 1](histogram-render.resources/histogram-render-02.png "Histogram render: Example 1"){zoomable="yes"}

![Histogram render: Example 2](histogram-render.resources/histogram-render-03.png "Histogram render: Example 2"){zoomable="yes"}
