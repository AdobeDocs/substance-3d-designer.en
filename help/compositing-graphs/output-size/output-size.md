---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/output-size.html"
breadcrumb-title: ""
description: Configure output size settings for Substance compositing graphs to control texture resolution and quality.
helpx_creative_field: ""
helpx_description: Designer > Substance graphs > Output size
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Output size
user-guide-description: ""
user-guide-title: ""
---


# Output size

It's the first of a graph's <b>Base parameters</b> and, along with the <b>Output Format</b> (or bitdepth), is critical to understand well since it has a large impact on a graph's output, both within Designer and in other applications as a published [Substance 3D asset (SBSAR)](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html) file.

>[!TIP]
>
> We strongly recommend acquiring a good understanding of [inheritance in Substance graphs](../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) as a foundation for using the Output Size property efficiently.

>[!NOTE]
>
> Use the ![](props-output-size-lock.jpg) lock button to have the Height value *match* the Width value.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

## Power of 2 values

The Output size parameter determines the resolution of the *texture* output by a graph or node.

A texture which is an object in graphics computing bound by some restrictions imposed by the way graphics processing hardware performs its computations. One of these restrictions is the texture should represent an image which pixel count in X and Y is a *power of two*.

</td>
<td width="33.33%" style="border: 0;" valign="top">

| Power of 2 | Pixels |
| --- | --- |
| 7 | 128 |
| 8 | 256 |
| 9 | 512 |
| 10 | 1024 |
| 11 | 2048 |
| 12 | 4096 |
| 13 | 8192 |

</td>
</tr>
</table>

The Output size property uses *logarithmic steps* to easily map increases of powers of two (e.g., 256, 512, 1024, ...) to a *linear scale* (e.g. 8, 9, 10, ...). This means increasing or decreasing the Output Size value in X or Y by 1 is akin to multiplying or dividing the current resolution by 2.

This also applies when the Output Size value is controlled by a [function](../../function-graphs/function-graphs.md), where the function should output the target logarithmic values (relative or absolute) instead of the target resolution.

>[!IMPORTANT]
>
> Increasing or decreasing resolution in both X and Y multiplies or divides the pixel count by *4*, which has a significant impact on a graph's *performance* and *memory footprint*.  
> As such, we strongly recommend using the *lowest resolution* actually needed to get a desired result. Keeping resolutions under control is one of many of our [performance optimization guidelines](../../best-practices/performance-optimization/performance-optimization-guidelines.md).

>[!NOTE]
>
> In [Function graphs](../../function-graphs/function-graphs.md), the `$size` and `$sizelog2` [system variables](../../function-graphs/variables/system-variables/system-variables.md) return a Float2 value matching the current resolution of the node or graph as a raw pixel count or power of two respectively.  
> E.g., for a 1024\*512 image, `$size` returns `(1024,512)` while `$sizelog2` returns `(10,9)`.

## Relative size

When the Output Size property uses a *Relative to...* [inheritance method](../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md), its value is expressed as a modifier *relatively to the inherited logarithmic value*.

Modifiers relative to the inherited resolution range from -12 to +12 on a logarithmic scale, with the default being 0. This means each step above or below results in doubling or halving of resolution. The table on the right gives an example of how relative resolution changes in one dimension for an inherited value of 9 (i.e., 512 = 2^9) and 11 (i.e., 2048 = 2^11):

Notice how above 8196, the size is *capped*. This cap is controlled by the <b>Cooking Size Limit</b> setting in the <b>General</b> section of the [Preferences](../../interface/preferences-window/preferences-window.md). Please note working with very large resolutions comes with a proportional performance cost and exponential memory footprint. Also, limits in graphics processing puts a hard limit on the maximum size of a texture.

| -5 | -4 | -3 | -2 | -1 | 0 | +1 | +2 | +3 | +4 | +5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | 32 | 64 | 128 | 256 | <b>512</b> | 1024 | 2048 | 4096 | 8196 | 8196 |
| 64 | 128 | 256 | 512 | 1024 | <b>2048</b> | 4096 | 8196 | 8196 | 8196 | 8196 |

>[!NOTE]
>
> Below 16 the resolution is *not* capped but it is not recommended to go lower, as there are no performance gains below that threshold. To the contrary, performance actually *drops* because of the specific implementation of the <b>Substance engine</b>. Therefore, use 16x16 as a general minimum resolution in Substance graphs.

## Changing the inheritance method

In most cases, the default [inheritance method](../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) for the Output Size property is the following depending on the item:

* Graph: *Relative to parent*
* Node: *Relative to input* – the values inherited by the node's [Primary input](../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md) are used in this case
* [Bitmap](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md) node: *Absolute* – see the [Bitmap resource](../../resources/bitmap-resource/bitmap-resource.md) page and [performance optimization guidelines](../../best-practices/performance-optimization/performance-optimization-guidelines.md) to know why that is

Display the properties of a node or graph by clicking that item, then in the [Properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html) panel find the <b>Output Size</b> property in the <b>Base parameters</b> section. Click the inheritance method drop down menu select the desired inheritance method.

![Output size inheritance method](change-mode.gif "Output size inheritance method"){width="512px"}

## Example problems

If you are a new [Adobe Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) user, you might run into some common problems. We'll list some examples below, along with solutions.

+++Problem 1
**![(error)](error.svg) Problem**

![Example problem 1](problem2-bad.png "Example problem 1")



The **Parent Size** setting is *grayed out*, and the graph uses in an undesired 256\*256 resolution.

In the graph's properties, the inheritance method of the Output Size property was set to *Absolute*, which stops inheritance in favour of an arbitrary value.

**![(tick)](check.svg) Solution**

![Example problem 1 Solution](problem2-good.png "Example problem 1 Solution")



Set the inheritance method for the graph's Output size to *Relative to parent*.

+++

+++Problem 2
**![(error)](error.svg) Problem**

![Example problem 2](problem1-bad.png "Example problem 2")



Above you see a case where the output of a graph results in a different resolution (512\*512) than set in the parent (1024\*1024), despite the graph being set to *Relative to parent*.

The problem stems from the [Bitmap](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md) node. It defaults to the *Absolute* inheritance method, and picked 512\*512 as a resolution based on the [Bitmap resource](../../resources/bitmap-resource/bitmap-resource.md). The node connected to it are set to *Relative to input*, thus inherit their Output Size from the Bitmap node.

**![(tick)](check.svg) Solution**

![Example problem 2 Solution](problem1-good.png "Example problem 2 Solution")



Set the Output Size's inheritance method of the Bitmap node to *Relative to parent*, resolving the issue further down the chain.

+++

+++Problem 3
**![(error)](error.svg) Problem**

![Example problem 3](problem3-bad.png "Example problem 3")



Above you see an issue where the resolution jumps much higher halfway through the chain, resulting to much higher output resolution than defined by the parent.

The problem is caused by a relative modifier of 3 on the [Transformation 2D](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/transformation-2d/transformation-2d.md) node, making the output 8 times larger.

**![(tick)](check.svg) Solution**

![Example problem 3 Solution](problem3-good.png "Example problem 3 Solution")



Set the relative modifiers for Width and Height to 0, leading to no upscaling.

+++
