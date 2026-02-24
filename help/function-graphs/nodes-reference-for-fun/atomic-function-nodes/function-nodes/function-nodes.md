---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/function-graphs/nodes-reference-for-function-graphs/atomic-function-nodes/function-nodes.html"
breadcrumb-title: ""
description: Access function nodes in Substance 3D Designer function graphs to call and execute custom function graphs.
helpx_creative_field: ""
helpx_description: Designer > Function graphs > Nodes reference for function graphs > Function
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Function
user-guide-description: ""
user-guide-title: ""
---



# Function nodes

Function nodes transform the input value according to the mathematical function they represent.

Although their input connectors are generally not typed, they do not support all value types.

## Node list

+++Pow
![Pow node icon](Pow_Node.jpg "Pow node icon")



Returns the first input raised to the power of the second input: <b>X^Y</b>.

+++

+++2Pow
![2Pow node icon](2Pow_Node.jpg "2Pow node icon")



Returns 2 to the power of its input value: <b>2^X</b>.

+++

+++Square root
![Square Root node icon](SquareRoot_Node.jpg "Square Root node icon")



Returns the square root of its input value: <b>√X</b>.

+++

+++Exponential
![Exponential node icon](Exponential_Node.jpg "Exponential node icon")



Returns the exponential value of its input value: <b>e^X</b>

<b>e</b> is approximately equal to 2.7182818.

+++

+++Logarithm
![Logarithm node icon](Logarithm_Node.jpg "Logarithm node icon")



Returns the natural logarithm of its input value: <b>ln(X)</b>.

+++

+++Logarithm base 2
![Logarithm Base 2 node icon](LogarithmBase2_Node.jpg "Logarithm Base 2 node icon")



Returns the base 2 logarithm of its input value: <b>log2(X)</b>.

+++

+++Absolute
![Absolute node icon](Absolute_Node.jpg "Absolute node icon")



Returns the absolute value of its input: <b>abs(X)</b>.

+++

+++Ceil
![Ceil node icon](Ceil_Node.jpg "Ceil node icon")



Rounds its input value up. It returns the smallest integer value not less than X: <b>ceil(X)</b>.

+++

+++Floor
![Floor node icon](Floor_Node.jpg "Floor node icon")



Rounds its input value down. It returns the largest integer value not greater than X: <b>floor(X)</b>.

+++

+++Linear interpolation
![Linear Interpolation node icon](LinearInterpolation_Node.jpg "Linear Interpolation node icon")



Returns the linear interpolation between two values in function of a floating value: <b>(1 - X)\*A + X\*B</b>.

+++

+++Minimum
![Minimum node icon](Minimum_Node.jpg "Minimum node icon")



Returns the lowest of the two input values: <b>min(A, B)</b>.

+++

+++Maximum
![Maximum node icon](Maximum_Node.jpg "Maximum node icon")



Returns the highest of the two input values: <b>max(A, B)</b>.

+++

+++Cosine
![Cosine node icon](Cosine_Node.jpg "Cosine node icon")



Returns the cosine of its input value in radians: <b>cos(X)</b>.

+++

+++Sine
![Sine node icon](Sine_Node.jpg "Sine node icon")



Returns the sine of its input value in radians: <b>sin(X)</b>.

+++

+++Tangent
![Tangent node icon](Tangent_Node.jpg "Tangent node icon")



Returns the tangent of its input value in radians: <b>tan(X)</b>.

+++

+++Arc tangent 2
![Arc Tangent 2 node icon](ArcTangent2_Node.jpg "Arc Tangent 2 node icon")



Returns the angle between the input 2D vector and the horizontal.

It is the reciprocal of the <b>Cartesian</b> function.

It is not necessary to switch the X and Y component of the input vector as in the usual <b>atan2</b> function.

+++

+++Cartesian
![Absolute node icon](Absolute_Node.jpg "Absolute node icon")



Converts polar coordinates to cartesian coordinates.

It is the reciprocal of the <b>Arc tangent 2 </b>function: <b>Length \* Float2(cos(Angle), sin(Angle).</b>

Polar coordinates are a distance from the origin and an angle in radians from the horizontal.

+++

+++Random
![Random node icon](Random_Node.jpg "Random node icon")



Returns a random value between 0 and the input value <b>X</b>.

+++
