---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/release-notes/version-13-1.html"
breadcrumb-title: ""
description: Review release notes for Substance 3D Designer version 13.1 to learn about node graph improvements and AxF export support.
helpx_creative_field: ""
helpx_description: Designer > Release Notes > Version 13.1
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Version 13.1
user-guide-description: ""
user-guide-title: ""
---


# Version 13.1

<b>Substance 3D Designer 13.1</b> adds many quality-of-life improvements to the node graph, mainly regarding frames, to enhance the material creation experience. There is also the addition of AxF export which enables an interoperability workflow for users working with the AxF format. 

*Release date: December 12, 2023*

![Substance 3D Designer 13.1 banner](24-library-hero-1920x620.png "Substance 3D Designer 13.1 banner")

## Frames improvements

Frames are a mandatory tool to keep you graph well organized and readable. That is the reason we decided to polish them in this new version.

### Auto-expand

As the graph grows, the frames' content may need to be rearranged. Nodes may shift to make room for additions or content may need to be spaced out more to promote readability. To facilitate these adjustments, it is now possible to automatically expand a frame when moving included objects: hold <b>Shift</b> at any point while moving an object to have the frame borders automatically adjust to keep that object within their bounds.

![autoexpand](autoexpand.gif)

### Fit size to content

As you make adjustments in your graph, a frame may not be gracefully adjusted to its content anymore. This new command allows you to automatically adjust the position and size of the frame so it adjusts to the span of its content, with a padding of one medium grid cell. If the frame has a description, it is adjusted to make use of any empty space next to the description, if possible.

![fitsize](fitsize.gif)

### Enhanced descriptions

Thanks to HTML code, you can now have formatted text in a frame's description. This applies to comments as well.

![richtext](description-3.png)

### <b>...And much more!</b>

A lot of things have been rethought, like belonging rules to be more tolerant, interaction zones to easily resize frames, snapping rules to not misaligned your nodes on the grid, and the visual aspect to bring a bit of freshness. Feel free to visit the frames' [documentation](../../help/interface/the-graph-view/graph-items/frame/frame.md) to learn more.

## Quality of life improvements

* <b>Node menu improvements: </b>in order to save time while searching for the node you need, we improved a bit the node menu. Search is now more forgiving and will give you a result even if there is no perfect match. Moreover, you can now use the up arrow to directly access to the last element in the list.
* <b>Node placement: </b>if you like to have a perfect layout for your graph, these two small changes will please you! When you copy/paste nodes from one graph to one other, pasted nodes are now aligned to the main grid. And when you add a node on a long link, this one will now be placed at the middle of the visible part of the link, in order to make it visible in every situation.
* <b>2D View options: </b>if you are an intensive user of the [2D view](../../help/interface/2d-view/2d-view.md), you will save time as options like 'Show checkerboard', 'Keep view size', 'Use physical size' and 'Display tiling' are now saved, so you don't have to set them again when you create a new 2D view or even when you restart Designer.

## AxF export

<table>
<tr style="border: 0;">
<td width="25.00%" style="border: 0;" valign="top">

