---
title: "Gradient map"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Gradient map"
---

# Gradient map

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Atomic node: Gradient map](comp_gradient.png "Atomic node: Gradient map"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Remaps the grayscale values in an image using a custom gradient.

This node serves a dual purpose: It may be simply used as a<b> </b>grayscale-to-color conversion node, or to colorize grayscale input my mapping it to a custom color ramp.

</td>
</tr>
</table>

The node offers an advanced and feature-rich gradient editor to map multiple colors with precision: go to the section in this page to learn more.

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

## Parameters

|  |  |
| --- | --- |
| <b>Color mode</b> *Boolean* | Sets the output mode to Color or Grayscale. |
| <b>Gradient adressing</b> *Boolean* | Sets the gradient to either repeat (tile) or clamp values that are out of the &#91;0, 1&#93; range. |
| <b>Gradient</b> *Array of gradient keys* | The custom gradient ramp used to map the input grayscale values.   May be edited in place or using the . |

## Gradient editor

This window offers controls to edit the reference gradient used by the Gradient Map node to map grayscale values to colors.

It can be opened from the Gradient Map node's <b>Properties</b> in the following ways:

* Click LMB on the <b>Gradient Editor</b> button;
* Double-click LMB on a pin in the gradient bar. The clicked pin will then be automatically selected in the Gradient Editor so you can directly edit its values.

![Gradient Editor](image2017-2-17-16-13-5.png "Gradient Editor")

### Editing the gradient pins

The colors and their positions along the gradient is controlled by pins placed along the gradient bar.

Each pin sets a color at its position along the gradient.

The portions of the gradient before and after the first and last pins are set to those pin's colors respectively.

![Gradient Editor - Gradient view](image2017-2-17-17-27-46.png "Gradient Editor - Gradient view")

The following controls are available to edit pins:

+++Add pin


Click LMB on the gradient or just below to add a pin at the position you clicked in the gradient bar.





The new pin will be set to the gradient's color at that position.





+++

+++Move pin


Hold LMB and drag the selected pins along the gradient bar to move them.







You can also set the position of a pin with a numerical value by selecting it and using thePositionparameter. The position is a value in the &#91;0;1&#93; range where 0 is the start of the gradient and 1 is its end.







When multiple pins are selected, they can all be movedconcurrently. When one or more pins reach and end of the gradient as they are moved, two behaviours are available depending on the mouse button used for moving:



* LMB:Pins remain at the end, meaning they will be stacked at that location as they reach it and their relative positions are changed;


* MMB:Pins loop back around to the other end of the gradient, meaning their relative positions remain unchanged.


+++

+++Delete pin


Select the pins and press Delete, or drag the pins off the gradient bar to delete them.





+++

+++Desaturate


This button desaturates the colors set on the selected pins.



+++

+++Invert positions


Mirrors the positions of the selected pins on the gradient.





+++

+++Invert colors


Switches the colors of the selected pins to their negative.



+++

+++Clear all


Removes all the pins from the gradient bar.





+++

### Interpolation modes

Once pins are set up, you can control how colors transition from one pin to the next using the available interpolation modes:

+++Linear


The default interpolation mode: applies a simple linear interpolation between each pin, so the gradient progresses uniformly.



+++

+++Flat Tangents


When thinking about the transition between gradients as Bezier curves where pins are points of the curve, this mode sets these points to have horizontal tangents.





This results in a transition that is evocative of a smoothstep interpolation.





When this mode is selected, theMidpointparameter is enabled and lets you offset the horizontal position of the curve's vertical midpoint between the points. This effectively tips the scale between the 'out' and 'in' tangents.



+++

+++Smooth


Applies smoothing to the interpolation curve between each point.





When this mode is selected, theSmoothnessparameter is enabled and lets you adjust the intensity of the smoothing where a value of 0 is equal to theLinearinterpolation mode.



+++

+++No Interpolation


Color only changes at a pins' location, and stays constant until the next pin along the gradient bar.





This results in hard steps between colors, and only the colors set by the pins are present on the gradient.



+++

### color picker

![Gradient Editor - Color picker](image2017-2-17-18-21-29.png "Gradient Editor - Color picker")

The Color Picker lets you set a color in several ways:

+++Gradient area and hue bar


Tweak the positions of the gizmo in the gradient and of the notch in the hue bar to set a color.





+++

+++RGB, HSV and Alpha sliders


The RGB, HSV and Alpha sliders let you set a color precisely, by tweaking the sliders or directly setting their numerical values.





Alternatively, use a hexcode in the dedicated input field below the sliders.





+++

+++Pick on screen


Use thePickbutton and click LMB anywhere in the screen to sample the color at that location.





+++

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

The selected color is previewed in the upper half of the color thumbnail.  
The lower half displays the previously used color. Double-click LMB on it to revert the tweaked color to it.

</td>
<td width="16.67%" style="border: 0;" valign="top">

![Color Picker - Revert color](image2015-8-27-14-40-39.png "Color Picker - Revert color")

</td>
</tr>
</table>

When multiple pin are selected, the RGB, HSV and Alpha sliders turn into delta (Δ) sliders, meaning they are used to offset the value of each pin by the same amount.

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

Additionally, the following capabilities are available below the color thumbnail as buttons:

<b>Invert:</b> Switches the color to its negative;

<b>To Gray:</b> Desaturates the color;

<b>Copy</b>*:* Copy the currently selected color to the clipboard;

<b>Paste:</b> Switch to the color currently in the clipboard;

<b>sRGB</b>: Use the sRGB color space to display colors. When disabled, the Linear color space is used;

<b>Float:</b> Display RGB, HSV and Alpha slider values in floating point.

</td>
<td width="25.00%" style="border: 0;" valign="top">

![Color Picker - Buttons](invert2.gif "Color Picker - Buttons")

</td>
</tr>
</table>

### Gradient Eyedropper

The Gradient Eyedropper is one of the most useful features this node offers, as you can create complex gradients just by drawing a line on a reference picture.

![Gradient Editor - Gradient Picker](pickgradient.gif "Gradient Editor - Gradient Picker")

The <b>Precision</b> slider will help you adjust your newly created gradient by increasing or decreasing the number of keys: the lower their values, the more precise your gradient will match your picked values.

## Input connectors

|  |  |
| --- | --- |
| <b>Input</b> *Grayscale* PRIMARY | The grayscale image to be processed. |

## Output connectors

|  |  |
| --- | --- |
| <b>Output</b> *Grayscale* |  |

## Examples

*Coming soon.*
