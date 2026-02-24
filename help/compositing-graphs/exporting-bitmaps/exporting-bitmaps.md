---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/exporting-bitmaps.html"
breadcrumb-title: ""
description: Learn how to export textures and bitmaps from Substance compositing graphs for use in external applications and workflows.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Exporting Bitmaps
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Exporting Bitmaps
user-guide-description: ""
user-guide-title: ""
---



# Exporting Bitmaps

This page explains how Substance 3D Designer can export to many different Bitmap file formats, and how to export multiple UV-Tiles in batches.[If you want to export to PSD files,](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/exporting-psd-186974407.html) [there is a separate dedicated page for this.](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/exporting-psd-186974407.html)

![Exporting simplified](exportflow.png "Exporting simplified")

## Exporting concepts

It's good to keep the following in mind when exporting a bitmap:

* You<b> export from a Graph</b>, not a Package. A package does not generate image content by itself.
* The number (and resolution) of bitmaps exported is determined by the <b>Outputs</b> of a Graph.
* Filetype is set for all Outputs/bitmaps.
* Exporting is different from [Publishing](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/publishing-sbsar-file-200574380.html), make sure you understand well the difference!

## Export methods

Once you are ready to export, there are two ways to access the Export Dialog:

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

In the [Explorer window](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html), Right-clicking on the Graph to export and choosing **"Export Outputs as bitmaps"**

![](export-explorer.gif)

</td>
<td style="border: 0;" valign="top">

In the [Graph View](../../help/interface/the-graph-view/the-graph-view.md), by clicking the Tools button ![](image2019-9-17-14-44-17.png) and choosing **"Export Outputs..."**

![](export-graph.gif)

</td>
</tr>
</table>

## Export dialog

The Export Dialog presents you with a few options to customize your export.

The version shown to the right is the standard dialog, changing resolution happens either on the Graph, Outputs or by setting the Parent resolution before opening the dialog.

1. <b>Destination: </b>location for all files to be saved.
1. <b>Format:</b> filetype used for all exported files.
1. <b>Pattern</b>: generic method to generate filetypes based on metadata keywords. An example filename based on the first output is shown below, for verification.  
   Listed below are all available options:
   1. *$(graph)* - name of current Graph
   1. *$(identifier)* - identifier of current output
   1. *$(description)* - description of current output
   1. *$(label)* - label of current output
   1. *$(user\_data)* - custom user data of current output
   1. *$(group)* - output group of current output
   1. *$(colorspace)* - color space of current output (only available for *OCIO* and *Adobe ACE* [color management](../../help/color-management/color-management.md) modes)
1. <b>Outputs:</b> Toggle on or off specific Outputs and Output Groups from your Graph. Buttons toggle all on or off. Useful when only one bitmap has changed.
1. <b>Automatic Export:</b> Toggle button to enable automatic re-exporting of Graph outputs as soon as a change is made. Only for current graph. Can be heavy and slow depending on settings.
1. <b>Export Button:</b> Exports with current settings, or closes dialog.

![Export outputs dialog](fromgraph-1.png "Export outputs dialog")

## Export dialog (Batch/UV tiles)

When working with UV-Tile meshes in Designer, the Export Dialog can be used in a slightly different way that allows batch-exporting of multiple UV-Tiles at once. Make sure you understand this workflow, and have properly assigned a [Substance graph](../../help/compositing-graphs/substance-compositing-graphs.md) to one or more UV-Tiles.  
The batch tab is also a faster way to export your graph at a different resolution than the working (parent) resolution.

Start the dialog with the same methods as detailed above, just making sure you right click *on the UV-Tile-assigned graph in the Explorer*, or that you have *opened the specific UV-Tile-assigned Graph* in the Graph view when using the Tools button.

1. <b>Batch Tab</b>: Make sure to select this tab instead of the standard <b>From Graph </b>method, otherwise options 2-3 will not be available.
1. <b>UV Tiles:</b> Just as with Outputs, allow you to toggle on or off the exporting of specific UV Tiles.
1. <b>&#91;Output size&#93;(../../help/compositing-graphs/output-size/output-size.md): </b>Override export resolution, allowing you to work smaller and more efficient, while exporting at maximum size.

![Batch export outputs dialog](batch.png "Batch export outputs dialog")
