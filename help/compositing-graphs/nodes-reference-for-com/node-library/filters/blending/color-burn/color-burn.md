---
title: "Color Burn"
description: "Use the Color Burn blend node to darken textures by increasing contrast for creating shadow and burn effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Color Burn
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blending/color-burn.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - color
  - color-grading
  - effects
---




# Color Burn

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](color-burn.png){width="128px"}

## Color Burn

**In:** *Filters/Blending*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Performs a Color Burn blend between Foreground and Background. Mathematically the formula is 1 - (1-Background) / Foreground.

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
