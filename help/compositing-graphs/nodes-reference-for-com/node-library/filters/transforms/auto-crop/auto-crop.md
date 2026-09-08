---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/transforms/auto-crop.html"
breadcrumb-title: ""
description: Use the Auto Crop node to automatically crop textures to remove empty borders and optimize texture dimensions.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Transforms > Auto Crop
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Auto Crop
user-guide-description: ""
user-guide-title: ""
---

# Auto Crop

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](../../../../../../assets/autocropgrayscale.png){width="200px"}

</td>
<td style="border: 0;" valign="top">

![](../../../../../../assets/autocropcolor.png){width="200px"}

</td>
</tr>
</table>

<b>In:</b> Filters &gt; Transforms

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **Auto Crop** node adjusts the **Input** so that its content is either placed at the *center* of the image without being resized, or *resized to the span* of the image.

The content of the image is defined by a box fitted to the *first and last pixels* on **X** and **Y** which values are *higher than 0* (i.e. non-black). The **Color** version lets you choose from the RGB and Alpha channels for defining that box.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Mode</b> <i>Integer</i> | Set the cropping method which should be applied:<br><br>- <i>Crop square</i>: the image is cropped so that the shape is at the center of the smallest <i>square</i> image which can fully include it<br>- <i>Crop auto</i>: The image is cropped so that the shape is at the center of the smallest <i>square or non-square</i> image which can fully include it<br>- <i>Fit (Keep ratio)</i>: The image is resized to the <i>full span</i> of the image while keeping its <i>proportions</i> (i.e. width to length ratio)<br>- <i>Fill (Stretch)</i>: The image is resized to the <i>full span</i> of the image |
| <b>Use alpha</b> <i>Boolean</i> | Use the alpha channel of the <b>Input</b> to determine the image content's <i>bounds</i> for cropping. When set to <i>False</i>, black pixels are used instead.<br><br><i>Note:</i> This parameter is only available in the <b>Color</b> version of the node. |
| <b>Filtering Mode</b> <i>Integer</i> | Defines how to treat the sampled results when <i>interpolating</i> between pixels:<br><br>- <i>Nearest</i>: will sample exactly the <i>same</i> value (faster)<br>- <i>Bilinear</i>: will apply a bilinear filter on the result for a <i>smoother</i> look<br>- <i>Auto</i>: Uses the most appropriate of the two modes above depending on the selected <b>Mode</b> for cropping |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/autocrop-demo-01-resized.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/autocrop-variant2.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/autocrop-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/autocrop-variant4.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/autocrop-variant3.png" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/autocrop-node.png" />
        </td>
    </tr>
</table>
