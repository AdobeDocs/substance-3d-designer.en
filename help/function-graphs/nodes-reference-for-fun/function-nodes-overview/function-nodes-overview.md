---
title: "Function Nodes Overview"
description: ""
helpx_description: "Designer > Function graphs > Nodes reference for function graphs > Function Nodes Overview"
---

# Function Nodes Overview

This page provides a full overview of all function nodes and explains color coding used for Function Data Types.You can click through to more detailed pages with further explanations.

These function nodes are accessible by right-clicking in the graph function editor, and choosing Element, by pressing Spacebar or Tab in a function, or through the Functions section of the Library.

## Color Coding

Function Nodes and their Link wires are Color Coded according to the following scheme:

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Float Colors

### Float (1)

Lime Green

### Float2

Flat green

### Float3

Light Blue

### Float4

Flat Blue

</td>
<td style="border: 0;" valign="top">

### Integer Colors

### Integer(1)

Flat Yellow

### Integer2

Warm Yellow

### Integer3

Orange

### Integer4

Flat Red

</td>
<td style="border: 0;" valign="top">

### Other Colors

### Boolean

White

### String

Lila

</td>
</tr>
</table>

## Node List

| Element | Type | Input | Output | Description |
| --- | --- | --- | --- | --- |
| [Constant](../atomic-function-nodes/constant-nodes/constant-nodes.md) | Float | - | Float | Defines a constant floating value, eg 0.1 |
|  | Float2 | - | Float2 | Defines a constant vector of 2 floating values, eg (0.1, 0.2) |
|  | Float3 | - | Float3 | Defines a constant vector of 3 floating values, eg (0.1, 0.2, 0.3) |
|  | Float4 | - | Float4 | Defines a constant vector of 4 floating values, eg (0.1, 0.2, 0.3, 0.4) |
|  | Integer | - | Integer | Defines a constant integer value, eg 1 |
|  | Integer2 | - | Integer2 | Defines a constant vector of 2 integer values, eg (1, 2) |
|  | Integer3 | - | Integer3 | Defines a constant vector of 3 integer values, eg (1, 2, 3) |
|  | Integer4 | - | Integer4 | Defines a constant vector of 4 integer values, eg (1, 2, 3 ,4) |
|  | Boolean | - | Boolean | Defines a constant boolean value, eg True, or False |
|  | String | - | String | Defines a constant String value, eg "Substance" |
| [Vector](../atomic-function-nodes/vector-and-swizzle-nodes/vector-and-swizzle-nodes.md) | Vector Float2 | Float1 | Float 2 | Casts 2 floating values in a vector with 2 coordinates |
|  | Vector Float3 | Float1 / Float2 | Float 3 | Casts 2 floating values in a vector with 3 coordinates |
|  | Vector Float4 | Float1 / 2 / 3 | Float 4 | Casts 2 floating values in a vector with 4 coordinates |
|  | Swizzle Float1 | Vector Float | Float1 | Extracts a floating coordinate from a vector |
|  | Swizzle Float2 | Vector Float | Float2 | Extracts 2 floating coordinates from a vector |
|  | Swizzle Float3 | Vector Float | Float3 | Extracts 3 floating coordinates from a vector |
|  | Swizzle Float4 | Vector Float | Float4 | Extracts 4 floating coordinates from a vector |
|  | Vector Integer2 | Integer2 | Vector Integer2 | Casts 2 integer values in a vector with 2 coordinates |
|  | Vector Integer3 | Integer3 | Integer3 | Casts 2 integer values in a vector with 3 coordinates |
|  | Vector Integer4 | Integer4 | Integer4 | Casts 2 integer values in a vector with 4 coordinates |
|  | Swizzle Integer1 | Vector Integer | Integer1 | Extracts an integer coordinate from a vector |
|  | Swizzle Integer2 | Vector Integer | Integer2 | Extracts 2 integer coordinates from a vector |
|  | Swizzle Integer3 | Vector Integer | Integer3 | Extracts 3 integer coordinates from a vector |
|  | Swizzle Integer4 | Vector Integer | Integer4 | Extracts 4 integer coordinates from a vector |
| [Variables](../../variables/variables.md) | Set | any | input type | Sets a variable |
|  | Get Integer1 | - | Integer1 | Get a function or graph Integer value input |
|  | Get Integer2 | - | Integer2 | Get a function or graph Integer2 value input |
|  | Get Integer3 | - | Integer3 | Get a function or graph Integer3 value input |
|  | Get Integer4 | - | Integer4 | Get a function or graph Integer4 value input |
|  | Get Float1 | - | Float1 | Get a function or graph floating value input |
|  | Get Float2 | - | Float2 | Get a function or graph Float2 value input |
|  | Get Float3 | - | Float3 | Get a function or graph Float3 value input |
|  | Get Float4 | - | Float4 | Get a function or graph Float4 value input |
|  | Get Boolean | - | Boolean | Get a function or graph boolean value input |
| Samplers | Sample Grey | Vector Float2 | Float4 | Returns the greyscale value of an input image at the given UV coordinates (float2) |
|  | Sample Color | Vector Float2 | Float4 | Returns the color value of an input image at the given UV coordinates (float2) |
| Cast | To Float | Integer1 | Float1 | Converts an integer in a float |
|  | To Float2 | Integer2 | Float2 | Converts an Integer2 in a Float2 |
|  | To Float3 | Integer3 | Float3 | Converts an Integer3 in a Float3 |
|  | To Float4 | Integer4 | Float4 | Converts an Integer4 in a Float4 |
|  | To Integer | Float1 | Integer1 | Converts a Float in an Integer |
|  | To Integer2 | Float2 | Integer2 | Converts a Float2 in an Integer2 |
|  | To Integer3 | Float3 | Integer3 | Converts a Float3 in an Integer3 |
|  | To Integer4 | Float4 | Integer4 | Converts a Float4 in an Integer4 |
| [Operator](../atomic-function-nodes/operator-nodes/operator-nodes.md) | Add | Vector Float / Integer | Type of a &amp; b | Adds 2 values of the same type: a + b |
|  | Subtraction | Vector Float / Integer | Type of a &amp; b | Subtracts 2 values of the same type: a - b |
|  | Multiplication | Vector Float / Integer | Type of a &amp; b | Multiplies 2 values of the same type: a \* b |
|  | Scalar Multiplication | Vector Float | Type of a | Multiplies a value by a floating value: a \* scalar |
|  | Division | Float1 / Integer1 | Type of a &amp; b | Divides 2 values of the same type: a / b |
|  | Negation | Float1 / Integer1 | Type of a | Returns the negation value: -a |
|  | Modulo | Float1 / Integer1 | Type of a | Returns the modulo value: mod(a, divisor) |
|  | Dot Product | Vector Float | Type of a &amp; b | Returns the dot product of 2 values of the same type: dot(a, b) |
| [Logical](../atomic-function-nodes/logical-nodes/logical-nodes.md) | And | Boolean | Boolean | Returns true if the 2 boolean entries are true. Returns false if one the entry is false. |
|  | Or | Boolean | Boolean | Returns true if 1 of the boolean entries is true. Returns false if they are both false. |
|  | Not | Boolean | Boolean | Returns the negation boolean of the entry: !a |
| [Comparison](../atomic-function-nodes/comparison-nodes/comparison-nodes.md) | Equal | Float1 / Integer1 | Boolean | Returns true if a = b |
|  | Not Equal | Float1 / Integer1 | Boolean | Returns true if a != b |
|  | Greater | Float1 / Integer1 | Boolean | Returns true if a &gt; b |
|  | Greater or Equal | Float1 / Integer1 | Boolean | Returns true if a &gt;= b |
|  | Lower | Float1 / Integer1 | Boolean | Returns true if a &lt; b |
|  | Lower or Equal | Float1 / Integer1 | Boolean | Returns true if a &lt;= b |
| [Function](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/function-nodes-reference-129368124.html) | Absolute | Float1 / Integer1 | Float1 | Returns the absolute value of a: abs(a) |
|  | Floor | Float1 / Integer1 | Float1 | Returns the highest value lower or equal to a: floor(a) |
|  | Ceil | Float1 / Integer1 | Float1 | Returns the smallest value upper or equal to a: ceil(a) |
|  | Cosine | Float1 / Integer1 | Float1 | Returns the cosine value of a: cos(a) |
|  | Sine | Float1 / Integer1 | Float1 | Returns the sine value of a: sin(a) |
|  | Tangent | Float1 / Integer1 | Float1 | Returns the tangent value of a: tan(a) |
|  | Arc Tangent 2 | Vector Float2 | Float1 | Returns the arc tan 2 value of a vector2 entry: arctan2(xa, ya) |
|  | Cartesian | Float1 | Float2 | Converts 2 polar coordinates to cartesian coordinates: carth(rho, theta) |
|  | Square Root | Float1 / Integer1 | Float1 | Returns the square root value of a |
|  | Logarithmic | Float1 / Integer1 | Float1 | Returns the logarithmic value of a: log(a) |
|  | Exponential | Float1 / Integer1 | Float1 | Returns the exponential value of a: exp(a) |
|  | Pow 2 | Float1 / Integer1 | Float1 | Returns the power of 2 value of a |
|  | Linear Interpolation | Float1 / Integer1 | Float1 | Returns the linear interpolation between 2 values, depending on a floating value : (1-x)a + x \* b |
|  | Minimum | Float1 / Integer1 | Type of a &amp; b | Returns the minimum value between a and b |
|  | Maximum | Float1 / Integer1 | Type of a &amp; b | Returns the maximum value between a and b |
| Random |  | Float1 | Float1 | Generates a floating value between 0 and a |
| [Control](../atomic-function-nodes/control-nodes/control-nodes.md) | Sequence | any | Type of input | Allows to choose which value to compute first between 2 values. |
|  | If...Else | Boolean / a &amp; b | Type of a &amp; b | Returns true if the condition in If is true. Returns false if it's false. |
