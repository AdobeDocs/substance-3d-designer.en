---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/package-metadata.html"
breadcrumb-title: ""
description: Learn how to create and manage package metadata in Substance 3D Designer for organized asset libraries.
helpx_creative_field: ""
helpx_description: Designer > Package Metadata
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Package Metadata
user-guide-description: ""
user-guide-title: ""
---

# Package Metadata

Package Metadata is a dictionary of text (string) values defined at the Package level. It is included in the SBSAR when publishing, and it is a general purpose storage aimed to be used by python scripting.

## Displaying and editing metadata through Designer interface

If you are developing a Python plugin, you may want to edit metadata manually for testing and debugging purpose. Here is how you can do that:

1. If you double-click on a package in the explorer, it opens the Properties panel on this package.

   ![Package metadata](../assets/empty.png "Package metadata")
1. Here you have a dedicated section "Metadata". It is likely to be empty in your case, like in the capture above.

   You can add a new metadata by using the "plus" button.

   ![Add metadata button](../assets/hoveradd.png "Add metadata button")
1. A new item appears in the section:

   ![New metadata](../assets/newitem-1.png "New metadata")
1. There is a "Key" field and a "Value" field. Both can be set to anything that suits your need. The "Key" field must have a unique value across the list.

   ![New metadata value](../assets/newitemfilled.png "New metadata value")
1. You can also choose the "Type" of the item. At the moment it can be "String" or "URL":

   ![Change metadata type](../assets/typecombo.png "Change metadata type")
1. Here "URL" means a reference to a resource included in the package. To do so, choose a file on your hard drive, and drag-and-drop it on the package in the Explorer. It can be a regular resource, like an image, or any other file, like a text file.

   ![Generic resource in package](../assets/resourceinpackage.png "Generic resource in package")
1. The file appears as a new resource in the package.

   Now go back to the package Properties panel, create a new metadata, give it a proper key, and choose "URL" as type. Then select the "..." button in the "Value" field, and choose "From Resource". Finally, pick the file you included just before, and validate:

   ![URL metadata](../assets/urlmetadata.gif "URL metadata")
1. Now you can see the "URL" of the resource is stored in the "Value" field.

   You can also delete metadata using the "X" button to the right of the item:

   ![Delete metadata](../assets/hoverdelete.png "Delete metadata")

>[!NOTE]
>
> Moving or re-ordering metadata entries is disabled: the order is not meaningful, and will not be maintained when publishing the package.

## Metadata in published SBSAR files

In some scenarios, you may want to retrieve the metadata you defined on a package in the matching published SBSAR. Below you can read how metadata are transformed and stored in the archive, and the proper way to exploit them from it.

The metadata is stored according to the JSON format in a file named /assemblies/content/0000/metadata.json (the path is relative to the root of the .sbsar archive).

Regular (string) metadata is stored as is, e.g. "key": "stringValue", one per line. Again, the original order of the various keys is not retained, and is implementation defined. Never rely on the ordering in your process, as with regular Python dicts!

As the aim of URL metadata is to allow users and plugins to include foreign files in the .sbsar archive, they are subject to a specific transformation: First, the file of the resource matching the stored URL is copied in to the archive in an implementation defined location (usually in a numbered subfolder, which will contain only this file. The point is to avoid name conflict.) The file will retain its original name (the name of the resource is discarded at this point). Then instead of the original URL in the metadata.json, the path to the copied file in the archive relative to the metadata.json is written.

If we export the example package created in the previous section (after creating at least one graph with some outputs), we get this archive content:

```

myPackage.sbsar

|-- assemblies

        |-- content

            |-- 0000

                |-- New_Graph.sbsasm

                |-- New_Graph.xml

                |-- metadata.json

                |-- resources

                    |-- 0

                        |-- TEXT.txt
```


And metadata.json content is:

```

{

    "myResource": "resources/0/TEXT.txt",

    "myText": "This is a text"

}
```


At the moment, no specific tool is provided to access the metadata and resources stored in the archive. The recommended way is to open the archive with the LZMA decoder of your choice and to parse the metadata.json with a regular JSON parser (If the keys or value strings contain some fancy characters, they will be escaped the JSON way).

>[!NOTE]
>
> There is not information left on whether each metadata was a simple string or an URL, so you have to know what each key you may want to read is supposed to mean.
