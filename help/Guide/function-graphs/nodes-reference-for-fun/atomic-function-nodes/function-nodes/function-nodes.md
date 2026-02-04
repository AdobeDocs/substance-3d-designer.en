---
title: "Function | Substance 3D Designer"
description: "Designer > Function graphs > Nodes reference for function graphs > Function"
---

# Function nodes

Function nodes transform the input value according to the mathematical function they represent.

Although their input connectors are generally not typed, they do not support all value types.

## Node list

+++Pow




Returns the first input raised to the power of the second input:X^Y.



+++

+++2Pow




Returns 2 to the power of its input value:2^X.



+++

+++Square root




Returns the square root of its input value:√X.



+++

+++Exponential




Returns the exponential value of its input value:e^X





eis approximately equal to 2.7182818.



+++

+++Logarithm




Returns the natural logarithm of its input value:ln(X).



+++

+++Logarithm base 2




Returns the base 2 logarithm of its input value:log2(X).



+++

+++Absolute




Returns the absolute value of its input:abs(X).



+++

+++Ceil




Rounds its input value up. It returns the smallest integer value not less than X:ceil(X).



+++

+++Floor




Rounds its input value down. It returns the largest integer value not greater than X:floor(X).



+++

+++Linear interpolation




Returns the linear interpolation between two values in function of a floating value:(1 - X)*A + X*B.



+++

+++Minimum




Returns the lowest of the two input values:min(A, B).



+++

+++Maximum




Returns the highest of the two input values:max(A, B).



+++

+++Cosine




Returns the cosine of its input value in radians:cos(X).



+++

+++Sine




Returns the sine of its input value in radians:sin(X).



+++

+++Tangent




Returns the tangent of its input value in radians:tan(X).



+++

+++Arc tangent 2




Returns the angle between the input 2D vector and the horizontal.





It is the reciprocal of theCartesianfunction.





It is not necessary to switch the X and Y component of the input vector as in the usualatan2function.



+++

+++Cartesian




Converts polar coordinates to cartesian coordinates.





It is the reciprocal of theArc tangent 2function:Length * Float2(cos(Angle), sin(Angle).





Polar coordinates are a distance from the origin and an angle in radians from the horizontal.



+++

+++Random




Returns a random value between 0 and the input valueX.



+++
