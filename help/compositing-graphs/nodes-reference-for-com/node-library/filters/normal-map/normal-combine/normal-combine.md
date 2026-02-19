---
title: "Normal Combine"
description: "Use the Normal Combine node to combine multiple normal maps for layering surface details and details."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Normal Combine
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/normal-combine.html"
helpx_creative_field:
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - normal-maps
  - blending
  - compositing
---




# Normal Combine

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](normal-combine.png){width="128px"}

<b>In:</b> Filters &gt; Normal map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Normal Combine combines the details of two normal maps in a mathematically correct way.

It is similar to the well-known "Overlay" method from other 2D image editing software, but does work slightly different internally (three options).

</td>
</tr>
</table>

This is the best and most correct way to add 2D-generated normal map details to a baked map.

If you want to blend two normal maps without combining their details (using a mask, for example), you should use [Normal Blend](../normal-blend/normal-blend.md).

## Input connectors

<b>Normal 2</b> *Color*Description

<b>Normal 1</b> *Color*Description

## Parameters

<b>Technique</b> *Integer*Sets which internal blending technique to use, trading in speed for quality.  
*- Whiteout (Low quality)  
* Channel mixer (High quality)  
* Detail oriented (High quality)*

## Examples
