---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/clone-patch.html"
breadcrumb-title: ""
description: Use the Clone Patch node to clone and patch areas in scanned materials for removing artifacts and imperfections.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Clone Patch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Clone Patch
user-guide-description: ""
user-guide-title: ""
---

# Clone Patch

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/clone-patch.png){width="128px"}

![](../../../../../../assets/clone-patch-grayscale.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Clone Patch is a procedural, parametric "Clone Stamp" node. It clones one area of an input to another, hiding potentially unwanted details. While it's not as quick and easy as using a familiar tool in a brush-based application, it does provide the key advantage of being non-destructive and working within a node-based workflow. Additionally, this node performs a smart analysis of both target and source area, and tries to blend things as well as possible based on contrast, values and shapes.

This is mostly intended for those rare moments where you want to do a manual fix of a specific area, in case there is an unwanted detail somewhere.

Keep in mind this does not work like a standard, simple "Stamp" brush. The shape of your blended area is based on the shapes and values of the areas you're working with, meaning this is quite a heavy node that requires patience - but does offer excellent results.

Also important to understand is the fact that you can move the Target area with a gizmo, but the Source area needs to be set by changing the "Source Matrix" Parameters.

>[!NOTE]
>
> If you want this for a full material (as is most often the case), see [Material Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/material-clone-patch/material-clone-patch.md).
> 
> For those cases where you want to perform this operation on multiple inputs at the same time (without it being a material), see [Multi Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-clone-patch/multi-clone-patch.md).

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Is Normal (only for Color)</b> <i>False/True</i> | Sets whether the input is a Normalmap, and whether blending should be treated as such. |
| <b>Shape</b> <i>Square, Disc</i> | Sets Stamp shape. Used only as base. |
| <b>Edge</b> |  |
| <b>Threshold</b> <i>0.0 - 1.0</i> | Sets how far the blended area should reach. This grows in steps, along shapes in the target area, and has very little effect with uniform backgrounds<i>.</i> |
| <b>Blur</b> <i>0.0 - 2.0</i> | Blurs the edges of the stamp area in case a softer transition is needed. |
| <b>Smoothness</b> <i>0.0 - 2.0</i> | Rounds off the edges of the stamp shape, making for smoother-flowing outlines. |
| <b>Grid Resolution</b> <i>1 - 11</i> | Sets the quality resolution of the blending analysis. A higher value means more accurate blending. |
| <b>Transformations</b> |  |
| <b>Source Matrix</b> <i>(Transformation Matrix)</i> | Transforms source (Scale &amp; Rotation). Cannot be done on canvas, change through these parameters only. |
| <b>Source Offset</b> <i>-0.5 - 0.5</i> | Translates source location. Cannot be done on canvas, change through these parameters only. <i>This parameter is probably the main one you want to change!</i> |
| <b>Target Matrix</b> <i>(Transformation Matrix)</i> | Transforms target location (Scale &amp; Rotation). Can also be done through gizmo on canvas. |
| <b>Target Offset</b> <i>-0.5 - 0.5</i> | Translates target location. Can also be done through gizmo on canvas. |
