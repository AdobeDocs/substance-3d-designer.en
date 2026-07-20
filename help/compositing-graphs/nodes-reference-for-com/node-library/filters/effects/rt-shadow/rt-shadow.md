---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/rt-shadow.html"
breadcrumb-title: ""
description: Use the RT Shadows node to compute real-time shadow information from geometry for creating dynamic lighting effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > RT Shadows
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: RT Shadows
user-guide-description: ""
user-guide-title: ""
---

# RT Shadows

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![RT Shadows node icon](../../../../../../assets/rt-shadow.png "RT Shadows node icon")

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates ray traced shadows from a height map input.   
  
This node should not be used in combination with the CPU (SSE) engine due to computation time.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Samples</b> <i>Integer</i> | The number of rays used to compute the shadows.<br>A higher value provides a smoother and more precise result, at the cost of performance. |
| <b>Mode</b> <i>Integer</i> | The method of drawing the shadows on the surface. |
| <b>Height Scale</b> <i>Float</i> | A multiplier for the intensity of the input height map. |
| <b>Light Position</b> <i>Float2</i> | The position of the light source on a sphere enclosing the surface:<br><br>- <b>X</b>: horizontal position, in number of turns;<br>- <b>Y</b>: vertical position, where 0.5 is the zenith and 0/1 are the horizon. |
| <b>Light Intensity</b> <i>Float</i> | The intensity of the light source. |
| <b>Light Size</b> <i>Float2</i> | (Available when <b>Mode</b> is set to <i>Shaded</i>) The size of the light source as a rectangle. |
| <b>Light Scale (Soft Shadows)</b> <i>Float</i> | A multiplier for the contribution of the <b>Light Size</b> to the direction of the rays.<br>A higher value results in smoother shadows. |
| <b>Keep Light Above Horizon</b> <i>Boolean</i> | If <b>Light Position</b> is set in a way that places the light below the horizon, this parameter prevents the light from crossing that threshold, meaning that Y values are clamped to the &#91;0;1&#93; range. |
| <b>Shadow Opacity</b> <i>Float</i> | A multiplier for the opacity of shadows drawn on the surface. |
| <b>Shadow Attenuation</b> <i>Float</i> | A multiplier for the attenuation of the shadows the farther they are from their caster.<br>A value of 0 results in uniform shadows (soft shadows are still applied). |
| <b>Max Shadows Length</b> <i>Float</i> | The maximum distance a shadow can be drawn from its caster.<br>A value of 0 results in no visible shadows. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/RTShadows-01.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/RTShadows-02.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/RTShadows-03.jpg" />
        </td>
    </tr>
</table>
