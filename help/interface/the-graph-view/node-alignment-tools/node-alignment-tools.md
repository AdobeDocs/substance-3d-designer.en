---
title: "Node alignment tools"
description: "Use node alignment tools to organize and align nodes in the graph view for cleaner, more readable graphs."
helpx_description: "Designer > Interface > The graph view > Node alignment tools"
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/the-graph-view/node-alignment-tools.html"
---

# Node alignment tools

![Node alignment toolbar](node-alignment-toolbar.png "Node alignment toolbar"){zoomable="yes"}

The Node Alignment Tools let you arrange nodes in graphs to improve their readability and authoring experience. They offer actions for aligning nodes, distributing them evenly and snapping them to the grid.

They act on the <b>nodes currently selected only</b>.

>[!NOTE]
>
> Keyboard shortcuts
> 
> Some actions have keyboard shortcuts for quick acces: H, V and S. They are displayed between parentheses in the list of actions below.
> 
> Note that these will override any [keyboard shortcut assigned to nodes](../../preferences-window/preferences-window.md).

## Alignments

Nodes may be aligned horizontally and vertically, with three modes for each axis:

### Horizontal alignments

<b>!&#91;&#93;(node-alignment-h-left.png) Left:</b> Align the left side of the selected nodes to the left side of the leftmost node.

<b>!&#91;&#93;(node-alignment-h-center.png) Center (H):</b> Align the horizontal center of the selected nodes to the horizontal center of the bounding box encompassing them.

<b>!&#91;&#93;(node-alignment-h-right.png) Right:</b> Align the right side of the selected nodes to the right side of the rightmost node.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node alignment tools: left](node-alignment-left.gif "Node alignment tools: left"){zoomable="yes"}

*Left*

</td>
<td style="border: 0;" valign="top">

![Node alignment tools: center](node-alignment-center.gif "Node alignment tools: center"){zoomable="yes"}

*Center*

</td>
<td style="border: 0;" valign="top">

![Node alignment tools: right](node-alignment-right.gif "Node alignment tools: right"){zoomable="yes"}

*Right*

</td>
</tr>
</table>

### Vertical alignments

<b>!&#91;&#93;(node-alignment-v-top.png) Top:</b> Align the top side of the selected nodes to the top side of the uppermost node.

<b>!&#91;&#93;(node-alignment-v-middle.png) Middle (V):</b> Align the vertical center of the selected nodes to the vertical center of the bounding box encompassing them.

<b>!&#91;&#93;(node-alignment-v-bottom.png) Bottom:</b> Align the bottom side of the selected nodes to the bottom side of the lowermost node.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Node alignment tools: top](node-alignment-top.gif "Node alignment tools: top"){zoomable="yes"}

*Top*

</td>
<td style="border: 0;" valign="top">

![Node alignment tools: middle](node-alignment-middle.gif "Node alignment tools: middle"){zoomable="yes"}

*Middle*

</td>
<td style="border: 0;" valign="top">

![Node alignment tools: bottom](node-alignment-bottom.gif "Node alignment tools: bottom"){zoomable="yes"}

*Bottom*

</td>
</tr>
</table>

### Stacking

The <b>Stack </b>option ![](node-alignment-stack.png) lets you <b>avoid any overlap</b> when using alignments. It is enabled by default.

When enabled, nodes will be moved as far as possible to the reference position until they would collide with another node in the selection. This effectively stacks them in the selected axis with a margin of one medium grid cell between each node.

![Node alignment tools: stacking](node-alignment-stacking.gif "Node alignment tools: stacking"){zoomable="yes"}

## Distributions

Nodes can be distributed evenly between the nodes at each extremes of the current selection on the desired axis.

<b>!&#91;&#93;(node-alignment-distribute-h.png) Horizontally:</b> Nodes are distributed evenly between the leftmost and rightmost nodes in the selection.

<b>!&#91;&#93;(node-alignment-distribute-v.png) Vertically:</b> Nodes are distributed evenly between the topmost and lowermost nodes in the selection.

The distributions aim for <b>even spacing</b> between the nodes, regardless of their size.

When multiple nodes have their centers perfectly aligned on the selected axis, they remain and are <b>treated as one</b> in the distribution. The *largest* of the aligned nodes is used for computing the even spacing.

Note that when the total size of the selected nodes is greater than the space available on the selected axis, overlapping may occur.

<table>
<tr style="border: 0;">
<td width="58.33%" style="border: 0;" valign="top">

![Node alignment tools: horizontal distribution](node-alignment-distribute-h.gif "Node alignment tools: horizontal distribution"){zoomable="yes"}

*Horizontally*

</td>
<td width="100.00%" style="border: 0;" valign="top">

![Node alignment tools: vertical distribution](node-alignment-distribute-v.gif "Node alignment tools: vertical distribution"){zoomable="yes"}

*Vertically*

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="58.33%" style="border: 0;" valign="top">

## Grid snapping

The <b>Snap (S) !&#91;&#93;(node-alignment-snap.png)</b> action moves each selected node so that their top-left corner rests on the closest point on the medium grid.

</td>
<td width="100.00%" style="border: 0;" valign="top">

![Node alignment tools: grid snapping](node-alignment-snapping.gif "Node alignment tools: grid snapping"){zoomable="yes"}

</td>
</tr>
</table>
