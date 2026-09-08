---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-mapper-color.html"
breadcrumb-title: ""
description: Use the Spline Mapper Color node to map color textures along spline paths with customizable parameters.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Point List
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Mapper Color
user-guide-description: ""
user-guide-title: ""
---

# Spline Mapper Color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](../../../../../../assets/spline-mapper-color-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Maps an input color image on a primitive shape stretched along the input splines.

The primitive shape can be a plane, a half-cylinder or cylinder. The cylinders can be twisted along the spline to deform the mapped image accordingly.

</td>
</tr>
</table>

The node outputs the mapped image as a color image, as well as other information such as height, UVs (I.e., image coordinates) and an ID mask for selecting each mapped spline independently.

>[!IMPORTANT]
>
> The result may include undesired artifacts outside of the spline's envelope when using very low thickness values. This is a known issue.

>[!NOTE]
>
> See also [Spline Mapper Grayscale](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/spline-mapper-grayscale/spline-mapper-grayscale.md).

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines’ points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>&nbsp;&nbsp;- Sign: Spline is closed (negative) or open (positive);<br>&nbsp;&nbsp;- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |
| <b>Color Map</b> <i>Color</i> | The input color image that should be mapped along the input splines. |
| <b>Height Map</b> <i>Grayscale</i> | The input grayscale height map that should be mapped along the input splines. |
| <b>Twist Curve</b> <i>Grayscale</i> | The image describing a curve using the values of its first row of pixels.<br>When the <b>Shape</b> parameter is set to <i>Half-Cylinder</i> or <i>Cylinder</i>, this input is used to control the twisting of the UVs around the shape. Its impact is controlled using the <b>Twist UVs Curve Multiplier</b> parameter.<br>The curve provides a profile for the amount of rotation along the spline, where the first pixel in the row is the rotation at the start of the spline, and the last is the rotation at the end. The grayscale value represents a number of turns.<br>You may use a [Curve](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/curve/curve.md) node to author the curve. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Color</b> <i>Color</i> | The result of mapping the input Color image across the input splines, as a color image. |
| <b>Height</b> <i>Grayscale</i> | The result of mapping the input Height image across the input splines, as a grayscale image. |
| <b>UV</b> <i>Color</i> | The UVs (I.e., coordinates) of the mapping across the input splines, encoded in a color image. |
| <b>ID</b> <i>Grayscale</i> | A mask of the images mapped along the input splines, where the white values are incremented by 1 from one spline to the next so that each shape can be selected independently. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Segments Amount</b> <i>Integer</i> | Splines are simplified into segments before image coordinates traverse them.<br>A higher amount of segments results in a smoother mapping along curves. |
| <b>Auto Scale UVs</b> <i>Boolean</i> | Adjusts the scale of the coordinates automatically to retain a square image when mapping it along the splines. |
| <b>UV Scale</b> <i>Float2</i> | Adjusts the scale of the mapped coordinates in X (horizontally) and Y (vertically).<br>Higher values result in a more densely tiled image. |
| <b>Mode</b> <i>Integer</i> | The method of selecting the splines along which the image should be mapped:<br>- <i>Draw Spline List</i>: All the splines in the input list are used;<br>- <i>Draw Single Spline</i>: Only the spline with the specified index is used;<br>- <i>Draw Spline Range</i>: Only the splines which index is included in the specified range are used. |
| <b>Draw Spline Index</b> <i>Integer</i> | (Available when ‘Mode’ is set to ‘Draw Single Spline’) The index of the spline along which the image should be mapped. |
| <b>Draw Spline Range</b> <i>Integer2</i> | (Available when ‘Mode’ is set to ‘Draw Spline Range’) The range of indexes for the splines along which the image should be mapped. |
| <b>Start</b> <i>Float</i> | Offsets the start of the portion of the spline which should be mapped.<br>The value represents the normalized length of the spline. |
| <b>End</b> <i>Float</i> | Offsets the end of the portion of the spline which should be mapped.<br>The value represents the normalized length of the spline. |
| <b>Thickness Mode</b> <i>Integer</i> | The method of setting the thickness of the mapped image:<br>- <i>Manual</i>: Set the thickness explicitly with an arbitrary value;<br>- <i>From Spline</i>: Use the thickness of the spline. |
| <b>Thickness</b> <i>Float</i> | (Available when ‘Thickness Mode’ is set to ‘Manual’) The arbitrary value for the thickness of the mapped image along the splines. |
| <b>Thickness Multiplier</b> <i>Float</i> | (Available when ‘Thickness Mode’ is set to ‘From Spline’) A global multiplier for the thickness of the mapped image along the splines, when that thickness it driven by that of the splines. |
| <b>Shape</b> <i>Integer</i> | The primitive shape used to map image coordinates along the splines:<br>- <i>Plane</i>: Coordinates are mapped to a flat plane;<br>- <i>Half Cylinder</i>: Coordinates are mapped to a half-cylinder which base circle’s axis follows the direction of the spline;<br>- <i>Cylinder</i>: Coordinates are mapped to a cylinder which base circle’s axis follows the direction of the spline. |
| <b>Cylinder Height Multiplier</b> <i>Float</i> | (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’) A multiplier for the intensity of the cylinder’s height contribution in the Height output.<br>Height adjustments are cumulative. |
| <b>Cylinder Height Offset</b> <i>Float</i> | (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’) Offsets the center of the Cylinder or Half-Cylinder shape profile from the spline's surface to one diameter beneath the surface. |
| <b>Twist UVs Intensity</b> <i>Float</i> | (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’) The twisting of the image coordinates around the cylinder, in number of turns.<br>Twisting involves rotating the cylinder at the end of the spline only. The rotation is then interpolated along the spline. |
| <b>Twist UVs Curve Multiplier</b> <i>Float</i> | (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’) A multiplier for the intensity of the Twist Curve input’s contribution to the twisting of the cylinder.<br>The curve provides a profile for the amount of rotation along the spline, where the first pixel in the row is the rotation at the start of the spline, and the last is the rotation at the end. The grayscale value represents a number of turns. |
| <b>Twist UVs Curve Offset</b> <i>Float</i> | (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’) Applies a global offset to the rotation values supplied by the Twist Curve, in number of turns. |
| <b>Spline Height Multiplier</b> <i>Float</i> | Adjusts the intensity of the Spline Height input’s contribution to the Height output.<br>Height adjustments are cumulative. |
| <b>Input Height Multiplier</b> <i>Float</i> | Adjusts the intensity of the Height Map input’s contribution to the Height output.<br>Height adjustments are cumulative. |
| <b>Background Color</b> <i>Float4</i> | The color of the background in the Color output. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.<br>This also impacts uniform distribution. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="../../../../../../assets/SplineMapperColor-Variant1-Before.jpg" alt="SplineMapperColor-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="../../../../../../assets/SplineMapperColor-Variant1-After.jpg" alt="SplineMapperColor-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](../../../../../../assets/SplineMapperColor-Demo.gif "Node example 2")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 3](../../../../../../assets/SplineMapperColor-Variant1-After1.jpg "Node example 3")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
