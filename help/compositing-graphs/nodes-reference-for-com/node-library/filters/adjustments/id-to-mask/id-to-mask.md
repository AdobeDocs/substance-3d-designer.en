---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/id-to-mask.html"
breadcrumb-title: ""
description: Use the ID To Mask Grayscale node to convert ID map values into grayscale masks for material selection.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > ID To Mask Grayscale
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: ID To Mask Grayscale
user-guide-description: ""
user-guide-title: ""
---


# ID To Mask Grayscale

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![ID To Mask Grayscale icon](IDToMask.png "ID To Mask Grayscale icon"){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Creates a mask out of an ID map where the pixels with the selected pixel values are white.

An ID map is an image where pixels which are part of a whole (E.g., a shape) all hold the same unique identification value. In this case, the value is an integer.

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
| <b>ID</b> *Grayscale* PRIMARY | The input ID map from which a mask should be extracted. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* | The binary mask extracted from the input ID map. |

## Parameters

|  |  |
| --- | --- |
| <b>Selection mode</b> *Integer* | The method of selecting the pixel values in the ID map which should be white in the mask:<ul data-preserve-html="true"> <li data-preserve-html="true"><b>Solo:</b> Select a single pixel value</li> <li data-preserve-html="true"><b>Range:</b> Select a range of pixel values</li> </ul> |
| <b>ID Integer</b> *Integer*   *Available when 'Selection mode' is set to 'Solo'* | The pixel value in the ID map which should be white in the output mask. |
| <b>ID Range</b> *Integer2*    *Available when 'Selection mode' is set to 'Range'* | The range of pixel values in the ID map, from start to end, which should be white in the output mask. |

## Examples

<table>
  <tr>
    <td>
      <img src="id_to_mask_grayscale_example_1_before.jpg" alt="id_to_mask_grayscale_example_1_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="id_to_mask_grayscale_example_1_after.jpg" alt="id_to_mask_grayscale_example_1_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![ID to mask: Example 2](id_to_mask_example_2.gif "ID to mask: Example 2"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![ID to mask: Example 3](id_to_mask_example_3.png "ID to mask: Example 3"){zoomable="yes"}

</td>
</tr>
</table>
