---
title: "Dot node (also Portal)"
description: ""
helpx_description: "Designer > Interface > Graph view > Graph items"
---

# Dot node (also Portal)

<table>
<tr style="border: 0;">
<td width="25.00%" style="border: 0;" valign="top">

![Dot node icon](graphatomic-dot.png "Dot node icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

The <b>Dot</b> node is a helper that lets you simplify and clean up graphs by rerouting and grouping connections. It is especially useful for graphs with many long connections running over other connections or nodes.

A pair of Dot nodes can be used as <b>portals</b> to hide a connection going over a long distance, or in places where routing the connection would be challenging.

</td>
</tr>
</table>

## Creating Dot nodes

Dot nodes may be added in any graph type, in any of the following ways:

+++Insert on link
Hold the <b>Alt</b> key while hovering a connection to display the Dot node preview, then click LMB to add a Dot node on the connection at that location.



+++

+++Node connector
Press the <b>Alt</b> key while dragging a new connection from a node connector to insert a Dot node at that location.

You may continue dragging the new connection and repeat the operation to route that connection how you like.



+++

+++Node menu
Press <b>Spacebar</b> to display the <b>Node menu</b>, then select the 'Dot' item or type 'dot' in the search field to surface the item and find it more quickly.



+++

>[!TIP]
>
> When a Dot node is created, its 'Name' property automatically gains focus so you can immediately edit the node's name.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Merging links

Press ALT and move a Dot node over links to merge multiple node connections together.

</td>
<td style="border: 0;" valign="top">

![Merging links](dot-node-congrenate-links-optim.gif "Merging links"){width="512px"}

</td>
</tr>
</table>

## Portals

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

![Dot node as portal - icon](DotNode_Portal-1.png "Dot node as portal - icon")

</td>
<td width="100.00%" style="border: 0;" valign="top">

Dot nodes can be used as <b>portals</b> to send data over a long distance in the graph without having a cumbersome long link that hurts readability. This effectively hides the link between Dot nodes.

</td>
</tr>
</table>

![Dot node as portal](DotNode_Portal.gif "Dot node as portal")

### Creating portals

A portal is automatically created between two Dot nodes – a transmitter and a receiver – when the transmitter Dot node is named. Naming a Dot node is done by setting a unique identifier in its <b>Name</b> property.

When one or more named Dot nodes exist in a graph, any Dot node can be connected to it as a receiver by:

* Creating a link between the receiver's input and a transmitter's output;
* Selecting the transmitter's name in the receiver's <b>Input Portal</b> property.

Duplicating or copying receivers preserves their connection to the transmitter as a portal.

### Identifying portals

Dot nodes used as portals have a wireless signal icon placed next to the connector used as a portal.

Selecting any Dot node used as a portal displays its hidden connections to other portals as a dashed line.

### Deleting portals

A portal is deleted when the transmitter's <b>Name</b> is cleared, or when the hidden connection is deleted by:

* Selecting a portal, then selecting the hidden connection and deleting it;
* Selecting the receiver and pressing the <b>X</b> button next to the <b>Input Portal</b> drop down in the Properties.

>[!IMPORTANT]
>
> Using Dot nodes as portals is not supported in [FX-Map graphs](../../../../function-graphs/fxmaps/fxmaps.md).

Check out this tutorial about Dot nodes as portals:
