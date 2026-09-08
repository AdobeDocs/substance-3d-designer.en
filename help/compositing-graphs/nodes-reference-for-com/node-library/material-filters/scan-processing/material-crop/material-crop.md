---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/material-crop.html"
breadcrumb-title: ""
description: Use the Material Crop node to crop texture regions from scanned materials for isolating specific areas of interest.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Material Crop
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Crop
user-guide-description: ""
user-guide-title: ""
---

# Material Crop

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/crop-material.png){width="128px"}

## Material Crop

**In:** *Material Filters/Scan Processing*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

This node is the multi-channel, full material version of [Crop](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md). It allows you to perform a crop operation on any and all Material channels in parallel.

>[!NOTE]
>
> [See the original ](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md)[Crop](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md)[ for more info.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md)

## Parameters

### Parameters

* **Channels**  
  * Toggle material channels on and off in this group, when using Specular/Glossiness maps instead of Metallic/Roughness for example.
* **Input Size**: *0 - 8192*Input image's resolution and proportions. Very important for non-square images.
* **Background**: *(Color value) / (Grayscale value)*Background uniform value for areas not covered by Crop.
* **Transform**: *(Transformation Matrix)*  
  Rotates and scales the result. Result can be modified by directly interacting with the canvas.
* **Offset**: *0.0 - 1.0*  
  Moves or translates the result. Result can be modified by directly interacting with the canvas.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
