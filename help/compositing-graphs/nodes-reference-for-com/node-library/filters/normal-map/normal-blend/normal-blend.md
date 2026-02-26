---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-blend.html"
breadcrumb-title: ""
description: Use the Normal Blend node to blend normal maps together for creating smooth transitions between surface details.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Blend
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Normal Blend
user-guide-description: ""
user-guide-title: ""
---

# Normal Blend

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/normal-blend.png){width="128px"}

## Normal Blend

**In:** *Filters/Normal Map*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Normal Blend allows you to blend two Normalmaps together with an optional mask, while making sure all values stay normalised. It doesn't differ much from an [atomic Blend Node](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/blend/blend.md), but has added internal calculations for Normalmaps.

Normal Blend is not intended for combining (overlaying) Normalmaps, where the top map adds detail to the bottom map. For that, use [Normal Combine](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/normal-map/normal-combine/normal-combine.md) instead.

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

![](../../../../../../assets/normalblend-ex.gif)

*(.gif format introduces dithering in example, in-application results are smooth)*

</td>
</tr>
</table>
