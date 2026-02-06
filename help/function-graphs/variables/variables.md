---
title: "Variables"
description: ""
helpx_description: "Designer > Function graphs > Variables"
---

# Variables

>[!NOTE]
>
> For information about the creation and usage of variables nodes, please refer the *[Variables Nodes section](../nodes-reference-for-fun/atomic-function-nodes/get-nodes/get-nodes.md)*.

## Definition

If you have little knowledge in programming, you may be familiar with the concept of variable.

If not, here is a simple definition:

>[!NOTE]
>
> A variable, is just a "container" with a specific name that contains a value.
> 
> You can use the value contained in a variable by calling it with its name.

## Types of variables

In Substance 3D Designer you have two families of variables : Numerics and Booleans.

## Numeric variables

Numeric variables are basically numbers. But we make a clear distinction between two types of numbers:

* Integers : 0 | 1 | -1 | 203568 , etc...
* Floats: 0.23 | 1.0 | -0.3546 | etc...

>[!WARNING]
>
> Designer makes a clear distinctions between integers and floats : by default you can't operate them together.
> 
> Fortunately, you can use the *To Integer* or To Float nodes to perform type conversions.

### Multiple numeric values in the same variable

Depending on your needs, you can accumulate up to to 4 numeric values inside the same variable.

Once again all the values have to be from the same type.

To do so, you have the choice between all these numeric values :

![](image2015-12-18-14-10-36.png)

## Boolean

A Boolean is a pure binary value, meaning that it's value can only be *True* or *False* (you can also say 0 or 1).
