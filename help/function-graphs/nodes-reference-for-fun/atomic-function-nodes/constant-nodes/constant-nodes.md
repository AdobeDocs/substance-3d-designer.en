---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/constant-nodes.html"
breadcrumb-title: ""
description: Access constant nodes in Substance 3D Designer function graphs to define constant values and parameters.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Constant
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Constant
user-guide-description: ""
user-guide-title: ""
---

# Constant

Constant nodes are a way to create a static value for use inside Substance function graphs. Unlike [variables](../../../../function-graphs/variables/variables.md), they cannot be modified externally.

Additionally, this page provides some extra information for each data type and common use cases.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Integers

</td>
<td style="border: 0;" valign="top">

### Floats

</td>
<td style="border: 0;" valign="top">

### Others

</td>
</tr>
</table>

## Integers

Constant integers generate whole numbers, and have a step of  1.

[They can be converted to Float,](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/cast-nodes/cast-nodes.md) which is recommended to do when performing any operation more complex than additions, subtractions and simple comparisons.

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Integer type icon](../../../../assets/fn-constant-integer.png "Integer type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Integer</b>

An integer has a single component. It is useful as an index for making selections, such as:

* selecting an option presented to the user as a drop down menu (see 'Drop down list' in [this page](../../../../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md)).
* selecting the input of a [Multi switch](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blending/multi-switch/multi-switch.md) node.<b></b>

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

Integer2 is not common, but is used for example to set X and Y 2D tiling in a [Tile generator](../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/tile-generator/tile-generator.md).

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

Integer 3 is not common and is unlikely to be encountered much.<b>  
</b>

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

Integer 4 is not common and is unlikely to be encountered much.<b>  
</b>

</td>
</tr>
</table>

## Floats

Constant Floats generate fractional numbers, not wholenumbers, which means they will always have values after the decimal sign, and can in- or decrease by steps smaller than 1 (default 0.01).

[Floats can be converted to Integers](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/cast-nodes/cast-nodes.md) but they will be rounded up or down to the nearest Integer, meaning data and accuracy is lost.

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Float type icon](../../../../assets/fn-constant-float.png "Float type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Float</b>

A Float, has a single component, the (1) is omitted from the name for brevity. Float is very common and used for any value that requires precise control in the form of a slider or Angle. You can find it in almost every Node's parameters. It is also the preferred data type for a grayscale value!<b></b>

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

A Float2 node generates a static 2-component Float Vector. Components are named X, Y. Float2 is quite common and is used for [sampling coordinates](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/sampler-nodes/sampler-nodes.md), and for [Transformation Offsets](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/transforms/transforms.md)

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

A Float3 node generates a static 3-component Float Vector. Components are named X,Y,Z. Float3 is uncommon, it is mainly used to represent [3D scale coordinates](../../../../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/patterns/cube-3d/cube-3d.md), and as a simpler way to store color without Alpha data.<b>  
</b>

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

A Float4 generates a static 4-component Float Vector.Components are named X,Y,Z,W. Float4 is very common, as it is the preferred way to store and set [Color information, where XYZW data represents RGBA values.](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/uniform-color/uniform-color.md)<b>  
</b>

</td>
</tr>
</table>

## Others

Two additional data types exist inside Substance function graphs: booleans and strings. Strings were introduced alongside the [Text](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/text/text.md) node in Designer version 6.

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Boolean type icon](../../../../assets/fn-constant-boolean.png "Boolean type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>Boolean</b>

A Boolean is the simplest data type there is, knowing only two states: True or False, 1 or 0. It is represented by the color white. It is not possible to interchange between Boolean and Integer without [Casting](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/cast-nodes/cast-nodes.md), or by using [Logical Nodes.](../../../../function-graphs/nodes-reference-for-fun/atomic-function-nodes/logical-nodes/logical-nodes.md) A Boolean is quite common and it's an excellent way to control the flow of a function or graph, a typical use would be for a [Switch Node.](../../../../compositing-graphs/nodes-reference-for-com/node-library/filters/blending/switch/switch.md)<b></b>

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![String type icon](../../../../assets/fn-constant-string.png "String type icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

<b>String</b>

A String Node generates a static String, a piece of text. It is the most exotic type of Data available in Functions, and generally can not be used much in conjunction with other Function nodes. It's main goal is to function as a final output for the [Text Node.](../../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/text/text.md)

</td>
</tr>
</table>
