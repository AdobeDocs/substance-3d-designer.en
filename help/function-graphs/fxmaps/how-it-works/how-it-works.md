---
title: "How it works"
description: "Learn how FXMaps work in Substance 3D Designer to apply function graphs to textures for procedural effects."
helpx_description: Designer > Function graphs > FXMaps > How it works
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/fxmaps/how-it-works.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - infographic
  - data-visualizations
  - asset-warp
---




# How it works

Understanding how an FX-Map graph works is the key to mastering this powerful feature.

An FX-Map graph can contain one or more of the three FX-Map node types: Quadrant, Iterate and Switch. Of these nodes, the one you will likely use most often is the Quadrant, with the Iterate node a close second.

The Parameter Set node is the prime mover of FX-Maps. It creates the core region quad-tree graph FX-Maps rely on, but it is not displayed as one. Visually, the quad-tree graph is shown in the form of a Markov Chain.

When rendering the FX-Map, the simplified FX-Map graph is ‘unwrapped’ to look like the big tree-like graph. The engine “walks” the entire quad-tree, working top to bottom, then left to right.

FX-Map nodes don’t blindly copy and paste their images. When each image is rendered, any dynamic functions it has are run. The functions affect each image rendered by the node. You can therefore give each individual image a random rotation, or scale factor, or a number of other adjustments.
