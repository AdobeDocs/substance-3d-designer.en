---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/smart-auto-tile.html"
breadcrumb-title: ""
description: Use the Smart Auto Tile node to automatically create seamless tiles from scanned materials using intelligent pattern detection.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Smart Auto Tile
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Smart Auto Tile
user-guide-description: ""
user-guide-title: ""
---

# Smart Auto Tile

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](smart-auto-tile.resources/smart-auto-tile-01.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node turns a non-tiling set of Basecolor, Normal and Heightmaps into a tiling version according to smart analysis of the inputs. It is similar to [Make It Tile Photo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/tiling/make-it-tile-photo/make-it-tile-photo.md), but much more advanced as it uses information from all channels to blend things together in the smartest way (similar to what [Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md) does). It also has an internal [Crop](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md) function to determine which area to use when tiling - make sure to [read more about the Crop node](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md) to understand this function properly.

To use this node, start by defining your Cropped area and then use the Edge settings to determine how the tiled edges are blended into the centre. The Treshold parameters are of key importance to this! Keep in mind that big, uniform areas don't work very well with this effect; the more details and shapes there are, the more it has to work with.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Mask</b> <i>Grayscale Input</i> | Mask slot used for masking the node's effects. Can be toggled with the "Use Mask" parameter. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Crop</b> |  |
| <b>Input Size</b> <i>0 - 8192</i> | Input images' resolution and proportions. Very important for non-square images. |
| <b>Transform</b> <i>(Transformation Matrix)</i> | Rotates and scales the result. The result can be modified by directly interacting with the canvas. |
| <b>Offset</b> <i>0.0 - 1.0</i> | Moves or translates the result. The result can be modified by directly interacting with the canvas. |
| <b>Edge</b> |  |
| <b>Detect Edges</b> <i>False/True</i> | Turns on or off special edge detected blending. |
| <b>Use Threshold Per Channel</b> <i>False/True</i> | Switches between a global treshold value, or one for every channel. |
| <b>Threshold</b> <i>0.0 - 1.0</i> |  |
| <b>Threshold Base Color</b> <i>0.0 - 1.0</i> |  |
| <b>Threshold Normal</b> <i>0.0 - 1.0</i> |  |
| <b>Threshold Height</b> <i>0.0 - 1.0</i> |  |
| <b>Cut Offset</b> <i>0.0 - 0.5</i> | Main control for moving the cut, both X- and Y-axes are separated. |
| <b>Blur</b> <i>0.0 - 2.0</i> | Blurs the blending transition. |
| <b>Smoothness</b> <i>0.0 - 2.0</i> | Controls jaggedness of edge analysis results. |
| <b>Grid Resolution</b> <i>1 - 11</i> | Quality resolution of edge analysis. |
| <b>Use Base Color</b> <i>False/True</i> | Toggles Base Color processing (in and out). |
| <b>Use Normal</b> <i>False/True</i> | Toggles Normal processing (in and out). |
| <b>Use Height</b> <i>False/True</i> | Toggles Normal processing (in and out). |
| <b>Use Mask</b> <i>False/True</i> | Toggles the use of the Mask map on or off, for custom stamp mask shapes. |
