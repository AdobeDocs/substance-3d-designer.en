---
title: "Multi-Material Blend | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Multi-Material Blend"
---

# Multi-Material Blend

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](multi-material-blend.png){width="128px"}

## Multi-Material Blend

**In:** *Material Filters/Blending*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

This node combines multiple materials based on a Material ID / Color ID map, one that can be baked from a mesh. It takes up to 16 different full materials, with whatever kind of channels you enable in the Channels group.

The node is very useful when texturing full props, as it allows full parametrisation of materials while still dynamically combining them all. Perfect for texturing simple to complex props that have proper ID bakes, or even for creating fully pipelined "Template" Substances that fully cohere to team standards.

Keep in mind that when using this, Material 1, Slot 1 is always the default material and will appear anywhere no other material appears. That is why you cannot set up a color for it. If you want to play this safe, you can for example plug in a [Base Material](../../pbr-utilities/base-material/base-material.md) that is set to rough black.

## Parameters

### Inputs

* **1-16 Full material slots**Amount of slots is determined by the **Materials** dropdown.
* **Color ID**: *Color Input*   
  Baked Color ID map.

### Parameters

* **Materials**: *2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16*Sets the maximum amount of different materials to blend.
* **Channels**  
  Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.
* **Material 2-16**One group appears for every material enabled.  
  * **Color**: *(Color value)*Color to pick from the ID map that matches this material slot.
  * **Fuzziness**: *0.01 - 1.0*Bleed over into neighbouring colors.
  * **Padding**: *0.0 - 1.0*Hardness of transitions: mask contrast.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
