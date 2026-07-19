---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/the-explorer-window.html"
breadcrumb-title: ""
description: Use the Explorer window in Substance 3D Designer to browse, organize, and manage your project files and resources.
helpx_creative_field: ""
helpx_description: Designer > Interface > Explorer
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Explorer
user-guide-description: ""
user-guide-title: ""
---

# Explorer

This page describes the Explorer dock in [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html). This dock lets you manage packages and their resources.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Overview

The Explorer dock is where you manage your files and resources currently open in Substance 3D Designer. It shows you a list of all packages currently open, with each package expanded as a hierarchy to show [resources ](../../resources/resources.md)inside of it.

The Explorer is where you start and end your projects, as it lets you create, save and export any kind of resource.

</td>
<td style="border: 0;" valign="top">

![Explorer dock](../../assets/explorer-3.jpg "Explorer dock")

</td>
</tr>
</table>

You can do a few important actions through the Explorer dock:

* Create new packages and graphs
* Load existing packages
* Save and close loaded packages
* [Import and link resources](../../resources/importing-linking-and-new/importing-linking-and-new-resources.md)
* [Export graph results to textures](../../compositing-graphs/exporting-bitmaps/exporting-bitmaps.md)
* [Publish a package to a Substance 3D asset (SBSAR)](../../compositing-graphs/publishing-asset-files/publishing-substance-3d-asset-files-sbsar.md)
* [Send packages to other Substance 3D applications](send-to-interoperability/send-to-interoperability.md)
* [Bake maps from a mesh](../../bakers/bakers.md)

## Top toolbar

This toolbar lets you quickly perform functions related to your overall workflow. All buttons are *context-aware*, which means they activate and change their behaviour based on your current selection in the Explorer.

![](../../assets/save.png)&nbsp;&nbsp;<b>Save</b> selected package.

![](../../assets/sendto-icon.jpg)&nbsp;&nbsp;<b>Publish or [send](../../interface/the-explorer-window/send-to-interoperability/send-to-interoperability.md)</b> selected element(s):

* [Publish any selected package to a Substance 3D asset (SBSAR)](../../compositing-graphs/publishing-asset-files/publishing-substance-3d-asset-files-sbsar.md);
* Send the selected package to [Substance 3D Sampler](https://www.adobe.com/products/substance3d-sampler.html), [Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html) or [Substance 3D Stager](https://www.adobe.com/products/substance3d-stager.html).

![](../../assets/republish.png)&nbsp;&nbsp;<b>Publish or send as previous:</b> Publish or send the selected elements with the same settings as before. This option is only available on a package that has already been published *at least once* in the *current* session.

![](../../assets/graph-cleaner.jpg)&nbsp;&nbsp;<b>Remove unused nodes</b> in selected graph(s). The tool follows these rules:

* The tool is only available if selected items are of the *same type*: only graphs, folders or packages;
* When the selection includes folders or packages, the tool cleans all graphs therein *recursively*;
* If one of the targeted graphs is a [Substance graph](../../compositing-graphs/substance-compositing-graphs.md), a second option is available which lets you clean all parameter functions on nodes in that graph.

Learn more about the tool in the 'Remove unused nodes' section of the [Graph view](../../interface/the-graph-view/the-graph-view.md) page.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Publish/Send dropdown menu](../../assets/explorer-sendto-displayed.jpg "Publish/Send dropdown menu")

*Publish/Send*

</td>
<td style="border: 0;" valign="top">

![Remove unused nodes drop down menu](../../assets/explorer-graph-cleaner.jpg "Remove unused nodes drop down menu")

*Remove unused nodes*

</td>
</tr>
</table>

## Contextual menus

Most of your interaction with the Explorer is through contextual menus, which are displayed by clicking RMB on an item in the Explorer's tree view.

The available options differ depending on the selected and clicked item(s):

+++Empty space

Empty space is only available below any currently open Packages. Clicking next to existing items is not considered empty space.

<b>New Package</b>: Creates a new empty package;

<b>Open Package</b>: Opens a file dialog to open an SBS file.

+++

+++Package

