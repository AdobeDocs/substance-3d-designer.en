---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-uncombine.html"
breadcrumb-title: ""
description: Use the Normal Uncombine node to separate combined normal map data into individual X, Y, and Z components.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal map > Normal uncombine
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Uncombine
user-guide-description: ""
user-guide-title: ""
---



# Normal Uncombine

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Normal uncombine icon](NormalUncombine.png "Normal uncombine icon"){width="200px"}

<b>In:</b> Filters &gt; Normal map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Removes from a normal map the surface details described by a height map.

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
| <b>Combined normal</b> *Color* PRIMARY | The normal map from which details should be removed. |
| <b>Height</b> *Grayscale* | The height map representing the surface details which should be removed from the combined normal map. |

## Output connectors

|  |  |
| --- | --- |
| <b>Uncombined normal</b> *Color* | The normal map where the surface details described by the input height map were removed. |
| <b>Guessed intensity</b> *Float* | An estimate of the intensity which should be set to a [Normal](../../../../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md) node connected to the input height map, to match the intensity of the input normal map. |

## Parameters

|  |  |
| --- | --- |
| <b>Normal format</b> *Integer* | The format of the input normal map. Effectively inverts the green channel.<ul data-preserve-html="true"> <li data-preserve-html="true"><b>DirectX:</b> The Y axis points up</li> <li data-preserve-html="true"><b>OpenGL:</b> The Y axis points down</li> </ul> |

## Examples

<table>
  <tr>
    <td>
      <img src="normal_uncombine_example_3_before.jpg" alt="normal_uncombine_example_3_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="normal_uncombine_example_3_after.jpg" alt="normal_uncombine_example_3_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Normal uncombine: Example 2](normal_uncombine_example_4.png "Normal uncombine: Example 2"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="normal_uncombine_example_1_before.jpg" alt="normal_uncombine_example_1_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="normal_uncombine_example_1_after.jpg" alt="normal_uncombine_example_1_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Normal uncombine: Example 4](normal_uncombine_example_6.png "Normal uncombine: Example 4"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="normal_uncombine_example_2_before.jpg" alt="normal_uncombine_example_2_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="normal_uncombine_example_2_after.jpg" alt="normal_uncombine_example_2_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Normal uncombine: Example 6](normal_uncombine_example_5.png "Normal uncombine: Example 6"){zoomable="yes"}
