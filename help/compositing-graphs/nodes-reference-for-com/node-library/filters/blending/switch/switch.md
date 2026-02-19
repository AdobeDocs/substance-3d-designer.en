---
title: "Switch"
description: "Use the Switch node to switch between two input textures based on a mask for conditional texture selection."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Switch
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blending/switch.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - transitions
  - selections
  - content-aware-fill
---




# Switch

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](switch-1.png){width="128px"}

![](switch-grayscale.png){width="128px"}

## Switch (Grayscale)

**In:** *Filters/Blending*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

A simple 2-position switch node. Returns either Input 1 or Input 2 based on the Switch parameter setting. Result is unmodified. See [Multi Switch](../multi-switch/multi-switch.md) for a more advanced version.

Very useful for exposing a boolean (True/False) choice in a graph, where you only need a single button and not a complex drop-down list for a whole selection of options.

Important: make sure to use the appropriate version for your input! Use "Switch" for Color inputs, "Switch Grayscale" for Grayscale inputs.

## Parameters

### Inputs

* **Input 1 (True)**: *Color or Grayscale Input*
* **Input 2 (False)**: *Color or Grayscale Input*

### Parameters

* **Switch**: *False/True*Switches between Input 1 (True) and 2 (False).

## Example Images

</td>
</tr>
</table>
