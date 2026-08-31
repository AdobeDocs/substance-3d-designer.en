---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/utilities-mesh-based-generators/mesh-data-combiner.html"
breadcrumb-title: ""
description: Use the Mesh Data Combiner node to combine multiple mesh data inputs for advanced mesh-based texture generation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Utilities (Mesh Based Generators) > Mesh Data Combiner
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Mesh Data Combiner
user-guide-description: ""
user-guide-title: ""
---

# Mesh Data Combiner

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](mesh-data-combiner.resources/mesh-data-combiner-01.png){width="128px"}

<b>In:</b> Mesh Based Generators &gt; Utilities

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is a very simple node that "packs" baked mesh data into a single group, for use with "Compact Material Mode".

This node is mostly a helper that makes it easier to work with lots of baked inputs on certain nodes in the gallery, like [Material Mesh Data Blender](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/mesh-based-generators/utilities-mesh-based-gen/material-mesh-data-ble/material-mesh-data-blender.md). It allows you to avoid manually connecting everything.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

Toggle which map inputs to enable and output into the packed result.

|  |  |
|:---|:---|
| <b>Ambient Occlusion</b> <i>False/True</i> |  |
| <b>UV Masks</b> <i>False/True</i> |  |
| <b>Curvature</b> <i>False/True</i> |  |
| <b>Height</b> <i>False/True</i> |  |
| <b>Position (Grayscale)</b> <i>False/True</i> |  |
| <b>Thickness</b> <i>False/True</i> |  |
| <b>Normal</b> <i>False/True</i> |  |
| <b>Position (RGB)</b> <i>False/True</i> |  |
| <b>Color ID</b> <i>False/True</i> |  |
| <b>World Space Direction</b> <i>False/True</i> |  |
| <b>World Space Normal</b> <i>False/True</i> |  |
