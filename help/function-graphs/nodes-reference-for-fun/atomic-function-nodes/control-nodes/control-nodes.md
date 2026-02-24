---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/control-nodes.html"
breadcrumb-title: ""
description: Access control nodes in Substance 3D Designer function graphs to control flow and execution logic.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Control
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Control
user-guide-description: ""
user-guide-title: ""
---



# Control nodes

This page describes nodes of [Function graphs](../../../../help/function-graphs/the-function-graph/the-function-graph.md) which purpose is controlling the *flow of execution*.

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![If...Else node](https://helpx.adobe.com/content/dam/substance-3d-designer/function-graphs/nodes/atomic-function-nodes/control/IfElse_Node.jpg "If...Else node")

</td>
<td width="100.00%" style="border: 0;" valign="top">

## If...Else

Similarly to programming langages, the If... Else node introduces the possibility to filter the result according to predefined conditions.

</td>
</tr>
</table>

You will use this node in conjunction with the[ Logical nodes](../../../../help/function-graphs/nodes-reference-for-fun/atomic-function-nodes/logical-nodes/logical-nodes.md) and the [Comparison nodes](../../../../help/function-graphs/nodes-reference-for-fun/atomic-function-nodes/comparison-nodes/comparison-nodes.md) that will help you build the condition to check.

+++Input connectors
<b>Condition</b> *Boolean*  
The condition that controls the node's output.

<b>If</b> *Variabe type*The value output by the node if <b>Condition</b> is *True*.

<b>Else</b> *Variabe type*The value output by the node if <b>Condition</b> is *False*.

+++

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Sequence node](https://helpx.adobe.com/content/dam/substance-3d-designer/function-graphs/nodes/atomic-function-nodes/control/Sequence_Node.jpg "Sequence node")

</td>
<td width="100.00%" style="border: 0;" valign="top">

## Sequence

Ensures a portion of the graph is computed before another one.

</td>
</tr>
</table>

This is critical for controlling the state of variables are they are created, read and updated.

You may learn more about the Sequence node in the [Using the Set/Sequence nodes](../../../../help/function-graphs/fxmaps/using-functions-in-fxmaps/using-the-set-sequence/using-the-set-sequence-nodes.md) page of this documentation.

+++Input connectors
<b>In</b> *Variable type*  
The portion of the graph that should be computed first

<b>Last</b> *Variable type*  
The portion of the graph that should be computed last

+++

<table>
<tr style="border: 0;">
<td width="33.33%" style="border: 0;" valign="top">

![Whle Loop node](https://helpx.adobe.com/content/dam/substance-3d-designer/function-graphs/nodes/atomic-function-nodes/control/WhileLoop-Node.jpg "Whle Loop node")

</td>
<td width="100.00%" style="border: 0;" valign="top">

## While Loop

Executes the <b>Init</b> branch once, then iterates over the <b>Exit Cond.</b> and <b>Loop Body</b> branches until the <b>Exit Cond.</b> branch returns *True*.

Once the loop is completed, the node outputs the result of the <b>Loop Body</b>'s last iteration.

</td>
</tr>
</table>

Loops have an implicit maximum number of iterations which can be disabled by setting it to -1.

Variables retain their value across iterations, and can be accessed in the exit condition (Exit Cond.).  
This means you may add to an index value every iteration and check its value in the exit condition to control the number of loops you need.

>[!IMPORTANT]
>
> Nodes connected to the <b>Exit Cond.</b> and <b>Loop Body</b> branches cannot be connected to other branches of the graph.

+++Input connectors
<b>Init.</b> *Variable type*  
The portion of the graph that is computed before the first iteration – I.e. the start of the loop.

<b>Exit Cond.</b> *Boolean*  
The condition that needs to be true for the loop to stop. It is recomputed on each iteration.  
*Note:* The maximum number of iterations is still limited to the <b>Max iterations</b> parameter.

<b>Loop Body</b> *Variable type*  
The graph that benefits from the loop. It is recomputed on each iteration.

+++

+++Parameters
<b>Max. iterations</b> *Integer*  
The maximum number of iterations performed by the node.  
The node stops iterating when whichever of the following criteria is met first: this maximum number is reached or the exit condition becomes true .  
This maximum can be disabled by setting the value to *-1*. At that point, only the exit condition can stop the iterations.

Setting 'Max. iterations' to -1 improves performances in small loops as there is one less counter to keep track and update.

However, be mindful of how the node is configured as it is possible to produce an <b>infinite loop</b> that may result in Designer becoming unresponsive.

+++

Check out this tutorial about the While Loop node:
