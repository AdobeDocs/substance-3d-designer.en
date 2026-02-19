---
title: "Get a variable value"
description: "Learn how to retrieve variable values in Substance 3D Designer function graphs using the Get Variable node."
helpx_description: Designer > Function graphs > Variables > Get a variable value
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/variables/get-a-variable-value.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - nodes
  - smart-object
  - puppet
---




# Get a variable value

In order to use a variable in a function, you need to "call" it, meaning to need to import the value of the variable into the function.

To do so you need to use a *Get* node:

![](image2015-12-21-7-29-51.png)

There is different kinds of Get nodes: choose the right one according of the type of value you want to import:

![](image2015-12-21-7-31-4.png)

## Assign a variable to a Get node

By default, a get node will display a warning sign: it means that it is not linked to any variable yet.

To link a variable, go to the parameters, and choose one variable in "Variables/Get \*\*\*" list (\*\*\*will be replaced by the type of value your Get node can call).

The variable name will be displayed into the node:

![](assign-getfloat.gif)

Note that only the variables that are from the same type of the Get node will appear in the list.

>[!WARNING]
>
> Note that variables created with a *Set* node, will not appear in a *Get* node list.
> 
> But you can still get the variable by manually writing the name in the list.
> 
> Don't forget, that you can just call a variable created with a Set node, if :
> 
> * The Get and Set nodes are in function graphs controlling parameters of a same node
> * The parameter controlled by the *Get* node graph is either the same, or located below the parameter of the *Set* node graph, in the parameters stack..
