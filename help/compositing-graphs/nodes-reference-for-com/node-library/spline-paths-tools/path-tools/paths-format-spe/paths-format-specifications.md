---
title: "Paths Format Specifications"
description: ""
helpx_description: "Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Spline  Path Tools > Path Tools > Paths Format Specifications"
---

# Paths Format Specifications

This page describes the Paths format and provides guidance for manipulating data in that format using functions included in the Paths tools.

## Format specifications

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

This section explains how a <b>Paths document</b> (or image) is encoded:

A Paths document is a list of paths, each of which describes a list of segments, encoded in a <b>32bit floating-point color texture</b>.

The texture is split into 'top' (*$pos.y &lt; 0.5*) and 'bottom' (*$pos.y &gt; 0.5*) parts.

Any data in a pixel in the 'top' part is semantically closely related to the matching pixel in the 'bottom' part, and vice-versa.

</td>
<td width="33.33%" style="border: 0;" valign="top">

![Paths Polygon encoded data](PathsPolygon_Data.jpg "Paths Polygon encoded data")

</td>
</tr>
</table>

>[!NOTE]
>
> Paths data require 32-bit precision and using lower bitdepth will produce incorrect results.
> 
> Therefore, make sure to set the 'Ouptut Format' parameter of nodes generating Paths data to 'HDR High Precision (32F)'.

Let `*uv\_pos*` be a 2D address (such as *$pos*) of a pixel of the 'top' part.

In the rest of this document:

* <b>top&#91;uv\_pos&#93;.XYZW</b> will be referring to the 4 floats stored in the pixel of the top part.  
  top&#91;uv\_pos&#93; == sample\_color(paths, uv\_pos)
* <b>bottom&#91;uv\_pos&#93;.XYZW</b> will be referring to the 4 floats stored in the matching pixel of the bottom part.  
  bottom&#91;uv\_pos&#93; == sample\_color(paths, uv\_pos + Float2(0, 0.5))

top&#91;uv\_pos&#93; and bottom&#91;uv\_pos&#93; together are forming a semantic unit U&#91;uv\_pos&#93; of the document, composed of 8 floats.

### Document header

Every Paths document starts with a document header. It is the very first semantic unit U&#91;(0,0)&#93;:

+++Top
<b>X</b>

