---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/scatter-on-spline-grayscale.html"
breadcrumb-title: ""
description: Use the Scatter on Spline Grayscale node to distribute grayscale elements along spline paths for procedural patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Scatter on Spline Grayscale
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Scatter on Spline Grayscale
user-guide-description: ""
user-guide-title: ""
---

# Scatter on Spline Grayscale

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](scatter-on-spline-grayscale.resources/scatter-on-spline-grayscale-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Draws the specified pattern(s) along the input splines over the input background.

</td>
</tr>
</table>

The node offers deep customization options for controlling how patterns are scattered.

Some aspects of the scattering may be controlled using images from other nodes in the graph to further the dynamic aspect of the result.

>[!NOTE]
>
> See also [Scatter on Spline Color](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/spline-paths-tools/spline-tools/scatter-on-spline-color/scatter-on-spline-color.md).

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Background</b> <i>Grayscale</i> (Primary) | The grayscale image over which splines should be drawn. |
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines' points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |
| <b>Pattern Input &#35;</b> <i>Grayscale</i> | The pattern(s) which should be scattered along the splines. |
| <b>Scale Map</b> <i>Grayscale</i> | The map controlling the scale of the scattered patterns. The effect of this map is controlled by the 'Scale Map Input Multiplier' parameter and is combined with the other parameters in the 'Size' group. |
| <b>Height Map</b> <i>Grayscale</i> | The map controlling the height of the scattered patterns. The effect of this map is controlled by the 'Height Input Multiplier' parameter and is combined with the other 'Color' parameters in the 'Color' group. |
| <b>Mask Map</b> <i>Grayscale</i> | The map controlling the masking of the scattered patterns. The effect of this map is controlled by the 'Mask Map Threshold' parameter and is combined with the other 'Mask' parameters in the 'Color' group. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Grayscale</i> | The image representing the pattern(s) scattered along the input spline(s) over the input background. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Spline Input</b> <i>Integer</i> | The method of selecting which splines should be used for scattering patterns:<br><br>- <i>All splines</i>: Use all splines in the input list;<br>- <i>Single Spline</i>: Use only the specified spline from the input list;<br>- <i>Spline Range</i>: Use only the splines in the specified range from the input list. |
| <b>Spline Index</b> <i>Integer</i> (Available when 'Spline Input' is set to 'Single Spline') | The list index of the spline which should be used for scattering patterns. |
| <b>Spline Range</b> <i>Integer2</i> (Available when 'Spline Input' is set to 'Spline Range') | The range of list indexes including the splines which should be used for scattering patterns. |
| <b>Scatter Mode</b> <i>Integer</i> | The method of scattering the patterns along the splines, which impacts the amount of patterns on each spline:<br><br>- Shape Amount: The specified amount of evenly spaced patterns is scattered;<br>- Shape Spacing: The number of patterns is automatically adjusted to fit the specified even spacing.<br><br>In both cases, the first and last patterns fall exactly on the start and end of each spline respectively. |
| <b>Shape Amount</b> <i>Integer</i> (Available when 'Scatter Mode' is set to 'Shape Amount') | The amount of evenly spaced patterns scattered along each spline. |
| <b>Shape Distribution Along Spline</b> <i>Integer</i> (Available when 'Scatter Mode' is set to 'Shape Amount') | The method of distributing the patterns along a spline:<br><br>- <i>From Source</i>: The spacing of the patterns is influenced by the spline point's tangents, where shapes are further apart near points with long tangents;<br>- <i>Uniform</i>: The patterns are evenly spaced along the spline regardless of its tangents and trajectory. |
| <b>Shape Spacing</b> <i>Float</i> (Available when 'Scatter Mode' is set to 'Shape Spacing') | The minimum distance along a spline by which patterns should be spaced, while still landing the first and last pattern on the start and end of each spline respectively. |
| <b>Start</b> <i>Float</i> | <span id="_Hlk135680521"></span>Offsets the point from the start of a spline where the scattering starts. The value is the normalized length of each spline. |
| <b>End</b> <i>Float</i> | Offsets the point from the start of a spline where the scattering ends. The value is the normalized length of each spline. |
| <b>Shape Pivot</b> <i>Float2</i> | Offsets the pivot of the pattern X and Y in spline tangent space.<br>Considering the pivot is what is placed on the spline, this effectively offsets the patterns along or perpendicularly to the spline.<br>Note: The positions of the pivots impacts the effect of the 'Scale' and 'Rotation (Pivot)' parameters. |
| <b>Pattern</b> |  |
| <b>Pattern</b> <i>Integer</i> | The pattern which should be scattered along the splines:<br><br>- <i>Pattern Input</i>: Use the patterns supplied to the 'Pattern Input #' inputs;<br>- Square;<br>- Disc;<br>- Paraboloid;<br>- Bell;<br>- Gaussian;<br>- Thorn;<br>- Pyramid;<br>- Brick;<br>- Gradation;<br>- Waves;<br>- Half Bell;<br>- Ridged Bell;<br>- Crescent;<br>- Capsule;<br>- Cone;<br>- Gradation w. offset;<br>- Hemisphere. |
| <b>Pattern Input Number</b> <i>Integer</i> (Available when 'Pattern' is set to 'Pattern Input') | Selects the index of the input pattern which should be scattered. |
| <b>Pattern Input Distribution</b> <i>Integer</i> (Available when 'Pattern' is set to 'Pattern Input') | The method used to select which of the input patterns should be scattered on a given spline:<br><br>- <i>Random</i>: a pattern is randomly selected;<br>- <i>Along Spline</i>: The pattern index increases gradually along the spline;<br>- <i>Pattern Index</i>: Loops over the index of input patterns along each spline;<br>- <i>Spline Index</i>: Loops over the index of input patterns from one spline to the next in the list of input splines. |
| <b>Distribution Jittering</b> <i>Float</i> (Available when 'Pattern Input Distribution' is set to 'Along Spline') | Randomly increases or decreases the selected index of patterns on the spline. |
| <b>Override First Pattern</b> <i>Boolean</i> | Manually select the index of the pattern that should be placed at the start of each spline. |
| <b>First Pattern Input Index</b> <i>Integer</i> (Available when 'Override First Pattern' is set to 'True') | The index of the pattern that should be placed at the start of each spline. |
| <b>Override Last Pattern</b> <i>Boolean</i> | Manually select the index of the pattern that should be placed at the end of each spline. |
| <b>Last Pattern Input Index</b> <i>Integer</i> (Available when 'Override Last Pattern' is set to 'True') | The index of the pattern that should be placed at the end of each spline. |
| <b>Duplicates</b> |  |
| <b>Distribution Mode</b> <i>Integer</i> | The method used to place the duplicate patterns:<br><br>- <i>Linear</i>: duplicates are evenly spaced along the spline's normal from the pattern's original location;<br>- <i>Circular</i>: duplicated are arranged along a virtual circle centered on the spline at the pattern's original location. |
| <b>Duplicates Amount</b> <i>Integer</i> | The number of duplicated patterns. |
| <b>Offset</b> <i>Float2</i> (Available when 'Distribution Mode' is set to 'Linear') | Applies an offset to the duplicates' positions along the spline's tangent (parallel) and normal (perpendicular).<br>Duplicates on opposite sides of the spline are moved in opposite directions. |
| <b>Offset Center</b> <i>Float2</i> (Available when 'Distribution Mode' is set to 'Linear') | Applies an offset to the duplicates along the spline on X (parallel) and Y (perpendicular). |
| <b>Spread Angle</b> <i>Float</i> (Available when 'Distribution Mode' is set to 'Circular') | The arc of the virtual circle along which duplicates are distributed, as the angle of that arc where 1 is the full circle. |
| <b>Offset Distance</b> <i>Float</i> (Available when 'Distribution Mode' is set to 'Circular') | The radius of the virtual circle along which duplicates are distributed. |
| <b>Rotation</b> <i>Float</i> | Rotates the virtual circle along which duplicates are distributed. |
| <b>Offset Start/End Attenuation</b> <i>Float2</i> | Factors in the distance from the midpoint of the spline to its Start and End, when applying offsets to duplicates.<br>This means offsets are decreased for duplicates closer to a spline's extremities. |
| <b>Offset Attenuation by Thickness</b> <i>Float</i> | Factors in the spline's thickness when applying offsets to duplicates.<br>This means offsets are decreased for duplicates on a portion of a spline with a lower thickness. |
| <b>Size</b> |  |
| <b>Size Mode</b> <i>Integer</i> | The method of setting the size of the scattered patterns:<br><br>- <i>Normal</i>: Size is controlled uniformly using a global 'Scale' parameter;<br>- <i>Use Thickness from Spline</i>: Size is driven by the spline's thickness. |
| <b>Thickness Affects</b> <i>Integer</i> (Available when 'Size Mode' is set to 'Use Thickness from Spline') | Specifies which axis of a pattern's scale should be driven by the spline's thickness:<br><br>- X &amp; Y: Thickness is multiplied against the size in both the X and Y axes;<br>- <span id="_Hlk135741125"></span>X: Thickness is multiplied against the size on the X axis only;<br>- Y: Thickness is multiplied against the size on the Y axis only.<br><br>When not multiplied, the pattern's original scale is the full span of the image.<br>This means in the 'X' mode, the size in the Y axis is the full span of the image and needs to be tweaked using the Size parameter. The same applied for size in the X axis when using the 'Y' mode. |
| <b>Size</b> <i>Float2</i> | The original size of patterns in X and Y before other adjustments are made by other parameters. |
| <b>Size Random</b> <i>Float2</i> | Applies a random multiplier up to the specified value for reducing the size of the patterns in X and Y. |
| <b>Thickness Scale</b> <i>Float</i> (Available when 'Size Mode' is set to 'Use Thickness from Spline') | An additional multiplier for the scale of the patterns when driven by the spline's thickness. |
| <b>Scale</b> <i>Float</i> (Available when 'Size Mode' is set to 'Normal') | A global control for the size of all patterns, where 1 is the full span of the image.<br>Scaling is applied relatively to a pattern's pivot. The pivot position can be offset using the 'Shape Pivot' parameter. |
| <b>Scale Random</b> <i>Float</i> | Applies a random multiplier up to the specified value for decreasing the size of the patterns. |
| <b>Scale Map Input Multiplier</b> <i>Float</i> | Controls the intensity of the Scale Map input. This map acts as a multiplier for the current size of the patterns.<br>The effect of this map is combined with the other parameters in the 'Size' group. |
| <b>Scale Input Sampling Mode</b> <i>Texture Space</i> | The method of mapping the values in the Scale Map to the splines:<br><br>- <i>Texture space</i>: The values are applied to the splines where they would be if placed in a texture using the texture's UV coordinates. This effectively applies the value to the splines 'in place';<br>- <i>Horizontal along spline</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), where each row is applied to a different spline from top to bottom;<br>- <i>Hor. along spline (rand. offset X)</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), with a random horizontal offset in the Scale map for each spline (I.e., each row in Spline Coords);<br>- <i>Hor. along spline (rand. offset Y)</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), with a random vertical offset in the Scale map for each spline (I.e., each row in Spline Coords). |
| <b>Start/End Attenuation</b> <i>Float2</i> | Factors in the distance from the midpoint of the spline to its Start and End when scaling the patterns.<br>This means size is decreased for patterns closer to a spline's extremities. |
| <b>Position</b> |  |
| <b>Local Offset</b> <i>Float2</i> | Applies an offset to the patterns' positions along the spline's tangent (parallel) and normal (perpendicular). |
| <b>Local Offset Random</b> <i>Float2</i> | Applies an additional random offset to the patterns' positions along the spline's tangent (parallel) and normal (perpendicular). |
| <b>Local Offset Random Center</b> <i>Float2</i> | Offsets the center of the random offset applied by the Local Offset Random parameter along the spline's tangent (parallel) and normal (perpendicular). |
| <b>Local Offset Start/End Attenuation</b> <i>Float2</i> | Factors in the distance from the midpoint of the spline to its Start and End when applying position offsets to the patterns.<br>This means offsets are decreased for patterns closer to a spline's extremities. |
| <b>Local Offset Attenuation by Thickness</b> <i>Float</i> | Factors in the spline's thickness when applying offsets to patterns.<br>This means offsets are decreased for duplicates on a portion of a spline with a lower thickness. |
| <b>Offset on Spline</b> <i>Float</i> | Applies a position offset to the patterns along the splines. |
| <b>Random Offset on Spline</b> <i>Float</i> | Applies an additional position offset to the patterns along the splines. |
| <b>Rotation</b> |  |
| <b>Align with Tangent</b> <i>Boolean</i> | Rotates the patterns to match the direction of the spline at their location. |
| <b>Rotation (Pivot)</b> <i>Float</i> | Rotates the patterns around their pivots.<br>The pivot position can be offset using the 'Shape Pivot' parameter. |
| <b>Rotation Random (Pivot)</b> <i>Float</i> | Applies an additional random rotation to the patterns around their pivots.<br>The pivot position can be offset using the 'Shape Pivot' parameter. |
| <b>Rotation Random Center (Pivot)</b> <i>Float</i> | Rotates around the pattern's pivots the center of the random rotations applied by the Rotation Random parameter. |
| <b>Rotation (Center)</b> <i>Float</i> | Rotates the patterns around their center. |
| <b>Rotation Random (Center)</b> <i>Float</i> | Applies an additional random rotation to the patterns around their center. |
| <b>Rotation Random Center (Center)</b> <i>Float</i> | Rotates around the pattern's center the center of the random rotations applied by the Rotation Random parameter. |
| <b>Color</b> |  |
| <b>Blend Mode</b> <i>Integer</i> | The method of blending together the colors of patterns with both the background and other overlapping patterns:<br><br>- <i>Max</i>: Use the brightest color;<br>- <i>Add</i>: Add the colors together. |
| <b>Shape Base Color</b> <i>Float</i> | The base color of the patterns. |
| <b>Shape Base Color Multiplier</b> <i>Float</i> | The intensity of the patterns' Shape Base Color.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Spline Thickness Multiplier</b> <i>Float</i> | The intensity by which the color of each pattern is multiplied against the thickness of the spline at its location.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Shape Index Multiplier</b> <i>Float</i> | The intensity by which the color of each pattern is multiplied against its normalized index.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Hemisphere Height Mode</b> <i>Integer</i> (Available when 'Pattern' is set to 'Hemisphere') | The effect of the spline's height on a Hemisphere pattern scattered onto it:<br><br>- <i>Offset</i>: the spline height is added to the height of the Hemisphere;<br>- <i>Scale</i>: the spline height is multiplied against the height of the Hemisphere. |
| <b>Spline Height Multiplier</b> <i>Float</i> | The intensity by which the color of each pattern is multiplied against the height of the spline at its location.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Shape Scale Multiplier</b> <i>Float</i> | The intensity by which the color of each pattern is multiplied against its scale.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Random Luminance</b> <i>Float</i> | Applies a random multiplier up to the specified value for decreasing the luminance of the patterns.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Height Input Multiplier</b> <i>Float</i> | Controls the intensity of the Height Map input. This map acts as a multiplier for the current luminance of the patterns.<br>The effect of this map is combined with the other parameters in the 'Color' group.<br>Note: The output color is the weighted result of all color multipliers. |
| <b>Height Map Input Sampling Mode</b> <i>Integer</i> | The method of mapping the values in the Height Map to the splines:<br><br>- <i>Texture space</i>: The values are applied to the splines where they would be if placed in a texture using the texture's UV coordinates. This effectively applies the value to the splines 'in place';<br>- <i>Horizontal along spline</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), where each row is applied to a different spline from top to bottom;<br>- <i>Hor. along spline (rand. offset X)</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), with a random horizontal offset in the Scale map for each spline (I.e., each row in Spline Coords);<br>- <i>Hor. along spline (rand. offset Y)</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), with a random vertical offset in the Scale map for each spline (I.e., each row in Spline Coords). |
| <b>Mask Random</b> <i>Float</i> | Adjusts the range of the random masking of patterns, where 0 means no patterns are masked and 1 means all patterns are. |
| <b>Mask Map Threshold</b> <i>Float</i> | Values in the Mask Map below this threshold value are processed as black, while values above the threshold are processed as white.<br>This means all patterns in areas of the Mask Map below this value will be masked. |
| <b>Mask Map Input Sampling Mode</b> <i>Integer</i> | The method of mapping the values in the Mask Map to the splines:<br><br>- <i>Texture space</i>: The values are applied to the splines where they would be if placed in a texture using the texture's UV coordinates. This effectively applies the value to the splines 'in place';<br>- <i>Horizontal along spline</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), where each row is applied to a different spline from top to bottom;<br>- <i>Hor. along spline (rand. offset X)</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), with a random horizontal offset in the Scale map for each spline (I.e., each row in Spline Coords);<br>- <i>Hor. along spline (rand. offset Y)</i>: The values are applied to the encoded splines' coordinates directly (see Spline Coords input), with a random vertical offset in the Scale map for each spline (I.e., each row in Spline Coords). |
| <b>Invert Mask Map</b> <i>Boolean</i> | Inverts the values of the Mask Map using a 'One minus' operation (1 - x). |
| <b>Mask Invert</b> <i>Boolean</i> | Inverts the masking of the patterns. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points' positions to retain the spline shape in non-square resolutions. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="scatter-on-spline-grayscale.resources/ScatterOnSplineGrayscale-Variant1-Before.jpg" alt="ScatterOnSplineGrayscale-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="scatter-on-spline-grayscale.resources/ScatterOnSplineGrayscale-Variant1-After.jpg" alt="ScatterOnSplineGrayscale-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="scatter-on-spline-grayscale.resources/ScatterOnSplineGrayscale-Variant2-Before.jpg" alt="ScatterOnSplineGrayscale-Variant2-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="scatter-on-spline-grayscale.resources/ScatterOnSplineGrayscale-Variant2-After.jpg" alt="ScatterOnSplineGrayscale-Variant2-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node example 2](scatter-on-spline-grayscale.resources/ScatterOnSplineGrayscale-Demo.gif "Node example 2")

</td>
<td style="border: 0;" valign="top">

![Node demo 2](scatter-on-spline-grayscale.resources/ScatterOnSplineGrayscale-Demo2.gif "Node demo 2")

</td>
</tr>
</table>
