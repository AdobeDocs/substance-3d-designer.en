---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/fxmaps/the-iterate-node.html"
breadcrumb-title: ""
description: Use the Iterate node in FXMaps to create repeating patterns and procedural variations in your materials.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > FXMaps > The Iterate Node
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: The Iterate Node
user-guide-description: ""
user-guide-title: ""
---



# The Iterate Node

The Iterate node lets you multiply a Quadrant node’s images and is essentially a “repeater” node. A Quadrant node at a depth of 1 would normally output 4 quadrants. The Iterate node lets you repeat its output imagery as many times as you like, with each set of repeats treated separately.

The Iterate node has no other properties beyond a “How repetitions do you want?” parameter. The result is that the new images are, by default, simply overlaid on, and blended with, those produced by the Quadrant node.

The Iterate node repeats the received input image. The number of repetitions is defined by its Iterations property:

The key to using the Iterate node is that any dynamic functions attached to each repeated image will also be processed. This means each repetition can have its own set of unique adjustments. You can use the Random Seed property of the Iterate node to modify how this works. You can also access the *$number* system variable within your dynamic functions to determine which repetition is currently being rendered, and modify the function's result accordingly.

For example: if you apply a random rotation to each image in a Quadrant node, then feed that Quadrant node’s output to an Iterate node’s active input, each of the repeated images will also have its own random rotation.

All the same dynamic features available on the Quadrant node also apply to the repeated images produced by the Iterate node. It’s as if the node duplicated the Quadrant node at the same level, instead of adding another depth level.

## The Pass-through Connector

Each Iterate node has two connectors along its base. The left connector is a pass-through connector. The image it receives is passed straight through to the node’s output connector, where it is blended with any repeated images:

Note that the pass-through image is always passed through untouched, regardless of the Iteration parameter’s setting.

![](iterate.jpg)
