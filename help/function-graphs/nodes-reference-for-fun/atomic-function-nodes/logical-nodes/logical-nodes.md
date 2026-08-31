---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/logical-nodes.html"
breadcrumb-title: ""
description: Access logical nodes in Substance 3D Designer function graphs to perform boolean logic operations and comparisons.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Logical
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Logical
user-guide-description: ""
user-guide-title: ""
---

# Logical nodes

Logical nodes are used to add multiple conditions to your graph:

![](logical-nodes.resources/logical-nodes-01.png)

## The *And* node

![](logical-nodes.resources/logical-nodes-02.png)

The And node takes two Boolean nodes as input:

* If both of the inputs are True, then the output of the *And* node will be *True*
* In any other case the *And* node will return *False*

## The *Or* node

![](logical-nodes.resources/logical-nodes-03.png)

The Or node takes two Boolean nodes as input:

* If at least one of the input isTrue (1), then the output of the *Or* node will be *True*
* If both of the inputs are False, the *Or* node will return *False*

## The *Not* node

![](logical-nodes.resources/logical-nodes-04.png)

The Not node takes a Boolean as input: it will will look at the input value and return its opposite:

* *True* input gives *False* output
* *False* input gives *True* output
