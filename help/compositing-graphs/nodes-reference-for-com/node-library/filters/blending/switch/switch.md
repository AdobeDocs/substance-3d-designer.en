---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blending/switch.html"
breadcrumb-title: ""
description: Use the Switch node to switch between two input textures based on a mask for conditional texture selection.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Switch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Switch
user-guide-description: ""
user-guide-title: ""
---

# Switch

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](switch.resources/switch-1.png){width="128px"}

![](switch.resources/switch-grayscale.png){width="128px"}

<b>In:</b> Filters &gt; Blending

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

A simple 2-position switch node. Returns either Input 1 or Input 2 based on the Switch parameter setting. Result is unmodified. See [Multi Switch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blending/multi-switch/multi-switch.md) for a more advanced version.

Very useful for exposing a boolean (True/False) choice in a graph, where you only need a single button and not a complex drop-down list for a whole selection of options.

Important: make sure to use the appropriate version for your input! Use "Switch" for Color inputs, "Switch Grayscale" for Grayscale inputs.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input 1 (True)</b> <i>Color or Grayscale Input</i> |  |
| <b>Input 2 (False)</b> <i>Color or Grayscale Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Switch</b> <i>False/True</i> | Switches between Input 1 (True) and 2 (False). |
