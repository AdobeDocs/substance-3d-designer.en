---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/plane-light.html"
breadcrumb-title: ""
description: Use the Plane Light node to add planar light sources to HDRI environments for directional lighting control.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Plane Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Plane Light
user-guide-description: ""
user-guide-title: ""
---

# Plane Light

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](plane-light.resources/plane-light-01.png){width="200px"}

<b>In:</b> 3D View &gt; HDRI Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a spherically projected plane shape. The plane can be placed and oriented in 3d using the input parameters.

It differs from the simpler [Shape Light](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/3d-view-library/hdri-tools/shape-light/shape-light.md) in that it has more advanced placement options outside of simpler Distance from origin projection, and more patterns and masks can be applied, similar to [Line Light](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/3d-view-library/hdri-tools/line-light/line-light.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Background Image Input</b> <i>Color Input</i> | Optional background onto which to compose the generated light. |
| <b>Shape Image Input</b> <i>Color Input</i> | Optional image to map onto Line light. Only used when Shape Color Mode is set to Image Input. |
| <b>Pattern Image Input</b> <i>Grayscale Input</i> | Custom pattern image, used when the "Pattern" parameter is set to "Image Input". |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Position Mode</b> <i>Ground / Ceiling, Distance from Origin, World Positions</i> | Select from three different placement modes. Ground/Ceiling and Distance from Origin support manipulation in the 2D view, World positions can only be changed through properties, but does support more exact placement. |
| <b>Show Ground Grid</b> <i>False/True</i> | Helper function to enable a debug ground grid to be drawn. Helps estimate position of lines in space. |
| <b>Position Coordinates</b> |  |
| <b>Up Vector</b> <i>Z Up, Y Up</i> | Only with World Position mode, determine orientation of coordinate system. |
| <b>Plane UV Position</b> | Only with Ground / Ceiling and Distance from Origin. Sets plane position in UV space. |
| <b>Plane World Position</b> <i>-2.0 - 2.0</i> | Only with World Positions mode. Sets plane position world space. No 2D view interaction supported. |
| <b>Plane Absolute Height</b> <i>0.0 - 1.0</i> | Only with Ground / Ceiling Position Mode, sets absolute height from ceiling. Use Show Ground Grid to estimate position better. |
| <b>Distance from Origin</b> <i>0.0 - 1.0</i> | Only with Distance from Origin Position Mode. Sets distance from panorama center for both points. |
| <b>Shape Color Mode</b> <i>RGB, Temperature (Kelvin), Image Input</i> | Choose what method to use to set shape color. Image Input enables use of the second input slot. |
| <b>Color</b> <i>(Color value)</i> | Only with Shape Color Mode set to RGB. Picks color for shape. |
| <b>Temperature</b> <i>800.0 - 20000.0</i> | Only with Shape Color Mode set to Temperature. Sets Kelvin value for shape color. |
| <b>Shape Image UV Mode</b> <i>Stretch, Stretch Middle only, Repeat + Spacing</i> | Only with Shape Color Mode set to Image Input. Sets how image is applied to the line shape, determines UV repetition behaviour. |
| <b>Shape Image Repeat Spacing</b> <i>0.0 - 1.0</i> | Only with Shape Color Mode set to Image Input and with UV Mode set to Repeat + Spacing. Sets amount of spacing when image repeats along line. |
| <b>Shape Image Gamma</b> <i>sRGB, Linear</i> | Only with Shape Color Mode set to Image Input. Determine how to interpret Shape Image Input. |
| <b>Exposure (EV)</b> <i>0.0 - 10.0</i> | Set exposure value for generated shape, Ideally matched to background image exposure value. |
| <b>Plane Scale</b> <i>0.0 - 1.0</i> | Set uniform scale of the Plane shape. |
| <b>Plane Size</b> <i>0.0 - 1.0</i> | Set non-uniform size of the Plane shape. |
| <b>Plane Rotation</b> <i>0.0 - 1.0</i> | Rotate Plane along its central axis. |
| <b>Pattern</b> <i>Smooth Square, Sharp Square, Cone, Hemisphere, Image Input</i> | Select what pattern shape to use. |
| <b>Pattern Hardness</b> <i>0.0 - 1.0</i> | Set hardness/contrast for pattern. |
| <b>Pattern UV Mode</b> <i>Stretch, Stretch Middle only</i> | Set how to use secondary pattern mask, applied on top of Shape Image. |
| <b>Enable Ground Clipping</b> <i>False/True</i> | Enable if Plane can be clipped by a ground plane, or is still shown when going below it. Use Show Ground Grid to better estimate this. |
| <b>Ground Height</b> <i>-2.0 - 0.0</i> | Adjust ground height for clipping. |
| <b>Enable Backgound Input</b> <i>False/True</i> | Toggles use of optional background image. Composites generated light on top of background. |
| <b>Background Color</b> <i>(Color value)</i> | If Background Input is not used, set a solid color background value here. |
| <b>Background Gamma</b> <i>sRGB, Linear</i> | If Background Input is used, set how to interpret Background input. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="plane-light.resources/plane-light-02.gif" />
        </td>
    </tr>
</table>
