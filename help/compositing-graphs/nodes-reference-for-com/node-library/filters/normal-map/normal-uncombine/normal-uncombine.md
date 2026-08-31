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

![Normal uncombine icon](normal-uncombine.resources/normal-uncombine-01.png "Normal uncombine icon"){width="200px"}

<b>In:</b> Filters &gt; Normal map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Removes from a normal map the surface details described by a height map.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Combined normal</b> <i>Color</i> PRIMARY | The normal map from which details should be removed. |
| <b>Height</b> <i>Grayscale</i> | The height map representing the surface details which should be removed from the combined normal map. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Uncombined normal</b> <i>Color</i> | The normal map where the surface details described by the input height map were removed. |
| <b>Guessed intensity</b> <i>Float</i> | An estimate of the intensity which should be set to a [Normal](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md) node connected to the input height map, to match the intensity of the input normal map. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Normal format</b> *Integer* | The format of the input normal map. Effectively inverts the green channel.<ul data-preserve-html="true"> <li data-preserve-html="true"><b>DirectX:</b> The Y axis points up</li> <li data-preserve-html="true"><b>OpenGL:</b> The Y axis points down</li> </ul> |

## Examples

<table>
  <tr>
    <td>
      <img src="normal-uncombine.resources/normal-uncombine-02.jpg" alt="normal_uncombine_example_3_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="normal-uncombine.resources/normal-uncombine-03.jpg" alt="normal_uncombine_example_3_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Normal uncombine: Example 2](normal-uncombine.resources/normal-uncombine-04.png "Normal uncombine: Example 2"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="normal-uncombine.resources/normal-uncombine-05.jpg" alt="normal_uncombine_example_1_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="normal-uncombine.resources/normal-uncombine-06.jpg" alt="normal_uncombine_example_1_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Normal uncombine: Example 4](normal-uncombine.resources/normal-uncombine-07.png "Normal uncombine: Example 4"){zoomable="yes"}

<table>
  <tr>
    <td>
      <img src="normal-uncombine.resources/normal-uncombine-08.jpg" alt="normal_uncombine_example_2_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="normal-uncombine.resources/normal-uncombine-09.jpg" alt="normal_uncombine_example_2_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

![Normal uncombine: Example 6](normal-uncombine.resources/normal-uncombine-10.png "Normal uncombine: Example 6"){zoomable="yes"}
