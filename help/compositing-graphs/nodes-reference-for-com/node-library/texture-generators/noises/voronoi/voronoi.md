---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/voronoi.html"
breadcrumb-title: ""
description: Use the Voronoi node to generate Voronoi patterns for creating cellular textures and organic material effects.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Voronoi
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Voronoi
user-guide-description: ""
user-guide-title: ""
---

# Voronoi

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](voronoi.resources/voronoi-01.png){width="200px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **Voronoi** node generates a 3D Voronoi noise mapped to a 2D image using a *Z-down orthographic projection*.

This node can be tested with [Cube GBuffers](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d-gbuffers/cube-3d-gbuffers.md) as input instead of an actual baked map (as seen in the Example Image below).

>[!WARNING]
>
> This noise is meant to be used with the *GPU engine only* (i.e., **Direct**or **OpenGL**). Go to **Tools &gt; Switch engine...** or press the **F9** key to select the desired engine.

</td>
</tr>
</table>

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Invert</b> <i>Boolean</i> | Inverts the output image. |
| <b>Scale</b> <i>Float</i> | Controls the scale of the Voronoi noise.<br><br>*Note*: When **Tiling** is enabled on *any axis*, the scale adjustement is *stepped*. This is expected. |
| <b>Size</b> <i>Float3</i> | Controls the size of the Voronoi noise in the **X**, **Y** and **Z** axes. Non-uniform values result in a *stretching or squashing* effect.<br><br>*Note*: When **Tiling** is enabled on *any axis*, the size adjustment is *stepped*. This is expected. |
| <b>Offset</b> <i>Float3</i> | Applies an offset to the *position* of the Voronoi noise in the **X**, **Y** and **Z** axes. |
| <b>Disorder</b> <i>Float3</i> | The intensity of the *random offset* applied to each point of the noise in the **X**, **Y** and **Z** axes. |
| <b>Distortion Intensity</b> <i>Float</i> | Controls the intensity of a *warping effect* applied on the Voronoi noise. |
| <b>Distortion Scale Multiplier</b> <i>Float</i> | Controls the scale of the *deforming pattern* used in the warping effect controlled by the **Distortion Intensity**. |
| <b>Rounded Curve</b> <i>Float</i> | Rounds the *slope* around each point of the noise to make it *convex*.<br><br>*Note*: This parameter is not available when the **Style** parameter is set to *Edge*. |
| <b>Distance Scale</b> <i>Float</i> | Adjusts the *distance of the gradient* around each point of the noise. |
| <b>Distance Mode</b> <i>Integer</i> | Sets the method to *compute the distance gradient* around each point of the noise:<br><br>- *Euclidean*<br>- *Manhattan*<br>- *Chebyshev*<br>- *Minkowski* |
| <b>Minkowski Number</b> <i>Float</i> | The order *p* of the Minkowski distance. If we divide the distance gradient into quadrants, this number impacts these quadrants as follows:<br><br>- p is *exactly* 1: Straight<br>- p is *lower* than 1: Concave<br>- p is *greater* than 1: Convex<br><br>Interesting values:<br><br>- *1.0*: Manhattan distance<br>- *2.0*: Euclidean distance<br>- *Infinity*: Chebyshev distance<br><br>*Note*: This parameter is only available when the **Distance Mode** parameter is set to *Minkowski*. |
| <b>Style</b> <i>Integer</i> | Sets the method *rendering the data* of the Voronoi noise, considering the noise is based on a set of points in space:<br><br>- *F1*: the distance to the *closest point* in space<br>- *F2*: the distance to the *second closest point* in space<br>- *F2-F1*<br>- *F1\*F2*<br>- *F1/F2*<br>- *Edge*: the *edge between each cell* of the noise in space<br>- *Random color*: assign a *random flat color* to each cell of the noise in space |
| <b>Edge Thickness</b> <i>Float</i> | Adjusts the thickness of the edges detected between cells of the Voronoi noise. Edges are detected in the X, Y and Z axes, thus some thicknesses may increase quicker than other depending on the cells' *depth*.<br><br>*Note*: This parameter is only available when the **Style** parameter is set to *Edge*. |
| <b>Random Color Seed Mode</b> <i>Integer</i> | Sets the method of *acquiring* the random seed for the color selection per cell:<br><br>- *Global Random Seed*: Use the seed *inherited* by the node<br>- *Manual Seed*: Use a *discrete* seed<br><br>*Note*: This parameter is only available when the **Style** parameter is set to *Random color*. |
| <b>Random Color Seed</b> <i>Integer</i> | The discrete random seed which should be used for the color selection per cell.<br><br>*Note*: This parameter is only available when the **Style** parameter is set to *Random color* and the **Random Color Seed Mode** parameter is set to ***Manual Seed***. |
| <b>Non Square Expansion</b> <i>Boolean</i> | Enables compensation of squash and stretch with non-square ratios. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="voronoi.resources/voronoi-02.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi.resources/voronoi-03.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi.resources/voronoi-04.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi.resources/voronoi-05.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi.resources/voronoi-06.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi.resources/voronoi-07.jpg" />
        </td>
    </tr>
</table>
