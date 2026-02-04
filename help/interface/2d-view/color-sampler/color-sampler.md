---
title: "Color sampler tool"
description: ""
helpx_description: "Designer > Interface > 2D view > Color sampler tool"
---

# Color sampler tool

![Color sampler tool](color-sampler-demo.png "Color sampler tool"){zoomable="yes"}

The Color Sampler tool lets you <b>track the value of a specific pixel</b> in the [2D View](../2d-view.md) as you tweak parameters or switch nodes.

It places a pin in the viewport and samples the color and position of the pixel at that location.

## Using the tool

Follow these steps to access and use the tool:

1. Click the ![](color-sampler-information-button.png) <b>Information</b> button in the 2D view toolbar to open the Information dock and toolbar
1. Click the ![](color-sampler-tool-icon.png) <b>Color Sampler tool</b> button in the Information toolbar
1. In the viewport, click on the specific pixel you want to sample to place a ![](color-sampler-pin-icon.png) <b>pin</b>
1. Examine the sampled values in the dedicated section of the Information dock
1. When you are done with the tool, click the ![](color-sampler-remove-pin.png) <b>Delete</b> button to remove the pin from the viewport.  
   You can also remove the pin by clicking RMB on it and selecting the 'Delete' action in the contextual menu.

Here is a demonstration of the tool in action:

![Color sampler: using the tool](color-sampler-demo.gif "Color sampler: using the tool"){zoomable="yes"}

*Click to enlarge*

+++Copy the sampled RGBA values


You can copy the sampled values by clicking RMB on the pin and selecting the 'Copy RGBA values' action in the contextual menu.





The copied values can bepasted in parameters using a color thumbnail.





The color thumbnails in the Information panel can also be dragged and dropped directly onto the color thumbnails of those parameters.







Click to enlarge



+++

## Sampled information

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

The information is grouped into three types and two formats.

* <b>Sampled values</b> stored in each of the image's RGBA channels:  
  Varying\* / Floating point
* <b>Sampled color</b> in the HSV representation:  
  8-bit integer / Floating point
* <b>Position</b> of the pixel in number of pixels and normalized image space:  
  Integer / Floating point

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Sampled information](color-sampler-information.png "Sampled information"){zoomable="yes"}

</td>
</tr>
</table>

The value depends on the bitdepth used by the image. In a Substance graph, the bitdepth is controlled by the <b>Output Format</b> [base parameter](../../../compositing-graphs/graph-parameters/graph-parameters.md).

The available bitdepths are:

* <b>8-bit integer:</b> 256 integer values from 0 to 255.
* <b>16-bit integer:</b> 65,536 integer values from 0 to 65,535.
* <b>HDR low precision (16-bit)</b>: A floating point value encoded using 16-bit.
* <b>HDR high precision (32-bit)</b>: A floating point value encoded using 32-bit. This is the highest precision available in Designer.
