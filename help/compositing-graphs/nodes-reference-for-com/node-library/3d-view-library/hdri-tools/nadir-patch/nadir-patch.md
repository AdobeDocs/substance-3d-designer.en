---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/3d-view-library/hdri-tools/nadir-patch.html"
breadcrumb-title: ""
description: Use the Nadir Patch node to patch the nadir region of HDRI panoramas for fixing bottom artifacts in environment maps.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > 3D View (Library) > HDRI Tools > Nadir Patch
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Nadir Patch
user-guide-description: ""
user-guide-title: ""
---

# Nadir Patch

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](nadir-patch.resources/nadir-patch-01.png){width="200px"}

<b>In:</b> 3D View &gt; HDRI Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

This node provides functionality to patch over the central ground point (nadir) of a spherically mapped image. It can be used to hide or "clone out" an ugly nadir, or visible camera or tripod. It works like a [Clone Patch](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/material-filters/scan-processing/clone-patch/clone-patch.md), but with adjustments for spherically mapped images. The user selects a point elsewhere in the image, that is the cloned and blended in at the nadir. No other external inputs are required other than a single HDRI to process, but an external mask can be used as alpha for the patch effect.

effect can be quickly checked and validated with [Nadir Extract](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/3d-view-library/hdri-tools/nadir-extract/nadir-extract.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|  |  |
|:---|:---|
| <b>Input</b> <i>Color Input</i> |  |
| <b>Mask Input</b> <i>Grayscale Input</i> | Optional mask slot used for masking the patch. Function like an alpha. |

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Enable</b> <i>False/True</i> | Enable or disable patching effect. |
| <b>Show Frames Helper</b> <i>False/True</i> | Show or hide the helper lines, for debug purposes. |
| <b>Frame Thickness</b> <i>0.0 - 1.0</i> | Thickness of helper lines. |
| <b>Patch Scale</b> <i>0.0 - 1.0</i> | Global, uniform scale of patch. Affects both source and target. |
| <b>Patch Size</b> <i>0.0 - 1.0</i> | Non-uniform size of patch. |
| <b>Patch Rotation</b> <i>0.0 - 1.0</i> | Rotation of the patch. Affects source and target. |
| <b>Patch Alpha</b> <i>Smooth Square, Gaussian, Mask Input</i> | Set what alpha is used to blend the patch with the background. |
| <b>Patch Hardness</b> <i>0.0 - 1.0</i> | Set hardness/contrast of alpha. |
| <b>Source Rotation Offset</b> <i>0.0 - 1.0</i> | Rotation only for source of the patch. |
| <b>Position Coordinates</b> |  |
| <b>Source Position</b> | Position of source. Has handle in 2D view. |
| <b>Patch Position</b> | Position of target. Has handle in 2D view. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="nadir-patch.resources/nadir-patch-02.gif" />
        </td>
    </tr>
</table>