The number of paths (should be a positive integer in &#91;0; 16777216&#93;).

If some paths are empty, they still count here. So you can think of it as a 'number of paths headers to decode'.

<b>YZ</b>

The pixel size for this document (I.e., exactly `Float2(1,1) / $size`).

This is useful when reading the Paths from from a [Pixel processor](../../../../atomic-nodes/pixel-processor/pixel-processor.md) or an [Fx-Map](../../../../atomic-nodes/fx-map/fx-map.md), for instance, whose Output Size is different.

<b>W</b>

1/16 = 0.0625 (header flag)

+++

+++Bottom
<b>XY</b>

The address of the last vertex defined in this document. This is useful to append new data.

It can hence actually be any address that is greater (in scanline order) than the address of the last vertex. It must me in the range &#93;0, 1&#91;×&#93;0,.5&#91;

<b>ZW</b>

Unused, should be Float2(0, 1)

+++

### Path headers

The document header is immediately followed by number-of-paths = top&#91;(0,0)&#93;.X path-headers, one by semantic unit.  
E.g. if there are 3 paths in the document, they will be stored in U&#91;(0,1)\*pixel\_size&#93;, U&#91;(0,2)\*pixel\_size&#93; and U&#91;(0,3)\*pixel\_size&#93; (with pixel\_size = top&#91;(0,0)&#93;.YZ).

If there are more paths than what one line of pixel can contains, the remaining path-headers are written one the next line(s), in scanline order.  
It is allowed to have null path-headers (`top[...].XYZW = Float4(0,0,0,0)`); such path still could as one empty path.

The path-header of the Nth path will be defined at address `path\_addr` will be defined as:

+++Top
<b>X</b>

Number of vertices in this path. Must be in the &#91;0, 16777216&#93; range.

If the start and end vertices of a closed path are at the same position, they still count for 2 vertices.  
A path with 0 vertices is a valid path anyway.

<b>Y</b>

*Is\_closed* flag: 1 if the path is closed (e.g. a circle), 0 otherwise (e.g. a straight line).

<b>Z</b>

The path index *N.*It must absolutely match *path\_addr* (see note below).

<b>W</b>

The header flag: 1/16 = 0.0625.

+++

+++Bottom
<b>XY</b>

Start (or first) vertex address.

<b>ZW</b>

End (or last) vertex' address.

+++

>[!NOTE]
>
> You can compute `path\_addr` from N using the function `Utils/pixel\_index\_to\_position` in paths\_tools.sbs: `path\_addr = pixel\_index\_to\_position(N+1)`

### Vertices information

Vertices can be found anywhere in the image after the headers (document or path headers). Vertices can be of various "types" (Start, Mid or End) and they are explicitly linked together using 2 address pointers ("links").

<b>Start</b> and <b>End</b> vertices are special in this respect: To allow the representation of closed paths or of an arbitrary network of paths linked together, one of the link is actually used to form a circular forward linked list of all the other Start or End vertices that represent the same vertex. Such vertices matching each others are called "siblings". &#91;Illustration welcomed&#93;

Formally, each vertex at address `*vert\_addr*` is defined like this:

+++Top
<b>XY</b>

The vertex position. Coordinates can be any float value that is not NaN or ±inf. There is no notion of tiling at this level (it can be handle or not by the implementation of each filter), so paths are supposed to be defined on the euclidean plane.

<b>Z</b>

The vertex path index. A vertex can only belong to one Path. (As mentioned earlier, Start and End vertices can have siblings though.) The path index can be used to retrieve the path-header (see Section Path Headers above), so make sure to keep it in sync.

<b>W</b>

Vertex type. It is split between the sign of the value, and its absolute value:

On the sign part, a value of 0 would mean there is no vertex here actually (all other components should be 0 too). A negative value means the vertex is marked as a "corner"; a positive one that the vertex is "smooth". Corner vs. smooth vertex is a pure, isolated attribute and has no impact or meaning on the rest of the Paths encoding.

On the absolute value part, the kind of pixel (Start, Mid or End) and another flag (trivial\_link) are encoded:

* *0.125*: End vertex (the last vertex of the shape; always non-trivial links, see below)

* *0.25*: Start vertex (the first vertex of the shape; always non-trivial links, see below)

* *0.5*: Mid vertex with non-trivial links

* *1*: Mid vertex with trivial links

"Trivial links" refers to the fact that the previous and next vertices (in the list of vertices of the current path) are stored in the pixel to left (vert\_addr-(0,pixel\_size)) and to the right (vert\_addr+(0,pixel\_size)) respectively, while "non-trivial links" means that at least one of these is stored elsewhere.

+++

+++Bottom
Regardless of links "triviality", trustworthy values of links are stored in the bottom part:

<b>XY</b>

The address of the previous vertex of this path. For Start vertices, this points to the next sibling vertex.  
if |top&#91;vert\_addr&#93;.W| = 1, then bottom&#91;vert\_addr&#93;.XY = vert\_addr - (0,pixel\_size)

<b>ZW</b>

The address of the next vertex of this path. For End vertices, this points to the next sibling vertex.  
if |top&#91;vert\_addr&#93;.W| = 1, then bottom&#91;vert\_addr&#93;.ZW = vert\_addr + (0,pixel\_size)

+++

## Reading and writing Paths information

If you want to make your own Paths-processing nodes, you have several tools.

The basics are provided by the [Paths Vertex Processor](../paths-vertex-processor/paths-vertex-processor.md) and [Paths Vertex Processor Simple](../paths-vertex-processor-1/paths-vertex-processor-simple.md) nodes, which can basically be used the same way as a [Pixel Processor](../../../../atomic-nodes/pixel-processor/pixel-processor.md).

If you need features beyond what the Paths Vertex Processor nodes offers (more input textures, or more previous or next vertices), copying the implementation of this graph might be good starting point (assuming you replace the <b>Get(&quot;%perVertex&quot;)</b> node with you custom processing).

But in case you want to do something more alien than applying a per-vertex function, here is a detailed explanation of the tools you can use. These are usually small helper functions that can be found in the same package as the other Paths nodes (*paths\_tools.sbs)*. (These functions are not exposed in the [<b>Library</b>](../../../../../../interface/the-library/the-library.md) and <b>Node menu</b>.)

### <b>&#39;Read&#39; functions</b>

Under the `Read` folder, you can find several of these, useful to gather information about the Paths:

Some can give you information about a given pixel. They all take the sampled Float4 value in the \*top\* part as input. If you look at their implementation, they are super-simple. Their point is to convey more meaning than just atomic nodes:

+++is_header
Check that the current sampled value is either a path header or a document header.

+++

+++path_is_closed
Check the Is\_Closed flag (.Y) in a path header. It \*assumes you already checked it's a path\* with `is\_header` and that `current\_pixel\_is\_document\_header` returned false.

+++

+++is_vertex
Check that the current sampled value is a vertex, i.e. not a header, nor an empty pixel.

+++

+++is_start_vertex
Check if a \*top-part sampled\* value is a Start vertex (no need to check `is\_vertex` first).

+++

+++is_mid_vertex
Check if a \*top-part sampled\* value is a vertex that is not a Start nor End vertex (no need to check `is\_vertex` first).

+++

+++is_end_vertex
Check if a \*top-part sampled\* value is an End vertex (no need to check `is\_vertex` first).

+++

+++is_segment_start
Short-hand for `is\_start\_vertex || is\_mid\_vertex`. More useful for [Fx-Map](../../../../atomic-nodes/fx-map/fx-map.md)-based processing, to process each segment at most once.

+++

+++is_corner
Check the corner flag of the vertex (no need to check `is\_vertex` first: if the answer is true, you are on a vertex for sure). Please remind that this flag is somewhat not supported yet by official nodes.

+++

+++has_trivial_links
If that is a vertex, tells whether you can easily deduce the position of the previous and next vertices without sampling the bottom part. (Note: A non-vertex will always return false.)

You probably don't want to use this directly, but rather use one of the `sample\_next\*` or `sample\_prev\*` functions, which take care of that for you.

+++

+++sample_next, sample_prev
Given the top-part sampled value `*sampled*` and its position `*sampled\_position*`, returns the next (respectively previous) vertex top-part sampled value, and Set a Float2 variable `*next\_sampled\_pos*` to the position (in the top-part) of this neighbor (i.e. &lt;returned value&gt; = SampleColor(next\_sampled\_pos, image0)). `*input0PixSize*`must be equal to the path's pixel size (top&#91;(0,0)&#93;.YZ).

If the current pixel (`*sampled*`) is a <b>Start</b> vertex, *sample\_prev* will return the next sibling of this vertex; likewise if it is an <b>End</b> vertex, *sample\_next* will return the next sibling of this vertex (i.e. maybe not what you want). See `*sample\_next\_advanced*` and `*sample\_prev\_advanced*` below to solve this.

Please note that for simplicity, <b>Paths info are assumed to be stored in input0!</b> Also, unlike what the function's doc states, you don't need to pre-declare `*next\_sampled\_pos*`. `*[out]next\_sampled\_pos*` is a dummy parameter to remind you that this second "return value" exists.

You can check the `*paths\_trace*` [Fx-Map](../../../../atomic-nodes/fx-map/fx-map.md), in the Iterations parameter of the 3rd Iterate node, for an example of how to use it.

![Minimal use case of sample_next](paths-spec_fxmap-sample-next_02.png "Minimal use case of sample_next")



![Use case of sample_next in Preview Paths (path_trace)](paths-spec_fxmap-sample-next_01.png "Use case of sample_next in Preview Paths (path_trace)")



+++

+++sample_next_advanced, sample_prev_advanced
This is aimed to work on closed paths. For open paths, the Start or End vertex doesn't have a sibling, and in this case both functions return the same and only neighbor. For Start or End vertices with more than one sibling (Paths connected as a network), that would return the neighboring vertex of the next sibling in the linked list.

+++

### <b>&#39;Write&#39; functions</b>

Under the `Write` folder, you will find small helpers that builds a Float4 ready to be written <b>by an &#91;Fx-Map&#93;(../../../../atomic-nodes/fx-map/fx-map.md)</b>.

Indeed, the [Fx-Map](../../../../atomic-nodes/fx-map/fx-map.md) multiplies RGB by Alpha before drawing, so the actual values are un-premultiplied to compensate for that. If you want to use these function e.g. in a [Pixel Processor](../../../../atomic-nodes/pixel-processor/pixel-processor.md), we recommend that you apply the premultiplication yourself again, or that you write a custom version (more optimized for your use case and easier to use).

+++document_header
Builds the top part of the document header, declaring the number of paths you provide.

+++

+++document_last_vertex_spec
Builds the \*bottom\* part of the document header, which specify the last vertex address (see A.1.).

+++

+++path_header
Builds the top part of a path header, according to the number of vertices in the path `*nbVertices*`, the `*isClosed*` flag, and the `*pathIndex*`.

+++

+++start_vertex, mid_vertex, end_vertex
Builds the top part of a vertex, setting the position, type and other options accordingly.

About *mid\_vertex* and the *hasTrivialLinks* parameter: Ideally you should set the appropriate value, but if for any reason you end up not being able to tell whether links will be trivial or not, you can safely set it to false (at the cost of slower processing of your generated path).

+++

There is no bottom-part builder for path headers nor vertices: both encode two links to the top part, so this function would essentially be a Vector Float4 constructor from two Float2. Don't forget to divide XYZ by W if you are writing using an [Fx-Map](../../../../atomic-nodes/fx-map/fx-map.md) (W being the Y of an address, it should never be null).

You will find a pertinent example of how to use these functions in the <b>*paths\_polygon.sbs* </b>package hosting the [Paths Polygon](../paths-polygon/paths-polygon.md) node.

### Methods for processing paths

You will likely use either a Pixel Processor or an Fx-Map to implement your custom processing, each of which has its strength and weaknesses:

+++FX-Map
The [Fx-Map](../../../../atomic-nodes/fx-map/fx-map.md)-based solution will usually be preferred when performing high-level operation requiring a global knowledge of the whole path (or paths), or a cumulative one (e.g. repacking vertices after decimation or tessellation). It is also the easiest to approach, so if you are doing a custom processing for the first time, you may want to use a Fx-Map, despite it *might* be slower.

You need to be familiar with Fx-Map in the first place. If that's not the case, please check the [specific documentation](../../../../atomic-nodes/fx-map/fx-map.md).

We recommend that you look at the implementation of [Preview Paths](../preview-paths/preview-paths.md) in <b>*paths\_trace.sbs*</b> and [Paths Polygon](../paths-polygon/paths-polygon.md) in <b>*paths\_polygon.sbs*</b> to get an idea about how to read and write (respectively) path using an Fx-Map.

+++

+++Pixel Processor
The [Pixel Processor](../../../../atomic-nodes/pixel-processor/pixel-processor.md) solution will be fitting if you only need "local" information. Here we mean "local" not spatially (the distance between element) but rather topologically (vertices linked together). This is how the Vertex Processor is implemented. The Pixel Processor is usually faster than the Fx-Map for this kind of operation, as each pixel's function is evaluated in parallel, while only a limited amount of data is accessed. Implementation effort might be far more important though, as you can only modify the current pixel.

We won't get into detail, as there is so much to say depending on you specific use case, but the first thing to do is checking where you are:

Are you in the top ($pos.y &lt; 0.5) or bottom ($pos.y &gt; 0.5) part? We recommend that remember that in a dedicated variable (e.g. `*isTop*`), and that you create a `*vert.addr*` Float2 those value is `*$pos*` for the top part, and `$pos - (0,0.5)` for the bottom part.

What is at *vert.addr*? Sample it and check whether there's anything (W != 0) then, if there is, what exactly. A header (W = 0.0625) (check with `*Read/is\_header*`) or a vertex (check with `Read/is\_vertex`)? And if it's a header, is it the document header or a Path header? (You can use `*Read/current\_pixel\_is\_document\_header*` to check that.) Use one or several of the helper functions to match what is interesting to you.

+++
