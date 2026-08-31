---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/tiling/make-it-tile-photo.html"
breadcrumb-title: ""
description: Use the Make It Tile Photo node to convert photographs into seamless tiling textures for material creation.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Tiling > Make It Tile Photo
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Make It Tile Photo
user-guide-description: ""
user-guide-title: ""
---

# Make It Tile Photo

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](make-it-tile-photo.resources/make-it-tile-photo-01.png)

![](make-it-tile-photo.resources/make-it-tile-photo-02.png)

<b>In:</b> Filters &gt; Tiling

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node provides edge-fixup functionality for any image that might not tile due to non-continuous edges. It does not affect anything other than the input image's edges. If you want to adjust scale or tile in different ways, look at [Make It Tile Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/tiling/make-it-tile-patch/make-it-tile-patch.md).

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Mask Warping H</b> <i>-100.0 - 100.0</i> | Introduces warping on the horizontal axis, to avoid undefined transitions. |
| <b>Mask Warping V</b> <i>-100.0 - 100.0</i> | Introduces warping on the vertical axis, to avoid undefined transitions. |
| <b>Mask Size H</b> <i>0.0 - 1.0</i> | Sets how far the transition edge reaches horizontally. |
| <b>Mask Size V</b> <i>0.0 - 1.0</i> | Sets how far the transition edge reaches vertically. |
| <b>Mask Precision H</b> <i>0.0 - 1.0</i> | Sets how smooth the transition is horizontally. |
| <b>Mask Precision V</b> <i>0.0 - 1.0</i> | Sets how smooth the transition is vertically. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="make-it-tile-photo.resources/make-it-tile-photo-03.png" />
        </td>
    </tr>
</table>
