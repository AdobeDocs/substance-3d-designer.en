---
title: "Channels shuffle"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Channels shuffle"
---

# Channels shuffle

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Channels shuffle](comp_shuffle.png "Atomic node: Channels shuffle"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Rearranges the color channels of one or two input images into the output image.

I.e., takes two inputs and allows you to return an output where any of the Red, Green, Blue and Alpha channels are swapped or set to any of the channels from the input.

Essentially it allows you to pack and swap RGB channels in any possible way. Grayscale inputs are treated as if they are Color: Red, Green, Blue and Alpha all return the same values.

</td>
</tr>
</table>

Channel Shuffle has basic options, but in most cases of Channel-packing or Stripping and setting Alpha Channels it is quicker to use [RGBA Merge](../../node-library/filters/channels/rgba-merge/rgba-merge.md), [RGBA Split](../../node-library/filters/channels/rgba-split/rgba-split.md), [Alpha Merge](../../node-library/filters/channels/alpha-merge/alpha-merge.md) and [Alpha Split](../../node-library/filters/channels/alpha-split/alpha-split.md). They are set up to do default actions that do not require changing multiple parameters and converting to Grayscale afterwards. If you're after a more advanced version with more blending options, look at [Channel Mixer](../../node-library/filters/adjustments/channel-mixer/channel-mixer.md).

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">



</td>
<td width="83.33%" style="border: 0;" valign="top">



</td>
<td width="100.00%" style="border: 0;" valign="top">



</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">



</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Parameters

|  |  |
| --- | --- |
| <b>Red channel</b> *Integer* | Choose the source channel to be inserted into the output image's Red channel. |
| <b>Green channel</b> *Integer* | Choose the source channel to be inserted into the output image's Green channel. |
| <b>Blue channel</b> *Integer* | Choose the source channel to be inserted into the output image's Blue channel. |
| <b>Alpha channel</b> *Integer* | Choose the source channel to be inserted into the output image's Alpha channel. |

## Input connectors

|  |  |
| --- | --- |
| <b>Input 1</b> *Color/Grayscale* PRIMARY | Primary input image. |
| <b>Input 2</b> *Color/Grayscale* | Secondary input image. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale/Color* |  |

## Examples

*Coming soon.*
