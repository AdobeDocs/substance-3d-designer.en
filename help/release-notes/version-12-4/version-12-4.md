---
title: "Version 12.4"
description: ""
helpx_description: "Designer > Release Notes > Version 12.4"
---

# Version 12.4

**Substance 3D Designer 12.4** brings several quality of life improvements (a tool to clean a graph, using basic formulas to set parameters, a button to generate random seed, a lock for size, etc.) and support of Substance model graphs in the Python API. See below for more details about all these changes.

Release date: *January 31st, 2023*

## Quality of Life improvements

### Clean graph tool

When you edit your graph, you sometimes have to experiment several possibilities, and plug / unplug various nodes until the moment you get the result you want. Then at the end, you have some nodes in your graph that are not connected to an output, therefore have no impact on the final result. This new tool will allow you to automatically detect and delete those nodes in order to clean your graphs before finalizing them. The cleaning tool is also optionally looking in parameters functions, and can be launched on the current graph through the dedicated button in the Graph View toolbar, or on a selection of graphs from the Explorer view.

![](final-clean.gif){width="640px"}

### Type formulas in parameters fields

No need to use a calculator or to compute in your head anymore when you want to enter specific parameter values. You can now directly enter basic formulas like additions, divisions, mutliplications or subtractions when setting a numeric value for a parameter in the [Properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html) and other places in the application.

![](final-formula.gif){width="640px"}

### Quick access buttons in the 3D View

We have added an additional toolbar in the [3D view](../../interface/3d-view/3d-view.md) corresponding to all the options available in the [Display](../../interface/3d-view/3d-view.md) menu, for quick access to all these options (E.g., Wireframe, Grid, Bounding Box, etc.) as button toggles. We also added a toggle to show / hide the environment map.

![](final-3dview.gif){width="640px"}

### Button to generate a Random Seed

You can now quickly create different variations by using a new button to generate the random seed for your graph, instead of moving a slider.

![](final-seed.gif){width="640px"}

### Lock for the Output Size widget

You can now lock the width and the height of the Output Size in order to make sure to keep a square size and avoid to manipulate the two values each time you want to update them.

![](final-lock.gif){width="640px"}

### Transform image input to Color/Greyscale

Quickly switch between an [Input Color](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/input/input.md) and an [Input Greyscale](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/input/input.md) through the node contextual menu.

![](final-switch.gif){width="640px"}

### Select clicked pin when displaying the Gradient Editor

In the property panel, if you click a pin to edit a gradient, you will now automatically select the corresponding pin in the displayed [Gradient Editor](../../compositing-graphs/nodes-reference-for-com/atomic-nodes/gradient-map/gradient-map.md).

![](final-gradient.gif){width="640px"}

### Select downstream nodes

New entry in the [node contextual menu](../../interface/the-graph-view/the-graph-view.md) to select all the nodes connected to the output of the selected node(s), directly or indirectly. So you select all the nodes impacted by your node. Useful to delete part of your graph or to rework the graph layout.

![](final-downstream.gif){width="640px"}

## Python API Updates

This 12.4 version brings also the full support of Substance model graphs through the Python API. It means that you have now all required tools to create, edit, or evaluate Substance model graphs. For full details, take a look at the documentation available from the software Help menu.

## Release notes

### 12.4.0

*(Released January 24, 2023)*

<b>Added:</b>

* &#91;3D View&#93; Add quick access buttons to set display options (Wireframe, environment map, scene stats, etc.)
* &#91;Color management&#93; Improve quality of baked 3D LUTs in ACE mode
* &#91;Documentation&#93; Sample projects for Substance graphs
* &#91;Documentation&#93; Sample project for function graphs
* &#91;Explorer&#93; Allow moving Graph and Resources from one parent to another without closing or invalidating widgets
* &#91;Gradient Editor&#93; Select clicked pin when displaying the gradient editor
* &#91;Graph&#93; Add option in a node's contextual menu to select all its children
* &#91;Graph&#93; Clean graph tool to detect and remove unused nodes in all graphs types and property graphs
* &#91;Graph&#93; Transform image input to color/greyscale
* &#91;Parameters&#93; Add a lock on integer2 widgets
* &#91;Parameters&#93; Allow to type basic formulas as a parameter
* &#91;Substance model&#93; Toggle to switch between values and icons for value nodes
* &#91;UI&#93; Button to generate a random value when a random seed is required
* &#91;UI&#93; Highlight in the 3D View the item currently selected in the Scene Browser
* &#91;UX&#93; Reset slider ranges when their value is reset
* &#91;API&#93; Allow adding actions to graph view toolbars
* &#91;API&#93; Allow to create/edit/evaluate a Substance model graph from the API

<b>Fixed:</b>

* &#91;3D View&#93; 'DirectX Normal' property value is not shared across renderers
* &#91;3D View&#93; Scene statistics display is stretched when viewport is small
* &#91;3D View&#93; Wireframe display property is not saved
* &#91;Content&#93; Radial Blur Color parameters have no effect on the alpha channel
* &#91;Localization&#93; Additional sliders and buttons are displayed in Enviroment OpenGL Properties.
* &#91;MDL&#93;&#91;Substance model&#93; Crash when deleting exposed nodes
* &#91;Preferences&#93; Default\_config file is never recreated if deleted
* &#91;Substance model&#93; Crash reordering parameter that doesn't appears at instance level
* &#91;API&#93; SDProperty.getDefaultValue() almost always returns None
