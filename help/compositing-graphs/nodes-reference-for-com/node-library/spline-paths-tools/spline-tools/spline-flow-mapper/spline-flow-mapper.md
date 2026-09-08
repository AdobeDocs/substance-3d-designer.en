---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/spline-paths-tools/spline-tools/spline-flow-mapper.html"
breadcrumb-title: ""
description: Use the Spline Flow Mapper node to create flowing texture patterns along spline paths for organic effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Spline Flow Mapper
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Spline Flow Mapper
user-guide-description: ""
user-guide-title: ""
---

# Spline Flow Mapper

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](../../../../../../assets/spline-flow-mapper-icon.png "Node icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Draws a flow map where flow vector data is drawn along the input splines.

This lets you use splines to control the direction, trajectory, intensity and thickness of flow, as well as the gradient ramp used to fade the drawn data into the neutral background.

</td>
</tr>
</table>

>[!IMPORTANT]
>
> The result may include undesired artifacts outside of the spline's envelope when using very low thickness values. This is a known issue.

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Spline Coords</b> <i>Color</i> | The coordinates of the input splines' points encoded in the RGBA channels of a color image:<br><b>R</b> - X position<br><b>G</b> - Y position<br><b>B</b> - Height<br><b>A</b> - Packed data:<br>- Sign: Spline is closed (negative) or open (positive);<br>- Absolute value: Thickness + 1. |
| <b>Spline Data</b> <i>Color</i> | Additional data of the input splines encoded in the RGBA channels of a color image.<br><b>R</b> - Tangents X<br><b>G</b> - Tangents Y<br><b>B</b> - Unused<br><b>A</b> - Unused |
| <b>Spline Amount</b> <i>Integer</i> | The number of input splines. |
| <b>Attenuation Profile Curve</b> <i>Grayscale</i> | <span id="_Hlk135812146"></span>The image describing a curve using the values of its first row of pixels. When the Attenuation Profile parameter is set to Input Profile Curve, this input is used to control the gradient ramp for the attenuation of the flow vector data drawn along the spline.<br>You may use a [Curve](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/curve/curve.md) node to author the curve. |

<a name="outputs"></a>

## Outputs

|  |  |
|:---|:---|
| <b>Output</b> <i>Color</i> | The output flow map encoded in a color image. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Segments Amount</b> <i>Integer</i> | Splines are simplified into segments before vector flow data traverses them. A higher amount of segments results in a smoother flow mapping along curves. |
| <b>Mode</b> <i>Integer</i> | The method of selecting the splines along which vector flow data should be drawn:<br><br>- <i>Draw Spline List</i>: All the splines in the input list are used;<br>- <i>Draw Single Spline</i>: Only the spline with the specified index is used;<br>- <i>Draw Spline Range</i>: Only the splines which index is included in the specified range are used. |
| <b>Draw Spline Index</b> <i>Integer</i> (Available when 'Mode' is set to 'Draw Single Spline') | The index of the spline along which vector flow data should be drawn. |
| <b>Draw Spline Range</b> <i>Integer2</i> (Available when 'Mode' is set to 'Draw Spline Range') | The range of indexes for the splines along which vector flow data should be drawn. |
| <b>Thickness Mode</b> <i>Integer</i> | The method of setting the thickness of the drawn vector flow data<br><br>- <i>Manual</i>: Set the thickness explicitly with an arbitrary value;<br>- <i>From Spline</i>: Use the thickness of the spline. |
| <b>Thickness</b> <i>Float</i> (Available when 'Thickness Mode' is set to 'Manual') | The arbitrary value for the thickness of the vector flow data drawn along the splines. |
| <b>Thickness Multiplier</b> <i>Float</i> (Available when 'Thickness Mode' is set to 'From Spline') | A global multiplier for the thickness of the vector flow data drawn along the splines, when that thickness it driven by that of the splines. |
| <b>Direction</b> <i>Integer</i> | The direction of the vector flow in relation to the spline.<br><br>- <i>Tangent</i>: Use the spline's tangent vector;<br>- <i>Normal</i>: Use the spline's normal vector;<br>- <i>Normal Mirrored</i>: Use the mirrored version of the spline's normal vector. |
| <b>Flip Direction</b> <i>Boolean</i> | Inverts the direction of the splines, which also impacts the direction of the flow vector. |
| <b>Attenuation Profile</b> <i>Integer</i> | The gradient ramp used to draw the attenuation of the flow vector data drawn along the spline:<br><br>- <i>Linear</i>: Use a linear gradient ramp;<br>- <i>Gaussian</i>: Use a gaussian gradient ramp<br>- <i>Input Profile Curve</i>: Use the curve provided to the Attenuation Profile Curve input as a gradient ramp. |
| <b>Start Attenuation</b> <i>Boolean</i> | <span id="_Hlk135769398"></span>Adds a half-circle at the start of the spline. The half-circle uses the same attenuation as the spline. |
| <b>End Attenuation</b> <i>Boolean</i> | Adds a half-circle at the end of the spline. The half-circle uses the same attenuation as the spline. |
| <b>Spline Height Attenuation</b> <i>Float</i> | The intensity of the flow vector data drawn along the spline is multiplied against the spline's height, where the drawn data fades to the background's neutral (0.5, 0.5, 0) color as the height gets closer to 0. |
| <b>Non-Square Correction</b> <i>Boolean</i> | Adjust the points' positions and thickness to retain the spline shape in non-square resolutions. This also impacts uniform distribution. |

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

<table>
  <tr>
    <td>
      <img src="../../../../../../assets/SplineFlowMapper-Variant1-Before.jpg" alt="SplineFlowMapper-Variant1-Before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="../../../../../../assets/SplineFlowMapper-Variant1-After.jpg" alt="SplineFlowMapper-Variant1-After">
      <br><i>After</i>
    </td>
  </tr>
</table>

</td>
<td style="border: 0;" valign="top">

![Node example 2](../../../../../../assets/SplineFlowMapper-Demo.gif "Node example 2")

</td>
</tr>
</table>
