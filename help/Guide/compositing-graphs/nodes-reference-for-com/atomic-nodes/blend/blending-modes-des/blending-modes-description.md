---
title: "Blending modes | Substance 3D Designer"
description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Atomic nodes > Blend > Blending modes"
---

# Blending modes

The [Blend](../blend.md) node offers the following blending modes:

+++Copy


TheCopyblending mode will just place the foreground on top of the background.







For color images, the alpha channel is taken into account by default in the opacity.





This can be changed by using the 'Alpha blending' parameter.





+++

+++Add (Linear dodge)


TheAddblending mode will add the foreground input value to each corresponding pixel in the background.





+++

+++Subtract


TheSubstractblending mode will substract the foreground input value from each corresponding pixel in the background.





If the result of the substraction is lower than 0, the value is capped to 0, resulting pure black.





+++

+++Multiply


TheMultiplyblending mode will multiply the background input value by each corresponding pixel in the foreground.





As the value of each pixel is comprised between 0 and 1, the result is always equal or lower (darker) compared to the original.





+++

+++Add sub


TheAdd Subblending mode works as following:



* Foreground pixels with a value higher than 0.5 are added to their respective background pixels.


* Foreground pixels with a value lower than 0.5 are substracted from their respective background pixels.




+++

+++Max (Lighten)


TheMaxBlending mode will pick the higher value between the background and the foreground.





+++

+++Min (Darken)


TheMinBlending mode will pick the lower value between the background and the foreground.





+++

+++Switch


TheSwitchblending mode is similar to the Copy mode, with onecrucialdifference:



* 'Opacity' set to 0: The stream of nodes connected to the 'Foreground' inputwon't be computed.


* 'Opacity' set to 1: The stream of nodes connected to the 'Background' inputwon't be computed.




Therefore, this mode may be used to improve the performances of your graph.





TheSwitchandSwitch grayscalenodes are setup to use the blend nodes in these specific configurations.



[Switch](../../../node-library/filters/blending/switch/switch.md)

[Switch grayscale](../../../node-library/filters/blending/switch/switch.md)



+++

+++Divide


TheDivideblending mode will divide the background input pixels value by each corresponding pixel in the foreground.





+++

+++Overlay


TheOverlayblending mode combines Multiply and Screen blend modes:



* If the value of the lower layer pixel is below 0.5, then aMultiplytype blending is appliedIf the value of the lower layer pixel is above 0.5, then aScreentype blending is applied


* If the value of the lower layer pixel is below 0.5, then aMultiplytype blending is applied


* If the value of the lower layer pixel is above 0.5, then aScreentype blending is applied




+++

+++Screen


With Screen blend mode the values of the pixels in the two inputs are inverted, multiplied, and then inverted again.





The result is the opposite effect to multiply and is always equal or higher (brighter) compared to the original.





+++

+++Soft light


The Soft Light blend mode creates a subtle lighter or darker result depending on the brightness of the foreground color.





Blend colors that are more than 50% brightness will lighten the background pixels and colors that are less than 50% brightness will darken the background pixels.





+++
