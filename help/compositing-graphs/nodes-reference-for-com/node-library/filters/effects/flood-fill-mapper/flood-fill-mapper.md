---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/flood-fill-mapper.html"
breadcrumb-title: ""
description: Use the Flood Fill Mapper node to map values across connected regions using flood fill algorithms for texture processing.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill Mapper
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Flood Fill Mapper
user-guide-description: ""
user-guide-title: ""
---

# Flood Fill Mapper

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](flood-fill-mapper.resources/floodfill-mapper-gray.png)![](flood-fill-mapper.resources/floodfill-mapper-color.png)

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Flood Fill Mapper allows remapping of an existing Pattern or Texture onto every single cell from a [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md). It is different from other Flood Fill conversions like [Random Grayscale](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-random-gra/flood-fill-to-random-grayscale.md) or [Gradient](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill-to-gradient/flood-fill-to-gradient.md) in that it does not generate solid colors or values, but allows you to use you own input maps. It can be seen as a sort of combination of [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md) and [Tile Sampler](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-sampler/tile-sampler.md) or [Shape Mapper](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/shape-mapper/shape-mapper.md), as it provides quite a few similar controls and interfaces.

The Color version has additional controls to work with Normal Maps, where it can [compensate for tangent-space Normap Map rotations](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/normal-map/normal-vector-rotation/normal-vector-rotation.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Flood Fill Bbox</b> <i>Color Input</i> | Standard Flood Fill input, required. |
| <b>Pattern Input 1-8</b> <i>Grayscale/Color Input</i> | Custom pattern image input. |
| <b>Pattern Distribution Map</b> <i>Grayscale Input</i> | ID Map to determine which pattern goes to which cell. Can come from other Flood Fill Map such as Flood Fill to Index. |
| <b>Scale Map</b> <i>Grayscale Input</i> | Map to determine Scale per cell. |
| <b>Rotation Map</b> <i>Grayscale Input</i> | Map to determine Rotation per Cell. |
| <b>Luminance Offset Map</b> <i>Grayscale Input</i> | Map to set Luminance per Cell |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Tiling Mode</b> <i>No Tiling, H+V</i> | Set wether to use Tiling or not. Only visible if Size or Scale ar set below 1. |
| <b>Pattern</b> |  |
| <b>Pattern Input Number</b> <i>1 - 8</i> | Set amount of Custom Pattern Inputs to use. |
| <b>Pattern Distribution Mode</b> <i>Random, Shape Size, Distribution Map Input</i> | Set the method to determine what Pattern is shown in a Cell. |
| <b>Pattern Distribution Jittering</b> <i>0.0 - 1.0</i> | Allows for a slight varaition or Offset in the Pattern distribution without changing everything through teh Random Seed. |
| <b>Size</b> |  |
| <b>Size Mode</b> <i>Relative to Texture, Relative to Shape BSphere, Relative to Largest Shape, Relative to Smallest Shape, Fit Shape BBox</i> | Set how the size of the pattern in each cell is determined. |
| <b>Size</b> <i>0.0 - 1.0</i> | Allows for non-uniform scaling of the Pattern. |
| <b>Scale</b> <i>0.0 - 1.0</i> | Set the global (uniform) scale for the effect. |
| <b>Scale Map Mulitplier</b> <i>0.0 - 1.0</i> | Set influence of the optional Scale Map. |
| <b>Scale Random</b> <i>-1.0 - 1.0</i> | Set the amount of random variation within pattern scale. |
| <b>Rotation</b> |  |
| <b>Rotation</b> <i>0.0 - 1.0</i> | Set global, uniform rotation for every cell. |
| <b>Rotation Map Mulitplier</b> <i>0.0 - 1.0</i> | Set influence of the optional Rotation map. |
| <b>Rotation Random</b> <i>0.0 - 1.0</i> | Set the amount of random rotation for every cell. |
| <b>Rotation Autoscale</b> <i>False/True</i> | Set if a pattern should adjust its scale to fit within a cell when rotated. |
| <b>Position</b> |  |
| <b>Position Offset</b> <i>0.0 - 1.0</i> | Set global Position offset for every cell. |
| <b>Position Offset Alignment</b> <i>Texture, Pattern</i> | Set to either align the offset 0-point to the Pattern cell or to the texture. |
| <b>Position Offset Random</b> <i>0.0 - 1.0</i> | Set the amount of per-cell Position offset randomisation. |
| <b>Color (Only for Grayscale version)</b> |  |
| <b>Luminance Range</b> <i>0.0 - 1.0</i> | Sets the global contrast on the texture, where 0 becomes middle gray. |
| <b>Luminance Range Random</b> <i>0.0 - 1.0</i> | Sets the amount of randomisation for the Luminance Range. |
| <b>Luminance Offset</b> <i>-1.0 - 1.0</i> | Sets the offset for the Luminance, working as a brightness control. |
| <b>Luminance Offset Random</b> <i>0.0 - 1.0</i> | Sets the amount of randomisation for the Luminance Offset. |
| <b>Luminance Offset Map Mulitplier</b> <i>0.0 - 1.0</i> | Sets the influence of the optional Luminance Offset map. |
| <b>Background Color</b> <i>(Grayscale value)</i> | Sets the background color onto which textures are blended. |
| <b>Color (Only for Color version)</b> |  |
| <b>Is Normal Map</b> <i>False/True</i> | Set to interpret Pattern Input as a Normal Map. Will compensate and fix Normal Tangent space rotation. |
| <b>Normal Format</b> <i>DirectX, OpenGL</i> | Switch between different Normal Map formats (inverts the green channel). Only Active when Is Normal Map is True. |
| <b>HSL Adjustment</b> <i>-1.0 - 1.0</i> | Adjust HSL globally. |
| <b>HSL Random</b> <i>-1.0 - 1.0</i> | Set HSL randomisation per cell. |
| <b>Alpha Adjustment</b> <i>-1.0 - 1.0</i> | Set global Alpha adjustment, reduces Alpha contrast. |
| <b>Alpha Random</b> <i>-1.0 - 1.0</i> | Set Alpha Adjustment randomisation per cell. |
| <b>Background Color</b> <i>(Color value)</i> | Sets the background color onto which textures are blended. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="flood-fill-mapper.resources/floodfill-mapper-ex01.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="flood-fill-mapper.resources/floodfill-mapper-ex02.jpg" />
        </td>
    </tr>
</table>
