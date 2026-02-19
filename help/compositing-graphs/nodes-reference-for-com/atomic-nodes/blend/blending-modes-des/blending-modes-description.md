---
title: "Blending modes"
description: "Learn about blending modes available in Substance 3D Designer for combining textures with different compositing effects."
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Blend > Blending modes
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/atomic-nodes/blend/blending-modes-description.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
  - photography
helpx_experience_level:
  - any
helpx_learn_topic:
  - enhancing-color
  - appearance
  - blending
---




# Blending modes

The [Blend](../blend.md) node offers the following blending modes:

## Copy

The *Copy* blending mode will just place the foreground on top of the background.

![Blending mode: Copy](image2015-8-20-9-38-0.png "Blending mode: Copy"){zoomable="yes"}

For color images, the alpha channel is taken into account by default in the opacity.

This can be changed by using the 'Alpha blending' parameter.

![Blending mode: Copy (2)](image2015-8-20-14-15-29.png "Blending mode: Copy (2)"){zoomable="yes"}

## Add (Linear dodge)

The *Add* blending mode will add the foreground input value to each corresponding pixel in the background.

![Blending mode: Add (Linear dodge)](image2015-8-20-9-38-19.png "Blending mode: Add (Linear dodge)"){zoomable="yes"}

## Subtract

The *Substract* blending mode will substract the foreground input value from each corresponding pixel in the background.

If the result of the substraction is lower than 0, the value is capped to 0, resulting pure black.

![Blending mode: Substract](image2015-8-20-9-38-35.png "Blending mode: Substract"){zoomable="yes"}

## Multiply

The *Multiply* blending mode will multiply the background input value by each corresponding pixel in the foreground.

As the value of each pixel is comprised between 0 and 1, the result is always equal or lower (darker) compared to the original.

![Blending mode: Multiply](image2015-8-20-9-38-53.png "Blending mode: Multiply"){zoomable="yes"}

## Add sub

The *Add Sub* blending mode works as following:

* Foreground pixels with a value higher than 0.5 are added to their respective background pixels.
* Foreground pixels with a value lower than 0.5 are substracted from their respective background pixels.

![Blending mode: Add sub](image2015-8-20-9-39-11.png "Blending mode: Add sub"){zoomable="yes"}

## Max (Lighten)

The *Max* Blending mode will pick the higher value between the background and the foreground.

![Blending mode: Max (Lighten)](image2015-8-20-9-40-12.png "Blending mode: Max (Lighten)"){zoomable="yes"}

## Min (Darken)

The *Min* Blending mode will pick the lower value between the background and the foreground.

![Blending mode: Min (Darken)](image2015-8-20-9-40-31.png "Blending mode: Min (Darken)"){zoomable="yes"}

## Switch

The *Switch* blending mode is similar to the Copy mode, with one *crucial* difference:

* 'Opacity' set to 0: The stream of nodes connected to the 'Foreground' input *won't be computed*.
* 'Opacity' set to 1: The stream of nodes connected to the 'Background' input *won't be computed*.

Therefore, this mode may be used to improve the performances of your graph.

The [Switch](../../../node-library/filters/blending/switch/switch.md) and [Switch grayscale](../../../node-library/filters/blending/switch/switch.md) nodes are setup to use the blend nodes in these specific configurations.

![Blending mode: Switch](image2015-8-20-9-38-0.png "Blending mode: Switch"){zoomable="yes"}

## Divide

The *Divide* blending mode will divide the background input pixels value by each corresponding pixel in the foreground.

![Blending mode: Divide](image2015-8-20-9-41-32.png "Blending mode: Divide"){zoomable="yes"}

## Overlay

The *Overlay* blending mode combines Multiply and Screen blend modes:

* * If the value of the lower layer pixel is below 0.5, then a *Multiply* type blending is applied
  * If the value of the lower layer pixel is above 0.5, then a *Screen* type blending is applied

![Blending mode: Overlay](image2015-8-20-9-41-50.png "Blending mode: Overlay"){zoomable="yes"}

## Screen

With Screen blend mode the values of the pixels in the two inputs are inverted, multiplied, and then inverted again.

The result is the opposite effect to multiply and is always equal or higher (brighter) compared to the original.

![Blending mode: Screen](image2015-8-20-9-42-11.png "Blending mode: Screen"){zoomable="yes"}

## Soft light

The Soft Light blend mode creates a subtle lighter or darker result depending on the brightness of the foreground color.

Blend colors that are more than 50% brightness will lighten the background pixels and colors that are less than 50% brightness will darken the background pixels.

![Blending mode: Soft light](image2015-8-20-9-42-32.png "Blending mode: Soft light"){zoomable="yes"}
