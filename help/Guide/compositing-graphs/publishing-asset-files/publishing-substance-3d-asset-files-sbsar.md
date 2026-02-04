---
title: "Publishing Substance 3D asset files (SBSAR) | Substance 3D Designer"
description: "Designer > Substance graphs > Publishing Substance 3D asset files (SBSAR)"
---

# Publishing Substance 3D asset files (SBSAR)

This page explains how Substance 3D Designer can publish packages as <b>Substance 3D asset</b> files, a special file format with the <b>SBSAR</b> extension, used within the Substance ecosystem as well as in other applications supporting it.

It's usually better to use a Substance 3D asset instead of bitmaps, as it is a lot more flexible and lightweight. If you are using them in Substance 3D [Painter](../../../substance-3d-painter/home/home.md), [Sampler](../../../substance-3d-sampler/substance-3d-sampler.md) or [Player](https://helpx.adobe.com/substance-3d-player/home.html), it is faster to use the [Send To functionality](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/send-to-215286290.html).

![Publishing SBSAR files simplified](exportflow.png "Publishing SBSAR files simplified")

## Publishing concepts

it is good to keep the following in mind when publishing a Substance graph:

* You<b> publish a package</b>, with all it contents, not an individual [Substance graph](../substance-compositing-graphs.md). A Substance 3D asset then lets you generate content from all Substance graphs inside this package.
* Published packages are <b>completely stand-alone</b>: all resources required are embedded into the file. That means they are much easier to share than SBS files.
* The output from Substance 3D assets can be <b>completely dynamic</b>. [Resolution is not set; exposed parameters can be modified.](../compositing-graph-key-con/substance-compositing-graph-key-concepts.md) However, editing the Graph is no longer possible.
* Substance 3D assets can be used outside of Designer, in all Adobe Substance 3D products, Adobe Dimension as well as any other application that has a [Substance integration](../../../substance-3d-integrations/home/home.md).
* Publishing is different from[ Exporting](../exporting-bitmaps/exporting-bitmaps.md), make sure you understand well the difference.

## Preparing to publish

Publishing takes some more preparation than Exporting Bitmaps. That's because your published Substance 3D assets are dynamic tools, not just a static snapshot of the current state of your textures. Specifically, you want to keep the following in mind:

* Make sure graph resolutions ([Output Size](../output-size/output-size.md)) are set to the *Relative To parent* [inheritance method](../inheritance-compositing/inheritance-in-substance-compositing-graphs.md), which means they are dynamic and can be changed on the fly.
* Make sure[ graph outputs](../nodes-reference-for-com/atomic-nodes/output/output.md) are set up correctly with names, labels and usage tags.
* Make sure [Parameters, if needed are organized and named properly.](../manage-parameters/exposing-a-parameter/exposing-a-parameter.md)
* Make sure the [Output size](../output-size/output-size.md) property of all [Bitmap](../nodes-reference-for-com/atomic-nodes/bitmap/bitmap.md) nodes are set to the *Absolute* [inheritance method](../inheritance-compositing/inheritance-in-substance-compositing-graphs.md). If that is not the case, their referenced [Bitmap resource](../../resources/bitmap-resource/bitmap-resource.md) will be saved at the default <b>256\*256</b> resolution in the published Substance 3D asset file, which will *impact the quality* of one or more outputs.
* If graphs are present in the package that should not be available outside of Designer (for example helper or "tool" sub-graphs that only work in a specific context), set them up to be hidden in their properties. See further below.

## Publishing methods

Once you are ready to publish, there are two ways to access the Publishing Dialog, both are through [the Explorer Window](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html).

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

In the [Explorer window](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html), Right-clicking on the package and choosing ![](image2020-9-23-9-39-58.png) **Publish .sbsar file...**, alternative Hotkey Ctrl + P.

After Publishing with dialog once, you can also use ![](image2020-9-23-11-15-35.png) **Publish .sbsar file as previous** to repeat the publishing process without seeing the dialogs, immediately publishing with the same settings.

</td>
<td style="border: 0;" valign="top">

![](publish-rightclick.gif)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

In the [Explorer window](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html), by clicking the Publish button ![](image2020-9-23-9-39-58.png) in the top toolbar.

