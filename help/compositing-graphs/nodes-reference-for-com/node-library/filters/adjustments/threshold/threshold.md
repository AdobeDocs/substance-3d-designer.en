---
title: "Threshold"
description: "Use the Threshold node to convert grayscale textures to black and white based on a threshold value for creating masks."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Threshold
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/threshold.html"
helpx_creative_field:
  - video
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - reflections
  - enhancing-color
  - food-photography
---




# Threshold

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](threshold-2.png){width="200px"}

## Threshold

**In:** *Filters/Adjustments*

**Simple**

</td>
<td style="border: 0;" valign="top">

## Description

Returns white if the *comparison criteria* set in the **Mode** parameter is met for the input pixel value relatively to the **Threshold** value.  
Similar to [Histogram Scan](../histogram-scan/histogram-scan.md), but with contrast always at maximum level. Serves as a more precise and faster way to obtain similar results to Histogram Scan.

### Parameters

* **Threshold**: *0.0 - 1.0*  
  Luminance value against which the input pixel value is compared.
* **Mode**:  
  The criterion by which the input pixel value should be compared against the **Threshold** value:
  * *Greater*
  * *Greater or equal*
  * *Lower*
  * *Lower or equal*

## Example Images

</td>
</tr>
</table>
