---
title: "Cracks Weathering | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Weathering > Cracks Weathering"
---

# Cracks Weathering

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](cracks-weathering.png){width="128px"}

## Cracks Weathering

**In:** *Mesh Based Generators**/Weathering*

**Complex**

</td>
<td style="border: 0;" valign="top">

## Description

This is a full-material effect that works on multiple channels at once. It adds a random crack pattern, with control over spread and depth.

Make sure to properly understand the [Link Creation Modes](../../../../../../interface/the-graph-view/link-creation-modes/link-creation-modes.md) when working with full materials.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked or generated map used for internal effects and masking.
* **Height** : *Grayscale Input*   
  Baked or generated map used for internal effects and masking.
* **Mask** : *Grayscale Input*   
  Mask slot used for masking the node's effects. Can be toggled with the "Mask" parameter.

### Parameters

* **Channels**   
  * Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.
* **Advanced**   
  * **Normal Format**: *DirectX, OpenGL*  
    Switches between different Normalmap formats (inverts the green channel).
  * **Mask**: *False/True*  
    Toggles the use of the Mask map on or off.
* **Effect**   
  * **Cracks Propagation**: *0.0 - 1.0*How far the cracks should spread. This is the main control for this effect.
  * **Cracks Depth**: *0.0 - 1.0*Depth of the crack effect. This mostly affects height and slightly affects visula thickness.
* **Blending**   
  * Controls how strongly the effect blends into each resulting channel.

## Example Images

![](cracks-ex.gif)

</td>
</tr>
</table>
