---
title: "Color (Blend Node)"
description: "Use the Color blend node to blend textures using color mode for preserving luminance while changing hue and saturation."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Color (Blend Node)
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blending/color-blend-node.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - blending
  - color
  - creating-color-palettes
---




# Color (Blend Node)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](difference.png){width="128px"}

## Color

**In:** *Filters/Blending*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a Color blend mode, which preserves the luminance of the Background, while adopting the hue and chrominance of the Foreground.

## Parameters

### Inputs

* **Foreground**: *Color Input*
* **Background**: *Color Input*
* **Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Opacity**: *0.0 - 1.0*  
  Blending Opacity between Foreground and Background.
* **Alpha Blending**: *False/True*  
  Toggles blending of the Foreground and Background alpha channels. If set to False, the alpha channel of the foreground is ignored.

## Example Images

</td>
</tr>
</table>
