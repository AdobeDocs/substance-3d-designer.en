---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/shape-light.html"
breadcrumb-title: ""
description: Use the Shape Light node to add custom-shaped light sources to HDRI environments for creative lighting effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Shape Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Shape Light
user-guide-description: ""
user-guide-title: ""
---


# Shape Light

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](panorama-shape.png){width="200px"}

## Shape Light

**In:** *3D View/HDRI Tools*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a spherically projected rectangular shape. The shape transformation is driven by a transformation gizmo.

## Inputs

* **Background Image Input**: *Color Input*Optional background onto which to compose the generated light.
* **Shape Image Input**: *Color Input*Optional image to map onto Sphere light. Only used when Shape Color Mode is set to Image Input.

## Parameters

* **Shape Matrix**   
  * **Matrix**: *(Transformation Matrix)*  
    Transformation control for the result. Result can be modified by directly interacting with the canvas.
  * **Offset**: *-2.0 - 2.0*  
    Moves or translates the result. Result can be modified by directly interacting with the canvas.
* **Shape**: *Rectangle, Disc*  
  Choose what shape to place.
* **Shape Color Mode**: *RGB, Temperature (Kelvin), Image Input*  
  Choose what method to use to set shape color. Image Input enables use of the second input slot.
* **Color**: *(Color value)*  
  Only with Shape Color Mode set to RGB. Picks color for shape.
* **Shape Temperature**: *800.0 - 20000.0*  
  Only with Shape Color Mode set to Temperature. Sets Kelvin value for shape color.
* **Shape Image Input Gamma**: *sRGB, Linear*  
  Only with Shape Color Mode set to Image Input. Determine how to interpret Shape Image Input.
* **Shape Exposure (EV)**: *0.0 - 10.0*  
  Set exposure value for generated shape, Ideally matched to background image exposure value.
* **Shape Hardness**: *0.0 - 1.0*  
  Set hardness of shape edges.
* **Hotspot Exposure (EV)**: *0.0 - 10.0*  
  Set Exposure of central hotspot. Note this is not very visible in RGB mode.
* **Hotspot Size**: *0.0 - 1.0*  
  Size of the central Hotspot.
* **Hotspot Falloff**: *0.0 - 1.0*  
  Falloff of central hotspot.
* **Hotspot Position**: *0.0 - 1.0*  
  X and Y position of the central hotspot.
* **Enable Backgound Input**: *False/True*  
  Toggles use of optional background image. Composites generated light on top of background.
* **Background Color**: *(Color value)*  
  If Background Input is not used, set a solid color background value here.
* **Background Gamma**: *sRGB, Linear*If Background Input is used, set how to interpret Background input.

## Example Images

![](shape-light-ex.gif)

</td>
</tr>
</table>
