---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-vector-rotation.html"
breadcrumb-title: ""
description: Use the Normal Vector Rotation node to rotate normal map vectors for adjusting surface lighting and detail orientation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Vector Rotation
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Normal Vector Rotation
user-guide-description: ""
user-guide-title: ""
---


# Normal Vector Rotation

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](normal-vector-rotation.png){width="128px"}

## Normal Vector Rotation

**In:** *Filters/Normal Map*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Normal utility node that rotates all vectors of an input Normalmap in Tangent space. Doesn't actually transform pixels, instead it modifies the values they represent. It can make use of an optional map to add random rotations to grayscale facets.

## Inputs

* **Normal**: *Color Input*   
  Base map to perform rotation on. Required.
* **Rotation Map (optional)**: *Grayscale Input*   
  Grayscale map that modulates Rotation strength.

## Parameters

* **Rotation Angle**: *0.0 - 1.0*  
  Sets Angle by which to rotate the Normalmap
* **Normal Format**: *DirectX, OpenGL*  
  Switch between different Normal Map formats (inverts the green channel)

## Examples

</td>
</tr>
</table>
