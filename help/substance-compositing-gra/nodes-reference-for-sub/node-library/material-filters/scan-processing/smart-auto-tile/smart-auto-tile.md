---
title: "Smart Auto Tile"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Smart Auto Tile"
---

# Smart Auto Tile

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](smart-auto-tile.png){width="128px"}

## Smart Auto Tile

**In:** *Material Filters/Scan Processing*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This node turns a non-tiling set of Basecolor, Normal and Heightmaps into a tiling version according to smart analysis of the inputs. It is similar to [Make It Tile Photo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/tiling/make-it-tile-photo/make-it-tile-photo.md), but much more advanced as it uses information from all channels to blend things together in the smartest way (similar to what [Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md) does). It also has an internal [Crop](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md) function to determine which area to use when tiling - make sure to [read more about the Crop node](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/crop/crop.md) to understand this function properly.

To use this node, start by defining your Cropped area and then use the Edge settings to determine how the tiled edges are blended into the centre. The Treshold parameters are of key importance to this! Keep in mind that big, uniform areas don't work very well with this effect; the more details and shapes there are, the more it has to work with.

## Parameters

### Inputs

* **Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects. Can be toggled with the "Use Mask" parameter.

### Parameters

* **Crop**   
  * **Input Size**: *0 - 8192*Input images' resolution and proportions. Very important for non-square images.
  * **Transform**: *(Transformation Matrix)*  
    Rotates and scales the result. The result can be modified by directly interacting with the canvas.
  * **Offset**: *0.0 - 1.0*  
    Moves or translates the result. The result can be modified by directly interacting with the canvas.
* **Edge**   
  * **Detect Edges**: *False/True*Turns on or off special edge detected blending.
  * **Use Threshold Per Channel**: *False/True*Switches between a global treshold value, or one for every channel.
  * **Threshold**: *0.0 - 1.0*
  * **Threshold Base Color**: *0.0 - 1.0*
  * **Threshold Normal**: *0.0 - 1.0*
  * **Threshold Height**: *0.0 - 1.0*
  * **Cut Offset**: *0.0 - 0.5*Main control for moving the cut, both X- and Y-axes are separated.
  * **Blur**: *0.0 - 2.0*Blurs the blending transition.
  * **Smoothness**: *0.0 - 2.0*Controls jaggedness of edge analysis results.
  * **Grid Resolution**: *1 - 11*Quality resolution of edge analysis.
  * **Use Base Color**: *False/True*Toggles Base Color processing (in and out).
  * **Use Normal**: *False/True*Toggles Normal processing (in and out).
  * **Use Height**: *False/True*Toggles Normal processing (in and out).
  * **Use Mask**: *False/True*  
    Toggles the use of the Mask map on or off, for custom stamp mask shapes.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
