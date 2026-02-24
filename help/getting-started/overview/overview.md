---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/getting-started/overview.html"
breadcrumb-title: ""
description: Get an overview of Substance 3D Designer and learn about its capabilities for creating procedural materials and textures.
helpx_creative_field: ""
helpx_description: Designer > Getting started > Overview
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Overview
user-guide-description: ""
user-guide-title: ""
---



# Overview

[Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) is an application intended for creating 2D textures, materials and filters in a node-based interface, with a heavy focus on procedural generation, parametrisation and non-destructive workflows. It is the longest-running application in the Substance 3D ecosystem and resources made with it are the most versatile and dynamic possible.

Here is how it compares to other applications:

|  | <div><img alt="Substance 3D Sampler icon" class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell_position-par_dx_table_row-r0-column-c1_position_position-par_image_713298714" src="sa-appicon-noshadow-256.png" title="Substance 3D Sampler icon" width="64px"/></div>  Substance 3D  Sampler | <div><img alt="Substance 3D Painter icon" class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell_position-par_dx_table_row-r0-column-c2_position_position-par_image" src="pt-appicon-noshadow-256.png" width="64px"/></div>  Substance 3D  Painter | <div><img alt="Substance 3D Designer icon" class="" data-preserve-html="true" id="root_content_flex_items_position_position-par_dynamic_grid_items_grid-cell_position-par_dx_table_row-r0-column-c3_position_position-par_image" src="ds-appicon-noshadow-256.png" title="Substance 3D Designer icon" width="64px"/></div>  Substance 3D Designer |
| --- | --- | --- | --- |
| <b>Learning curve</b> | Low | Medium | High |
| <b>Author materials</b> | Yes | Yes | Yes |
| <b>Author 3D models</b> | No | Limited\* | Limited\* |
| <b>Author filters, patterns and effects</b> | No | Limited | Yes |
| <b>Export parametric content</b> | No | No | Yes |

\*: Displacement only, see <b>Scene export</b> feature in the [3D View](../../help/interface/3d-view/3d-view.md) section.

In short, Substance 3D Designer should be seen as the most technical, advanced texturing application available.

It allows you to author content for almost any usecase or scenario. It means you are not limited to a single type of output – such as a unique material/set of textures for a UV-mapped mesh – but can create content for a much more extended set of uses.

For example, most of the procedural, smart content in Painter and Sampler was authored and exported from Designer. Things like Brush Alphas, Generators, Filters and Base Materials can all be authored in Designer.

## Workflow

Substance 3D Designer is a Node-based editor that allows you to build content in many different ways with varying complexities. [The workflow is further explained on dedicated pages](../../help/getting-started/workflow-overview/workflow-overview.md), but the following are benefits of working with the software:

<b>&#91;Non-linear&#93;(../../help/compositing-graphs/substance-compositing-graphs.md) </b>: you can can author a multitude of texture outputs at once. Edit one mask or slider, and automatically any connected output is re-calculated. No more need to separately author maps such as Basecolor, Roughness, Normal, etc..

<b> &#91;Non-destructive&#93;(../../help/compositing-graphs/compositing-graph-key-con/substance-compositing-graph-key-concepts.md) </b>: you can reverse any action *without* losing any of your work. It becomes much quicker to iterate and experiment, finding even more efficient workflows.

<b> &#91;Integrated Baking&#93;(../../help/bakers/bakers.md) </b>: access advanced, blazing-fast mesh baking tools right inside the software. You no longer have to perform baking in a separate software and perform lengthy import and export processes.

<b> &#91;Parametric&#93;(../../help/compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md) </b>: you can set-up to control nearly any aspect of a texture through a single slider or dropdown. This allows you to add endless control and variation to just a single asset.

## Filetypes

The application and its ecosystem use 4 different filetypes. To be clear: these are filetypes that are <b>exported from Substance 3D Designer</b> and can be imported into some, or all other Substance 3D applications.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](ds-sbs-48.png)

### Substance 3D File

*(\*.SBS)*

Substance Files are the **main source files** for Designer. When you open a Substance File, you can **view and edit all nodes in a Graph**. They are represented as packages, that can contain any number of resources such as Graphs, Functions, Bitmaps, Meshes, etc... They are harder to share and less fast to calculate. They can only be opened in Substance 3D Designer and the Substance Player.

