---
title: "Material Adjustment Blend"
description: "Use the Material Adjustment Blend node to blend material adjustments between materials for fine-tuning composite effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Blending (Material) > Material Adjustment Blend
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/blending-material/material-adjustment-blend.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
helpx_experience_level:
  - intermediate
helpx_learn_topic:
  - materials
  - adjustments
  - channels
---




# Material Adjustment Blend

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](material-adjustment-blend.png){width="128px"}

## Material Adjustment Blend

**In:** *Material Filters/Blending*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

This node allows adjusting of any and all channels of a full material, based on a mask. It is intended for making a full material workflow easier and quicker.

It is useful for when you want to adjust a few channels of a material (such as making diffuse brighter and roughness darker) based on the same mask.

## Parameters

### Inputs

* **Color ID Mask**: *Color Input*   
  Mask slot used for masking the node's effects.
* **Greyscale Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Channels**  
  Toggles material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness.  
  This also enables and disables the appearance of the channel's relevant groups.
* **Diffuse**  
  Performs adjustment operations on the Diffuse channel, in areas defined by the mask.
* **Base Color**  
  Performs adjustment operations on the Base Color channel, in areas defined by the mask.
* **Normal**
  * **Intensity**: *0.0 - 1.0*Tones down Normal Intensity
* **Specular**  
  Performs adjustment operations on the Specular channel, in areas defined by the mask.
* **Emissive**  
  Performs adjustment operations on theEmissive channel, in areas defined by the mask.
* **Glossiness**  
  Performs adjustment operations on the Glossiness channel, in areas defined by the mask.
* **Roughness**  
  Performs adjustment operations on the Roughness channel, in areas defined by the mask.
* **Metallic**  
  Performs adjustment operations on the Metallic channel, in areas defined by the mask.
* **Specular Level**  
  Performs adjustment operations on the Specular Level channel, in areas defined by the mask.
* **Ambient Occlusion**  
  Performs adjustment operations on the Ambient Occlusion channel, in areas defined by the mask.
* **Height**  
  Performs adjustment operations on the Height channel, in areas defined by the mask.
* **Opacity**  
  Performs adjustment operations on the Opacity channel, in areas defined by the mask.
* **Color ID Mask**: *False/True*Set to use Color ID Mask instead of grayscale mask.
* **Fuzziness**: *0.01 - 1.0*If Color ID Mask is enabled, this determines the spread of the Color ID selection color.
* **Color**: *(Color value)*Sets what color to pick from the Color ID map and mask with.
* **Padding**: *0.0 - 1.0*Determines Blending contrast/transitions of the Color ID masking.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
