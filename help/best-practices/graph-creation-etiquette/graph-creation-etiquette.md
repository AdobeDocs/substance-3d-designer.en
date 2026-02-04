---
title: "Graph Creation Etiquette"
description: ""
helpx_description: "Designer > Best Practices > Graph Creation Etiquette"
---

# Graph Creation Etiquette

Creating large, complex graphs can quickly get confusing and become hard to navigate. A number of tools can be used to alleviate these issues, and there are some good habits to get in to, to avoid issues later on. This page provides a conclusive list of techniques we recommend using for clean, efficient, functional Graphs that are easily shared and understood.

## General

### Graph Organization

#### Graph items

Graph items are helper objects that can be placed next to and around your nodes in [the Graph View](../../interface/the-graph-view/the-graph-view.md). Out of the three, the Frame provides the quickest and biggest benefits, while the Comment and Navigation Pin are more suited for specific scenarios.

#### Frames

The number one thing that leads to cleaner, easier to read graphs, is the placement of Frames around core groups of your graph. Without Frames, a big Graph is almost unreadable, and even small Graphs become much easier to understand once frames are drawn. A huge advantage of Frames is that their<b> names are always rendered at the same scale</b>, even if you zoom out very far.

![Frames in Substance graphs](frames.gif "Frames in Substance graphs")

Frames make it much easier to understand what is going on in a graph. They can help you as an author coming back to your work months later, or another user such as a colleague to find their way around a Graph they are not used to.

Use the following criteria when placing Frames:

* Identify **chunks of functionality** (for example a 8 nodes that together create a dirt effect) and group these using Frames.
* Always try to **use different colors** for your Frames: Frames with the same blue, default color don't stand out much from each other.
* Use **clear, descriptive names** that are not overly long (see section below for more tips)
* Don't put **too much or too little** in a Frame, as this doesn't help readability. The exact amount obviously differs between graphs and functiuonality.
* If neccessary, **add text in the description** to help understand what happens in a frame.

#### Comments and Pins

Comments and pins are only secondary to Frames and are not an absolute must for well-authored graphs. They can be used in the following scenarios:

* Comments are good for adding additional text beyond what a Frame's description allows. You can add small bits of text per-node, mostly for little detailed pieces of info. Comments do not scale well and don't read from a distant zoom level.
* Navigation Pins allow you to cycle through specific areas of the Graph using the F2 shortcut. This can be useful for very big graphs where one often needs to jump between two areas that are very far from each other.

### Input &amp; output placement

Inputs and outputs should be placed at the extreme ends of Graphs: all outputs on the right, all inputs to the left, each vertically aligned. This makes it easier to find and identify them.

![Input and output placement](inout.gif "Input and output placement")

The above example is an extreme case: Frames are not always needed or possible, but it should be clear that vertical alignment of In- and Outputs is a lot more clear that random, shuffled placement.

### Link rerouting

In large, very long Graphs, sometimes links are made across a very large span. This leads to confusing Link wires crossing through the Graph without much control. The shortcut "Alt + Shift Drag" allows you to reorganize these Links, rerouting them on a different path by subdividng a link and adding an extra handle in the middle. It is recommended to make use of this in scenarios where it makes sense.

![Link rerouting](linkjreroute.gif "Link rerouting")

### Label, indentifier and usage

Any Graph that is meant for sharing or publishing should have proper care put into the additional metadata that improves user-friendliness. The following points are important:

The default suggested Labels are never sufficient, take the time and effort to add custom Labels to exposed parameters and your in- and outputs.

![Identifier and label](output-label.png "Identifier and label")

Try to not have identifier and Label differ too much: in case the Identifier is used elsewhere (in multiple Functions) it can be very hard to find which UI property is related to what variable.

![Identifier clarity](labelvsidentifier.png "Identifier clarity")

Try to match your Labels to terms you use in Frames (Frame Labels) and comments. It makes it easier to find out what section of the graph is linked to what exposed parameter

![Matching frame and parameter labels](match-labels.png "Matching frame and parameter labels")

### Parameter settings

When exposing Parameters, more than just the Label and Identifier is important, The following points should be kept in mind:

* Choose the correct Editor type. A Slider might not always make sense: an Angle or Dropdown Ui element are also possibilities.
* Set up proper Min and Max values and decide if clamping them makes sense.
* Choose a default value that makes sense: Defaults that reurn useless, edge case results should be avoided.
* Consider remapping the range through a [Function ](../../function-graphs/function-graphs.md)if required: a Slider from 0.125 to 0.357 doesn't make any sense, you can easily remap this with a Linear Interpolation and have the UI element utilize a 0 to 1 range.

## Substance graphs

### Color &amp; grayscale management

Great care is required when using color and Grayscale data, mixing both types can't be done easily on the fly. The following points should be kept in mind:

* Graphs should never contain dotted red (error) links.
* There should be no unnecessary conversions between color and grayscale and vice-versa. In some cases the "automatically insert color/grayscale conversion node" in the Graph Preferences can lead to long, useless chains of Docked conversion nodes.
* Data is ideally kept as grayscale as long as possible, and only converted when absolutely needed. This reduces complexity and saves on performance.
* Inputs and Outputs should be created or set-up with the correct type in mind: for example it makes no sense to have a "mask" input set to color if it will be converted to grayscale for use as a binary mask.

![Color and grayscale conversions](colorgray01.png "Color and grayscale conversions")

### Resolution control

Controlling the resolution of a [Substance graph](../../compositing-graphs/substance-compositing-graphs.md) can be confusing, so proper care is required to do this correctly. Making mistakes can lead to severly impacted peformance, or low-quality, unuseable results.

[To fully understand this topic make sure you know about Absolute and Relative Output Sizes.](../../compositing-graphs/output-size/output-size.md)

* A graph should be set to "Relative to Parent" resolution in almost every case, unless there is a very specific exception where it is not required (very rare).
* Nodes generally shouldn't have override settings for the Output Size. Resolution is best controlled through the Parent or Graph properties in most cases.
* For Bitmaps, special care should be set that the default, Absolute Output Size does not spread throughout the entire Graph, this should be overriden to Relative to Parent. This is one of the few exceptions to the above rule.
