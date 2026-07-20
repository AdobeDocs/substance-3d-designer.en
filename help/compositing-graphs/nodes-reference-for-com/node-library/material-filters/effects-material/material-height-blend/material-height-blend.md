---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/material-filters/effects-material/material-height-blend.html"
breadcrumb-title: ""
description: Use the Material Height Blend node to blend multiple materials based on height maps for creating layered material effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Material Filters > Effects (Material) > Material Height Blend
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Material Height Blend
user-guide-description: ""
user-guide-title: ""
---

# Material Height Blend

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/material-height-blend.png){width="128px"}

<b>In:</b> Material Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node is a more advanced version of [Height Blend](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/effects-material/height-blend/height-blend.md) that blends two materials based on their Heightmaps. There is no user-defined mask, so you must have two Heightmaps, one for each material, of which at least one is not a uniform value.

This can be useful for combining two different, high-quality materials without a high-quality blending mask.

If you want to blend in water or snow, the nodes [Snow Cover](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/effects-material/snow-cover/snow-cover.md) and [Water Level](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/effects-material/water-level/water-level.md) are available instead.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Channels</b> | Toggle material channels on and off in this group, for example when using Specular/Glossiness maps instead of Metallic/Roughness. |
| <b>Height Offset</b> <i>0.0 - 1.0</i> | Offsets Heightmaps so the blend level is moved along the height axis. This is the main control for the blending. |
| <b>Contrast</b> <i>0.0 - 1.0</i> | Adjusts the contrast of the blending, makes transitions sharper. |
| <b>Mode</b> <i>Balanced height, Bottom height priority</i> |  |
| <b>Opacity</b> <i>0.0 - 1.0</i> | Blending Opacity of the foreground height, fades it in or out. |
| <b>Albedo Matching</b> <i>0.0 - 1.0</i> | The amount of internal color matching to perform between Albedo colors. |
