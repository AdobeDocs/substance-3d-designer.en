---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/emboss-with-gloss.html"
breadcrumb-title: ""
description: Use the Emboss With Gloss node to create embossed effects with gloss maps for adding depth and shine to textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Emboss With Gloss
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Emboss With Gloss
user-guide-description: ""
user-guide-title: ""
---

# Emboss With Gloss

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](emboss-with-gloss.resources/emboss-with-gloss-01.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs an Embossing effect with added gloss (specular reflection) on a color and height input. Essentially adds fake, baked lighting to an image based on height information. Useful for some texturing styles that require lighting baked into the textures.

For a version with more options, see [Uber Emboss](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/uber-emboss/uber-emboss.md). There's also the simpler, atomic version of [Emboss](../../../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/emboss/emboss.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Color</b> <i>Color Input</i> |  |
| <b>Height</b> <i>Grayscale Input</i> |  |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Highlight Color</b> <i>(Color value)</i> | Color of the specular highlight. |
| <b>Shadow Color</b> <i>(Color value)</i> | Color used in shadowed/unlit areas. |
| <b>Gloss</b> <i>0.0 - 0.5</i> | Glossiness highlight size. |
| <b>Intensity</b> <i>0.0 - 10.0</i> | Intensity of the highlight. |
| <b>Light Angle</b> <i>0.0 - 1.0</i> | Incidence angle of the (faked) light. |
