---
title: "Flood Fill to GrayscaleColor"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Filters > Effects > Flood Fill to GrayscaleColor"
---

# Flood Fill to Grayscale/Color

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](floodfill-to-grayscale.png){width="128px"}

![](floodfill-to-color.png){width="128px"}

## Flood Fill to Random Grayscale/Color

**In:** *Filters/Effects*

****Simple****

</td>
<td style="border: 0;" valign="top">

## Description

Uses Flood Fill data to generate grayscale or color value swatches. Unlike [Flood Fill to Random Grayscale](../flood-fill-random-gra/flood-fill-to-random-grayscale.md), these two nodes allow more control to set the exact variation and tones, with an additional extra input map to determine the base value to randomize on a per-cell basis.

It's a powerfull system to give every cell a unique value or color, yet still retain control and base it off of a pre-determined input.

## Parameters

### Inputs

* **Flood Fill**: *Color Input*
* **Grayscale/Color Input**: *Grayscale/Color Input*

### Parameters

* **Luminance/Color Adjustment**: *-1.0 - 1.0*Set the bias or base value for the node. When a Grayscale or Color input is used, this is used to change that initial value as a starting point.
* **Luminance/Color Random**: *-1.0 - 1.0*Set the amount of variation.

</td>
</tr>
</table>
