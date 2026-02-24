---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/scripting-api-reference.html"
breadcrumb-title: ""
description: Access the complete Substance 3D Designer Python scripting API reference for plugin development.
helpx_creative_field: ""
helpx_description: Designer > Scripting > Scripting API reference
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Scripting API reference
user-guide-description: ""
user-guide-title: ""
---


# Scripting API reference

This page describes the main concepts of the API.

For more detailed information please refer to the documentation shipped with the application that is accessible in <b>Help &gt; Python API Documentation...</b>. In this documentation, do a <b>Quick Search</b> for the module names (in parentheses below) to easily find their definition.

## Context

The context (*Context*) object is the <b>main entry point to the API</b>. It is created the first time the user get it by using the method '<b>*getContext()*</b>' from the '*sd*' module.

This object allows to essentially <b>retrieve the application</b> (*SDApplication*) object.

## Application (SDApplication)

The application (*SDApplication*) is the object that allows <b>access to the main API managers</b> such as:

* the <b>Package </b>Manager (*SDPackageMgr*) that manages all of the application's <b>packages</b>;
* the <b>Module </b>Manager (*SDModuleMgr*) that manages all of the application's <b>modules</b>;
* the <b>UI </b>Manager (*SDUIMgr*) that can create <b>menus and docks</b> in the application's window.

You can register <b>callbacks</b> with the application that will be called when certain events happen.

## Package Manager (SDPackageMgr)

This object manages all the application's <b>packages</b>. Packages are displayed in the '<b>*Explorer*</b>' component.

It allows you to:

* <b>create</b> a new package;
* <b>load/unload</b> a package;
* <b>save</b> a package;
* <b>find</b> a package.

## Package (SDPackage)

A package (*SDPackage*) is a <b>collection of resources</b> (*SDResource*).

The content of a package can be <b>stored</b> to a file with the <b>.sbs</b> extension through the '*SDPackageMgr*' object. This object allows you to <b>retrieve </b>specific resources.

To <b>create</b> a specific resource, see the related object static methods (Ex: '*SDSBSCompGraph.sNew()*').

A package also contains a metadata dictionary (SDMetadataDict). You can find more info on metadatas [here](../../help/package-metadata/package-metadata.md).

## Resource (SDResource)

A resource (*SDResource*) is an object that can be <b>referenced</b> by another resource.

There are multiple resource <b>types</b>:

* Folders (*SDResourceFolder*);
* Graphs (*SDGraph*);
* Bitmaps (*SDResourceBitmap*);
* SVG Images (*SDResourceSVG*);
* Fonts (*SDResourceFont*);
* Scenes (*SDResourceScene*);
* BSDF Measurements (*SDResourceBSDFMeasurement*);
* Light Profiles (*SDResourceLightProfile*).

A resource can be <b>created</b> from static method '*sNew()*' under:

* a package;
* a folder.

A resource can have several <b>properties</b> (*SDProperty*).

## UI Manager (SDUIMgr)

The UI manager allows <b>creating user interface elements</b> in Substance Designer's main window, such as <b>menus</b>, <b>docks</b> and allows registering <b>callbacks</b> to be called when user interface related events happen.

Additionally, the UI manager has access to the <b>current active graph</b> and the <b>selection</b> of the active graph.

## Graphs (SDGraph)

A graph (*SDGraph*) is an object that contains:

* <b>nodes </b>(*SDNode*);
* <b>graph objects</b> (*SDGraphObjects*);
* <b>properties </b>(*SDProperty*).

There are 4 different graph types:

* Substance graph (*SDSBSCompGraph*)
* Substance function graph (*SDSBSFunctionGraph*)
* Substance FXMap graph (*SDSBSFxMapGraph*)
* MDL graph (*SDMDLGraph*)

A graph can have one or multiple <b>output</b> nodes. The output nodes represent the <b>results</b> of the graph.

All the available nodes for a graph can be <b>retrieved</b> with the method '*getNodeDefinitions()*'.

A new node can be <b>created</b> with the method '*newNode()*'.

A new <b>instance</b> node can be created from a resource (*SDResource*) with the method '*newInstanceNode()*'.

## Node (SDNode)

A node (*SDNode*) represents an <b>operation</b> carried out on an object.

It can be created from:

