---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/symmetry-slice.html"
breadcrumb-title: ""
description: Use the Symmetry Slice node to slice textures along symmetry axes for creating mirrored patterns and effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Symmetry Slice
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Symmetry Slice
user-guide-description: ""
user-guide-title: ""
---

# Symmetry Slice

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](symmetry-slice.resources/mirror-2.png){width="128px"}

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Complex Symmetry/mirroring operation node. Allows for a large variety of geometric operations with full control, but requires some experimenting.

Compared to [Mirror](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/mirror-filter-node/mirror-filter-node.md) and [Symmetry](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/symmetry/symmetry.md), this node has many more options.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Symmetry Mode</b> <i>0 - 6</i> | Choose symmetry geometry/mirror line. Options are Horizontal, Vertical, Diagonal Left-Right, Diagonal Right-Left, Vertical Invert, Corner and Diagonal Corner. |
| <b>Transfer Mode</b> <i>0 - 6</i> | Blend mode. Options are: |
| <b>Blend</b> <i>0.0 - 1.0</i> | Blends the original image back into the result. |
| <b>Flip Side</b> <i>False/True</i> | Flips origin, meaning the origin side of the operation is reversed. Left to right symmetry for example becomes right to left. |
| <b>Flip Side2</b> <i>False/True</i> | Only used when Symmetry Mode is 5 or 6. Flip corner origin. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="symmetry-slice.resources/symslice.png" />
        </td>
    </tr>
</table>
