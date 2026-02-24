---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blending/multi-switch.html"
breadcrumb-title: ""
description: Use the Multi Switch node to switch between multiple input textures based on a selector for conditional texture selection.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blending > Multi Switch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Multi Switch
user-guide-description: ""
user-guide-title: ""
---


# Multi Switch

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](multi-switch-greyscale.png){width="128px"}

![](multi-switch.png){width="128px"}

## Multi Switch (Grayscale)

**In:** *Filters/Blending*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Acts as a switch-box, only passing through the input defined by the 'Input Selection' parameter. So if two Inputs are connected, only one of those will be returned (unmodified), depending on the user's choice.

Very useful for adding many different options in a graph. Combined with [exposing ](../../../../../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md)(preferably as a Drop Down List), a lot of customisation is possible.

Important: make sure to use the appropriate version for your input! Use "Multi Switch" for Color inputs, "Multi Switch Grayscale" for Grayscale inputs.

## Parameters

### Inputs

* **Input 1-20**: *Color Input*

### Parameters

* **Input Number**: *2 - 20*Amount of inputs to expose. Important: does not remove connections when the number is reduced!
* **Input Selection**: *1 - 20*Which input to return as the result.

## Example Images

</td>
</tr>
</table>
