---
title: "Vector editing tools"
description: ""
helpx_description: "Designer > Resources > Vector graphics (SVG) resource > Vector editing tools"
---

# Vector editing tools

This page describes the editing tools available in the [2D View](https://docs.substance3d.com/display/SDDOC/2D+view) panel for compatible vector graphics.

## Overview

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

The [2D View](https://docs.substance3d.com/display/SDDOC/2D+view) panel offers basic vector editing tools which let you create or edit vector graphics *manually* directly within [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html). These tools are particularly useful, for instance, for quickly creating *masks* or *patterns*.

The tools support pen input. To take advantage of pen displays, you may [undock](https://docs.substance3d.com/display/SDDOC/Customizing+your+workspace) the [2D view](https://docs.substance3d.com/display/SDDOC/2D+view) panel, then place and resize it into any configuration which is more comfortable for painting.

Edits can be *undone individually*, and all the other features of the 2D View panel are still *available* to you while you edit the vector image, such as [Histogram](https://docs.substance3d.com/display/SDDOC/2D+view#id-2Dview-Histogram) panel, [Tiled display](https://docs.substance3d.com/display/SDDOC/2D+view#id-2Dview-Viewport), and [Background image](https://docs.substance3d.com/display/SDDOC/2D+view#id-2Dview-Backgroundimage).

</td>
<td style="border: 0;" valign="top">

![](2dview-vectorediting-main.png){width="512px"}

</td>
</tr>
</table>

>[!TIP]
>
> **Windows only**
> 
> Tablet users should apply the settings described in the following page for the most reliable experience in Designer: [Configuring Pens and Tablets](https://docs.substance3d.com/display/SPDOC/Configuring+Pens+and+Tablets)

>[!IMPORTANT]
>
> You can paint *only* on *8-bit* [vector graphics resources](../vector-graphics-svg-resource.md) which are [new or imported](https://docs.substance3d.com/display/SDDOC/Importing%2C+Linking+and+New+Resources).

![New SVG resource dialog](2dview-new-vector-image.png "New SVG resource dialog"){width="512px"}

## Enabling the vector editing tools

The vector editing tools will be enabled automatically in the [2D view](https://docs.substance3d.com/display/SDDOC/2D+view) panel when the following criteria regarding a vector graphics image are met:

* The vector graphics image is a [new or imported](https://docs.substance3d.com/display/SDDOC/Importing%2C+Linking+and+New+Resources) resource
* The bitmap is displayed in the [2D view](https://docs.substance3d.com/display/SDDOC/2D+view) panel

*New* vector graphics images can be created the following ways:

* In the [Explorer](https://docs.substance3d.com/display/SDDOC/The+Explorer+Window) panel, click RMB on an *SBS package* or a *folder* within a package to open their contextual menu, then open the **New** submenu and select the **SVG** option
* In a [graph](https://docs.substance3d.com/display/SDDOC/The+Graph+view), create an [SVG node](../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/svg/svg.md) and select the **From new resource...** option in the contextual menu

The **New vectorial data** window will open, letting you set the *name* and *resolution* of the new vector graphics resource.

>[!TIP]
>
> For the best performance with the vector editing tools, we recommend using vector graphics images with resolutions which are *powers of two* – e.g. 128, 256, 512, 1024, ...

### Exporting vector graphics from other software

Designer *only* supports vector graphics using the **SVG** file format.

For the best compatibility and reliability in Designer and its editing tools, please make sure all objects are converted to *outlines* and ungrouped to *separate* objects using *flat colors*, so that *none of the following remain*:

* **Text**
* **Gradients**
* **Patterns** (both for fills and stroke outlines)
* **Styles**

**Adobe Illustrator** users can refer to the attached image for recommended SVG *export settings.*

+++Adobe Illustrator export options


+++

>[!NOTE]
>
> To learn more about SVG limitations, exporting from other software and SVG properties in Designer, please refer to the [Vector graphics (SVG) resource](../vector-graphics-svg-resource.md) section.

## Tools

The painting tools and options are arranged in *toolbars* within the [2D view](https://docs.substance3d.com/display/SDDOC/2D+view) panel. These toolbars can be relocated to *any side* of the panel or as a *floating toolbar*, by clicking and holding **LMB** on their *handle* – displayed as a triple line – then releasing **LMB** at the desired location.

Two toolbars are displayed when the vector editing tools are enabled:

* **Tool selection** **toolbar**: lets you *select a tool* as well as the *fill/outline colors*, and is placed on the *left* side of the 2D View panel by default
* **Tool options toolbar**: lets you set the *options* for the *currently selected tool*, and is placed on the *top* side of the 2D View panel by default

Keyboard shortcuts let you access tools quickly, and are marked below between parentheses after the tool/function name:

+++Color selection


TheColor selectionthumbnailslet you define afillandoutlinecolor for vector shapes. You can open theColor editorfor each of these colors in the following ways:



* Fill color:Click on thefillcolor thumbnail (top), or double-click LMB on the canvas


* Outline color:Click on theoutlinecolor thumbnail (bottom), orhold Ctrland double-click LMB on the canvas




The set colors will then be applied to thecurrently selected shapes.





If the currentoutlinecolor isblack– i.e. luminance 0 or RGB (0, 0, 0) – it willnotbe applied to the selected shapes until youclick on the outline color thumbnail.



+++

+++Transformation




TheTransformationtool (V) can select shapes, which are then included in a transformation gizmo. This gizmo lets you perform the following actions:





Move: Click and hold LMBinsidethe gizmo





Scale: Click and hold LMB on any of thesquare handlesalong the gizmo toscalethe object horizontally, vertically, or both. By default, scaling is done relatively to the handle on theoppositeside of the gizmo. You can hold theAltkey to perform the scaling relatively to thecenterof the gizmo, and hold theShiftkey tolockthe gizmo width/heightratio





Rotate:Click and hold LMB next to any of thesquare handlesalong the gizmo,outsideof the gizmo.



+++

+++Node




TheNodetool (A) lets you select individual vertices (i.e. nodes) of the selected shape and edit its position and handles, as well as add and remove vertices. Once a shape is selected, the following actions can be performed:





Add vertex:Ctrl+LMB on the shape outline





Remove vertex: Ctrl+LMB on the vertex





Move vertex: Hold LMB on the vertex





Move vertex handles: Hold LMB on the handle





Move vertex handle independently: Hold Alt+LMB on the handle. Note that handles will beunlinkedpast this point until they arereset





Reset handles: Click Alt+LMB on the vertex. The handles will be reset to thevertex position





Move reset vertex handles: Hold Alt+LMB on the vertex.Linkedhandles will appear



+++

+++Shape




TheShapestool (M) offers a set of primitive shapes, using the currentlfillcolor, which can be built from and edited:



* Rectangle;


* Ellipse;


* Rounded rectangle:The rounded angles have a locked radius;


* Polygon:Creates an octogon.




To draw a primitive, HoldLMBanywhere in the canvas from any of itscorners. HoldAlt+LMBto draw the shape from itscenter.



+++

+++Pen




ThePentool (P) lets you draw a new custom shape, using the currentfillcolor. Two modes are available:





InPathmode, the shape is drawnone vertex at a time. The following controls are available:





Addstraight in/straight outvertex: Click LMB





Addcurve in/curve outvertex (alignedtangents): Hold LMB and drag





Addcurve in/curve outvertex (unalignedtangents)*: Hold LMB and drag, then hold Alt+LMB





Addcurve in/straight outvertex*: same as curve in/curve out vertex (unaligned tangents), but the out line needs to be placedon top of the new vertex





Addstraight in/curve outvertex*: Hold Alt+LMB and drag





Close shapeonnextvertex: Hold Ctrl





Close shapeoncurrentvertex: Press Enter, or click LMB on thefirst vertexof the current shape





Freehandmode lets you draw shapes directly by dragging the pen across the canvas while holding LMB.





Vertices areautomatically placedalong the stroke so that the resulting path matches the stroke as closely as possible. The shape isautomatically closedwhen the stroke ends, connecting the first vertex to the last in the stroke.



+++

+++Extrude




TheExtrudetool (E)adds togethera shape of aset diameter, drawn along a path using the selecteddrawing mode, and applies the result in the canvas following themerging modeset in the options toolbar.





The followingdrawing modesare available:





Freeform: draws the shapedirectly by draggingthe pen across the canvas while holding LMB. The shape is added together when the stroke ends.





Polygonal: draws the shapeone face at a timeby clicking LMB to add an angle. The shape is added together when the Enter key is pressed.





The drawn shape can be controlled using these parameters:





Size: Controls the diameter of the radial shape drawn at the cursor location.





Smoothness: Controls the amount by which the drawn shape should besmoothed out and simplifiedwhen added together at the end of the stroke.





When the drawing is completed, the shape is added together and merged with the currently selected shape using one of these availablemerging modes:





No merging: The shape is drawnon topof the selected shape as aseparate object.





Union: The shape isaddedto the selected shape.





Subtraction: The shape iscut outof the selected shape.





Intersection: Only theoverlappingportions of the new and the selected shape remain.



+++

## Shape operations

![Shape operations](2dview-vectorediting-shape-operations.png "Shape operations"){width="512px"}

In addition to the tools listed above, a number of operations can be performed on *selected shapes*, using the contextual menu available when clicking RMB. These operations nearly all have a keyboard shortcut (in parentheses below) are organised in the following categories:

+++Adding and removing shapes


Copy selection(Ctrl+C):Copythe selected shapes to the clipboard





Cut selection(Ctrl+X):Copythe selected shapes to the clipboard andremovethe shapes





Paste(Ctrl+V): Create the copied shape currently in the clipboard, at thecursor location





Paste in place(Ctrl+Shift+V): Create the copied shape currently in the clipboard, at thecopied shape location





Delete selection(Del):Removethe selected shapes



+++

+++Arranging shapes


Shapes are arranged in astack, which sets theorderof the shapes in the canvas – i.e. which is on top of which. New shapes are createdon topof the canvas by default, and the following controls let you change this arrangement:





Bring to front(Home):raisesthe selected shapes to thetopof the shapes stack





Bring forward(PgUp):raisesthe selected shapes up byone levelin the shapes stack





Send backward(PgDown):lowersthe selected shapes down byone levelin the shapes stack





Send to back(End):lowersthe selected shapes to thebottomof the shapes stack



+++

+++Send to new SVG image


You can use shapes in the current image to create anewSVG resourcein the currentSBS package. To that regard, the following actions are available:



[SVG resource](../vector-graphics-svg-resource.md)

[SBS package](../../../getting-started/overview/overview.md)



Copy selection to new SVG: Creates a new SVG resource, and copies the selected shapesin placein this new image.





Cut selection to new SVG: Creates a new SVG resource, copies the selected shapesin placein this new image, andremovesthem from thecurrent image.



+++
