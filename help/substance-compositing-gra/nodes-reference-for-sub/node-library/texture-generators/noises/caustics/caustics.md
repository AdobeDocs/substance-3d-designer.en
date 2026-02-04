---
title: "Caustics"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Caustics"
---

# Caustics

<table>
<tr style="border: 0;">
<td width="41.60%" style="border: 0;" valign="top">

![](rt-caustics-grayscale.png){width="128px"}

**In:** *Texture Generators**/Noises*

**Complex**

</td>
<td width="58.30%" style="border: 0;" valign="top">

## Description

Generates projected caustics based on a height map and a light direction.Comes in both Grayscale and color versions, differences are subtle but the color version adds color dispersioneffects. Light is cast from a single point, no Environment map is used.

</td>
</tr>
</table>

## Parameters

* **Output Color Space**: *Raw, sRGB*  
  Set output color space.
* **Photon Grid Size**: *Auto, 512, 1024, 2048, 4096*  
  Sets quality by adjusting grid size, but defaults to matching input. Can be used to speed up calculation.
* **Surface Height Scale**: *0.0 - 1.0*  
  Multiplier to determine how the height is interpreted.
* **Surface Height Position**: *0.0 - 1.0*  
  Set distance of refracting surface to projection.
* **Surface IOR**: *1.0 - 2.0*  
  Set refraction index, in the color version this adds more color dispersion.
* **Photon Size**: *1.0 - 50.0*  
  Photon size affects crispness of the effect.
* **Dispersion**: *0.0 - 0.01 (Color version only)*  
  Affect just the color dispersion. Not visible when IOR is low.
* **Jittering**: *0.0 - 1.0*  
  Add irregular jittering to the cast photon particles.
* **Light Position**:   
  Moves the light position. Also done through a gizmo in the 2D view.
* **Background Color**: *(Color value) (Color version only)*  
  Change the background color. Limited to black in the grayscale version.
* **Non Square Expansion**: *False/True*  
  Enable compensation of squash and stretch with non-square ratios.

## Example Images

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dx_table_row-r0-column-c0_image" src="rt-caustics-grayscale-1.png" width="300px"/></div> |
| --- |
|  |
