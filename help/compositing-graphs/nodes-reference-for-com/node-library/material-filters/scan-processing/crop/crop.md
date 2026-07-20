---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/crop.html"
breadcrumb-title: ""
description: Use the Crop node to crop material outputs to specific regions for processing scanned materials and textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Crop
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Crop
user-guide-description: ""
user-guide-title: ""
---

# Crop

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/crop-10.png){width="128px"}

![](../../../../../../assets/crop-grayscale.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Crop is a parametric, non-destructive version of the familiar crop tool. You select an area of an image and the result is returned with the unselected areas discarded.

It can be useful in many ways, as performing a Crop operation with atomic nodes is not so straightforward. Especially for converting non-square images, this node comes in handy. Make sure to set the input resolution correctly in that case.

Very important to understand is that to use this node with ease, you must make good use of the ability to preview a different node than the one whose parameters you're editing!  
In short: **Double-click** the node you are using as input for this one (the original, uncropped image), then **single-click** the crop node that follows right after it. You can then modify the crop gizmo to fit the area you want to crop to.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Input Size</b> <i>0 - 8192</i> | Input image's resolution and proportions. Very important for non-square images. |
| <b>Background</b> <i>(Color value) / (Grayscale value)</i> | Background uniform value for areas not covered by Crop. |
| <b>Transform</b> <i>(Transformation Matrix)</i> | Rotates and scales the result. The result can be modified by directly interacting with the canvas. |
| <b>Offset</b> <i>0.0 - 1.0</i> | Moves or translates the result. The result can be modified by directly interacting with the canvas. |
| <b>Is Normal (only for Color version)</b> <i>False/True</i> | Whether or not the input should be treated as a Normalmap. |
