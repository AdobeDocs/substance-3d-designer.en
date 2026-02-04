---
title: "Scatter Splines on Splines | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Spline Tools > Scatter Splines on Splines"
---

# Scatter Splines on Splines

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Scatter Splines on Splines: Icon](scatter-splines-on-splines-icon.png "Scatter Splines on Splines: Icon")

<b>In:</b> Spline &amp; Path Tools &gt; Spline Tools

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Description

Places splines along the input parent splines.

The node offers deep customization options for controlling how splines are scattered, and lets you scatter simple straight splines, or your own custom splines.

The node lets you create intricate structures for mapping colors and images using the [Spline Mapper](../spline-mapper-grayscale/spline-mapper-grayscale.md) nodes, or used as a skeleton for placing shapes using the [Scatter on Spline](../scatter-spline-grayscale/scatter-on-spline-grayscale.md) nodes.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Tutorial

Click the image on the right to access our <b>dedicated tutorial</b>, for a guided tour of the node's capabilities and its usage in the context of a Spline-based workflow.

</td>
<td style="border: 0;" valign="top">

[![Video Spline nodes](video_spline.png)](https://youtu.be/aUUWV1dYQdI)

</td>
</tr>
</table>

## Input connectors

|  |  |
| --- | --- |
| <b>Preview</b> *Grayscale* | The preview of the input splines as a grayscale image. |
| <b>Spline Coords</b> *Color* | The coordinates of the parent splines’ points encoded in the RGBA channels of a color image:  <b>R</b> - X position  <b>G</b> - Y position  <b>B</b> - Height  <b>A</b> - Packed data:          - Sign: Spline is closed (negative) or open (positive)          - Absolute value: Thickness + 1 |
| <b>Spline Data</b> *Color* | Additional data of the parent splines encoded in the RGBA channels of a color image:  <b>R</b> - Tangents X  <b>G</b> - Tangents Y  <b>B</b> - Tangents Z  <b>A</b> - Unused |
| <b>Spline Amount</b> *Integer* | The number of parent splines. |
| <b>Custom Spline Coords</b> *Color* | The coordinates of the custom splines’ points encoded in the RGBA channels of a color image:  <b>R</b> - X position  <b>G</b> - Y position  <b>B</b> - Height  <b>A</b> - Packed data:          - Sign: Spline is closed (negative) or open (positive)          - Absolute value: Thickness + 1 |
| <b>Custom Spline Data</b> *Color* | Additional data of the custom splines encoded in the RGBA channels of a color image:  <b>R</b> - Tangents X  <b>G</b> - Tangents Y  <b>B</b> - Tangents Z  <b>A</b> - Unused |
| <b>Custom Spline Amount</b> *Integer* | The number of custom splines. |
| <b>Scale Map</b> *Grayscale* | The grayscale map controlling the scale of the scattered splines.  The effect of this map is controlled by the <b>Scale Map Input Multiplier</b> parameter and is combined with the other parameters in the <b>Size</b> group. |
| <b>Rotation Map</b> *Grayscale* | The grayscale map controlling the rotation of the scattered splines.  The effect of this map is controlled by the <b>Rotation Map Input Multiplier</b> parameter and is combined with the other parameters in the <b>Rotation</b> group. |

## Output connectors

|  |  |
| --- | --- |
| <b>Preview</b> *Grayscale* | The preview of the scattered splines as a grayscale image. |
| <b>Spline Coords</b> *Color* | The coordinates of the scattered splines’ points encoded in the RGBA channels of a color image:  <b>R</b> - X position  <b>G</b> - Y position  <b>B</b> - Height  <b>A</b> - Packed data:          - Sign: Spline is closed (negative) or open (positive)          - Absolute value: Thickness + 1 |
| <b>Spline Data</b> *Color* | Additional data of the scattered splines encoded in the RGBA channels of a color image:  <b>R</b> - Tangents X  <b>G</b> - Tangents Y  <b>B</b> - Unused <b>A</b> - Unused |
| <b>Spline Amount</b> *Integer* | The number of scattered splines. |

## Parameters

|  |  |
| --- | --- |
| <b>Side</b> *Integer* | Controls on which side(s) of the parent splines the splines should be scattered, considering that 'forward' is the direction of the *parent* splines:   Left Place the splines on the left side.   Right Place the splines on the right side.   Left + Right Place the splines on both sides.   Left / Right - Alternate Place splines left then right alternatively (E.g., every other side).   Left / Right - Random Pick the side randomly for each spline. |
| <b>Amount Mode</b> *Integer* | The method of scattering the splines along the parent splines, which impacts the amount of scattered splines on each parent spline:   Fixed amount per spline The specified amount of evenly spaced splines is scattered.   Spacing The amount of splines is automatically adjusted to fit the specified even spacing.   In both cases, the first and last scattered splines fall exactly on the start and end of each parent spline respectively. |
| <b>Spline Amount Per Spline</b> *Integer* | The amount of evenly spaced splines scattered along each parent spline. |
| <b>Spline Spacing</b> *Float* | The minimum distance along parent splines by which splines should be spaced, while still landing the first and last spline on the start and end of each parent spline respectively. |
| <b>Spline Type</b> *Integer* | Selects which type of spline should be scattered on the parent splines:   Straight A simple, straight spline.   Custom spline The spline(s) provided to the <b>Custom Spline</b> inputs. Mutliple splines are supported when appended together into a list. |
| <b>Custom Spline Selection</b> *Integer* | When using multiple custom splines appended together into a list, this parameter lets you select how these splines should be distributed in the scattering.   Whole list All splines are scattered together as a group.   Sequential Each individual spline is scattered in order, looping around the list.   Random A random spline is picked from the list for every spline scattered. |
| <b>Start</b> *Float* | Offsets the point from the start of the parent splines where the scattering starts.  The value is the normalized length of each parent spline. |
| <b>End</b> *Float* | Offsets the point from the start of the parent splines where the scattering ends.  The value is the normalized length of each parent spline. |
| <b>Flip Direction</b> *Boolean* | Inverts the direction of the scattered splines. |
| <b>Left / Right Symmetry Mode</b> *Integer* | The method of symmetry applied to the splines scattered on each side of the parent splines.   Disabled No symmetry is applied, the splines are place on each side using a simple rotation.   Left symmetry The spline on the left is symmetrical to the one on the right relatively to the parent spline.   Right symmetry The spline on the right is symmetrical to the one on the left relatively to the parent spline. |
| <b>Left / Right Random Link</b> *Boolean* | Controls whether the splines on each side of the parent spline should use the same values when using random rotation, random scaling, etc. In other words:   *- False:* each spline uses separate random values  *- True:* both splines share the same random values |
| <b>Spline Pivot Mode</b> *Integer* | Sets the method of placing the pivot of scattered splines, which impacts rotation and scaling.   Note that the pivot is *always placed on the parent spline* and its controls impact the scattered spline. In other words: the pivot does not move, it is the scattered spline that moves and scales relatively to it.   Position along spline Move the pivot along the scattered spline.   Absolute position Set an arbitrary position for the pivot. |
| <b>Pivot Position Along Spline</b> *Float* | The normalized position of the pivot along the scattered spline, where 0 is its start and 1 is its end.   Note that the pivot follows the *direction* of the scattered spline and the spline's orientation may change to preserve the pivot's position and rotation relatively to the parent spline. |
| <b>Pivot Absolute Position</b> *Float2* | The position in UV space of the pivot. |
| <b>Non-Square Correction</b> *Boolean* | Adjust the splines positions and thickness to retain the their shape in non-square resolutions.   *Note:* When using custom splines, the custom spline should use the *same image ratio* as the <b>Scatter Splines on Splines</b> nodes. |

+++Size


+++

+++Position


+++

+++Rotation


+++

+++Height


+++

+++Thickness


+++

+++Preview


+++

## Examples

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Scatter Splines on Splines: Example 1](scatter-splines-on-splines-example-1.png "Scatter Splines on Splines: Example 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Scatter Splines on Splines: Example 1](scatter-splines-on-splines-example-2.png "Scatter Splines on Splines: Example 1"){zoomable="yes"}

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Scatter Splines on Splines: Example 3](scatter-splines-on-splines-example-4.png "Scatter Splines on Splines: Example 3"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Scatter Splines on Splines: Example 4](scatter-splines-on-splines-example-3.png "Scatter Splines on Splines: Example 4"){zoomable="yes"}

</td>
</tr>
</table>

## Renders

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Scatter Splines on Splines: Render 1](scatter-splines-on-splines-demo-1.png "Scatter Splines on Splines: Render 1"){zoomable="yes"}

</td>
<td style="border: 0;" valign="top">

![Scatter Splines on Splines: Render 2](scatter-splines-on-splines-demo-3.png "Scatter Splines on Splines: Render 2"){zoomable="yes"}

</td>
</tr>
</table>

![Scatter Splines on Splines: Render 3](scatter-splines-on-splines-demo-2.png "Scatter Splines on Splines: Render 3"){zoomable="yes"}

 