![AxF file icon](axf-file-icon.png "AxF file icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

AxF is a format from [X-Rite](https://www.xrite.com/axf). It provides a way to capture, store, edit, and communicate complex material characteristics using numerical data throughout the digital design workflow. In previous versions of Designer, you were able to [import AxF files](../../help/resources/axf-appearance-exchange/axf-appearance-exchange-format.md) and then improve the tiling or add procedural effects, but then, you were constrained to export changes as a new .sbsar file.

In this new release, we introduce the possibility to edit AxF materials in place, and then [export your changes](../../help/resources/axf-appearance-exchange/axf-appearance-exchange-format.md) as a new layer in the imported AxF file.

</td>
</tr>
</table>

![Export AxF](exportaxf.gif)

## API

Finally, this 13.1 version continues to improve the Python API by adding two more possibilities:

* <b>&#39;Visible if&#39; properties: </b>you can now set this property for graphs parameters, inputs and outputs.
* <b>Order of graphs Inputs/Outputs:</b> use sdsbscompgraph::reorderGraphInput and sdsbscompgraph::reorderGraphOutput to organize parameters as you need.

>[!NOTE]
>
> Designer 13.1 is the last major version based on Qt5, next major versions will be upgraded to Qt6. It may have an impact on your custom plugins.

## Release notes

### 13.1.0

*(Released December 12th, 2023)*

### Added

* &#91;Frames&#93; Auto Expand
* &#91;Frames&#93; Change rules to define when an object belongs to a frame
* &#91;Frames&#93; Disable text scaling for frames description
* &#91;Frames&#93; Fit size to content
* &#91;Frames&#93; New default, hover and selected states
* &#91;Frames&#93; Snap to Large Grid
* &#91;Frames&#93; Support HTML code for Frames description
* &#91;Frames&#93; Update interaction zones
* &#91;Frames&#93; Update visual aspect
* &#91;Graph&#93; Create the node at the middle of the visible link instead of middle of the link
* &#91;Graph&#93; Display properties of an item if it is the only one item with properties available in a selection
* &#91;Graph&#93; Remove "Scaling" option for comments in the graph
* &#91;Graph&#93; Snap nodes on the main grid when doing copy/paste
* &#91;UX&#93; Allow fuzzy search in Node menu and Library search
* &#91;UX&#93; Make the Node menu list loopN
* &#91;AxF&#93; Support AxF export
* &#91;AxF&#93; Disable AxF on Linux
* &#91;API&#93; Set the 'Visible if' property of graph parameters, inputs and outputs using the Python API
* &#91;API&#93; Set the order of graph I/O using the Python API
* &#91;Dependencies&#93; Update Boost to 1.80.0
* &#91;Dependencies&#93; Update OpenSubdiv to 3.5.x
* &#91;Dependencies&#93; Update FBX SDK to 2020.3
* &#91;Dependencies&#93; Update NGL to 1.35.0.20
* &#91;Color management&#93; Add support for OCIO ICC displays
* &#91;Levels&#93; Add a way to reset the histogram
* &#91;Python&#93; Warn users if QtForPython cannot be imported
* &#91;2D view&#93; Save the state of the view options
* &#91;3D View&#93; Add Position technique to the mesh info shader
* &#91;Export&#93; Add a 'Save settings' button to save changes to export options

### Fixes

* &#91;3D View&#93; Cannot assign a texture to an input of type texture\_2d of a MDL Material
* &#91;AxF&#93; Graph identifiers in templates list can be blank
* &#91;AxF&#93; Substance graph template field is blank by default
* &#91;Content&#93; Atlas Scatter: incorrect behavior in specific cases
* &#91;Content&#93; Flood Fill Mapper: blank output when all shapes have same Bbox size
* &#91;Content&#93; FloodFill to Position: Imprecision artefacts in some situations
* &#91;Content&#93; Incorrect 'Specular' output in 'BaseColor/Metallic/Roughness converter' node
* &#91;Content&#93; Mask to Path doesn't work in non square vertical
* &#91;Content&#93; Missing description for Input value, Input Grayscale, Input Color and Output nodes
* &#91;Content&#93; Missing description for Set and Sequence nodes
* &#91;Content&#93; Shape Splatter: Imprecision artefacts in 'Splatter data 2' output
* &#91;Engine&#93; Booleans in Value Processors always evaluate to 'False' (Apple Silicon only)
* &#91;Explorer&#93; Order of toolbar buttons is inconsistent between OS
* &#91;Frames&#93; Do not grab nodes when moving a frame with CTRL modifier
* &#91;Gradient Map&#93; reset all option should also reset the gradient widget
* &#91;GraphRender&#93; Some nodes are rendered black when tweaking in preview mode
* &#91;Graph&#93; 'Input value' preview is stuck to 'False' when tweaking default boolean value (Apple Silicon only)
* &#91;Graph&#93; Dot nodes close to Frame edge are not moved by the Frame
* &#91;Interoperability&#93; Resend icon is not updated after sending to Substance 3D Stager
* &#91;MDL&#93; Impossible to change Roughness in nodes where this param is available
* &#91;MDL&#93; Invalid connections in 'AxF to Metallic Roughness' template
* &#91;UI&#93; 'Export outputs' window can be minimised (Windows only)
* &#91;UI&#93; Images appear pixelated in About screen when using display scaling
* &#91;UI&#93; Node align tools in graph toolbar create multiple undo steps

### KNOWN ISSUES

* &#91;AxF OpenGL Shader&#93; Incorrect Ward for anisotropic distribution
* &#91;AxF OpenGL Shader&#93; Incorrect default roughness
* &#91;AxF OpenGL Shader&#93; Incorrect shading basis rotation
* &#91;AxF OpenGL Shader&#93; Incorrect ray below hemispheredetection
* &#91;AxF OpenGL Shader&#93; Incorrect contribution detection
* &#91;AxF&#93; 'Specular Color' map values are incorrect when exported
* &#91;AxF&#93; Preview and textures are not displayed correctly in 'Import AxF' dialog
* &#91;AxF&#93; Property "cc no refraction" is not injected correctly in AxF to AxF template
