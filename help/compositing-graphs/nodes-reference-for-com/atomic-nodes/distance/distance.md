---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/distance.html"
breadcrumb-title: ""
description: Use the Distance node to calculate distance maps from shapes for creating masks and procedural effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Distance
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Distance
user-guide-description: ""
user-guide-title: ""
---



# Distance

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Distance](comp_distance.png "Atomic node: Distance"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Finds the position of the nearest white pixel in a mask and outputs a gradient from that position, or the color at that position in a source image.

This node creates an outward linear fade (gradient) from any pixels in the input max over 0.5 grayscale value.

</td>
</tr>
</table>

The expanding outward fade will terminate as soon as it meets another cell: they will never overlap. Internally this is actually calculating and displaying the distance to the nearest pixel &gt; 0.5, with the distance node set as a clamp/maximum.

An optional source map allows for combining the cells with the texture from a secondary input map.

The distance node is not an easy node to master, but it's main use cases are expanding existing masks in a reliable way (as compared to blurring and adjusting contrast), generating Voronoi-type noise cells, and beveling existing shapes with a sharp, linear profile (that can be remapped later.

See the below [examples](#examples) for more info.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">



</td>
<td width="100.00%" style="border: 0;" valign="top">



</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Output connectors

</td>
<td style="border: 0;" valign="top">

### Examples

</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Toggles between a grayscale and a color output image. Also changes the 'Source input' input type. |
| <b>Maximum distance</b> *Float* | Adjusts the maximum distance for detecting the closest border in the mask, in pixels. |
| <b>Combine source/distance</b> *Boolean* | Determine how the optional 'Source input'is combined with the final cells.<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Combine:</i> Combines the 'Source input' value with the fading linear mask. If the 'Source input' input is connected, its value is combined with computed distance.</li> <li data-preserve-html="true"><i>Only Source:</i> Results in solid color only from the 'Source input'.</li> </ul> |
| <b>Distance mode</b> *Integer* | Selects the method computing the distance to the closest border in the extracted mask:<ul data-preserve-html="true"> <li data-preserve-html="true"><i>Euclidean:</i> Sum of squared X/Y differences.</li> <li data-preserve-html="true"><i>Manhattan:</i> Sum of absolute values of X/Y differences.</li> <li data-preserve-html="true"><i>Chebyshev:</i> Maximum of absolute values of X/Y differences.</li> </ul>  <div><img alt="Distance mode examples" class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_table_copy_copy_copy_row-yj03rtt-column-0i13nfd_image" src="distance-comparison.jpg" title="Distance mode examples"/></div> |

## Input connectors

|  |  |
| --- | --- |
| <b>Mask input</b> *Grayscale* PRIMARY | A grayscale mask, the borders of which a distance value should be computed.   A binary mask is extracted from the image, using a threshold value of 0.5, where all values above this threshold are white and all values below are black. |
| <b>Source input</b> *Color/Grayscale* | Optional grayscale image from which the pixel value at the closest border of the 'Mask input' should be copied. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Color/Grayscale* |  |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](distance-ex01.gif){width="250px"}

</td>
<td style="border: 0;" valign="top">

![](distance-ex02.gif){width="250px"}

</td>
<td style="border: 0;" valign="top">

![](distance-ex03.gif){width="250px"}

</td>
</tr>
</table>
