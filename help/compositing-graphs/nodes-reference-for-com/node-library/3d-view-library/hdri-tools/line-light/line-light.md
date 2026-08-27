---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/line-light.html"
breadcrumb-title: ""
description: Use the Line Light node to create linear light sources in HDRI environments for simulating fluorescent and strip lighting.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Line Light
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Line Light
user-guide-description: ""
user-guide-title: ""
---

# Line Light

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](line-light.resources/panorama-line-light.png){width="200px"}

<b>In:</b> 3D View &gt; HDRI Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a spherically projected line shape based on the coordinates of two points in space. Compared to [Shape Light](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/3d-view-library/hdri-tools/shape-light/shape-light.md) it has more options for orienting shapes and applying repeating patterns to the light shape.

The positioning modes for this node are slightly more complex than other HDRI Light Nodes. It is recommended to try a few different size modes to find which one works for you scenario.

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
| <b>Point 1 UV Position</b> | Only with Ground / Ceiling and Distance from Origin. Sets first point position in UV space. |
| <b>Point 2 UV Position</b> | Only with Ground / Ceiling and Distance from Origin. Sets second point position in UV space. |
| <b>Point 1 World Position</b> <i>-2.0 - 2.0</i> | Only with World Positions mode. Sets first point in world space. No 2D view interaction supported. |
| <b>Point 2 World Position</b> <i>-2.0 - 2.0</i> | Only with World Positions mode. Sets second point in world space. No 2D view interaction supported. |
| <b>Line Absolute Height</b> <i>0.0 - 1.0</i> | Only with Ground / Ceiling Position Mode, sets absolute height from ceiling. Use Show Ground Grid to estimate position better. |
| <b>Distance from Origin</b> <i>0.0 - 1.0</i> | Only with Distance from Origin Position Mode. Sets distance from panorama center for both points. |
| <b>Shape Color Mode</b> <i>RGB, Temperature (Kelvin), Image Input</i> | Choose what method to use to set shape color. Image Input enables use of the second input slot. |
| <b>Color</b> <i>(Color value)</i> | Only with Shape Color Mode set to RGB. Picks color for shape. |
| <b>Temperature</b> <i>800.0 - 20000.0</i> | Only with Shape Color Mode set to Temperature. Sets Kelvin value for shape color. |
| <b>Shape Image UV Mode</b> <i>Stretch, Stretch Middle only, Repeat + Spacing</i> | Only with Shape Color Mode set to Image Input. Sets how image is applied to the line shape, determines UV repetition behaviour. |
| <b>Shape Image Repeat Spacing</b> <i>0.0 - 1.0</i> | Only with Shape Color Mode set to Image Input and with UV Mode set to Repeat + Spacing. Sets amount of spacing when image repeats along line. |
| <b>Shape Image Gamma</b> <i>sRGB, Linear</i> | Only with Shape Color Mode set to Image Input. Determine how to interpret Shape Image Input. |
| <b>Exposure (EV)</b> <i>0.0 - 10.0</i> | Set exposure value for generated shape, Ideally matched to background image exposure value. |
| <b>Line Rotation</b> <i>0.0 - 1.0</i> | Rotates line along the axis of its length. Line is treated as flat card when rotating. |
| <b>Line Thickness</b> <i>0.0 - 1.0</i> | Sets thickness of the line card. |
| <b>Pattern</b> <i>Smooth Square, Sharp Square, Cone, Hemisphere, Image Input</i> | Select what pattern shape to use. |
| <b>Pattern Hardness</b> <i>0.0 - 1.0</i> | Set hardness/contrast of pattern. |
| <b>Pattern UV Mode</b> <i>Stretch, Stretch Middle only, Repeat + Spacing</i> | Set how to use secondary pattern mask, applied on top of Shape Image. |
| <b>Pattern Repeat Spacing</b> <i>0.0 - 1.0</i> | Only if Pattern UV Mode is set to Repeat + Spacing. Set amount of spacing between repeated patterns. |
| <b>Enable Ground Clipping</b> <i>False/True</i> | Enable clipping of line drawing. Effect is not visible when using Ground / Ceiling placement mode. |
| <b>Ground Height</b> <i>-2.0 - 0.0</i> | Sets relative height of fround plane, used for clipping. Affects drawn Ground Grid. |
| <b>Enable Backgound Input</b> <i>False/True</i> | Toggles use of optional background image. Composites generated light on top of background. |
| <b>Background Color</b> <i>(Color value)</i> | If Background Input is not used, set a solid color background value here. |
| <b>Background Gamma</b> <i>sRGB, Linear</i> | If Background Input is used, set how to interpret Background input. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="line-light.resources/line-light-ex.gif" />
        </td>
    </tr>
</table>
