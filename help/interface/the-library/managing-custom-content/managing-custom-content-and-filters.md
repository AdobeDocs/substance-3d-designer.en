---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/the-library/managing-custom-content-and-filters.html"
breadcrumb-title: ""
description: Learn how to manage custom content and filters in the Substance 3D Designer Library for organized asset access.
helpx_creative_field: ""
helpx_description: Designer > Interface > The Library > Managing custom content and filters
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Managing custom content and filters
user-guide-description: ""
user-guide-title: ""
---

# Managing custom content and filters

This page explains the method to create categories and filters to manage custom content in the Library. It also includes suggestions for project-based workflows.

## Overview

After [adding custom content to the Library](../../../interface/preferences-window/project-settings/project-settings.md), you need to make it *discoverable*.

The Library uses a number of *data points* for identifying content, for the purposes of filtering it and surfacing in searches. These data points include:

* Name
* Extension
* URL (i.e. *filename*)
* Attributes

You may organise your <b>Library</b> into categories containing specific filters, and tailor it to your project's needs.  
Indeed, custom categories and filters can be *project-specific* and be saved in [Project files](../../../interface/preferences-window/project-settings/project-settings.md) (\*.sbsprj). These files can then be assembled into [Configuration files](../../../interface/preferences-window/project-settings/project-settings.md) (\*.sbscfg) and distributed to a team so that artists can all use the *same <b>Library</b> categories* for any given project.

This means that with one or more Project files, you can set the folders which content should be added to the <b>Library</b>, as well as the categories and filters which will sort and organise that content.

![Custom content in Library](../../../assets/library-filters.png "Custom content in Library")

## Graph attributes

Graphs contained in [SBS](../../../getting-started/overview/overview.md) and [SBSAR](../../../getting-started/overview/overview.md) files can be *filtered and searched* in the Library by using the data set in the [Attributes](../../../compositing-graphs/graph-parameters/graph-parameters.md) section of the graph's properties. Some of these attributes can also be set on some other [Resource types](../../../resources/resources.md).

## Custom filters and folders

Filters are simple boolean (True/False) search parameters that will result in a resource showing up inside the Library when that <b>Filter</b> is selected. Resources can be anything kept inside a package. Keep the following in mind:

* A <b>Filter</b> will match against all resources, under *all watched paths*.
* A <b>Filter</b> can contain multiple conditions, *all of them must evaluate to True* (AND-condition) for the resource to show up under that filter.
* A [Resource](../../../resources/resources.md) can show up under multiple filters, it is *not exclusive* to any filter.
* A [Resource](../../../resources/resources.md) from a watched path is *still available* in the <b>Library</b> even if it is *not* under any <b>Filter</b>, by using the <b>Search</b> function.

### How to create filters and folders

Categories (i.e. Folders) and Filters are created and edited using the following buttons:

<b>!&#91;&#93;(../../../assets/library-icon-new-folder.png) Add Folder:</b> Creates an expandable folder in the Library view. You *cannot* create subfolders.

<b>!&#91;&#93;(../../../assets/library-icon-new-filter.png) Add Filter:</b> Adds a new Filter inside the selected folder. You *cannot* add filters to the existing default folders.

<b>!&#91;&#93;(../../../assets/library-icon-edit.png) Edit Item:</b> Edits the currently selected Folder or Filter. You *cannot* edit any of the properties of the default Folders and Filters.

To *remove* a Folder or Filter, *right-click* on it and select the <b>Remove</b> option from the contextual menu.

### Editing filters and folders

<b>Folders</b> and <b>Filters</b> are identified by the following data:

* <b>Name</b> displayed in the Library tree view.
* [Project Configuration file (SBSPRJ)](../../../pipeline-and-project-con/project-configuration-fil/project-configuration-files-sbsprj.md) in which this item is stored.

>[!WARNING]
>
> It is *very* important to set these up correctly, to ensure you are editing the *correct project*!

![Custom filter edition](../../../assets/library-filters-edit.png "Custom filter edition")

**Filters** usually need to have *conditions* set up for achieving their filtering purpose. These conditions are configured using the following criteria:

* **Resource Type**: sets a specific [Resource type](../../../resources/resources.md), such as [Graphs](../../../compositing-graphs/substance-compositing-graphs.md)
* **Attribute** to apply condition to – see list above
* **Condition logic**: lets the filter include results with positive, negative, partial and whole matches
* **Condition keyword:** the string against which the **Attribute** and **Condition logic** criteria are tested. When left blank, any resource which matches these two criteria are included

You can *add or remove* conditions using the '**+**' and '**x**' buttons on the far right of the Condition keyword.

>[!NOTE]
>
> A filter without any conditions set up will result in *all*  **Library** content being displayed.

## Best practices

### Recommended guidelines

* The general rule for the default library is the <b>Folder</b> is listed in the <b>Category</b> attribute, while the <b>Filter</b> name is determined by the <b>Tag</b> attribute
* Don't create custom nodes that mix with the default Library unless you *explicitly* want them to. Your nodes *will* show up under default Filters if they match, so you will have to make sure to use a *different tagging/naming system* to avoid that
* Use *unique*, *per-project* identifiers. These can be put anywhere you want (such as <b>Description</b>, <b>Category</b> or <b>User Data</b>), as long as you are *consistent* between all projects. This makes searching and filtering content *by project* much easier
* Use the <b>Author</b> attribute to keep track of the person initially responsible for the content, without having to dig through Version Control records
* An efficient way of creating <b>Icons</b> is either to use the <b>Generate</b> option of the [Icon](../../../compositing-graphs/graph-parameters/graph-parameters.md) graph attribute, or to create a graph [template](../../../interface/preferences-window/project-settings/project-settings.md) for generating them. That way you can ensure consistency and save work on creating them. All default library icons were created within Designer this way!

### Managing content of varying scope

* You can add Resources to *existing categories* if this makes more sense. It will be less work to manage and maintain filters, and you can use a special icon style to *tell them apart*.
* You can define your folders and filters in a *global* (studio-level) [Project Configuration file](../../../pipeline-and-project-con/project-configuration-fil/project-configuration-files-sbsprj.md), and then add content into them merely by adding watched paths from *consecutive* [Project files](../../../interface/preferences-window/project-settings/project-settings.md)
* You can define specific folders and filters for *each project* to keep them separated
* You can mix and match and use methods from all three above: use existing filters, define new global ones, and create per-project unique ones
