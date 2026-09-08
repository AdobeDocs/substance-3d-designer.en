---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/ambient-occlusion-hbao-filter-node.html"
breadcrumb-title: ""
description: Use the Ambient Occlusion HBAO filter node to generate ambient occlusion maps using horizon-based algorithms for realistic shading.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Ambient Occlusion (HBAO) (Filter Node)
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Ambient Occlusion (HBAO) (Filter Node)
user-guide-description: ""
user-guide-title: ""
---

# Ambient Occlusion (HBAO) (Filter Node)

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/hbao.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Takes a Heightmap as input and generates an Ambient Occlusion map from that. It uses Horizon-Based Ambient Occlusion, an algorithm originally intended for screen-space realtime AO-generation. Very useful for creating procedural AO maps from procedural Heightmaps.

For an alternative, more advanced but slower version of AO, see [Ambient Occlusion (RTAO)](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/ambient-occlusion-rtao/ambient-occlusion-rtao.md)

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Use World Units</b> <i>False/True</i> | Toggles use of world or sceen-space units. Enables extra parameters that allow for more precise control. |
| <b>Height Depth</b> <i>0.0 - 1.0</i> | Only used when World Units is set to False. Controls global scaling. |
| <b>Surface Size</b> <i>0.0 - 1000.0</i> | Only used when World Units is set to True. Controls global scaling. |
| <b>Height Scale (cm)</b> <i>0.0 - 1000.0</i> | Only used when World Units is set to True. Controls global scaling. |
| <b>Radius</b> <i>0.0 - 1.0</i> | Controls the spread of the AO. |
| <b>Quality</b> <i>4 samples, 8 samples, 16 samples</i> | Sets Quality level by determining amount of samples used for calculation. |
| <b>GPU Optimization</b> <i>False/True</i> | Enables internal GPU optimisation, speeds up processing. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/image2021-6-18-11-11-11-1.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/image2021-6-18-11-11-22.png" />
        </td>
    </tr>
</table>
