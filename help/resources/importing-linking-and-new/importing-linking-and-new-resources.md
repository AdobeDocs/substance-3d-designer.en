---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/resources/importing-linking-and-new-resources.html"
breadcrumb-title: ""
description: Learn how to import, link, and create new resources in Substance 3D Designer for your material projects.
helpx_creative_field: ""
helpx_description: Designer > Resources > Importing, linking and new resources
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Importing, linking and new resources
user-guide-description: ""
user-guide-title: ""
---

# Importing, linking and new resources

[Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) supports 3 modes of bringing in or creating new resources for use in your graph. These resources can be of many different types, including but not limited to [bitmaps](../../resources/bitmap-resource/bitmap-resource.md), [vector graphics](../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md), [3D scenes](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/3d-mesh-resource-200574577.html)and [fonts](../../resources/font-resource/font-resource.md). This page explains the different methods and when each one is best used.

All methods are accessed by [clicking RMB on a package in the Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html)[.](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html)

The following table gives a quick overview of the difference in functionalities between the methods.

|  | New | Import | Link |
| --- | --- | --- | --- |
| Graphs ([Substance graphs](../../compositing-graphs/substance-compositing-graphs.md), [Substance function graphs](../../function-graphs/function-graphs.md), [MDL graphs](../../mdl-graphs/mdl-graphs.md)) | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> |
| [Bitmaps](../../resources/bitmap-resource/bitmap-resource.md),[ vector graphics (SVG)](../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md) | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> |
| [3D scenes](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/3d-mesh-resource-200574577.html), [fonts](../../resources/font-resource/font-resource.md) | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> |
| Is created next to SBS file | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> |
| Editable in Designer | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> |
| External edits are automatically synched | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> | <div><img alt="(error)" data-preserve-html="true" src="../../assets/error.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> |
| Embedded in published SBSAR | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> | <div><img alt="(tick)" data-preserve-html="true" src="../../assets/check.svg"/></div> |

## New resources

Creating a new resource means a resource in your package will be created from scratch. All Designer-only resources can only be created this way, such as Substance graphs, Substance function graph and MDL graphs.

A special case is when you create a new [bitmap ](../../resources/bitmap-resource/bitmap-resource.md)or [SVG](../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md): these files will show up in your Explorer and behave like an imported resource, but without requiring an external file. They can be modified in Designer. New bitmaps and SVG's created in this way are good if you don't need to rely on an external editor: for example when you just want a quick and simple vector shape, or a simple painted 2D-bitmap mask.

## Imported resources

Importing a resource means a duplicate of the resource file will be created next to your SBS file (in the *Graphname*.resources folder), [except for SVG files](../../resources/vector-graphics-svg-res/vector-graphics-svg-resource.md). It is sometimes also referenced to as 'embeddin' a resource.

An imported resource can then be edited in Designer using the [bitmap painting tools](../../resources/bitmap-resource/bitmap-painting-tools/bitmap-painting-tools.md) or [vector editing tools](../../resources/vector-graphics-svg-res/vector-editing-tools/vector-editing-tools.md) in the [2D view](../../interface/2d-view/2d-view.md), once placed in the graph. Imported resources are no longer linked to their original source files: meaning if you change, remove or update the file originally imported, this has no effect on the resource in Designer.

In the case of [AxF files](../../resources/axf-appearance-exchange/axf-appearance-exchange-format.md) the process is a bit more complicated; a whole graph and MDL function, as well as bitmap resources are created from the AxF package. All of these can however still be edited in their respective editors: Substance graphs, MDL graphs or 2D view.

>[!WARNING]
>
> For new packages, imported and new resources are not saved to disk until you save the package.

## Linked resources

Linking a resource means Designer will reference the source file at its original location on disk, but still present it in the Explorer as if it was part of your package. You will not be able to edit the actual resource directly inside of Designer, only use it as a component in your graph or as a source for baking maps.

Linking is ideal if you know you will need to use an external editor to update your resource while you simultaneously work in Designer. Baking maps is a prime example: you could have Designer reference bitmaps form an external baking application, which will automatically reload and update your graph as soon as these files are changed. Similarly, 3D scenes can only be linked, so that every time when you export a new FBX file from your 3D application, Designer automatically updates the mesh used in the 3D view. If your are baking maps from this mesh you will have to manually start the baking process over, ideally by clicking RMB and selecting 'Refresh all baked maps'.

## Deleting resources

When deleting a resource from a package, the <b>Confirm item removal</b> dialog is displayed. If any items in the process of being removed are *referenced by other resources* – such as [graph instances](../../compositing-graphs/creating-compositing-gra/graph-instances-sub-gra/graph-instances-sub-graphs.md) and [bitmap resources](../../resources/bitmap-resource/bitmap-resource.md) used in [Substance graphs](../../compositing-graphs/substance-compositing-graphs.md) – then the dialog will include a *warning and list* of these items.

>[!NOTE]
>
> We recommend being mindful about these items and taking the necessary actions to *anticipate any broken dependencies* which would result from deleting items from a package.  
> These actions can include *removing all uses* of these resources before deletion.

!['Deleted resource being used' warning](../../assets/confirm-item-removal.png "'Deleted resource being used' warning"){width="512px"}
