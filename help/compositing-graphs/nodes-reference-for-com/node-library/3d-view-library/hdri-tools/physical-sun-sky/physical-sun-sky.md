---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/physical-sun-sky.html"
breadcrumb-title: ""
description: Use the Physical SunSky node to generate physically accurate sun and sky lighting environments for realistic material preview.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Physical SunSky
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Physical SunSky
user-guide-description: ""
user-guide-title: ""
---


# Physical Sun/Sky

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](panorama-physical-sun-sky.png){width="200px"}

## Physical Sun/Sky

**In:** *3D View/HDRI Tools*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Physical Sun and Sky implementation based on Hosek-Wikie skylight model. Provides an excellent base for an artifical HDRI.

## Parameters

* **Sun Position**:   
  range = &#91;0,1&#93;x&#91;0,1&#93; (longitude-latitude angles)
* **Turbidity**: *1.0 - 10.0*  
  Turbidity ranges from 1 to 10
* **Albedo**: *0.0 - 1.0*  
  Albedo ranges from 0 to 1.
* **Ground Color**: *(Color value)*  
  Color of the ground plane.
* **Exposure (EV)**: *-1.0 - 4.0*  
  Exposure value of resulting output.
* **Sun Size**: *0.0 - 4.0*  
  Scale of the Sun, any value different than 1 is non physically correct. Value has subtle effects!
* **Sun Intensity**: *0.0 - 1.0*  
  Intensity of sun disc. Sun disc is fairly small so effect is not immediately visible.
* **Sky Intensity**: *0.0 - 1.0*Intensity of the sky. Also affects flaring of sun in the sky, not the disc itself.

## Example Images

![](sky-ex.gif)

</td>
</tr>
</table>