* a <b>definition</b> (*SDDefinition*) (see '*SDGraph.newNode()'*);
* a <b>resource</b> (*SDResource*) (see '*SDGraph.newInstanceNode()'*).

A node can have multiple <b>properties</b>.

There are multiple <b>types</b> of node:

* *<b>SDSBSCompNode</b>*: A node of the Substance Graph (*SDSBSCompGraph*);
* *<b>SDSBSFunctionNode</b>*: A node of the Substance Function Graph (*SDSBSFunctionGraph*);
* *<b>SDSBSFxMapNode</b>*: A node of the Substance FXMap Graph (*SDSBSFxMapGraph*);
* *<b>SDMDLNode</b>*: A node of the MDL Graph (*SDMDLGraph*). *Note:* Many other specific nodes inherit from this node.

## Graph Objects (SDGraphObjects)

A graph object (*SDGraphObject*) is an object that <b>adds additional information</b> to the graph, but that is <b>*not* taken into account</b> during the graph evaluation process.

There are <b>3 types</b> of graph objects:

* <b>Pin</b> (*SDGraphObjectPin*)
* <b>Comment</b> (*SDGraphObjectComment*)
* <b>Frame</b> (*SDGraphObjectFrame*)

See the static method '*sNew()*' on these objects for more information regarding how to <b>create</b> them.

## Properties (SDProperty)

A property (*SDProperty*) is an object that <b>describes</b> a property of <b>another object</b> (a graph, a node, a resource, and so on).

It belongs to a specific <b>category</b> (*SDPropertyCategory*):

* <b>Input</b>: classifies an object's input properties, which usually<b> impact the operation</b> carried out by the current object;
  * Ex: the property '*color*' of a Uniform Color node in a Substance graph is an input property;
* <b>Output</b>: classifies an object's output properties. It is used to identify a <b>result</b> of an object;
* <b>Annotation</b>: classifies properties that <b>*do not* impact the operation</b> carried out by an object;
  * Ex: the '*label*' of a graph is an annotation property, because it does not impact the graph computation.

It contains the following <b>members</b>:

* <b>Id</b>: The identifier of the property in the context of his category;
* <b>Types</b>: The types supported by the current property. Some properties can support *multiple* types: '*int*', '*float*', etc.;
  * Ex: the input properties of an '*sbs::function::add*' node can support different types: '*int'*, '*int2'*, '*int3'*, '*int4'*, '*float'*, '*float2'*, '*float3'*, '*float4', etc.;*
* <b>Category</b>: The category the property belongs to (input, output, annotation);
* <b>Label</b>: The label of the property, used for display *only*;
* <b>Description</b>: The description of the property;
* <b>DefaultValue</b>: The default value;
* <b>IsConnectable</b>: Indicates if a connection (*SDConnection*) *can* be carried out on this property;
* <b>isReadyOnly</b>: Indicates if the property is read-only. If true, the value associated to it will *not* be modifiable;
* <b>isVariadic</b>: If true, this property will be represented as *multiple* properties on the object;
* <b>isPrimary</b>: Indicates whether the specified property is the *principal* property that controls some other properties. *Note:* this is specific to Substance *Compositing* Nodes (*SDSBSCompNode*)).

Examples:

* Properties of the '*sbs::compositing::input*' node:

<table data-preserve-html="true"><colgroup><col style="width: 276.0px;"/><col style="width: 129.0px;"/><col style="width: 283.0px;"/></colgroup><tbody><tr><th colspan="3" style="text-align: center;">sbs::compositing::input</th></tr><tr><td style="text-align: left;"><strong>Input</strong></td><td style="text-align: left;"><strong>Annotation</strong></td><td style="text-align: left;"><strong>Output</strong></td></tr><tr><td>$outputsize</td><td>label</td><td><p>unique&#95;filter&#95;output (CONNECTABLE)</p></td></tr><tr><td>$format</td><td>description</td><td><br/></td></tr><tr><td>$pixelsize</td><td>identifier</td><td><br/></td></tr><tr><td>$pixelratio</td><td>userdata</td><td><br/></td></tr><tr><td>$tiling</td><td>group</td><td><br/></td></tr><tr><td>$randomseed</td><td>visibleif</td><td><br/></td></tr><tr><td><p>bitmapresourcepath</p></td><td>usages</td><td><br/></td></tr></tbody></table>

* Properties of the '*sbs::compositing::blend*' node:

