---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/multi-crop.html"
breadcrumb-title: ""
description: Use the Multi Crop node to crop multiple texture channels simultaneously for processing scanned materials efficiently.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Multi Crop
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi Crop
user-guide-description: ""
user-guide-title: ""
---

# Multi Crop

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/crop-multi.png){width="128px"}

![](../../../../../../assets/crop-multi-grayscale.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is the multi-channel version of Crop. It crops out an area from an image and is mainly intended for use with multi-angle photos, which are then combined with [Multi-Angle to Albedo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-albedo/multi-angle-to-albedo.md) or [Multi-Angle to Normal](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/multi-angle-to-normal/multi-angle-to-normal.md).

>[!NOTE]
>
> See the original [Crop](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md) for more info.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Input Count</b> <i>1 - 8</i> | Sets the number of inputs to process in parallel. |
| <b>Input Size</b> <i>0 - 8192</i> | Input images' resolution and proportions. Very important for non-square images. |
| <b>Background</b> <i>(Color value) / (Grayscale value)</i> | Background uniform value for areas not covered by Crop. |
| <b>Transform</b> <i>(Transformation Matrix)</i> | Rotates and scales the result. The result can be modified by directly interacting with the canvas. |
| <b>Offset</b> <i>0.0 - 1.0</i> | Moves or translates the result. The result can be modified by directly interacting with the canvas. |
| <b>Is Normal (only for Color version)</b> <i>False/True</i> | Whether or not the input should be treated as a Normalmap. |
