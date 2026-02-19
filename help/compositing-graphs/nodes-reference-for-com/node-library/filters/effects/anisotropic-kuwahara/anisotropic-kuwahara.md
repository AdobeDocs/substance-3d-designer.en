---
title: "Anisotropic Kuwahara Color"
description: "Use the Anisotropic Kuwahara Color filter to create stylized, painterly color effects with directional smoothing."
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Anisotropic Kuwahara Color"
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/filters/effects/anisotropic-kuwahara.html"
---

# Anisotropic Kuwahara Color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Anisotropic Kuwahara Color icon](https://helpx.adobe.com/content/dam/substance-3d-designer/substance-graphs/nodes/filters/effects/anisotropic-kuwahara/AnisotropicKuwaharaColor.png "Anisotropic Kuwahara Color icon"){width="200px"}

<b>In:</b> Filters &gt; Effects

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Applies an anisotropic directional blur which conforms to the details of the image. The result is an image which appears to *flow* in the direction of the shapes within.

This adjustable blur computes or receives a *direction map* to determine that flow, which can be sharpened into flatter, more clearly defined areas.

</td>
</tr>
</table>

The flow may also be broken down by rotating the direction in which blurring is applied. Similarly, a custom direction map may be used to override the one computed out of the image.

This filter can produce a painterly effect, and is useful for stylization.

<b>Anisotropy</b>

The intensity of the flow is mainly controlled by the parameter, as demonstrated in the image below.

Left: Anisotropy 0.0 / Right: Anisotropy 1.0

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![A bowl of fruit with the kuwahara filter applied with 0 anisotropy.](https://helpx.adobe.com/content/dam/substance-3d-designer/substance-graphs/nodes/filters/effects/anisotropic-kuwahara/anisotropic_kuwahara_color_example_3_before.jpg){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![A bowl of fruit with the kuwahara filter applied with 0 anisotropy.](https://helpx.adobe.com/content/dam/substance-3d-designer/substance-graphs/nodes/filters/effects/anisotropic-kuwahara/anisotropic_kuwahara_color_example_3_after.jpg){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Color*  Primary | The color image which should be processed. |
| <b>Anisotropy angle map</b> *Grayscale* | The grayscale image describing the additional rotation applied to the computed direction, where the grayscale value is a number of turns.   The map still has an effect when the 'Anisotropy' parameter is set to 0, as it impacts the rotation of the kernel used by the Kuwahara filter. |
| <b>Slope map</b> *Grayscale* | The map representing slopes that the direction map is conformed to, according to the 'Slope Map Input Multiplier' parameter value. |
| <b>Radius map (optional)</b> *Grayscale* | When connected, the blurring 'Radius' is multiplied against the input image. |
| <b>Direction map</b> *Color* | The map describing the direction used by the anisotropic filter kernel.   The map still has an effect when the 'Anisotropy' parameter is set to 0, as it impacts the rotation of the kernel used by the Kuwahara filter.   Note: This input is only used when the 'Use Input Direction Map' parameter is set to 'True'. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Color* | The result of the anisotropic blurring applied by the node on the input image. |
| <b>Direction map</b> *Color* | The direction map computed from the input image and used to drive the anisotropic blurring.   If the 'Use Input Direction Map' parameter is set to 'True', the image provided to the 'Direction Map' input is used and output as is. |

## Parameters

|  |  |
| --- | --- |
| <b>Radius</b> *Float* | The blurring radius, where a higher value results in a stronger blurring effect.   The maximum value is 32. |
| <b>Smoothness</b> *Float* | Adjusts the amount of blending of colors in the computed direction.   When this value is 0, colors are mostly displaced in that direction and very little blending occurs. |
| <b>Sharpness</b> *Float* | Increases the contrast in the blurred areas, resulting in them looking flatter and more clearly defined. |
| <b>Anisotropy</b> *Float* | Adjusts the contribution of the direction map in the blurring.   The direction map and all its modifiers (both parameters and input maps) still have an effect when this parameter value is 0, as the direction map is used in the Kuwahara filter kernel. |
| <b>Use input direction map</b> *Boolean* | When 'True', no direction map is computed from the input image, and the image connected to the 'Direction Map' input is used to drive the anisotropic blurring instead. |
| <b>Tensor smoothness</b> *Float*   *Available when 'Use input direction map' is set to 'False'* | Adjusts the intensity of blurring applied to the directions computed from the image and stored in the direction map.   Increasing this value ensures a smoother result when the image has a lot of high frequency detail. |
| <b>Anisotropy angle</b> *Float*    *Available when 'Use input direction map' is set to 'False'* | Adds a rotation to the direction map, in number of turns.   This additional rotation is *cumulative* with the one specified by the 'Anisotropy Angle Map' input. |
| <b>Anisotropy angle map multiplier</b> *Float*   *Available when 'Use input direction map' is set to 'False'* | Adjusts the intensity of the values in the 'Anisotropy Angle Map' input, which are then added on top of the rotation applied to the direction map, in number of turns.   This additional rotation is *cumulative* with the one specified by the 'Anisotropy Angle' parameter. |
| <b>Slope map input multiplier</b> *Float*   *Available when 'Use input direction map' is set to 'False'* | Adjusts the intensity by which the direction map is conformed to the slopes provided by the 'Slope Map' input. |
| <b>Ignore alpha</b> *Boolean* | When 'True', the alpha channel of the image is not impacted by the filter.   When 'False', the filter is also applied to the alpha channel. |

## Examples

<table>
  <tr>
    <td>
      <img src="https://helpx.adobe.com/libs/settings/wcm/designs/default/resources/0.gif" alt="anisotropic_kuwahara_color_example_1_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="https://helpx.adobe.com/libs/settings/wcm/designs/default/resources/0.gif" alt="anisotropic_kuwahara_color_example_1_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://helpx.adobe.com/libs/settings/wcm/designs/default/resources/0.gif" alt="anisotropic_kuwahara_color_example_2_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="https://helpx.adobe.com/libs/settings/wcm/designs/default/resources/0.gif" alt="anisotropic_kuwahara_color_example_2_after">
      <br><i>After</i>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td>
      <img src="https://helpx.adobe.com/libs/settings/wcm/designs/default/resources/0.gif" alt="anisotropic_kuwahara_color_example_4_before">
      <br><i>Before</i>
    </td>
    <td>
      <img src="https://helpx.adobe.com/libs/settings/wcm/designs/default/resources/0.gif" alt="anisotropic_kuwahara_color_example_4_after">
      <br><i>After</i>
    </td>
  </tr>
</table>
