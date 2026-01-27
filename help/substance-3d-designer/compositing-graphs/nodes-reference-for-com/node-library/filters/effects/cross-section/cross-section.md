---
title: "Cross Section | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Cross Section"
---

# Cross Section

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

!['Cross section' node icon](cross-section-2.png "'Cross section' node icon"){width="200px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Draws a cross-sectional profile of an input. Can be adjusted to slice vertical or horizontal, and has controls for drawing style and graph offset and scaling.

</td>
</tr>
</table>

This node is especially useful for debugging and analyzing heightmaps. giving you a pixel-perfect profile view, without needing complex nodes or a lengthy, less precise setup in the 3D View.

Alternatively it can be used to create 2D shapes and silhouettes that are hard to achieve otherwise. Combined with a [Curve node ](../../../../atomic-nodes/curve/curve.md)it can directly visualize the curve profile applied to a linear gradient.

## Parameters

<b>Cross section coordinate</b> *Float*  
Set at what coordinate to sample the slice. Can be X or Y coordinate depending on Section Axis.

<b>Section axis</b> *Integer*  
Set if the slice is vertical or horizontal.

<b>Show helper</b> *Boolean*  
Enables an overlay displaying the position of the section over the input image.

Helper Settings

<b>Helper scale</b> *Float*  
    The size of the overlay expressed as a multiple, where 1.0 is the entire image.

<b>    Helper position</b> *Float2*  
    The (X, Y) position of the overlay in the output image, where (0.0, 0.0) is top left and (1.0, 1.0) is bottom right.

<b>Height scale</b> *Float*

Scales entire graph down. Useful for HDR viewing.

<b>Height offset</b> *Float*  
Shifts entire graph up or down. Useful for HDR viewing.

<b>Drawing style</b> *Integer*  
Switch between solid fill and line drawing.

<b>Invert Gradient</b> *Boolean*If Drawing Style is set to *Gradient* or *Gradient mirrored*, lets you invert that gradient without affecting the background.  
*Note:* Only available when 'Drawing style' is set to 'Gradient' or 'Gradient mirrored'.

<b>Smooth / Polygonal</b> *Boolean*  
Switches shape between perfect smooth profile, or jagged, polygonal.  
*Note:* Only available when 'Drawing style' is set to 'Solid', 'Gradient' or 'Gradient mirrored'.

<b>Segment amount</b>: *Integer*  
Sets the amount of segments used to draw when in Polygonal Style, or in Line Style.  
*Note:* Only available when 'Smooth / Polygonal' is set to 'Polygonal', or when 'Drawing style' is set to 'Line'.

<b>Line thickness</b> *Float*  
Sets the thickness of the line.  
*Note:* Only available when 'Drawing style' is set to 'Line.

<b>Line style</b> *Integer*  
Lets you choose coloring and falloff of the line.  
*Note:* Only available when 'Drawing style' is set to 'Line.

<b>Line smoothness</b> *Float*  
Sets gradient falloff of the line.  
*Note:* Only available when 'Drawing style' is set to 'Line.

<b>Color</b> *Float*  
Grayscale color of the line or shape.  
*Note:* Only available when 'Drawing style' is set to 'Solid', or 'Line' and 'Line style' is set to 'Smooth' or 'Solid'.

<b>Background color</b> *Float*Grayscale color of the background.  
*Note:* Not available when 'Drawing style' is set to 'Line' and 'Line style' is set to 'Segment ID' or 'Gradient along line'.

## Examples

![Cross section: example 1](cross-section-example-01.gif "Cross section: example 1")

![Cross section: example 2](cross-section-example-02.gif "Cross section: example 2")

![Cross section: example 3](cross-section-example-03.png "Cross section: example 3")

![Cross section: example 4](cross-section-example-04.png "Cross section: example 4")