<table data-preserve-html="true"><colgroup><col style="width: 278.0px;"/><col style="width: 129.0px;"/><col style="width: 283.0px;"/></colgroup><tbody><tr><th colspan="3" style="text-align: center;">sbs::compositing::blend</th></tr><tr><td style="text-align: left;"><strong>Input</strong></td><td style="text-align: left;"><strong>Annotation</strong></td><td style="text-align: left;"><strong>Output</strong></td></tr><tr><td>$outputsize</td><td><br/></td><td>unique&#95;filter&#95;output (CONNECTABLE)</td></tr><tr><td>$format</td><td><br/></td><td><br/></td></tr><tr><td>$pixelsize</td><td><br/></td><td><br/></td></tr><tr><td>$pixelratio</td><td><br/></td><td><br/></td></tr><tr><td>$tiling</td><td><br/></td><td><br/></td></tr><tr><td>$randomseed</td><td><br/></td><td><br/></td></tr><tr><td>source.connector (CONNECTABLE)</td><td><br/></td><td><br/></td></tr><tr><td><p>destination.connector (CONNECTABLE)</p></td><td><br/></td><td><br/></td></tr><tr><td>opacity.connector (CONNECTABLE)</td><td><br/></td><td><br/></td></tr><tr><td>opacitymult</td><td><br/></td><td><br/></td></tr><tr><td colspan="1">blendingmode</td><td colspan="1"><br/></td><td colspan="1"><br/></td></tr><tr><td colspan="1">colorblending</td><td colspan="1"><br/></td><td colspan="1"><br/></td></tr><tr><td colspan="1">maskrectangle</td><td colspan="1"><br/></td><td colspan="1"><br/></td></tr></tbody></table>

## Type (SDType)

A type (*SDType*) contains information of a value <b>type</b>, such as:

* <b>Id</b>: The identifier of the type;
* <b>Modifier</b>: The type modifier that can be one of the '*SDTypeModifier'* <b>enum</b> values:  
  * *Auto*;
  * *Uniform*: The value is evaluated *once* per operation;
  * *Varying*: The value is evaluated *multiple times* per operation (ex: for each texel).

Multiple types are defined, such as:

* <b>enums</b> (*SDTypeEnum*): describes an <b>enumeration</b> type with all its properties;
* <b>structures</b> (*SDTypeStruct*): describes a <b>structure</b> type with all its properties;
* <b>array</b> (*SDTypeArray*): describes an <b>array</b>.
* etc.

See Substance Designer's *Python API Documentation* for the exhaustive list.

## Values (SDValue)

A value (*SDValue*) is an object that <b>encapsulates</b> a *base type* value.

For instance:

* a '<b>*SDValueInt*</b>' object encapsulates an '*int*' value;
* a '<b>*SDValueFloat4*</b>' object encapsulates a '*float4*' value;
* etc.

The base type value can usually be <b>retrieved</b> with the '<b>get()</b>' method, but this can depend on the *type* of '*SDValue'* that has been returned.

## Connection (SDConnection)

A connection (*SDConnection*) represents a <b>link</b> between two different<b> properties</b> of two different <b>nodes</b>.

It contains:

* The <b>target node</b>;
* The <b>target property</b> of the target node;

All <b>connection operations</b> are carried out on a node:

* <b>creating</b> a new connection, see '*SDNode.newPropertyConnection()*'
* <b>deleting</b> an existing connection, see '*SDNode.deletePropertyConnection()*'
* <b>retrieving</b> the connections of a property, see '*SDNode.getPropertyConnections()*'

## Module (SDModule)

A module is a <b>collection of definitions and types</b>.

It allows easy retrieval of all the information on the nodes that can be created, as well as on enumerations and structures.

It contains:

* an <b>identifier</b> (*Id*) that is unique in the context of the module manager (*SDModuleMgr*);
* a list of <b>definitions</b> (*SDDefinition*);
* a list of <b>types</b> (*SDType*).

## Definition (SDDefinition)

A definition (*SDDefinition*) object contains information on the definition of a particular <b>object</b> based on <b>properties</b> ('*SDNode'*, etc.).

It contains:

* <b>Id</b>: the identifier of the definition;
* <b>Label</b>: The label of the definition;
* <b>Description</b>: The description of the definition;
* <b>Properties</b>: The properties of all the available property *categories* (*SDPropertyCategory*).
