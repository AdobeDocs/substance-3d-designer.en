---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/sampler-nodes.html"
breadcrumb-title: ""
description: Access sampler nodes in Substance 3D Designer function graphs to sample textures and extract color values.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Samplers
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Samplers
user-guide-description: ""
user-guide-title: ""
---


# Sampler nodes

![Sampler nodes](image2016-1-12-14-45-43.png "Sampler nodes")

These nodes sample a value in an input image at the provided 2D coordinates:

<b>Sample Gray</b> samples a luminance value at the input <b>Position</b> in a grayscale image and outputs it as a <b>Float</b> value.

<b>Sample Color</b> samples an RGBA value at the input <b>Position </b>in a color image and outputs it as a <b>Float4</b> value where the R,G,B and A components are mapped to the X, Y, Z and W components respectively.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

Coordinates start from the top left corner of an input, and range between 0 and 1 horizontally and vertically.

Positions out of this range are handled according to the selected <b>Addressing mode</b> (see below).

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Pixel coordinates](samplercoords.png "Pixel coordinates")

</td>
</tr>
</table>

>[!NOTE]
>
> The <b>Position</b> input should be a Float2 value where the image's X and Y coordinates are mapped to the X and Y components of the value respectively

## Parameters

+++Input image
Lets you select which node input to use for sampling.

The list adapts dynamically to the currently connected inputs. This means entries are added as you connect node inputs.

The numbering of the inputs starts at 0, so that an image connected to the node's first input is listed as *Input image 0*.

+++

+++Filtering mode
Lets you define how to handle interpolation when pixels from the sampled image do not map exactly to the output image, because of resolution differences.

<b>Nearest</b>  
The pixel will be mapped to the target *as-is* at the matching coordinate. If the target is of lower resolution the pixel may be entirely ignored. If the target is of higher resolution; it will be mapped to all pixels covering its span. The output is *crisper* and will look slightly *aliased*.

<b>Bilinear filtering</b>  
A filtering process is applied to the source image so its pixels are mapped to the target resolution in a way that *smooths out* the transitions between pixels. The output is *smoother* and will look slightly *blurred*.

+++

+++Addressing mode
Controls how position values outside of the &#91;0;1&#93; range are handled.

<b>Repeat</b>  
Loops over the &#91;0;1&#93; range as the value increases.  
E.g.: 3.4 is 0.4, -1.7 is 0.3.

<b>Clamp to Edge</b>  
Clamps values out of to the &#91;0;1&#93; range to its closest limit.  
E.g.: .3.4 is 1, -1.7 is 0.

+++
