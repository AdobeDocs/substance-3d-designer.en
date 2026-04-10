---
helpx_url: ""
breadcrumb-title: ""
description: Access constant nodes in Substance 3D Designer to define constant values in Substance graphs.
helpx_creative_field: ""
helpx_description: ""
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Constant
user-guide-description: ""
user-guide-title: ""
---

# Constant

Constant nodes are a way to create a static value for use inside Substance graphs.

They all include a simple [Value processor](../../atomic-nodes/value-processor/value-processor.md) node generating the value.

## Integers

Constant integers generate whole numbers, and have a step of 1.

[They can be converted to Float,](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/cast-nodes/cast-nodes.md) which is recommended to do when performing any operation more complex than additions, subtractions and simple comparisons.

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Integer type icon](../../../../assets/fn-constant-integer.png "Integer type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Integer</b>

An integer has a single component. It is useful as an index for making selections, such as:

* selecting an option presented to the user as a drop down menu (see 'Drop down list' in [this page](../../../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md)).
* selecting the input of a [Multi switch](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blending/multi-switch/multi-switch.md) node.<b></b>

>[!IMPORTANT]
>
> <b>Negative integers</b> in parameter functions are *not supported*. See [this page](../../../../technical-issues/parameters-not-working/parameters-not-working-as-expected.md) in the 'Technical issues' section for a workaround.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Integer2 type icon](../../../../assets/fn-constant-integer2.png "Integer2 type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Integer2</b>

An Integer2 node generates a static 2-component integer vector with (X, Y) components.

One common use case of Integer2 is setting to set X and Y grid sizes, as in the [Tile generator](../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md) node.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Integer3 type icon](../../../../assets/fn-constant-integer3.png "Integer3 type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Integer3</b>

An Integer3 node generates a static 3-component integer vector with (X, Y, Z) components.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Integer4 type icon](../../../../assets/fn-constant-integer4.png "Integer4 type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Integer4</b>

An Integer4 node generates a static 4-component integer vector with (X, Y, Z, W) components.

</td>
</tr>
</table>

## Floats

Constant Float values generate fractional numbers, I.e. they support values after the decimal sign, and can be adjusted in steps smaller than 1. (Default: 0.01)

[Floats can be converted to Integers](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/cast-nodes/cast-nodes.md) but they will be rounded up or down to the nearest Integer, meaning data and accuracy is lost.

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Float type icon](../../../../assets/fn-constant-float.png "Float type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Float</b>

A Float has a single component and is very commonly used for any single value that requires precision.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Float2 type icon](../../../../assets/fn-constant-float2.png "Float2 type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Float2</b>

A Float2 node generates a 2-component vector with (X, Y) components.

Float2 is commonly used for [sampling coordinates](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/sampler-nodes/sampler-nodes.md), [offset transformations](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/transforms.md) and general 2D vector manipulation.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Float3 type icon](../../../../assets/fn-constant-float3.png "Float3 type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Float3</b>

A Float3 node generates a 3-component (X, Y, Z) vector.

Float3 is mainly used when working with 3D objects and [3D scale coordinates](../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d/cube-3d.md) such as in [3D SDF nodes](../../../../function-graphs/nodes-reference-for-fun/function-node-library/function-node-library.md#sdf-functions), and as a simpler way to store RGB colors — I.e. without Alpha.

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Float4 type icon](../../../../assets/fn-constant-float4.png "Float4 type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Float4</b>

A Float4 generates a 4-component (X, Y, Z, W) vector.

Float4 is the preferred way to store and set color information where XYZW values are mapped to RGBA, such as in the [Uniform color node](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/uniform-color/uniform-color.md).

</td>
</tr>
</table>

## Non-numerical

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Boolean type icon](../../../../assets/fn-constant-boolean.png "Boolean type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Boolean</b>

A Boolean is the simplest data type there is, knowing only two states: <code>true</code> or <code>false</code>.

This type is quite common when working with toggle parameters and [If/Else](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/control-nodes/control-nodes.md) conditions.<br>Booleans are an simple and efficient way of controlling the flow of a function or graph, e.g. using a [Switch Node](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blending/switch/switch.md).

</td>
</tr>
</table>
