---
title: "Shape Splatter to Mask | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Texture Generators > Patterns > Shape Splatter to Mask"
---

# Shape Splatter to Mask

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](shape-splatter-to-mask.png){width="128px"}

## Shape Splatter to Mask

**In:** *Texture Generators**/Patterns*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Converts [Shape Splatter](../shape-splatter/shape-splatter.md) Data into a black and white mask based on Pattern ID. Allows you to for example create a mask of only a certain type of attern. Has extra options for selecting a range of Pattern ID's and to randomly hide some of the shapes.

## Parameters

### Parameters

* **Pattern ID Start Range**: *1 - 8*Set first Pattern ID in range to select.
* **Pattern ID End Range**: *1 - 8*Set last Pattern ID in range to select.
* **Random Mask**: *0.0 - 1.0*Set proportion of Patterns to randomly mask out.
* **Output**: *Binary Mask, Integer Mask, Grayscale Values*Determine type of output values. Binary Mask returns just black and white, 0-or-1 values, Integer Mask Wil encode higher values up to 8 for each Pattern in HDR format, Grayscale Values will spread the range proportionally between 0 and 1..

</td>
</tr>
</table>

 