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
<td style="border: 0;" valign="top">

![](emboss-with-gloss.png){width="128px"}

## Emboss With Gloss

**In:** *Filters/Effects*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Performs an Embossing effect with added gloss (specular reflection) on a color and height input. Essentially adds fake, baked lighting to an image based on height information. Useful for some texturing styles that require lighting baked into the textures.

For a version with more options, see [Uber Emboss](../../../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/effects/uber-emboss/uber-emboss.md). There's also the simpler, atomic version of [Emboss](../../../../../../help/compositing-graphs/nodes-reference-for-com/atomic-nodes/emboss/emboss.md).

## Parameters

### Inputs

* **Color**: *Color Input*
* **Height**: *Grayscale Input*

### Parameters

* **Highlight Color**: *(Color value)*Color of the specular highlight.
* **Shadow Color**: *(Color value)*Color used in shadowed/unlit areas.
* **Gloss**: *0.0 - 0.5*Glossiness highlight size.
* **Intensity**: *0.0 - 10.0*Intensity of the highlight.
* **Light Angle**: *0.0 - 1.0*  
  Incidence angle of the (faked) light.

## Example Images

|  |
| --- |
| There are no images attached to this page. |

</td>
</tr>
</table>
