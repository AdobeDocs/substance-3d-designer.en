---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/shape-extrude.html"
breadcrumb-title: ""
description: Use the Shape Extrude node to extrude shapes and create 3D-like depth effects in Substance 3D Designer textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape Extrude
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Shape Extrude
user-guide-description: ""
user-guide-title: ""
---


# Shape Extrude

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shape-extrude.png){width="128px"}

## Shape Extrude

**In:** *Texture Generators**/Patterns*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

An advanced node that allows 2d, binary "shape" inputs to be rendered to 3D-rotated heightmaps. Works similar like an extrude in a 3D package where a shape is extruded along it's axis, creating a volume. In combination with the Profile Gradient Mask, Revolution/Lathe-type bodies can be created as well. Very useful for creating complex artifcial shapes for heightmaps.

## Parameters

### Inputs

* **Extrude Shape Input**: *Grayscale Input*If Extrude Shape is set to Custom, you plug in your own (preferably) Binary shape mask here.
* **Profile Gradient**: *Grayscale Input  
  If Profile Type is set to Vertical Gradient, can be used to define scale of the shape along the axis, for Revolution bodies.*
* **Profile Mask**: *Grayscale Input*   
  Mask slot used for hiding or showing the Extruded shape along it's axis. Can be used to break continuity of the shape along its axis. Only interpreted as Binary: grayscale put values are rounded to 0 or 1.

### Parameters

* **Extrude Height**: *0.0 -* 1.0  
  Amount to extrude shape by upwards from center.
* **Extrude Depth**: *0.0 - 1.0*Amount to extrude shape by downwatds from center.
* **Extrude Shape**: *Cube, Cylinder, Custom Input*Use either built-in shapes or input your own Custom shape externally.
* **Extrude Shape Size**: *0.0 - 1.0*Only used with Built-In Cube and Cylinder, determines base shape size, can be scaled non-uniform.
* **Scale**: *0.0 - 1.0*  
  Set the global scale for the effect. With Built-In Shapes this is a uniform base shape scale, and does not affect Height or Depth.  
  With Custom Input this scales the entire final result in a uniform way.
* **Profile Type**: *Straight, Vertical Gradient, Mask*Main control to determine behaviour of effect and use of optional extra input maps.  
  Straight is standard Extrusion behaviour, Vertical Gradient allows custom scale values along entire axis, Mask allows hiding sections along axis by mask.
* **Bevel Height**: *0.0 - 1.0*Set how far the bevel reaches along extrusion axis.
* **Bevel Intensity**: *0.0 - 1.0*Set how much the bevel retracts from original shape.
* **Bevel Curve**: *-1.0 - 1.0*Set convex or concave curve of Bevel effect. A value of 0 means straight, no curve.
* **Mirror Bevel**: *False/True*Toggle to apply Bevel on top as well as bottom of shape.
* **Downscale Mulitplier**: *0 - 2*Built-in easy downscaling control. Can be used to quickly add Anti-Aliasing; make sure to increase node resolution as well.
* **Position**:   
  Main control for rotating result in 3D space. Correlates with interavtice Gizmo in the 2D view.
* **Output Range**: *&#91;0, 1&#93;, &#91;-1, 1&#93;*Set output min and max values. If range is set to &#91;-1,1&#93;, negative values are presented as black.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="shape-extrude-1.png" width="256px"/></div> |
| --- |
|  |

</td>
</tr>
</table>