</td>
<td style="border: 0;" valign="top">

![](sbsar-48.png)

### Substance 3D Asset

*(\*.SBSAR)*

Substance Archives are<b> compiled, optimized</b> Substance files. They are much faster to calculate and can easily be shared without reference issues. Parameters can still be tweaked, but editing the graph is <b>locked down</b>. Substance Archives can be used in all Substance 3D applications and any application that has a [Substance 3D integration](https://helpx.adobe.com/substance-3d-integrations/home.html) (some with an external plugin) such as Autodesk 3DS Max &amp; Maya, Unreal Engine or Unity Engine.

</td>
<td style="border: 0;" valign="top">

![](bmp-96.png){width="48px"}

### Static Files

*(\*.TGA, \*.BMP, \*.PNG, \*.FBX, \*.OBJ etc...)*

Substance 3D Designer always supports exporting to static file types. A 2D image can be exported to a bitmap file, a 3D model can be exported to common 3D filetypes. When exported to static files, **all dynamic functionality is lost**. Images are locked in resolution, 3D models are locked in polycount.

</td>
</tr>
</table>

This generally means you will keep your work in the SBS format when working inside Designer, you'll export to SBSAR if the target supports it (Painter for example), or you will use static bitmap files if there is no need or no support for SBSAR.

## Resource types

Substance 3D files can contain a large variety of resources that serve different purposes. Some resources can only be authored inside Designer, some will come from external applications.

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

[![](graph-5.png){width="150px"}](../../help/compositing-graphs/substance-compositing-graphs.md)

</td>
<td width="100.00%" style="border: 0;" valign="top">

### Substance graphs

Substance graphs allow you to generate and process *2D image data* and then output it to one or more texture outputs. In many use cases, a project will revolve around one or more Substance graphs.

[Go to the section dedicated to Substance graphs.](../../help/compositing-graphs/substance-compositing-graphs.md)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

[![](function-1.png){width="150px"}](../../help/function-graphs/function-graphs.md)

</td>
<td width="100.00%" style="border: 0;" valign="top">

### Substance function graphs

<b>Functions</b> are a higher level of abstraction and complexity: rather than processing image data (sets of pixel values), you *process single values* (integers, floats, vectors). Functions are used when you want to perform more complicated operations or if you want to fine tune specific behaviors. Functions generally do not work standalone, and they are not used outside the context of Substance graphs.

[Go to the section dedicated to Substance function graphs.](../../help/function-graphs/function-graphs.md)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

[![](mdl-graph.png){width="150px"}](../../help/mdl-graphs/creating-an-mdl-graph/creating-an-mdl-graph.md)

</td>
<td width="100.00%" style="border: 0;" valign="top">

### MDL graphs

MDL graphs are a special type of graph resource that can be authored. MDL stands for Material Definition Language. These graphs are not meant for generating and processing texture files and image data, but rather to generate the look of a material in a format that is portable and exchangeable between applications and renderers.

[Go to the section dedicated to MDL graphs.](../../help/mdl-graphs/mdl-graphs.md)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td width="16.67%" style="border: 0;" valign="top">

[![](folder-4.png){width="150px"}](../../help/resources/importing-linking-and-new/importing-linking-and-new-resources.md)

</td>
<td width="100.00%" style="border: 0;" valign="top">

### Non-graph resources

Non-graph resources can come from external applications (such as Photoshop or Autodesk Maya), while some can also be *created inside Designer*. The major difference is that they are not node-based graphs; most of them are elements to be used inside or alongside the previously mentioned graph types.

The following resource types exist:

* [Bitmaps](../../help/resources/bitmap-resource/bitmap-resource.md)
* [Vector graphics (SVG)](../../help/resources/vector-graphics-svg-res/vector-graphics-svg-resource.md)
* [3D mesh and scene](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/3d-mesh-resource-200574577.html)
* [Font](../../help/resources/font-resource/font-resource.md)
* [AxF](../../help/resources/axf-appearance-exchange/axf-appearance-exchange-format.md)

</td>
</tr>
</table>
