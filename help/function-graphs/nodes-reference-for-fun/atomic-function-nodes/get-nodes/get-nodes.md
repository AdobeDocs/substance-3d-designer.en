---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/get-nodes.html"
breadcrumb-title: ""
description: Access Get nodes in Substance 3D Designer function graphs to retrieve variable values and data.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Variables
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Variables
user-guide-description: ""
user-guide-title: ""
---

# Variables

Variables are a way of <b>storing values</b> to fetch it later (<b>Get</b>) and/or modify it (<b>Set</b>).

![Substance function graph - Get float](get-nodes.resources/get-nodes-01.gif "Substance function graph - Get float"){zoomable="yes"}

What a Get node essentially does, is grab a dynamic Variable, and return it from the Get Nodes' output for use in a function. These Get nodes form the link between the Input Parameters defined in the [graph parameters](../../../../compositing-graphs/graph-parameters/graph-parameters.md) and [parameter functions](../../../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md).

Every time you use a Get node, you must pick an available value from the dropdown menu. Get nodes will <b>grab a value of the corresponding type</b>. That means you will only see valid options in the menu of a Get node, you can never pick an invalid option. If a variable is not available, it means there's a type mismatch

There are a number of <b>&quot;System&quot; Variables</b>: pre-defined special variables that you can not declare yourself. These are quite important, and for the nodes below it is listed what System variables are available.

When a parameter is [exposed](../../../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md), it consists of applying a parameter function on it which only includes a Get node of the correct type.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Get

</td>
<td style="border: 0;" valign="top">

### Set

</td>
<td style="border: 0;" valign="top">

### Is defined

</td>
</tr>
</table>

## Get

<table>
<tr style="border: 0;">
<td width="25.00%" style="border: 0;" valign="top">

![Get float2 - Icon](get-nodes.resources/get-nodes-02.png "Get float2 - Icon"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

These nodes let you fetch the value of a variable which exists *in the current scope*.

The name of the variable being fetched is set in the Properties dock.

</td>
</tr>
</table>

'Get' nodes some limitations you need to be mindful of:

* <b>They are typed</b>, therefore you need to make sure the variable holds a value of the same type as the node. Type mismatches are reported in the Console.
* <b>They do not check for the existence of the variable</b> in the current scope. Unfound variables are reported in the Console.
* In complex functions using control flow nodes such as Sequence, be mindful about the <b>order in which you set and get variables</b>. When Designer detects a case of 'Get before Set', it is reported in the Console.

>[!NOTE]
>
> Built-in variables
> 
> Several 'Get' nodes will offer built-in variables to access existing values according to the current context – E.g.: the current pixel position in a Pixel processor, the current tiling mode of a node, ...
> 
> All built-in variables are listed in [this dedicated page](../../../../function-graphs/variables/system-variables/system-variables.md).

### Get nodes

+++Floats
![Get float - Icon](get-nodes.resources/get-nodes-03.png "Get float - Icon"){width="200px"}



Get Float

![Get float2 - Icon](get-nodes.resources/get-nodes-02.png "Get float2 - Icon"){width="200px"}



Get Float2

![Get float3 - Icon](get-nodes.resources/get-nodes-04.png "Get float3 - Icon"){width="200px"}



Get Float3

![Get float4 - Icon](get-nodes.resources/get-nodes-05.png "Get float4 - Icon"){width="200px"}



Get Float4

+++

+++Integers
![Get integer - Icon](get-nodes.resources/get-nodes-06.png "Get integer - Icon"){width="200px"}



Get Integer

![Get integer2 - Icon](get-nodes.resources/get-nodes-07.png "Get integer2 - Icon"){width="200px"}



Get Integer2

![Get integer3 - Icon](get-nodes.resources/get-nodes-08.png "Get integer3 - Icon"){width="200px"}



Get Integer3

![Get integer4 - Icon](get-nodes.resources/get-nodes-09.png "Get integer4 - Icon"){width="200px"}



Get Integer4

+++

+++Others
![Get boolean - Icon](get-nodes.resources/get-nodes-10.png "Get boolean - Icon"){width="200px"}



Get Boolean

![Get string - Icon](get-nodes.resources/get-nodes-11.png "Get string - Icon"){width="200px"}



Get String

+++

## Set

<table>
<tr style="border: 0;">
<td width="25.00%" style="border: 0;" valign="top">

![Set: Node icon](get-nodes.resources/get-nodes-12.png "Set: Node icon"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Text

</td>
</tr>
</table>

## Is defined

<table>
<tr style="border: 0;">
<td width="25.00%" style="border: 0;" valign="top">

![Is defined: Node icon](get-nodes.resources/get-nodes-13.png "Is defined: Node icon"){width="200px"}

</td>
<td width="100.00%" style="border: 0;" valign="top">

Text

</td>
</tr>
</table>
