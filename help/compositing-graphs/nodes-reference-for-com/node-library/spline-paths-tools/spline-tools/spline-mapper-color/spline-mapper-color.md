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

![Node icon](spline-mapper-color-icon.png "Node icon")

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

## Input connectors

<b>Spline Coords</b> *Color*The coordinates of the input splines’ points encoded in the RGBA channels of a color image:  
<b>    R</b> - X position  
<b>    G</b> - Y position  
<b>    B</b> - Height  
    <b>A</b> - Packed data:  
        * Sign: Spline is closed (negative) or open (positive);  
        * Absolute value: Thickness + 1.

<b>Spline Data</b> *Color*Additional data of the input splines encoded in the RGBA channels of a color image.  
<b>    R</b> - Tangents X  
<b>    G</b> - Tangents Y  
<b>    B</b> - Unused  
<b>    A</b> - Unused

<b>Spline Amount</b> *Integer*The number of input splines.

<b>Color Map</b> *Color*The input color image that should be mapped along the input splines.

<b>Height Map</b> *Grayscale*The input grayscale height map that should be mapped along the input splines.

<b>Twist Curve</b> *Grayscale*The image describing a curve using the values of its first row of pixels.  
When the <b>Shape</b> parameter is set to *Half-Cylinder* or *Cylinder*, this input is used to control the twisting of the UVs around the shape. Its impact is controlled using the <b>Twist UVs Curve Multiplier</b> parameter.  
The curve provides a profile for the amount of rotation along the spline, where the first pixel in the row is the rotation at the start of the spline, and the last is the rotation at the end. The grayscale value represents a number of turns.  
You may use a [Curve](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/curve/curve.md) node to author the curve.

## Output connectors

<b>Color</b> *Color*The result of mapping the input Color image across the input splines, as a color image.

<b>Height</b> *Grayscale*The result of mapping the input Height image across the input splines, as a grayscale image.

<b>UV</b> *Color*The UVs (I.e., coordinates) of the mapping across the input splines, encoded in a color image.

<b>ID</b> *Grayscale*A mask of the images mapped along the input splines, where the white values are incremented by 1 from one spline to the next so that each shape can be selected independently.

## Parameters

<b>Segments Amount</b> *Integer*Splines are simplified into segments before image coordinates traverse them.  
A higher amount of segments results in a smoother mapping along curves.

<b>Auto Scale UVs</b> *Boolean*Adjusts the scale of the coordinates automatically to retain a square image when mapping it along the splines.<b></b>

<b>UV Scale</b> *Float2*Adjusts the scale of the mapped coordinates in X (horizontally) and Y (vertically).  
Higher values result in a more densely tiled image.<b></b>

<b>Mode</b> *Integer*The method of selecting the splines along which the image should be mapped:  
*- Draw Spline List*: All the splines in the input list are used;  
*- Draw Single Spline*: Only the spline with the specified index is used;  
*- Draw Spline Range*: Only the splines which index is included in the specified range are used.

<b>Draw Spline Index</b> *Integer* (Available when ‘Mode’ is set to ‘Draw Single Spline’)The index of the spline along which the image should be mapped.

<b>Draw Spline Range</b> *Integer2* (Available when ‘Mode’ is set to ‘Draw Spline Range’)The range of indexes for the splines along which the image should be mapped.

<b>Start</b> *Float*Offsets the start of the portion of the spline which should be mapped.  
The value represents the normalized length of the spline.

<b>End</b> *Float*Offsets the end of the portion of the spline which should be mapped.  
The value represents the normalized length of the spline.

<b>Thickness Mode</b> *Integer*The method of setting the thickness of the mapped image:  
*- Manual*: Set the thickness explicitly with an arbitrary value;  
*- From Spline*: Use the thickness of the spline.

<b>Thickness</b> *Float* (Available when ‘Thickness Mode’ is set to ‘Manual’)The arbitrary value for the thickness of the mapped image along the splines.<b></b>

<b>Thickness Multiplier</b> *Float* (Available when ‘Thickness Mode’ is set to ‘From Spline’)A global multiplier for the thickness of the mapped image along the splines, when that thickness it driven by that of the splines.

<b>Shape</b> *Integer*The primitive shape used to map image coordinates along the splines:  
*- Plane*: Coordinates are mapped to a flat plane;  
*- Half Cylinder*: Coordinates are mapped to a half-cylinder which base circle’s axis follows the direction of the spline;  
*- Cylinder*: Coordinates are mapped to a cylinder which base circle’s axis follows the direction of the spline.<b></b>

<b>Cylinder Height Multiplier</b> *Float* (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’)A multiplier for the intensity of the cylinder’s height contribution in the Height output.  
Height adjustments are cumulative.

<b>Cylinder Height Offset</b> *Float* (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’)   
Offsets the center of the Cylinder or Half-Cylinder shape profile from the spline's surface to one diameter beneath the surface.

<b>Twist UVs Intensity</b> *Float* (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’)The twisting of the image coordinates around the cylinder, in number of turns.  
Twisting involves rotating the cylinder at the end of the spline only. The rotation is then interpolated along the spline.

<b>Twist UVs Curve Multiplier</b> *Float* (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’)A multiplier for the intensity of the Twist Curve input’s contribution to the twisting of the cylinder.  
The curve provides a profile for the amount of rotation along the spline, where the first pixel in the row is the rotation at the start of the spline, and the last is the rotation at the end. The grayscale value represents a number of turns.

<b>Twist UVs Curve Offset</b> *Float* (Available when ‘Shape’ is set to ‘Half Cylinder’ or ‘Cylinder’)Applies a global offset to the rotation values supplied by the Twist Curve, in number of turns.

<b>Spline Height Multiplier</b> *Float*Adjusts the intensity of the Spline Height input’s contribution to the Height output.  
Height adjustments are cumulative.<b></b>

<b>Input Height Multiplier</b> *Float*Adjusts the intensity of the Height Map input’s contribution to the Height output.  
Height adjustments are cumulative.<b></b>

<b>Background Color</b> *Float4*The color of the background in the Color output.

<b>Non-Square Correction</b>*Boolean*Adjust the points’ positions and thickness to retain the spline shape in non-square resolutions.  
This also impacts uniform distribution.

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="SplineMapperColor-Variant1-Before.jpg" alt="SplineMapperColor-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="SplineMapperColor-Variant1-After.jpg" alt="SplineMapperColor-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](SplineMapperColor-Demo.gif "Node example 2")

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 3](SplineMapperColor-Variant1-After1.jpg "Node example 3")

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>
