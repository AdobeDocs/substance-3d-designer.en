---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/voronoi-fractal.html"
breadcrumb-title: ""
description: Use the Voronoi Fractal node to generate fractal Voronoi patterns for creating organic cellular textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > Voronoi Fractal
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Voronoi Fractal
user-guide-description: ""
user-guide-title: ""
---

# Voronoi Fractal

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](voronoi-fractal.resources/voronoi-fractal-01.png){width="200px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The **Voronoi Fractal** node generates a *fractal* 3D Voronoi noise mapped to a 2D image using a *Z-down orthographic projection*.

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
| <b>Scale</b> <i>Float</i> | Controls the scale of the fractal Voronoi noise.<br><br>*Note*: When **Tiling** is enabled on *any axis*, the scale adjustement is *stepped*. This is expected. |
| <b>Size</b> <i>Float3</i> | Controls the size of the fractal Voronoi noise in the **X**, **Y** and **Z** axes. Non-uniform values result in a *stretching or squashing* effect.<br><br>*Note*: When **Tiling** is enabled on *any axis*, the size adjustment is *stepped*. This is expected. |
| <b>Offset</b> <i>Float3</i> | Applies an offset to the *position* of the fractal Voronoi noise in the **X**, **Y** and **Z** axes. |
| <b>Disorder</b> <i>Float3</i> | The intensity of the *random offset* applied to each point of the noise in the **X**, **Y** and **Z** axes. |
| <b>Distortion Intensity</b> <i>Float</i> | Controls the intensity of a *warping effect* applied on the fractal Voronoi noise. |
| <b>Distortion Scale Multiplier</b> <i>Float</i> | Controls the scale of the *deforming pattern* used in the warping effect controlled by the **Distortion Intensity**. |
| <b>Min Level</b> <i>Integer</i> | The minimum *level of of repetition* used in the fractal pattern. A wider minimum/maximum range results in a *richer pattern* with variation on more frequency ranges. |
| <b>Max Level</b> <i>Integer</i> | The maximum *level of of repetition* used in the fractal pattern. A wider minimum/maximum range results in a *richer pattern* with variation on more frequency ranges. |
| <b>Roughness</b> <i>Float</i> | Controls the *balance* between low and high *levels of repetition* in the fractal pattern.<br><br>*Note*: A value of **0** results in an output which is *not in line* with other low values following it. This is expected.<br><br>*Note 2*: This parameter is only available when the **Blend Mode** parameter is set to *Add*. |
| <b>Lacunarity</b> <i>Float</i> | Controls how the applied fractal pattern *fills space*. A *higher* value results in *less gaps* in the pattern and a *denser* noise. |
| <b>Global Opacity</b> <i>Float</i> | Controls the *range* of the fractal Perlin noise values from 0. |
| <b>Rounded Curve</b> <i>Float</i> | Rounds the *slope* around each point of the noise to make it *convex*.<br><br>*Note*: This parameter is not available when the **Style** parameter is set to *Edge*. |
| <b>Distance Scale</b> <i>Float</i> | Adjusts the *distance of the gradient* around each point of the noise. |
| <b>Distance Mode</b> <i>Integer</i> | Sets the method to *compute the distance gradient* around each point of the noise:<br><br>- *Euclidean*<br>- *Manhattan*<br>- *Chebyshev*<br>- *Minkowski* |
| <b>Minkowski Number</b> <i>Float</i> | The order *p* of the Minkowski distance. If we divide the distance gradient into quadrants, this number impacts these quadrants as follows:<br><br>- p is *exactly* 1: Straight<br>- p is *lower* than 1: Concave<br>- p is *greater* than 1: Convex<br><br>Interesting values:<br><br>- *1.0*: Manhattan distance<br>- *2.0*: Euclidean distance<br>- *Infinity*: Chebyshev distance<br><br>*Note*: This parameter is only available when the **Distance Mode** parameter is set to *Minkowski*. |
| <b>Blend Mode</b> <i>Integer</i> | Sets the method of blending together the values of *overlapping cells* in space:<br><br>- *Add*: Add the values<br>- *Max*: Retain the *highest* value<br>- *Min*: Retain the *lowest* value |
| <b>Style</b> <i>Integer</i> | Sets the method *rendering the data* of the fractal Voronoi noise, considering the noise is based on a set of points in space:<br><br>- *F1*: the distance to the *closest point* in space<br>- *F2*: the distance to the *second closest point* in space<br>- *F2-F1*<br>- *F1\*F2*<br>- *F1/F2*<br>- *Edge*: the *edge between each cell* of the noise in space<br>- *Random color*: assign a *random flat color* to each cell of the noise in space |
| <b>Edge Thickness</b> <i>Float</i> | Adjusts the thickness of the edges detected between cells of the fractal Voronoi noise. Edges are detected in the X, Y and Z axes, thus some thicknesses may increase quicker than other depending on the cells' *depth*.<br><br>*Note*: This parameter is only available when the **Style** parameter is set to *Edge*. |
| <b>Random Color Seed Mode</b> <i>Integer</i> | Sets the method of *acquiring* the random seed for the color selection per cell:<br><br>- *Global Random Seed*: Use the seed *inherited* by the node<br>- *Manual Seed*: Use a *discrete* seed<br><br>*Note*: This parameter is only available when the **Style** parameter is set to *Random color*. |
| <b>Random Color Seed</b> <i>Integer</i> | The discrete random seed which should be used for the color selection per cell.<br><br>*Note*: This parameter is only available when the **Style** parameter is set to *Random color* and the **Random Color Seed Mode** parameter is set to *Manual Seed*. |
| <b>Enable Tiling</b> <i>Boolean</i> | Adjusts the fractal Voronoi noise so its resulting pattern *repeats* in the X, Y and Z axes. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-02.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-03.gif" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-04.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-05.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-06.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-07.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-08.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="voronoi-fractal.resources/voronoi-fractal-09.jpg" />
        </td>
    </tr>
</table>