After Publishing with dialog once, you can also use the Publish as previous button ![](image2020-9-23-11-15-35.png) to repeat the publishing process without seeing the dialogs, immediately publishing with the same settings.

</td>
<td style="border: 0;" valign="top">

![](publish-toolbutton.gif)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Asset publishing options

Before the Asset Publish Options appear, you will be prompted to save the Substance 3D file (SBS) if this has not been done, and you will be prompted where to save the Substance 3D asset. To avoid seeing the file prompts and dialog and getting your file out faster, use <b>Publish as previous</b> methods described above.

</td>
<td style="border: 0;" valign="top">

![Asset publishing options](publish-dialog.png "Asset publishing options")

</td>
</tr>
</table>

The following options are available:

<b>File Path</b> opens a file dialog to choose where to save the Substance 3D asset file. The default path is the system's user documents. If the package was saved, the path is the package location. If the package was published during the session, the path is the last publish location.

<b>Archive compression</b> sets compression options for the archive, affects filesize.

<b>Generate missing icons</b> uses built-in[ PBR render](../nodes-reference-for-com/node-library/material-filters/pbr-utilities/pbr-render/pbr-render.md) techniques to create thumbnails for each graph's attribute.

<b>Exposed graphs </b>lists all graphs that will be exposed in this package, see below for excluding graphs.

>[!NOTE]
>
> **Random Seed Exposure**
> 
> The Random Seed exposure settings are no longer available in the Publish dialog. Instead, set your [graph's random seed attribute to Absolute instead of relative to avoid it becoming available.](../graph-parameters/graph-parameters.md)

## Excluding graphs from published asset

Some graphs in your package might not be intended for usage outside. These sub-graphs are usually meant as part of a larger whole, a subroutine of a master material.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

To exclude a graph from becoming visible or usable inside an Substance 3D asset file, access that graph's properties (double click empty area in graph View or single-click the graph in the Explorer), then open the <b>Attributes</b> rollout. Set <b>Exposed in SBSAR</b> to <b>No</b> to hide it when published.

</td>
<td style="border: 0;" valign="top">

![](image2020-9-23-10-40-21.png)

</td>
</tr>
</table>

### Publish dialog warnings

The Publish dialog sometimes gives warnings in yellow. Common ones are listed below, with an explanation and solution.

* One or more graphs do not have an output   
  This warning means you are trying to publish a package with one or more graphs that have no output nodes. Solution is to add [Output nodes ](../nodes-reference-for-com/atomic-nodes/output/output.md)to the graphs with a yellow warning triangle.
* One or more graphs have a non-relative to parent output size parameter   
  This warning means one or more graphs have been set to incorrect Output sizes. Usually it is the properties of a graph itself. The warning means you will not have dynamic resolution control over this graph when published. Solution is to go into graph properties for those with a yellow triangle, and set the Output Size's [inheritance method](../inheritance-compositing/inheritance-in-substance-compositing-graphs.md) to *Relative to Parent*.

## Substance 3D asset limitations

While the Substance 3D asset is the most powerful and most dynamic format in the Substance Ecosystem, there are some small, technical limitations to be aware of.

* Published Substance 3D asset packages are a one-way file format. You cannot "decompile" a Substance 3D asset back to a Substance 3D file (SBS). The only way to "edit" a Substance 3D asset, is to edit the original Substance 3D file. You can still use Substance 3D asset package contents as nodes inside new Substance graphs (open and drag-and-drop), so this is not a huge limitation.
* Substance 3D asset files have versions that infer compatibility. The core Substance Engine is updated from time to time with new features. packages that use these features need to be read by applications that support these new features. This is not an issue for all Substance Applications, as they are all updated at the same time, but Plugins and integrations might have longer compatibility delays.  
  Use the Substance Engine Compatibility display options in the [Project Preferences ](../../interface/preferences-window/project-settings/project-settings.md)to track down any potential issues.
* Some exposed parameters – such as *static* parameters – are *hidden* once a graph is published as part of a Substance 3D asset. See the [Limitations](../manage-parameters/exposing-a-parameter/exposing-a-parameter.md) section of the [Exposing a parameter](../manage-parameters/exposing-a-parameter/exposing-a-parameter.md) page for a list of these parameters and to learn more about static parameters in general.
