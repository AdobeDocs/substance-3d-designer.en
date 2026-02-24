---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/rt-shadow.html"
breadcrumb-title: ""
description: Use the RT Shadows node to compute real-time shadow information from geometry for creating dynamic lighting effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > RT Shadows
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: RT Shadows
user-guide-description: ""
user-guide-title: ""
---


# RT Shadows

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![RT Shadows node icon](rt-shadow.png "RT Shadows node icon")

<b>In:</b> *Filters/Effects*

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Generates ray traced shadows from a height map input.   
  
This node should not be used in combination with the CPU (SSE) engine due to computation time.

</td>
</tr>
</table>

## Parameters

<b>Samples</b> *Integer*  
The number of rays used to compute the shadows.  
A higher value provides a smoother and more precise result, at the cost of performance.

<b>Mode</b> *Integer*  
The method of drawing the shadows on the surface.

<b>Height Scale</b> *Float*  
A multiplier for the intensity of the input height map.

<b>Light Position </b>*Float2*  
The position of the light source on a sphere enclosing the surface:  
* <b>X</b>: horizontal position, in number of turns;  
* <b>Y</b>: vertical position, where 0.5 is the zenith and 0/1 are the horizon.

<b>Light Intensity</b> *Float*  
The intensity of the light source.

<b>Light Size</b> *Float2* (Available when <b>Mode</b> is set to *Shaded*)  
The size of the light source as a rectangle.

<b>Light Scale (Soft Shadows)</b> *Float*  
A multiplier for the contribution of the <b>Light Size</b> to the direction of the rays.  
A higher value results in smoother shadows.

<b>Keep Light Above Horizon</b> *Boolean*  
If <b>Light Position</b> is set in a way that places the light below the horizon, this parameter prevents the light from crossing that threshold, meaning that Y values are clamped to the &#91;0;1&#93; range.

<b>Shadow Opacity</b> *Float*  
A multiplier for the opacity of shadows drawn on the surface.

<b>Shadow Attenuation</b> *Float*  
A multiplier for the attenuation of the shadows the farther they are from their caster.  
A value of 0 results in uniform shadows (soft shadows are still applied).

<b>Max Shadows Length</b> *Float*  
The maximum distance a shadow can be drawn from its caster.  
A value of 0 results in no visible shadows.

## Example Images

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![RT Shadows node - Example 1](RTShadows-01.jpg "RT Shadows node - Example 1")

</td>
<td style="border: 0;" valign="top">

![RT Shadows node - Example 2](RTShadows-02.jpg "RT Shadows node - Example 2")

</td>
<td style="border: 0;" valign="top">

![RT Shadows node - Example 3](RTShadows-03.jpg "RT Shadows node - Example 3")

</td>
</tr>
</table>
