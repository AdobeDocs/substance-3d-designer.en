---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/3d-worley-noise.html"
breadcrumb-title: ""
description: Use the 3D Worley Noise node to generate Worley noise based on 3D position for creating volumetric texture effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Worley Noise
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Worley Noise
user-guide-description: ""
user-guide-title: ""
---

# 3D Worley Noise

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](3d-worley-noise.resources/3d-worley-noise-01.png){width="128px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

One of the most versatile and advanced noises in the library, it generates a Worley noise in 3D space, based on an input Position map. Has plenty of options that make it much more powerful than the standard [Cells ](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/cells-1/cells-1.md)or [Distance ](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/distance/distance.md)based noises.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Scale</b> <i>1 - 64</i> | Set the global scale for the effect. |
| <b>Size</b> <i>0.0 - 1.0</i> | Perform non-uniform scaling on X, Y and Z axes separately. |
| <b>Mode</b> <i>Euclidean, Manhattan, Chebyshev, Minkowski</i> | Change the distance metric. Allows for some very different noise types. |
| <b>Minkowski Number</b> <i>0.0 - 20.0</i> | Only with Minkowski distance metric. Blends between different types of metrics. |
| <b>Style</b> <i>F1, F2, F2-F1, Border, Random Color</i> | Set the Metric combination math. Allows for many more combinations. |
| <b>Border Width</b> <i>0.0 - 1.0</i> | When Border combination math is active, controls the width of the border. |
| <b>Roundess</b> <i>0.0 - 1.0</i> | Only availble with F1, F2 and F2-F1 modes. Sets the level mid position. |
| <b>Invert</b> <i>False/True</i> | Inverts the result. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="3d-worley-noise.resources/3d-worley-noise-02.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-worley-noise.resources/3d-worley-noise-03.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-worley-noise.resources/3d-worley-noise-04.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="3d-worley-noise.resources/3d-worley-noise-05.png" />
        </td>
    </tr>
</table>
