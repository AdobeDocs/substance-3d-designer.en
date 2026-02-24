---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/hald-clut.html"
breadcrumb-title: ""
description: Use the Hald CLUT node to apply color lookup tables using Hald CLUT format for color grading and correction.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Hald CLUT
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Hald CLUT
user-guide-description: ""
user-guide-title: ""
---


# Hald CLUT

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](hald-clut.png){width="128px"}

## Hald CLUT

**In:** *Filters/Adjustments*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Applies a LUT on the input image. The LUT has to be in the Hald format in 4096\*4096 resolution. See <http://www.quelsolaar.com/technology/clut.html> for more information.

### Inputs

* **input**: *Color Input*  
  Image onto which to apply the LUT.
* **lut**: *Color Input*Lut input slot. Must be 4096x4096.

## Parameters

* **LUT Intensity by Alpha**: *False/True*Defines if the LUT effect is weighted by the alpha channel.

Examples

![](content-hald-clut.jpg)

</td>
</tr>
</table>
