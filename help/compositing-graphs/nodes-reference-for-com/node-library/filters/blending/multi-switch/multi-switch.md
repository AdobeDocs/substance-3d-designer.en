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
<td width="33.33%" style="border: 0;" valign="top">

![](multi-switch.resources/multi-switch-01.png){width="128px"}

![](multi-switch.resources/multi-switch-02.png){width="128px"}

<b>In:</b> Filters &gt; Blending

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Acts as a switch-box, only passing through the input defined by the 'Input Selection' parameter. So if two Inputs are connected, only one of those will be returned (unmodified), depending on the user's choice.

Very useful for adding many different options in a graph. Combined with [exposing ](../../../../../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md)(preferably as a Drop Down List), a lot of customisation is possible.

Important: make sure to use the appropriate version for your input! Use "Multi Switch" for Color inputs, "Multi Switch Grayscale" for Grayscale inputs.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input 1-20</b> <i>Color Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Input Number</b> <i>2 - 20</i> | Amount of inputs to expose. Important: does not remove connections when the number is reduced! |
| <b>Input Selection</b> <i>1 - 20</i> | Which input to return as the result. |
