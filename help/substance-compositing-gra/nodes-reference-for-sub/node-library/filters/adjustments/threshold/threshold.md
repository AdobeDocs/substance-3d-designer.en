---
title: "Threshold"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Threshold"
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
Similar to [Histogram Scan](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-scan/histogram-scan.md), but with contrast always at maximum level. Serves as a more precise and faster way to obtain similar results to Histogram Scan.

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
