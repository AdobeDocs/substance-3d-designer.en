---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/channels/alpha-merge.html"
breadcrumb-title: ""
description: Use the Alpha Merge node to combine RGB textures with alpha channels for creating RGBA textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Channels > Alpha Merge
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Alpha Merge
user-guide-description: ""
user-guide-title: ""
---

# Alpha Merge

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](alpha-merge.resources/rgb-a-merge.png)

<b>In:</b> Filters &gt; Channels

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Adds an alpha channel to an input without alpha channel. Not to be confused with [RGBA Merge](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/channels/rgba-merge/rgba-merge.md), this node is much simpler and only adds alpha!

Simple but handy node for when you just want to mask something out, or when your result requires an alpha.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>RGB</b> <i>Color Input</i> | Color image without alpha |
| <b>A</b> <i>Grayscale Input</i> | Grayscale image to be used as result's alpha. |
