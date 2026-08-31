---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/sphere-light.html"
breadcrumb-title: ""
description: Use the Sphere Light node to add spherical light sources to HDRI environments for enhanced lighting control.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Sphere Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Sphere Light
user-guide-description: ""
user-guide-title: ""
---

# Sphere Light

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](sphere-light.resources/sphere-light-01.png){width="200px"}

<b>In:</b> 3D View &gt; HDRI Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a spherically projected sphere shape. The sphere transformation is driven by a transformation gizmo.

The Sphere Light is quite versatile and has options that allow it to no only generate simple round lights, but also planets or other celestial bodies. If you have no need for the more advanced lighting and rotation options, take a look at [Shape Light](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/3d-view-library/hdri-tools/shape-light/shape-light.md) instead.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Background Image Input</b> <i>Color Input</i> | Optional background onto which to compose the generated light. |
| <b>Shape Image Input</b> <i>Color Input</i> | Optional image to map onto Sphere light. Only used when Shape Color Mode is set to Image Input. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Position Mode</b> <i>Distance from Origin, World Position</i> | Choose between two modes of placement. Distance from Origin is similar to polar coordinates, the sphere is set relative to the center of the panorama, world position works like standard 3D coordinates. |
| <b>Position Coordinates</b> |  |
| <b>Up Vector</b> <i>Z Up, Y Up</i> | Only with World Position mode, determine orientation of coordinate system. |
| <b>Sphere World Position</b> <i>-2.0 - 2.0</i> | Only with World Position mode, sets sphere position in world space. |
| <b>Position</b> | Only with Distance from Origin mode. Sets position relative to center. Can be manipulated in 2D View. |
| <b>Distance from Origin</b> <i>0.0 - 20.0</i> | Only with Distance from Origin mode. Sets distance to origin, affects visible size of the sphere. |
| <b>Shape Color Mode</b> <i>RGB, Temperature (Kelvin), Image Input</i> | Choose what method to use to set shape color. Image Input enables use of the second input slot. |
| <b>Color</b> <i>(Color value)</i> | Only with Shape Color Mode set to RGB. Picks color for shape. |
| <b>Shape Temperature</b> <i>800.0 - 20000.0</i> | Only with Shape Color Mode set to Temperature. Sets Kelvin value for shape color. |
| <b>Sphere Image Input Gamma</b> <i>sRGB, Linear</i> | Only with Shape Color Mode set to Image Input. Determine how to interpret Shape Image Input. |
| <b>Sphere Rotation</b> <i>0.0 - 1.0</i> | Only with Shape Color Mode set to Image Input. Spins sphere around its centre to orient mapped image. |
| <b>Exposure (EV)</b> <i>0.0 - 10.0</i> | Set exposure value for generated shape, Ideally matched to background image exposure value. |
| <b>Sphere Radius</b> <i>0.0 - 1.0</i> | Sets radius/size of the sphere. |
| <b>Sphere Hardness</b> <i>0.0 - 1.0</i> | Sets the hardness/falloff of the sphere. |
| <b>Shading</b> <i>None, Limb Darkening, Shading Light</i> | Set if any shading should be applied to the sphere. Allows sphere not to appear as solid, unlit object. Limb darkening means a slight darkening appears at edges, Shading Light means the sphere is lit by an optional Shading Light. |
| <b>Shading Light World Position</b> <i>-1.0 - 1.0</i> | If Shading is set to Shading Light, the position of the light onto the sphere is controlled here. |
| <b>Penombra Transparency</b> <i>0.0 - 1.0</i> | If Shading is set to Shading Light, controls the falloff of the shading. |
| <b>Enable Backgound Input</b> <i>False/True</i> | Toggles use of optional background image. Composites generated light on top of background. |
| <b>Background Color</b> <i>(Color value)</i> | If Background Input is not used, set a solid color background value here. |
| <b>Background Gamma</b> <i>sRGB, Linear</i> | If Background Input is used, set how to interpret Background input. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="sphere-light.resources/sphere-light-02.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="sphere-light.resources/sphere-light-03.png" />
        </td>
    </tr>
</table>
