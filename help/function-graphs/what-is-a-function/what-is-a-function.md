---
title: "What is a function "
description: "Learn what functions are in Substance 3D Designer and how to use them to create reusable node networks."
helpx_description: "Designer > Function graphs > What is a function "
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/what-is-a-function.html"
helpx_creative_field:
  - painting-illustration
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - graphs
  - data-and-analytics
  - data-visualizations
---




# What is a function ?

Functions in Substance 3D Designer allows the user to generate results using the logic you would otherwise find in a programming language.

But rather than using lines of codes, functions in Designer keeps the same nodal approach. At first sight, a function graph looks really similar to a regular graph.

![](image2015-12-17-18-19-37.png)

You can encounter functions in 2 main cases:

* to control the result of a parameter
* if you edit a pixel processor

## Control the result of a parameter

In Substance 3D Designer, any parameter can be controlled by a function.

![](image2015-12-17-21-3-46.png)

Therefore you can imagine rules and dependencies between parts of your graph, to obtain unique results.

For example you can decide that the opacity of a blend node will be half of the intensity of a warp node :

![](warpblend.gif)

In fact, you may already have created functions without being aware of it:

if you have exposed a parameter, you have automatically created a function,and a variable: the function contains a get float node that catches the value of the newly created variable:

![](expose.gif)
