---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/adjustments/threshold.html"
breadcrumb-title: ""
description: Use the Threshold node to convert grayscale textures to black and white based on a threshold value for creating masks.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Adjustments > Threshold
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Threshold
user-guide-description: ""
user-guide-title: ""
---

# Threshold

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/threshold-2.png){width="200px"}

<b>In:</b> Filters &gt; Adjustments

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Returns white if the *comparison criteria* set in the **Mode** parameter is met for the input pixel value relatively to the **Threshold** value.  
Similar to [Histogram Scan](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/adjustments/histogram-scan/histogram-scan.md), but with contrast always at maximum level. Serves as a more precise and faster way to obtain similar results to Histogram Scan.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Threshold</b> <i>0.0 - 1.0</i> | Luminance value against which the input pixel value is compared. |
| <b>Mode</b> | The criterion by which the input pixel value should be compared against the **Threshold** value:<br><br>- *Greater*<br>- *Greater or equal*<br>- *Lower*<br>- *Lower or equal* |
