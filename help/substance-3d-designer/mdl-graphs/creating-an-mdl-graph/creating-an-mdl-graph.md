---
title: "Creating an MDL graph | Substance 3D Designer"
description: "Designer > MDL graphs > Creating an MDL graph"
---

# Creating an MDL graph

This page describes the process of creating an MDL graph to author MDL materials in Substance 3D Designer.

![MDL graph creation pathways](mdl-new-graph-hl.png "MDL graph creation pathways")

*Pathways for creating a new MDL graph in Designer's interface*

## Methods of creating an MDL graph

You may create an MDL graph by using any of the following methods:

* Select the **File &gt; New &gt; MDL graph** option in the *main menu bar*
* Click the ![](mdl-new-graph-icon.png) **Add MDL graph** button in the *main toolbar*
* Right-click an *existing package* in the **Explorer** panel, and select the **New &gt; MDL graph** option

You will be presented with the **New MDL graph** dialog, see below.

![New MDL graph dialog](mdl-templates.png "New MDL graph dialog")

*New MDL graph dialog*

## New MDL graph dialog

Regardless of the method used to create a new MDL graph you will always be met with the <b>New MDL graph</b> dialog which lets you configure the new graph.

### Templates

The<b> Templates</b> section allows you to select a graph template, which include preconfigured nodes to get you started with your graph faster. The preconfigured nodes include Output nodes, simple nodes to pass values to these outputs - e.g., Uniform color, and Input nodes depending on the template.

To start from a completely *blank* graph, select the <b>Empty</b> template.

The <b>Project</b> option lets you filter the templates list by Project file. This makes it easy to find the custom templates in the locations added under the <b>General</b> section of the Project settings for the project file.

>[!WARNING]
>
> If you select the wrong template, you *cannot* switch to a different template after creating the graph.  
> To port your existing graph to another template, you may create a new graph using the appropriate template, and copy-paste your graph to the new one. Reconnect nodes as appropriate, including the [Root](../main-mdl-graph-concepts/main-mdl-graph-concepts.md) node.

The templates list can be displayed in different modes using the *buttons* next to the **Project** combobox:

* **![](mdl-template-recent-icon.png) Display recently used**: filters the list to display the last templates used in order from *most recent to least recent*, the top item being the most recent
* **![](mdl-template-graphs-icon.png) Display graphs**: templates are displayed by their *label only*, in the order of the [Substance 3D](https://www.adobe.com/products/substance3d/3d-augmented-reality.html) files in the templates’ directory
* **![](mdl-template-packages-icon.png) Display Substance 3D files**: templates are displayed by their label as *children of the Substance 3D file they belong to*, in the order of the files in the templates’ directory
* **![](mdl-template-directory-icon.png) Display directories**: templates are displayed by their label as *children of the directory they belong to*, in the order of the files in the templates’ directory

### Properties

The <b>Graph Properties </b>section allows you to set up basic information regarding the new graph. Any of these can be changed afterwards at any time, but it makes sense to pay attention at first and set these up appropriately for your use case.

* <b>Graph name</b>: the graph's identifier. It needs to be unique for a given package and cannot include spaces and some special characters.
* <b>Create graph in package</b>: You can use this combo box to create a *new*package for the new graph or add the new graph to any *existing* package already loaded in the Explorer panel.  
  Note: If the creation process is started using the method <b>4</b> (see above), this parameter is *preset* to the existing package the process was started from.
* <b>Template details</b>: this section provides a short text explaining the characteristics and purpose of the template
