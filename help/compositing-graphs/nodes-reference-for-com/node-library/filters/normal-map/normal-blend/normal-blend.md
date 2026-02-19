---
title: "Normal Blend"
description: "Use the Normal Blend node to blend normal maps together for creating smooth transitions between surface details."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Blend
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-blend.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - intermediate
helpx_learn_topic:
  - blending
  - normal-maps
  - channels
---




# Normal Blend

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](normal-blend.png){width="128px"}

## Normal Blend

**In:** *Filters/Normal Map*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Normal Blend allows you to blend two Normalmaps together with an optional mask, while making sure all values stay normalised. It doesn't differ much from an [atomic Blend Node](../../../../atomic-nodes/blend/blend.md), but has added internal calculations for Normalmaps.

Normal Blend is not intended for combining (overlaying) Normalmaps, where the top map adds detail to the bottom map. For that, use [Normal Combine](../normal-combine/normal-combine.md) instead.

## Parameters

### Inputs

* **NormalFG**: *Color Input*   
  Foreground/Top Normalmap.
* **NormalBG**: *Color Input*   
  Background/Bottom Normalmap.
* **Mask**: *Grayscale Input*   
  Mask slot used for masking the node's effects. Can be toggled with the "Use Mask" parameter.

### Parameters

* **Opacity**: *0.0 - 1.0*  
  Blending Opacity between Foreground and Background
* **Use Mask**: *False/True*  
  Toggles the use of the Mask map on or off.

## Example Images

![](normalblend-ex.gif)

*(.gif format introduces dithering in example, in-application results are smooth)*

</td>
</tr>
</table>
