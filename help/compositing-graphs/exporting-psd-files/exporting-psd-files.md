---
title: "Exporting PSD files"
description: ""
helpx_description: "Designer > Substance compositing graphs > Exporting PSD files"
---

# Exporting PSD files

Substance 3D Designer allows to export textures to Adobe Photoshop Document, or PSD file.This page explains the special interface used to translate a graph's nodes into layers.**This process is not automatic: you have a lot of control, but it is limited and often not possible to obtain an accurate match between nodes and layers.** Additionally, there is no guarantee that your PSD contains the same outputs as your graph, unless you explicitly set it up to do so. Generally, the more accurate and correct you want to be, the more effort required from the user. In general the only thing that can be closely replicated in a non-destructive way, is [Blend Nodes](../nodes-reference-for-com/atomic-nodes/blend/blend.md). Adjustment Layers are not supported, nor are Layer styles or anything else beyond Layer blend modes.

[Substance 3D Designer can also export to bitmap files.](../exporting-bitmaps/exporting-bitmaps.md)

## PSD export dialog

The PSD Export Dialog can only be opened by one method. In the [Graph view](../../interface/the-graph-view/the-graph-view.md) of the graph you want to export to PSD, click the ![](image2019-9-17-14-44-17.png) <b>Tools</b> button and select <b>PSD Exporter</b>. The interface becomes visible within the <b>Graph View</b>.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![PSD Exporter user interface](psd-dialog.png "PSD Exporter user interface")

</td>
<td style="border: 0;" valign="top">

1. <b>Filename and Location:</b> set up folder and filename for export here. Press Export button to perform exporting process.
1. <b>Add Group:</b> Adds a layer group
1. <b>Add Layer dropdown:</b> choose one of two methods to add a layer. Layers can also be added by *dragging nodes with the Right mouse button* to the stack.
1. <b>Remove Layer dropdown:</b> remove either selected or all layers.
1. <b>Layerstack:</b> most setup work if performed here. Interface mirrors limited options in Photoshop. Setup Layer name, blend mode and opacity here. If a layer has two thumbnails the second thumbnail represents the Alpha channel.

</td>
</tr>
</table>

## Workflow

As Photoshop does not directly support multi-output materials, there are multiple ways to set your PSD up. Below is a rundown of the most common method.

* Set up a number of folders for all of your outputs. One folder for Basecolor, one for Normal, one for Roughness, etc..
* Right-mouse button drag-and-drop your outputs into the appropriate group. If you want to keep things simple, the PSD can be left at only this.
* To expand the PSD more: work your way back to the left of the graph, dropping relevant in-between steps of your graph in the appropriate group. It won't be possible to share layers between outputs/groups.

In the rare case that your PSD is the more important output, you can build your graph so that you only make use of blend modes. In that case it should be possible to recreate a more editable version of your graph as a layered document.
