---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/patterns/gradient-radial.html"
breadcrumb-title: ""
description: Use the Gradient Radial node to create radial gradients radiating from a center point for circular color transitions.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Gradient Radial
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Gradient Radial
user-guide-description: ""
user-guide-title: ""
---

# Gradient Radial

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](gradient-radial.resources/gradient-radial.png){width="128px"}

<b>In:</b> Texture Generators &gt; Patterns

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Similar to [Gradient Circular](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/gradient-circular/gradient-circular.md), creates a grayscale gradient transition defined by two custom points in a radial fashion. The transition is from a to b, defined by centerpoint and radius. Keep in mind results will not always tile.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Shape</b> <i>Cone, Hemisphere</i> | Determines transition profile. Cone is a sharp, linear transition, Hemisphere is soft and rounded in the centre. |
| <b>Point 1</b> | Center point of the gradient. Starts white. |
| <b>Point 2</b> | Radius point to determine extent of gradient. Ends black. |
| <b>Non Square Expansion</b> <i>False/True</i> | Enable compensation of squash and stretch with non-square ratios. |
