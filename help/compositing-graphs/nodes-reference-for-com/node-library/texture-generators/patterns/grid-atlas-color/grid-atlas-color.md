---
title: "Grid atlas color"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Generator > Pattern > Grid atlas color"
---

# Grid atlas color

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Grid atlas color icon](grid-atlas-color.resources/grid-atlas-color-01.png "Grid atlas color")

<b>In:</b> Generator &gt; Pattern

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Pack up to 16 color images on a grid of adjustable XY size.<br>The output atlas image can be sampled from by a [Shape splatter v2](../shape-splatter-v2/shape-splatter-v2.md) or a [Shape splatter mapper color](../shape-splatter-v2-mapper-color/shape-splatter-v2-mapper-color.md) node.

See also [Grid atlas grayscale](../grid-atlas-grayscale/grid-atlas-grayscale.md).

</td>
</tr>
</table>

<a name="inputs"></a>

## Inputs

|                         |                            |
|:------------------------|:---------------------------|
| <b>Input 1</b> *Color*  | The color image input #1.  |
| <b>Input 2</b> *Color*  | The color image input #2.  |
| <b>Input 3</b> *Color*  | The color image input #3.  |
| <b>Input 4</b> *Color*  | The color image input #4.  |
| <b>Input 5</b> *Color*  | The color image input #5.  |
| <b>Input 6</b> *Color*  | The color image input #6.  |
| <b>Input 7</b> *Color*  | The color image input #7.  |
| <b>Input 8</b> *Color*  | The color image input #8.  |
| <b>Input 9</b> *Color*  | The color image input #9.  |
| <b>Input 10</b> *Color* | The color image input #10. |
| <b>Input 11</b> *Color* | The color image input #11. |
| <b>Input 12</b> *Color* | The color image input #12. |
| <b>Input 13</b> *Color* | The color image input #13. |
| <b>Input 14</b> *Color* | The color image input #14. |
| <b>Input 2</b> *Color*  | The color image input #15. |
| <b>Input 2</b> *Color*  | The color image input #16. |

<a name="outputs"></a>

## Outputs

|               |                              |
|:--------------|:-----------------------------|
| <b>Output</b> | The output color grid atlas. |

<a name="parameters"></a>

## Parameters

|                                   |                                                                                                                                                                                                                                                                                                                                                                    |
|:----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <b>Grid size X</b> *Integer*      | The size of the grid on the X axis.<br>I.e. the number of images being packed on the X axis.                                                                                                                                                                                                                                                                       |
| <b>Grid size Y</b> *Integer*      | The size of the grid on the Y axis.<br>I.e. the number of images being packed on the Y axis.                                                                                                                                                                                                                                                                       |
| <b>Output size mode</b> *Integer* | The method of defining the size of the output image according to the node's 'Output size' base parameter:<br><br>- <b>Manual:</b> Use the size as is.<br>- <b>Automatic ratio:</b> Adjust the image ratio according to the grid size in order to minimise the image size. Deformation will occur for non-square grids using 3 rows or columns, e.g. (3, 2), (4, 3) |

## Examples

<img src="./grid-atlas-color.resources/grid-atlas-color-02.png" alt="Grid atlas color node in context of a graph" style="width: 50%"><br>
<i>Grid atlas color node in context of a graph</i>