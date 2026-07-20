---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/flood-fill-to-index.html"
breadcrumb-title: ""
description: Use the Flood Fill to Index node to fill regions with index values for creating numbered and labeled patterns.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to Index
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Flood Fill to Index
user-guide-description: ""
user-guide-title: ""
---

# Flood Fill to Index

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/floodfill-index.png){width="200px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Flood Fill to Index converts every Flood Fill cell to a value according to its index number, starting with 0 in the top left corner. It can be used to return grayscale tints in a normalised form (0.0 to 1.0, divided by as many cells as found by Flood Fill) or as an HDR, unclamped value (0 to n where n is the number of cells).

Additionally, Flood Fill to Index makes use of [values](../../../../../values-compositing-graphs/values-in-substance-compositing-graphs.md), returning the amount of shapes found and the optional, internal data table.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Flood Fill Bbox</b> <i>Color Input</i> | Standard Flood Fill input map. Required. |
| <b>Special Shape Info</b> <i>Color Input</i> | Extra Flood Fill map, needs to be explicitely enabled on previous Flood Fill node and is required to be connected!. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Output</b> <i>Normalised, Integer</i> | Determine if out put is in LDR 0-1 range or HDR 0-n range. |
| <b>Ignore Shape Smaller Than</b> <i>0.0 - 1.0</i> | Tolerance value for ignoring small shapes. |
| <b>Show Flood Fill Data Table</b> <i>False/True</i> | Returns extra (debug) data for advanced use. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/flood-fill-ex02.jpg" />
        </td>
    </tr>
</table>
