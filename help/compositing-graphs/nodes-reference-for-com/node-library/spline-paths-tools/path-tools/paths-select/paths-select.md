---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/path-tools/paths-select.html"
breadcrumb-title: ""
description: Use the Paths Select node to select and filter specific paths from a path list based on criteria.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Paths Select
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Paths Select
user-guide-description: ""
user-guide-title: ""
---

# Paths Select

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](paths-select.resources/paths-select-01.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Path Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Isolate one path among multiples contained in Paths.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Label</b> <i>Type</i> | A list of encoded segments paths. Connect this input to the result of a [Mask to Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/mask-to-paths/mask-to-paths.md) or to another Path-processing node. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Paths</b> <i>Color</i> | The Paths input with only one path. You can either use [Preview Paths](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/preview-paths/preview-paths.md) to get an idea of what the result represents, use another Paths-processing node, or input it to a [Paths to Spline](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/path-tools/paths-to-spline/paths-to-spline.md) to further process it as Splines. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Selection Mode</b> <i>Integer</i> | The method used to select the Paths:<br>*- By ID:* Selects the path from the list whose index matches the one specified in <b>Path ID</b>;<br>*- By Length:* Selects the paths whose length is above or below the threshold specified in <b>Target Length</b>. |
| <b>Path ID</b> <i>Integer</i> (Available when <b>Selection Mode</b> is set to *By ID*) | The index of the selected path.<br>A value greater than the number of paths in <b>Paths *results in*</b> a blank output. |
| <b>Length Greater or Lower?</b> <i>Boolean</i> (Available when <b>Selection Mode</b> is set to *By Length*) | Controls whether the selection should include or greater or lower length than the <b>Target Length</b>. |
| <b>Target Length</b> <i>Float</i> (Available when <b>Selection Mode</b> is set to *By Length*) | The length threshold used to select splines. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="paths-select.resources/paths-select-02.jpg" alt="PathsToSpline-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="paths-select.resources/paths-select-03.jpg" alt="PathsSelect-Variant1">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="paths-select.resources/paths-select-02.jpg" alt="PathsToSpline-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="paths-select.resources/paths-select-04.jpg" alt="PathsSelect-Variant2">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>
