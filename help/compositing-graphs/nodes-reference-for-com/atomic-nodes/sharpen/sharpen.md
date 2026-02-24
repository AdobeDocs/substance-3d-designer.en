---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/sharpen.html"
breadcrumb-title: ""
description: Use the Sharpen node to enhance texture details and edges for creating crisp, defined surface details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Sharpen
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Sharpen
user-guide-description: ""
user-guide-title: ""
---


# Sharpen

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Sharpen node icon](sharpen-4.png "Sharpen node icon")

<b>In:</b> Atomic Nodes

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The Sharpen Node perform a sharpening operation on an input. It is a useful node for applying that final touch of crispness to an image.

</td>
</tr>
</table>

It is mathematically very similar to Photoshop's Unsharp Mask, despite the name being different. It works well for things like a Basecolor map, but should be avoided on maps like Normal maps and Metallic maps.

## Inputs

<b>Input</b> *Color/Grayscale* (Primary)  
The image which should be sharpened.

## Parameters

<b>Intensity</b> *Float*  
Sets the intensity of the sharpening effect.

<b>Punchthrough Alpha</b> *Boolean* (Available when a color image is connected to the <b>Input</b>)  
Determines whether the image's alpha channel should be sharpened or left untouched.

## Examples

![Sharpen node - Example 1](sharpen-ex.png "Sharpen node - Example 1")
