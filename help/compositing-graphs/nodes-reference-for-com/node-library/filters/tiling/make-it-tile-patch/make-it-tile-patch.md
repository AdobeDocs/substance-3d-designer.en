---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/tiling/make-it-tile-patch.html"
breadcrumb-title: ""
description: Use the Make It Tile Patch node to patch and create seamless tiling textures from input images.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Tiling > Make It Tile Patch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Make It Tile Patch
user-guide-description: ""
user-guide-title: ""
---

# Make It Tile Patch

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](make-it-tile-patch.resources/make-it-tile-patch.png)

![](make-it-tile-patch.resources/make-it-tile-patch-grayscale.png)

<b>In:</b> Filters &gt; Tiling

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node is a grid-based semi-random tiler. It takes an input patch and stamps it around, attempting to turn it into a tiling image without too many repetitions, based on your settings.

Useful for when you have a small patch of texture and want to create a larger scale, tiling texture from it.

Keep in mind that this is different from [Make-It-Tile Photo](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/tiling/make-it-tile-photo/make-it-tile-photo.md), which mainly fixes up edges.

To do this with an entire material, see [Smart Auto Tile](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/smart-auto-tile/smart-auto-tile.md).

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Mask Size</b> <i>0.0 - 1.0</i> | Size of the round mask used when stamping the patch. |
| <b>Mask Precision</b> <i>0.0 - 1.0</i> | Falloff/smoothness precision of the mask. |
| <b>Mask Warping</b> <i>-100.0 - 100.0</i> | Introduces warping at mask edges. Good for avoiding smooth, undefined transitions between patches. |
| <b>Pattern size width</b> <i>0.0 - 1000.0</i> | Changes the width of the patch non-uniformly. |
| <b>Pattern size height</b> <i>0.0 - 1000.0</i> | Changes the height of the patch non-uniformly. |
| <b>Disorder</b> <i>0.0 - 1.0</i> | Introduces translational randomness, slightly shifting patches around. |
| <b>Size Variation</b> <i>0.0 - 100.0</i> | Introduces size variation for the mask. |
| <b>Octave</b> <i>0 - 6</i> | This is the main control that determines the overal size. |
| <b>Rotation</b> <i>-360.0 - 360.0</i> | Pre-rotates the patch. |
| <b>Rotation Variation</b> <i>0.0 - 360.0</i> | Introduces random rotation for every patch stamp. |
| <b>Background Color</b> <i>(Color value)</i> | Sets the background color for areas where no patch appears. |
| <b>Color Variation</b> <i>0.0 - 1.0 (Color Version Only)</i> | Introduces color variation per patch. |
| <b>Luminosity Variation</b> <i>(grayscale version only)</i> | Introduces luminosity variation per patch. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="make-it-tile-patch.resources/patch-ex.gif" />
        </td>
    </tr>
</table>
