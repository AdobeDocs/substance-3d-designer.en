---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/normal-map/bent-normal.html"
breadcrumb-title: ""
description: Use the Bent Normal node to generate bent normal maps that account for ambient occlusion and indirect lighting.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Normal Map > Bent Normal
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Bent Normal
user-guide-description: ""
user-guide-title: ""
---

# Bent Normal

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Bent Normal node icon](bent-normal.resources/rt-bent-normal.png "Bent Normal node icon")

<b>In:</b> Filters &gt; Normal Map

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a Bent Normal Map based on a height map input. A Bent Normal map is a special version of [Normal](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md) and [Ambient Occlusion (RTAO)](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/ambient-occlusion-rtao/ambient-occlusion-rtao.md), generating a normal map with embedded ambient occlusion.  
This can be used in realtime engines to have Ambient Occlusion baked into the normalmap, for instance for more accurate occlusion reflections on metals.

This node should not be used in combination with the CPU (SSE) engine due to computation time.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Use Physical Size</b> <i>Boolean</i> | Toggle to use Physical Size settings to determine the height scale. |
| <b>Physical Size</b> <i>Float3</i> | (Available when <b>Use Physical Size</b> is set to <i>True</i>) Adjusts the height scale based on the real physical size of the surface. |
| <b>Samples</b> <i>Integer</i> | Number of rays used to compute the bent normal.<br>A higher provides a smoother and more precise result at the cost of performance. |
| <b>Height Scale</b> <i>Float</i> | (Available when Use Physical Size is set to False) Multiplier for the intensity of the height map input. |
| <b>Distribution</b> <i>Integer</i> | Sets the distribution method. Affects falloff towards shadowed areas. |
| <b>Maximum Distance</b> <i>Float</i> | Sets the maximum distance rays can travel to be occluded. |
| <b>Spread Angle</b> <i>Float</i> | Sets the spreading angle for the rays to be shot at. A value of 1 is a full hemisphere. |
| <b>Normal Format</b> <i>Integer</i> | Inverts the output's green channel. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="bent-normal.resources/bent-normal-ex-1.jpg" />
        </td>
    </tr>
</table>
