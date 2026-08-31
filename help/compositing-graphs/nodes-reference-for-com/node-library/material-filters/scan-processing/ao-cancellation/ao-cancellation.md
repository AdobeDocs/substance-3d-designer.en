---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/scan-processing/ao-cancellation.html"
breadcrumb-title: ""
description: Use the AO Cancellation node to remove ambient occlusion from scanned materials for clean texture processing.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Scan Processing > AO Cancellation
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: AO Cancellation
user-guide-description: ""
user-guide-title: ""
---

# AO Cancellation

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](ao-cancellation.resources/ao-cancellation-01.png){width="128px"}

<b>In:</b> Material Filters &gt; Scan Processing

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node attempts to remove any Ambient Occlusion lighting information from your Albedo (Base Color) map, based on a separate AO map input. It can be used to ensure your Albedo information is PBR correct and mostly devoid of (strong) lighting information.

A useful node for when you have a baked AO map from a scanned mesh, or alternatively even an AO map generated from Height or Normal info.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>AO Cancellation</b> <i>0.0 - 1.0</i> | Strength with which to remove lighting information. |
| <b>AO Saturation</b> <i>0.0 - 1.0</i> | (De)Saturation compensation for areas where lighting is removed. This can be used to return any loss of color in darker areas. |
