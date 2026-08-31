---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/uber-emboss.html"
breadcrumb-title: ""
description: Use the Uber Emboss node to create advanced emboss effects with customizable depth, angle, and lighting controls.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Uber Emboss
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Uber Emboss
user-guide-description: ""
user-guide-title: ""
---

# Uber Emboss

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](uber-emboss.resources/uber-emboss-01.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Advanced, feature-rich version of [Emboss](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/emboss/emboss.md). Performs an elaborate 2D, fake lighting effect based on a Heightmap.

Useful when creating baked-in lighting for certain texturing styles when a lot of control is needed.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Color</b> <i>Color Input</i> | Base image to modify. |
| <b>Height</b> <i>Grayscale Input</i> | Heightmap used as driver for the effect. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Ambient Color</b> <i>(Color value)</i> | Color used in shadowed areas. |
| <b>Diffuse Color</b> <i>(Color value)</i> | Color used in lit areas. |
| <b>Specular Color</b> <i>(Color value)</i> | Color used for specular reflections |
| <b>Light Intensity</b> <i>0.0 - 1.0</i> | Intensity of the (faked) light. |
| <b>Light Angle</b> <i>0.0 - 1.0</i> | Incidence angle of the (faked) light |
| <b>Specular Intensity</b> <i>0.0 - 1.0</i> | Intensity of the specular reflections. |
| <b>Specular Glossiness</b> <i>0.0 - 1.0</i> | Size of the specular highlight. |
| <b>Diffuse Roughness</b> <i>0.0 - 1.0</i> | Roughness used in calculating the diffuse lighting. |
| <b>Shadows Opacity</b> <i>0.0 - 1.0</i> | Blending opacity of the shadowed areas. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="uber-emboss.resources/uber-emboss-02.png" />
        </td>
    </tr>
</table>
