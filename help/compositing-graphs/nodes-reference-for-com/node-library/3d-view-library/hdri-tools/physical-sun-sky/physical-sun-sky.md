---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/physical-sun-sky.html"
breadcrumb-title: ""
description: Use the Physical SunSky node to generate physically accurate sun and sky lighting environments for realistic material preview.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Physical SunSky
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Physical SunSky
user-guide-description: ""
user-guide-title: ""
---

# Physical Sun/Sky

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](physical-sun-sky.resources/panorama-physical-sun-sky.png){width="200px"}

<b>In:</b> 3D View &gt; HDRI Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Physical Sun and Sky implementation based on Hosek-Wikie skylight model. Provides an excellent base for an artifical HDRI.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Sun Position</b> | range = &#91;0,1&#93;x&#91;0,1&#93; (longitude-latitude angles) |
| <b>Turbidity</b> <i>1.0 - 10.0</i> | Turbidity ranges from 1 to 10 |
| <b>Albedo</b> <i>0.0 - 1.0</i> | Albedo ranges from 0 to 1. |
| <b>Ground Color</b> <i>(Color value)</i> | Color of the ground plane. |
| <b>Exposure (EV)</b> <i>-1.0 - 4.0</i> | Exposure value of resulting output. |
| <b>Sun Size</b> <i>0.0 - 4.0</i> | Scale of the Sun, any value different than 1 is non physically correct. Value has subtle effects! |
| <b>Sun Intensity</b> <i>0.0 - 1.0</i> | Intensity of sun disc. Sun disc is fairly small so effect is not immediately visible. |
| <b>Sky Intensity</b> <i>0.0 - 1.0</i> | Intensity of the sky. Also affects flaring of sun in the sky, not the disc itself. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="physical-sun-sky.resources/sky-ex.gif" />
        </td>
    </tr>
</table>
