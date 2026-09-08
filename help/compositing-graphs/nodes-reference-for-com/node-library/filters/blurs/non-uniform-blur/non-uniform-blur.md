---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/blurs/non-uniform-blur.html"
breadcrumb-title: ""
description: Use the Non Uniform Blur node to apply blur with different intensities in X and Y directions for anisotropic effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Blurs > Non Uniform Blur
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Non Uniform Blur
user-guide-description: ""
user-guide-title: ""
---

# Non Uniform Blur

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/non-uniform-blur-grayscale.png){width="128px"}

![](../../../../../../assets/non-uniform-blur.png){width="128px"}

<b>In:</b> Filters &gt; Blurs

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Performs a High Quality Blur, where the intensity is driven by an input mask. Options allow for Anisotropy and Assymetry to be added.

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Blur Map</b> <i>Grayscale Input</i> | Mask map to drive effect strength. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Intensity</b> <i>0.0 - 50.0</i> | Maximum strength to apply the blur with. Masked by the Blur Map, so this setting will have no effect on black areas of that map. |
| <b>Anisotropy</b> <i>0.0 - 1.0</i> | Optionally adds directionality to the blur effect. Driven by the Angle parameter. |
| <b>Asymmetry</b> <i>0.0 - 1.0</i> | Optionally adds a bias to the sampling. Driven by the Angle parameter. |
| <b>Angle</b> <i>0.0 - 1.0</i> | Angle to set directionality and sampling bias. |
| <b>Samples</b> <i>1 - 16</i> | Amount of samples, determines quality. Multiplied by amount of Blades. |
| <b>Blades</b> <i>1 - 9</i> | Amount of sampling sectors, determines quality. Multiplied by amount of Samples. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/nonuniform-example.gif" /><br><i>Below example is driven by a gradient ramp (at 90 degrees) in the Blur Map slot.</i>
        </td>
    </tr>
</table>