<b>New </b>lets you create new graphs ([Substance graph](../../compositing-graphs/substance-compositing-graphs.md), [bitmap](../../resources/bitmap-resource/bitmap-resource.md) and [vector graphics](../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md) resources, as well as *folders* for sorting content

<b>Import</b> and <b>Link </b>let you bring in [resources](../../resources/importing-linking-and-new/importing-linking-and-new-resources.md)

<b>Reload</b>, <b>Save, Save as</b> and<b> Save a copy as</b> let you save to disk or recall from disk a previously saved version of the package.

<b>Publish .sbsar file</b> and<b> Republish .sbsar file</b> let you [publish](../../compositing-graphs/publishing-asset-files/publishing-substance-3d-asset-files-sbsar.md) your uncompiled, unoptimized Substance graph, into an efficient and portable SBSAR file for us in other Substance applications and Integrations. Publish as Previous repeats the previous Publish action with the same options, skipping the options dialog for faster iteration. The toolbar contains buttons with the same functionality.

<b>Export with dependencies</b> is different from saving and publishing. It takes your SBS files, collects all referenced resources and dependencies and creates a self-contained package. The dialog lets you choose what libraries to gather, and if the file should be a compressed archive (7-zip). This is a good choice for sharing an SBS file with someone else, without worrying about missing dependencies.

<b>Send to...</b> opens a sub-menu letting you directly [send](send-to-interoperability/send-to-interoperability.md) your package to [Substance 3D Sampler](https://www.adobe.com/products/substance3d-sampler.html), [Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html), [Substance 3D Stager](https://www.adobe.com/products/substance3d-stager.html) or [Substance Player](https://helpx.adobe.com/substance-3d-player/home.html).

<b>Copy</b> copies the selected package.

<b>Paste</b> pastes copied graphs and/or resources *into* the selected package.

<b>Close package(s)</b> closes all selected packages

<b>Compute Outputs</b> forces Designer to calculate all outputs of all graphs in the package.

<b>Show In Explorer...</b> opens the location of the package in your OS' file explorer window

<b>Dependency Manager</b> opens the Dependency Manager window for the selected package.

<b>Open Dependencies</b> opens all dependenies in the Explorer (*[Substance graphs](../../compositing-graphs/substance-compositing-graphs.md) only*).

+++

+++Substance graph

<b>Open:</b> (Return) Opens this graph in [the graph View](../../interface/the-graph-view/the-graph-view.md).

<b>Copy:</b> *(Ctrl-C)* Copies the current graph to clipboard.

<b>Remove:</b> (Delete) Deletes graph from this package.

<b>Rename:</b> (F2) Rename this graph.

<b>View Outputs in 3D View:</b> Sends this graph's outputs to [the 3D View](../../interface/3d-view/3d-view.md), to display as a material.

<b>Compute Outputs:</b> Computes this graph's Outputs and keeps them in memory.

<b>Export outputs...:</b> Opens the dialog for [exporting to bitmaps.](../../compositing-graphs/exporting-bitmaps/exporting-bitmaps.md)

+++

+++3D scene resource

<b>Open:</b> (Return) Uses this 3D Mesh in[ the 3D View](../../interface/3d-view/3d-view.md), replacing the standard cube or plane.

<b>Copy:</b> (Ctrl-C) Copies this resource to clipboard.

<b>Paste:</b> (Ctrl-V) Pastes resource from clipboard.

<b>Remove:</b> (Del) Deletes resource from this package.

<b>Rename:</b> (F2) Rename this resource.

<b>Reload:</b> Force reload this mesh from disk.

<b>Show in Explorer:</b> Open a system file browser window at the location of the resource on disk.

<b>Relocate:</b> Change this Resource to be linked to another file.

<b>Bake model information...:</b> Opens the [Baking dialog.](../../bakers/bakers.md)

+++

+++Folder

<b>New:</b> Lets you create in the folder new graphs ([Substance graph](../../compositing-graphs/substance-compositing-graphs.md), [Substance function graph](../../function-graphs/function-graphs.md), [bitmap](../../resources/bitmap-resource/bitmap-resource.md) and [vector graphics](../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md) resources, as well as *folders* for sorting content.

<b>Import</b> and <b>Link: </b>Let you bring in [resources](../../resources/importing-linking-and-new/importing-linking-and-new-resources.md) and place them in the folder.

<b>Copy:</b> (Ctrl-C) Copies the folder and all its contents to clipboard.

<b>Paste:</b> (Ctrl-V) Pastes the folder and all its contents from clipboard.

<b>Rename:</b> (F2) Rename this folder.

<b>Remove:</b> *(Del)* Deletes the folder and all its contents from its package.

<b>Compute Outputs:</b> Computes the outputs of all graphs included in the folder and keeps them in memory.

+++

## Bottom toolbar

The toolbar at the bottom of the Explorer dock provides information about a package or a package resource:

<b>![](../../assets/explorer-dependencies.jpg)&nbsp;&nbsp;Dependencies:</b> When a package is selected, its package dependencies are listed in a dedicated panel.

<b>![](../../assets/explorer-information.jpg)&nbsp;&nbsp;Information:</b> Provides metadata related to the package or resource currently selected:

* Package: the full filepath of the package
* [Bitmap resource](../../resources/bitmap-resource/bitmap-resource.md): the full filepath of the resource, its [ICC profile](../../color-management/color-management.md), image size and [import method](../../resources/importing-linking-and-new/importing-linking-and-new-resources.md) (I.e., *linked* or *imported*)

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![Dependencies panel](../../assets/explorer-dependencies-displayed.jpg "Dependencies panel")

*Dependencies*

</td>
<td style="border: 0;" valign="top">

![Information panel](../../assets/explorer-information-displayed.jpg "Information panel")

*Information*

</td>
</tr>
</table>
