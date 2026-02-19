---
title: "Built-in variables"
description: "Learn about built-in system variables available in Substance 3D Designer function graphs for advanced workflows."
helpx_description: Designer > Function graphs > Variables > Built-in variables
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/variables/system-variables.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - data-visualizations
  - infographic
  - data-and-analytics
---




# Built-in variables

You can use built-in variables in [Substance function graphs](../../function-graphs.md) order to access specific values. They always begin with a `$` (Dollar) symbol.

Some variables are only available in specific contexts.

<b>All nodes</b>

System variables

| Name | Type | Purpose |
| --- | --- | --- |
| $size | Float2 | Returns the size of the current node in pixels.   If used in the [Output Size](../../../compositing-graphs/output-size/output-size.md) parameter set to a *Relative to...* [inheritance method](../../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md), returns the *inherited value*. |
| $sizelog2 | Float2 | As above, but returns the size as power-of-2 values (ex: for 2048\*2048 image, `$sizelog2` returns 11).   If used in the [Output Size](../../../compositing-graphs/output-size/output-size.md) parameter set to a *Relative to...* [inheritance method](../../../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md), returns the *inherited value*. |
| $pixelratio | Integer | Returns an integer value corresponding to the current node pixel ratio (inherited or absolute):   0: Stretch 1: Square |
| $tiling | Integer | Returns an integer value corresponding to the current node tiling mode (inherited or absolute):   0: No Tiling 1: Horizontal Tiling 2: Vertical Tiling 3: H and V Tiling |
| $physicalsize | Float3 | Returns the [graph's](../../../compositing-graphs/graph-parameters/graph-parameters.md) <b>Physical size</b> property value. |
| $uvtile | Integer2 | When using UDIM workflows, this variable returns the index of the current udim in U and V.   E.g., (2, 0) for tile 1003, (7, 11) for tile 1118, ... |

<b>FX-Map</b>

System variables

| Name | Type | Purpose |
| --- | --- | --- |
| $pos | Float2 | Returns the birth position of the pattern. The origin (0, 0) is located at the top left corner of the image. |
| $depth | Float | Returns the octave (level) number of the [FX-Map](../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/fx-map/fx-map.md) node. This allows a node to modify its behavior according to which level in the quad-tree it represents. |
| $depthpow2 | Float | As above, but returns the multiplicative inverse of 2 raised to the power of the octave (level) number – i.e. 1/(2^octave). This is a helper value that comes in useful for some common calculations. |
| $number | Float | Returns the number of the drawn pattern. This can be accessed by Dynamic Function graphs controlling an [Iterate](../../fxmaps/using-functions-in-fxmaps/iterate-and-number-var/iterate-and-number-variable.md) node to modify its behavior at each iteration step.   Note that `$number` starts counting from 0, not 1.   When using a chain of Iterate nodes, the `$number` variable will return the iteration number from the last Iterate node connected before the function parameter it is used. If you want to retrieve the iteration number from multiple Iterate nodes, you should use "custom variables" through [Set](../../fxmaps/using-functions-in-fxmaps/using-the-set-sequence/using-the-set-sequence-nodes.md) nodes. |

<b>Pixel processor</b>

System variables

| Name | Type | Purpose |
| --- | --- | --- |
| $pos | Float2 | Returns the position of the pixel being evaluated. |

<b>Global</b>

System variables

| Name | Type | Purpose |
| --- | --- | --- |
| $time | Float | This variable returns the time in seconds since the Substance Engine was started. It may be used in graphs which result should change according to elapsed time.  **Note:**  While there is currently no way to make this value change in Designer, applications that integrate the Substance Engine can leverage it, such as [Substance Player](https://helpx.adobe.com/substance-3d-player/home.html) for animation or [Substance 3D Painter](https://helpx.adobe.com/substance-3d-painter/home.html) for [dynamic strokes](https://helpx.adobe.com/substance-3d-painter/painting/dynamic-strokes/creating-custom-dynamic-strokes.html). |
| $normalformat | Integer | The normal format (I.e., DirectX or OpenGL) that used in the current environment.  **Note:**  This variable has no effect in Designer and may be used by other applications that integrate the Substance Engine. |
