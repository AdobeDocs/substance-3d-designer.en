---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/pbr-utilities/pbr-render-mapping.html"
breadcrumb-title: ""
description: Use the PBR Render Mapping node to convert material outputs to different PBR render mapping formats.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > PBR Utilities > PBR Render Mapping
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: PBR Render Mapping
user-guide-description: ""
user-guide-title: ""
---

# PBR Render Mapping

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/pbr-render-mapping-color.png)![](../../../../../../assets/pbr-render-mapping-grayscale.png)

<b>In:</b> Material Filters &gt; PBR Utilities

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This is an extension node for the [PBR Render node](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md), that allows you to map a separate texture onto the shape from a previous [PBR Render](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md). Its main goal is to let you remap each separate channel from your [PBR Render](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md), back onto the shape, to create composite map-channel breakdowns, as in the examples below. You're free to create your own composite method and masks by using the PBR Render Mapping nodes as component.

Color and Grayscale version exist for the two types of data: use color for diffuse maps, use grayscale for roughness, metal and other grayscale maps.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Texture</b> <i>Color/Grayscale Input</i> | Texture to map onto shape. |
| <b>UVs</b> <i>Color Input</i> | Mandatory UV-data input from a [PBR Render node.](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md) |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Background Color</b> <i>(Color value)</i> | Set a solid color value to use in the background. |

## Examples

Example is a composite of four different PBR Render Mapping nodes, using a [Histogram Select](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-select/histogram-select.md) on a [Linear gradient](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/gradient-linear-1/gradient-linear-1.md) as masks.

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/pbr-render-mapping-ex.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/pbr-render-mapping-ex-2.png" />
        </td>
    </tr>
</table>
