---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/texture-generators/noises/3d-voronoi.html"
breadcrumb-title: ""
description: Use the 3D Voronoi node to generate Voronoi patterns based on 3D world position for creating volumetric cellular textures.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Noises > 3D Voronoi
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D Voronoi
user-guide-description: ""
user-guide-title: ""
---

# 3D Voronoi

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![](../../../../../../assets/3dvoronoi.png){width="200px"}

<b>In:</b> Texture Generators &gt; Noises

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

The <b>3D Voronoi</b> node generates a Voronoi noise in 3D space based on the <b>Position Map</b> input.

This node can be tested with [Cube 3D GBuffers](../../../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d-gbuffers/cube-3d-gbuffers.md) as input instead of an actual baked map (as seen in the Example Image below).

</td>
</tr>
</table>

>[!WARNING]
>
> This noise is meant to be used with the <i>GPU engine only</i> (i.e., <b>Direct3D</b> or <b>OpenGL</b>). Go to <b>Tools &gt; Switch engine...</b> or press the <b>F9</b> key to select the desired engine.

<a name="parameters"></a>

## Parameters

|  |  |
|:---|:---|
| <b>Invert</b> <i>Boolean</i> | Inverts the output image. |
| <b>Scale</b> <i>Float</i> | Controls the scale of the 3D Voronoi noise.<br><br><i>Note</i>: When <b>Tiling</b> is enabled on <i>any axis</i>, the scale adjustement is <i>stepped</i>. This is expected. |
| <b>Size</b> <i>Float3</i> | Controls the size of the 3D Voronoi noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. Non-uniform values result in a <i>stretching or squashing</i> effect.<br><br><i>Note</i>: When <b>Tiling</b> is enabled on <i>any axis</i>, the size adjustment is <i>stepped</i>. This is expected. |
| <b>Offset</b> <i>Float3</i> | Applies an offset to the <i>position</i> of the 3D Voronoi noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. |
| <b>Disorder</b> <i>Float3</i> | The intensity of the <i>random offset</i> applied to each point of the noise in the <b>X</b>, <b>Y</b> and <b>Z</b> axes. |
| <b>Distortion Intensity</b> <i>Float</i> | Controls the intensity of a <i>warping effect</i> applied on the 3D Voronoi noise. |
| <b>Distortion Scale Multiplier</b> <i>Float</i> | Controls the scale of the <i>deforming pattern</i> used in the warping effect controlled by the <b>Distortion Intensity</b>. |
| <b>Rounded Curve</b> <i>Float</i> | Rounds the <i>slope</i> around each point of the noise to make it <i>convex</i>.<br><br><i>Note</i>: This parameter is not available when the <b>Style</b> parameter is set to <i>Edge</i>. |
| <b>Distance Scale</b> <i>Float</i> | Adjusts the <i>distance of the gradient</i> around each point of the noise. |
| <b>Distance Mode</b> <i>Integer</i> | Sets the method to <i>compute the distance gradient</i> around each point of the noise:<br><br>- <i>Euclidean</i><br>- <i>Manhattan</i><br>- <i>Chebyshev</i><br>- <i>Minkowski</i> |
| <b>Minkowski Number</b> <i>Float</i> | The order <i>p</i> of the Minkowski distance. If we divide the distance gradient into quadrants, this number impacts these quadrants as follows:<br><br>- p is <i>exactly</i> 1: Straight<br>- p is <i>lower</i> than 1: Concave<br>- p is <i>greater</i> than 1: Convex<br><br>Interesting values:<br>- <i>1.0</i>: Manhattan distance<br>- <i>2.0</i>: Euclidean distance<br>- <i>Infinity</i>: Chebyshev distance<br><br><i>Note</i>: This parameter is only available when the <b>Distance Mode</b> parameter is set to <i>Minkowski</i>. |
| <b>Style</b> <i>Integer</i> | Sets the method <i>rendering the data</i> of the 3D Voronoi noise, considering the noise is based on a set of points in 3D space:<br><br>- <i>F1</i>: the distance to the <i>closest point</i> in 3D space<br>- <i>F2</i>: the distance to the <i>second closest point</i> in 3D space<br>- <i>F2-F1</i><br>- <i>F1\*F2</i><br>- <i>F1/F2</i><br>- <i>Edge</i>: the <i>edge between each cell</i> of the noise in 3D space<br>- <i>Random color</i>: assign a <i>random flat color</i> to each cell of the noise in 3D space |
| <b>Edge Thickness</b> <i>Float</i> | Adjusts the thickness of the edges detected between cells of the 3D Voronoi noise. Edges are detected in the X, Y and Z axes, thus some thicknesses may increase quicker than other depending on the cells' <i>depth</i>.<br><br><i>Note</i>: This parameter is only available when the <b>Style</b> parameter is set to <i>Edge</i>. |
| <b>Enable Tiling</b> <i>Boolean</i> | Adjusts the 3D Voronoi noise so its resulting pattern <i>repeats</i> in the X, Y and Z axes. |

## Examples

<table style="margin-top: 32px; margin-bottom: 32px">
    <tr style="border: 0">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvoronoi-variant.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvoronoi-variant5.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvoronoi-variant2.jpg" />
        </td>
    </tr>
    <tr style="border: 0; background: transparent">
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvoronoi-variant4.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvoronoi-variant3.jpg" />
        </td>
        <td style="border: 0; background: transparent">
            <img src="../../../../../../assets/3dvoronoi-variant6.jpg" />
        </td>
    </tr>
</table>
