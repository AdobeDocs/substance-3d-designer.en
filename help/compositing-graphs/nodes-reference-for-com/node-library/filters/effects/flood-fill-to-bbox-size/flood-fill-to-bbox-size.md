---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/flood-fill-to-bbox-size.html"
breadcrumb-title: ""
description: Use the Flood Fill to BBox Size node to fill regions with bounding box size values for procedural scaling effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to BBox Size
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Flood Fill to BBox Size
user-guide-description: ""
user-guide-title: ""
---

# Flood Fill to BBox Size

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](flood-fill-to-bbox-size.resources/flood-fill-to-bbox-size-01.png){width="128px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Generates a grayscale map from a [Flood Fill](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/effects/flood-fill/flood-fill.md) base, with values tied to each tile's individual size.

Values are relative to the total canvas size (a full white tile would mean it stretches the entire canvas), so contrast is often low.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Output</b> <i>max(X, Y), X, Y</i> | Sets what metric the value is based on: width, length or both. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="flood-fill-to-bbox-size.resources/flood-fill-to-bbox-size-02.png" />
        </td>
    </tr>
</table>
