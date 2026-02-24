---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/vector-and-swizzle-nodes.html"
breadcrumb-title: ""
description: Use vector and swizzle nodes in Substance 3D Designer function graphs to manipulate vector data and components.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Vector
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Vector
user-guide-description: ""
user-guide-title: ""
---


# Vector and Swizzle nodes

Vector and Swizzle Nodes allow you to respectively Construct and Deconstruct Vector nodes from and into separate components.They are similar to [RGBA Merge](../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/channels/rgba-merge/rgba-merge.md) and [RGBA Split](../../../../help/compositing-graphs/nodes-reference-for-com/node-library/filters/channels/rgba-split/rgba-split.md), but then for Function Graphs. They are also a prime method for converting between Vector Data types, as [Casting ](../../../../help/function-graphs/nodes-reference-for-fun/atomic-function-nodes/cast-nodes/cast-nodes.md)is not an option in a lot of cases.

## Vector Nodes

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

Vector Nodes allow you to combine Vector or elements with fewer components, into Vectors with more components. There are a few specific rules or limitations for Vector nodes:

* Vector Nodes have **only two inputs**, even if the resulting Vector has more than 2 components.
* Vector Inputs are **not limited to one type**: they can take any lesser component as input.
* The order of the result output is determined by the **order of the Inputs**.

That means the following methods are best used:

* Construct a Vector 4 in two ways: either connect two 2-component Vectors, or connect a 1-component and a 3-component Vector.
* If you want to construct a 3 or 4 component Vector from single Integers or Float, you must first do at least one Vector 2 combination before you can combine them into a 3-component Vector.

Think well about the order of connections. Connection order of inputs is illustrated below.

![](vector-int1.png){width="200px"}

Example on Left Connects first an Integer(1) and then an Integer 3. Result is as below

| Output | X | Y | Z | W |
| --- | --- | --- | --- | --- |
| Input 1 | 0 |  |  |  |
| Input 2 |  | 1 | 2 | 4 |

![](vector-int2.png){width="200px"}

Example on Left swaps inputs around from first example, first Integer 3, then a Integer(1).

| Output | X | Y | Z | W |
| --- | --- | --- | --- | --- |
| Input 1 | 1 | 2 | 4 |  |
| Input 2 |  |  |  | 0 |

</td>
<td style="border: 0;" valign="top">

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="fn-vector-vectorint4.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c1_image" src="fn-vector-vectorint2.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r0-column-c2_image" src="fn-vector-vectorint3.png"/></div> |
| --- | --- | --- |
| **Vector Integer2** | **Vector Integer3** | **Vector Integer4** |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r2-column-c0_image" src="fn-vector-vectofloat3.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r2-column-c1_image" src="fn-vector-vectofloat2.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell1_position-par_dx_table_row-r2-column-c2_image" src="fn-vector-vectofloat4.png"/></div> |
| **Vector Float2** | **Vector Float3** | **Vector Float4** |

</td>
</tr>
</table>

## Swizzle Nodes

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

Swizzle Nodes deconstruct or split off components from multi-component Vectors, allowing you to utilize X, Y, Z and W components individually as well as swap them around. The following rules and limitations apply:

* Swizzle nodes have **only one output**.
* Swizzle Nodes **take any Input** of the correct type (Int or Float).

### Split Components

The most common usecase for Swizzle is to use it to split components, such as braking an Integer4 down into 4 individual Integers. The limitations do mean you will need four separate Swizzle Integer nodes for this.

Any other kind of split is also possible for an Integer4, such as two Integer2, or an Integer and an Integer3, again keeping in mind every result needs its own node.

### Swap/Swizzle Components

Like the name suggests, Swizzle can be used to change the order of values or even overwriting values. You can change the order from X,Y,Z,W to W,Y,X,Z, and you can change the values from X,Y,Z,W to X,X,X,W for example.

</td>
<td style="border: 0;" valign="top">

| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r0-column-c0_image" src="fn-vector-swizzleint1.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r0-column-c1_image" src="fn-vector-swizzleint2.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r0-column-c2_image" src="fn-vector-swizzleint3.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r0-column-c3_image" src="fn-vector-swizzleint4.png"/></div> |
| --- | --- | --- | --- |
| **Swizzle Integer** | **Swizzle** **Integer2** | **Swizzle** **Integer3** | **Swizzle** **Integer4** |
| <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r2-column-c0_image" src="fn-vector-swizzlefloat1.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r2-column-c1_image" src="fn-vector-swizzlefloat2.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r2-column-c2_image" src="fn-vector-swizzlefloat3.png"/></div> | <div><img class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid1_items_grid-cell1_position-par_dx_table_row-r2-column-c3_image" src="fn-vector-swizzlefloat4.png"/></div> |
| **Swizzle** **Float** | **Swizzle** **Float2** | **Swizzle** **Float3** | **Swizzle** **Float4** |

</td>
</tr>
</table>
