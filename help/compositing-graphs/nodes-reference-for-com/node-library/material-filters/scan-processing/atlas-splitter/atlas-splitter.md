---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/atlas-splitter.html"
breadcrumb-title: ""
description: Use the Atlas Splitter node to split texture atlases into individual textures for processing scanned materials.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > Atlas Splitter
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Atlas Splitter
user-guide-description: ""
user-guide-title: ""
---


# Atlas Splitter

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Node icon](atlas-splitter.png "Node icon")

<b>In:</b> Material Filters/Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Takes an atlas image input and splits out all separate elements as *individual materials*.

It can also be used to reorganize and move all elements into a grid.

The node works as an advanced application of the [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md) node.

</td>
</tr>
</table>

## Parameters

<b>Grid View</b> *Boolean*  
Displays all the detected shapes in a grid.

<b>Grid Opacity</b> *Float*  
Sets the Opacity of the Grid lines when Grid View is True. Debug option

<b>Grid Selection Opacity</b> *Float*  
Sets the Opacity of the Grid Selection highlight if Grid View is True. Debug option

<b>Auto Scale</b> *Boolean*  
Automatically scale the shapes to fit in the grid cell.

<b>Auto Crop</b> *Boolean*  
Automaticaly crops the output size according to the largest shape to minimize empty space.

<b>Shape Selection</b> *Integer*  
In Grid view sets which cell is highlighted, outside of Grid View this sets which cell is returned.

<b>Ignore Shape Smaller Than</b> *Float*  
Ignores shapes whose diagonal size is lower than the specified value.

<b>Auto Rotation</b> *Boolean*  
Automatically rotates the shape according to its bounding box size ratio.

<b>Rotation</b> *Float*  
Global shape Rotation Angle

<b>Input Normal Format</b> *Integer*  
Set the format of the input normal. Setting the wrong format will lead to incorrect result.

<b>Downscale Opacity Mask</b> *Integer*  
Downscales the Opacity Mask to remove potential noise or isolated pixel. It prevents the detection of unwanted shapes and also increases performance.

<b>Dilation Width</b> *Float*  
Applies a dilation effect based on the Opacity mask on all channels except the Normal and Height.

<b>Enable Additional Inputs</b> *Boolean*  
Makes USer 1 and User 2 inputs and settings available, for any additional maps not covered.

<b>Custom Background Color</b> *Boolean*  
Allows you to choose a custom background color, instead of a dilation of the contents of that layer.

<b>Base Color Bg Color</b> *Float3*  
Custom BG color for Base Color.

<b>Normal Bg Color</b> *Float3*  
Custom BG color for Normal Map.

<b>Metallic Bg Color</b> *Float*  
Custom BG color for Metallic.

<b>Roughness Bg Color</b> *Float*  
Custom BG color for Roughness

<b>Height Bg Color</b> *Float*  
Custom BG color for Height

<b>User 1 Bg Color</b> *Float*  
Custom BG color for custom User 1 Map

<b>User 2 Bg Color</b> *Float*Custom BG color for custom User 1 Map

## Examples
