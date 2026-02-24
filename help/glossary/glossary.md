---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/glossary.html"
breadcrumb-title: ""
description: Access the Substance 3D Designer glossary to find definitions of terms, concepts, and technical terminology.
helpx_creative_field: ""
helpx_description: Designer > Glossary
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Glossary
user-guide-description: ""
user-guide-title: ""
---


# Learn about terms and concepts used in Designer.

## &#35;

|  |  |
| --- | --- |
| <b><span id="three-d-scene"></span>3D scene</b> | A collection of objects and data involved in representing and animating a visualisation of 3D space:<ul data-preserve-html="true"> <li data-preserve-html="true">[Meshes](#mesh)</li> <li data-preserve-html="true">[Materials](#material)</li> <li data-preserve-html="true">Cameras</li> <li data-preserve-html="true">Lights</li> <li data-preserve-html="true">Animation</li> <li data-preserve-html="true">Simulations</li> <li data-preserve-html="true">...</li> </ul>[Popular file formats](https://www.adobe.com/products/substance3d/discover/3d-files-formats.html) to store 3D scenes include Pixar's [USD](#usd) and Autodesk's FBX. All file formats do not support all these components |

## A

|  |  |
| --- | --- |
| <b><span id="alpha"></span>Alpha channel</b> | The fourth channel of a color image, often used to describe opacity. |
| <b><span id="ambient-occlusion"></span>Ambient occlusion</b> | The attenuation of ambient light on surfaces that are less exposed and therefore harder to reach. |
| <b><span id="anisotropy"></span>Anisotropy</b> | The property of being dependent on direction. In other words, providing a different result when measured or observed on a different axis.   Anisotropic materials have a different look depending where they are looked from, and anisotropic filters are not applied uniformally in all directions. |
| <b><span id="api"></span>API</b> | An Application Programming Interface (API) is a collection of functions and procedures which lets users access the functions and procedures of another application of program.   An API provides a controlled and secure layer between the user and a program. It may also use another programming language to make that program easier to interact and more widely accessible.   Designer offers a [Python API](../scripting/scripting.md) which provides easy access to a wide range of its capabilities for manipulating data, building custom tools and accelerating workflows. |
| <b><span id="atomic-node"></span>Atomic node</b> | The fundamental building blocks of graphs. All [instance nodes](#instance-node) can be broken down into graphs of atomic nodes. Each graph type has its own set of atomic nodes. |

## B

|  |  |
| --- | --- |
| <b><span id="baking"></span>Baking</b> | The process of computing information out of a 3D model and storing the results into a [texture](#texture). The data is placed in the texture according to the model's [UVs](#uv). |
| <b><span id="base-color"></span>Base color</b> (Albedo) | A channel of a [material](#material) defined using the PBR Metallic Roughness [shading](#shader) model. Base color specifies the color of a surface without any lighting information.   It should not be confused with [Diffuse](#diffuse). |
| <b><span id="base-parameter"></span>Base parameter</b> | A parameter common to all nodes in a Substance graph that compute a [bitmap](#bitmap).   These include core aspects of the bitmap, such as its resolution ([Output size](#output-size)) and [bit depth](#bit-depth) (Output format), or how the bitmap is computed such as [tiling](#tiling) mode.   Base parameters are often [inherited](#inheritance) from other nodes upstream or the graph hosting the node. |
| <b><span id="bilinear-filtering"></span>Bilinear filtering</b> | An interpolation process used in computer imaging when a [texture sample](#texture-sampling) is not performed exactly at the center of a pixel.   For instance, this may occur when an image is enlarged. |
| <b><span id="bit-depth"></span>Bit depth</b> | The number of bits used to store the value of a pixel in a texture. Higher bit depths allow more values to be encoded, resulting in smoother gradients.   Different bit depths are available depending on the type of the value: - Integer values can be encoded using 8 bits (0 to 255) or 16 bits (0 to 65,535). - Floating point values can be encoded using 16 bits (+32767.9999 to -32768.0  ) or 32 bits (-3.4E+38 to +3.4E+38)   Low dynamic range images use integer values to encode steps from 0 to 1. High dynamic range images use floating point values to encode raw numerical values.   In Substance graphs, bit depth is controlled by the Output Format parameter. |
| <b><span id="bitmap"></span>Bitmap</b> | A digital image. Two types of images are most common:<ul data-preserve-html="true"> <li data-preserve-html="true">Grayscale images have only one channel: luminance (L);</li> <li data-preserve-html="true">Color images have three channels: red, green and blue (RGB). A fourth one may be present: alpha (A) which is often used for opacity. Color images in Designer are always RGBA.</li> </ul>  Bitmaps may be thought of as grids of values. Each cell of that grid is a pixel, which is short for 'picture element'. A pixel stores one value per channel. The type of that value depends on the [bit depth](#bit-depth) of the bitmap. |

## C

|  |  |
| --- | --- |
| <b><span id="cache"></span>Cache</b> (Memory) | A collection of data – E.g. node's [base parameters](#base-parameter) and output images – stored in memory to be reused.   Cache greatly speeds up graph computations by letting the [Substance Engine](#substance-engine) only recompute the parts of a graph that have changed. When tweaking node connections and parameters, all the nodes that precede it are not impacted by those changes, thus do not need to be [evaluated](#evaluation) again to update the graph. Their cache is used instead.   The cache can have a significant memory footprint when working with high resolutions and bitdepths in large graphs. |
| <b><span id="channel-packing"></span>Channel packing</b> | An optimisation technique where separate images are packed into the RGB(A) channels of a single color image.   For instance, an RMA texture is a roughness map (R), metalness map (M) and ambient occlusion map (A) all packed into a single color texture.   Another common technique is packing a grayscale texture into the blue channel of a normal map, as the blue channel – I.e., the 'Up' component of the normal vector – can be recomputed at runtime.   The [RGBA merge](../compositing-graphs/nodes-reference-for-com/node-library/filters/channels/rgba-merge/rgba-merge.md) node is useful for implementing this technique. |
| <b><span id="color-space"></span>Color space</b> | A definition of how a range of colors is represented. Digitally encoding and decoding a specific color requires such a definition to make sense of the numbers used.   An image file stores color values using a specified color space, so that these colors can be reproduced faithfully on a display that supports that color space. A display has specific color reproduction capabilities that allow it to fully or partially support a given color space.   Raw data – E.g. a normal map – is always encoded and decoded in a Linear color space because these colors are not meant to be visualised and no transformations should be applied to that data.   sRGB is a widely supported color space. Others popular color spaces include Adobe RGB, Rec. 2100 and ProPhoto RGB. |
| <b><span id="cooking"></span>Cooking </b>(<span id="compilation"></span>Compilation) | The process of translating data into another language so it can be executed quickly and efficently. Computing the result of a Substance graph requires compiling it first. Compilation is part of the graph [evaluation](#evaluation) process.   This compilation is performed on a flattened graph, which means all [instance nodes](#instance-node) are 'replaced' by their source graphs so that one larger graph remains, and that graph is what is compiled.   A compiled graph is not editable. Exposed parameter remain available if they are [dynamic](#dynamic-parameter), while [static](#static-parameter) parameters are locked and hidden. |
| <b><span id="culling"></span>Culling</b> | An optimization technique for rendering 3D scenes which removes geometry from a render's computations when it is not visible.   This may include objects or polygons outside of the camera's frustum (*frustum culling*), facing the oppsite way from the camera (*backface culling*) or completely hidden by other opaque objects (*occlusion culling*). |

## D

|  |  |
| --- | --- |
| <b><span id="dependency"></span>Dependency</b> | A file A that is used by another file B in such a way that file B does not work as intended when file A is missing.   A dependency of a [package](#package) can be another package because it references a graph inside it, an image file, a font, etc.   A package stores the path to its dependency, and a warning is raised if the dependency cannot be found at that path. Missing dependencies can also result in [ghost instance nodes](#ghost-instance-node) in a graph. |
| <b><span id="diffuse"></span>Diffuse</b> | A channel of a [material](../glossary/glossary.md) defined using the PBR Specular Glossiness [shading](#shader) model. Diffuse specifies the color of a surface when lit.   It should not be confused with [Base color (Albedo)](#base-color). |
| <b><span id="directx"></span>DirectX</b> | A collection of APIs for handling multimedia content. Its 3D API, Direct3D, is widely used in video game development and other 3D industries.   Direct3D places the origin of a texture – I.e., its (0, 0) coordinate – at the *top left*, (Y-down) whereas the [OpenGL](#opengl) API places it at the *bottom left* (Y-up).   This means a DirectX normal map has an *inverted green channel* compared to OpenGL. Indeed, the green channel hosts the normal vectors' Y-coordinate. |
| <b><span id="displacement"></span>Displacement</b> | The process of moving the [vertices](#vertex) of a 3D model, often along their [normal](#normal).   Displacement is often used in combination with [tessellation](#tessellation) and [normal maps](#normal-map) to model finer detail on a surface. |
| <b><span id="dynamic-parameter"></span>Dynamic parameter</b> | A parameter which value may change. In other words, any parameter which value is not constant is dynamic.    This includes exposed parameters, any parameters impacted by an exposed parameter, and any parameter value that is impacted by [sampling in a texture](#texture-sampling).   Contrarily to [static parameters](#static-parameter), the value of dynamic parameters can be adjusted on the fly after the graph is compiled into an SBSAR file. |

## E

|  |  |
| --- | --- |
| <b><span id="evaluation"></span>Evaluation</b> | The process of resolving the propagation of data and parameters in the graph. Evaluation verifies the validity of a graph and its connections, applies [inheritance](#inheritance), and [cooks](#cooking) the graph.   In the Graph View, a connection is represented with a dotted line when it is not evaluated. Evaluation turns connection into solid lines.    Every time a parameter is adjusted in a graph, the node hosting this parameter and all nodes downstream are [invalidated](#invalidation) and need to be re-evaluated before being [rendered](#rendering). |

## F

|  |  |
| --- | --- |
| <b><span id="filter"></span>Filter</b> (Node) | A node which applies a modification to an image (E.g., a deformation) or extracts information out of it (E.g., a mask). |

## G

|  |  |
| --- | --- |
| <b><span id="ghost-instance-node"></span>Ghost instance node</b> | An [instance node](#instance-node) referencing a subgraph that cannot be found – I.e., a missing [dependency](#dependency) – is loaded as a ghost instance node.   Ghost instance nodes are restored to their expected state by resolving the missing dependency and reloading the [package](#package). |
| <b><span id="glossiness"></span>Glossiness</b> | A channel of a [material](../glossary/glossary.md) defined using the PBR Specular Glossiness [shading](../glossary/glossary.md) model. Glossiness specifies the rugosity of a surface – I.e. microscopic variations of height, also called *microfacets*.   High glossiness results in a smooth look, while low glossiness results in a rough, matte look.   It is the inverse of [Roughness](#roughness). |

## H

|  |  |
| --- | --- |
| <b><span id="histogram"></span>Histogram (image)</b> | In the context of an image, a histogram represents the population of the values in a give range – often &#91;0, 1&#93;.   This population is visualized using vertical bars where a value more present in the image results in a higher bar for that value. The bars are distributed horizontally from low values (dark) to high values (bright).   Histograms of color images usually overlap the histograms of each of their channels – typically R, G, B. |

## I

|  |  |
| --- | --- |
| <b><span id="inheritance"></span>Inheritance</b> | In the context of Substance graphs, inheritance describes the property of nodes acquiring parameter values from their upstream nodes, or their parent graph.   Inherited parameters include [resolution](#resolution) ([Output size](#output-size)), [bitdepth](#bit-depth) ([Output format](#output-format)) and [tiling](#tiling) mode.   Learn more about inheritance in this [dedicated page](../compositing-graphs/inheritance-compositing/inheritance-in-substance-compositing-graphs.md). |
| <b><span id="instance-node"></span>Instance node</b> | An instance node represents a graph A into another graph B. In that case, graph A may be called a [subgraph](#subgraph) of graph B. Any change in graph A is propagated to all instance nodes that represent it.   The instance node applies its own set of values for the input parameters of graph A in the context of graph B. In that sense, graph B can host multiple instance node that all reference graph A, but each pass different values or textures as inputs into graph A.   All nodes in Designer's Library that are not [atomic nodes](#atomic-node) are instance nodes. |
| <b><span id="invalidation"></span>Invalidation</b> | The process declaring that the result of a node is outdated.   When a parameter is adjusted, the node hosting this parameter and all nodes downstream are invalidated, thus need to be [evaluated](#evaluation) and [rendered](#rendering) again. |

## M

|  |  |
| --- | --- |
| <b><span id="material"></span>Material</b> | The collection of properties and behaviours of matter in space, which includes surfaces and volumes. The appearance of an entity in 3D space is defined by its material.   Materials may be defined in various ways, and all definitions do not support all properties such as refraction, anisotropy or sheen. A [shader](#shader) is a particular implementation of a material definition.   <b>Important:</b> The term 'material' is an *umbrella term* used to refer to various things, including:<ul data-preserve-html="true"> <li data-preserve-html="true">The [shader](#shader) used to compute the appearance of a surface or volume;</li> <li data-preserve-html="true">The set of [textures](#texture) provided to a shader;</li> <li data-preserve-html="true">A Material ID, which is an attribute of a 3D primitive used to tell apart the parts that use different materials.</li> </ul> |
| <b><span id="mesh"></span>Mesh</b> | An 3D object made of [vertices](#vertex) connected by edges to form polygons – such as triangles – which in turn are assembled into surfaces. These surfaces may be open or closed.   The appearance of these surfaces is defined by the [material](#material) assigned to them. The level of detail of a mesh is also highly dependent on its [polycount](#polycount). |
| <b><span id="metadata"></span>Metadata</b> | Data that provides information about the file itself, its environment or anything related to the file's data.   Common metadata include the file's author, creation and modification dates, copyright and cover art.   In Designer, the contents of a [package](#package) can also have metadata. For instance, a Substance graph generating a fabric material may have metadata for the fabric's physical properties. |
| <b><span id="mipmap"></span>Mipmap</b> | A smaller version of a texture, often automatically-computed.   A texture can have a pyramid of smaller versions of itself, which are interchangeable at runtime so that the most appropriate size is used for optimal quality and performance.   For instance, a texture with high-frequency detail displayed at a smaller size will likely produce *moiré* artifacts. Additionally, a larger texture likely involves more [texture samples](#texture-sampling).   The term 'mipmap' originates from the MIP mapping technique, where MIP stands for the latin '*multum in parvo*', which means 'many things in a small place'. |

## N

|  |  |
| --- | --- |
| <b><span id="node"></span>Node</b> | Object in a graph that performs computations and outputs one or more results.   The result is controlled using input parameters. These parameters can be listed as controls in the Properties dock, or as input connectors on the node itself.   There are two main categories of nodes: [atomic nodes](#atomic-node) and instance nodes. |
| <b><span id="noise"></span>Noise</b> | A non-figurative image representing a random or pseudo-random distribution of shapes and colors. Noises are often used to add variation to surfaces or deformations.   Designer's node library includes a large collection of noise generators, such as [BnW Spots](../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/bnw-spots-2/bnw-spots-2.md), [Clouds](../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/clouds-2/clouds-2.md), [Perlin noise](../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/perlin-noise/perlin-noise.md) or [Voronoi](../compositing-graphs/nodes-reference-for-com/node-library/texture-generators/noises/voronoi/voronoi.md). |
| <b><span id="normal"></span>Normal</b> | In 3D computing, the normal of a surface is a [normalized](#normalization) vector perpendicular to that surface going from that surface outward.   This vector represents the orientation of a surface in 3D space and is used for [shading](#shader) that surface according to the scene's lights and camera perspective.   A [normal map](#normal-map) texture can be applied to a surface to modify its normals and add detail. |
| <b><span id="normal-map"></span>Normal map</b> | A texture applied on a surface to modify its normals.   It is most often used to fake details that would be inefficient to include in a model's geometry. Using such a map allows to have per-texel normals in addition to per-vertex normals, resulting in more surface information and thus more surface detail.   The X, Y and Z coordinates of the normal vectors are encoded into the map's red, green and blue channels respectively. Depending on the targeted graphics API ([DirectX](#directx) or [OpenGL](#opengl)), the green channel may be inverted. |
| <b><span id="normalization"></span>Normalization</b> | The process of remapping a range of values to the &#91;0, 1&#93; range, where the highest input value is remapped to 1.0 and the lowest input value is remapped to 0.0.   For vectors, normalization is adjusting the vector's length (or 'magnitude') to a value of 1.0. |

## O

|  |  |
| --- | --- |
| <b><span id="opengl"></span>OpenGL</b> | A 3D graphics API widely used in video game development and other 3D industries.   OpenGL places the origin of a texture – I.e., its (0, 0) coordinate – at the *bottom left*, (Y-up) whereas the [DirectX](#directx) API places it at the *top left* (Y-down).   This means an OpenGL normal map has an *inverted green channel* compared to DirectX. Indeed, the green channel hosts the normal vectors' Y-coordinate. |
| <b><span id="openusd"></span>OpenUSD</b> | See [USD](#usd). |
| <b><span id="output-format"></span>Output format</b> | [Base parameter](#base-parameter) of nodes in a Substance graph that describes the node's [bit depth](#bit-depth). |
| <b><span id="output-size"></span>Output size</b> | [Base parameter](#base-parameter) of nodes in a Substance graph that describes the node's [resolution](#resolution).   Learn more about Output size in this [dedicated page](../compositing-graphs/output-size/output-size.md). |

## P

|  |  |
| --- | --- |
| <b><span id="package"></span>Package</b> | A Substance 3D file ([SBS](#sbs-file)) is called a package, in the sense that it is a container for resources: graphs, [bitmaps](#bitmap), [3D scenes](#three-d-scene), etc.   A package also stores paths to its [dependencies](#dependency) as well as [metadata](#metadata). |
| <b><span id="pattern"></span>Pattern</b> | An image which should be used as a model or reference for producing another image.   In most cases, a pattern is an image meant to be repeated (E.g., tiled, scattered randomly or arranged according to some set of rules). |
| <b><span id="pixel-ratio"></span>Pixel ratio</b> | This [base parameter](#base-parameter) controls the compensation of the image's aspect ratio at the pixel level. In other words: whether the pixel size should be compensated to conserve a square ratio in a non-square image.   The parameter is used by non-local filters – I.e., filters which use the values of neighbouring pixels to compute the value of a pixel. |
| <b><span id="pixel-size"></span>Pixel size</b> | This base parameter defines the horizontal and vertical size of a pixel.   It acts as multiplier for non-local filters – I.e., filters which use the values of neighbouring pixels to compute the value of a pixel. |
| <b><span id="polycount"></span>Polycount</b> | The amout of polygons of a 3D [mesh](#mesh). Indeed, polycount is short for 'polygon count'.   More polygons can model finer detail. Meshes with a low polycount are called 'low-poly', while higher polycounts are called 'high-poly'. |
| <b><span id="primary-input"></span>Primary input</b> | The input connector of an [instance node](#instance-node) from which that node inherits its [base parameter](#base-parameter) values.   The primary input is marked with a small dot in its connector, and the '(Primary) suffix in its label.   When using nodes with more than one input, it is *strongly* recommended to be mindful of which of their inputs is the primary and how it impacts [inheritance](#inheritance) throughout the graph. |
| <b><span id="procedural"></span>Procedural</b> | The chacteristic of an piece of data or artifact to be created by following a computer algorithm, rather than manually.   Designer uses a procedural workflow where the algorithm is designed as a node graph.     Procedural workflows allow for faster iterations because variations and adjustments can be quickly generated by modifying the algorithm and its parameters.   When the result is entirely produced by the algorithm, that result is colloquially referred to as being '100% procedural'. Procedural generation is sometimes shortened to 'proc-gen'.   Most generators in Designer's node library are 100% procedural in that they require no input image to produce a result. |
| <b><span id="publishing"></span>Publishing (SBSAR)</b> | In Designer, publishing refers to exporting a [package](#package) as an SBSAR archive file which includes [compiled](#compilation) versions of the graphs, their resources ([bitmaps](#bitmap), fonts, etc.), their presets as well as their [metadata](#metadata).   The resulting SBSAR file may then be distributed and used in other Substance 3D applications or third-party applications through a [Substance 3D plugin](https://substance3d.adobe.com/plugins/). |

## R

|  |  |
| --- | --- |
| <b><span id="renderer"></span>Renderer</b> | A program which processes 3D information such as lights, meshes, and materials to create 2D images. |
| <b><span id="rendering"></span>Rendering </b>(3D View) | The process of computing an image according to input data, using a program such as a [renderer](#renderer). |
| <b><span id="resolution"></span>Resolution</b> | The amount of pixels horizontally and vertically that form a [bitmap](#bitmap). More pixels allow for representing finer detail.   In Substance graphs, the resolution of a bitmap computed by a [node](#node) is controlled by the node's '[Output size](#output-size)' [base parameter](#base-parameter). |
| <b><span id="roughness"></span>Roughness</b> | A channel of a [material](../glossary/glossary.md) defined using the PBR Metallic Roughness [shading](../glossary/glossary.md) model. Roughness specifies the rugosity of a surface – I.e. microscopic variations of height, also called *microfacets*.   High roughness results in a matte look, while low roughness results in a smooth, glossy look.   It is the inverse of [Glossiness](#glossiness). |

## S

|  |  |
| --- | --- |
| <b>Sampling</b> (Sample) | Acquiring the value of an image or function at a specific point.   See [texture sampling](#texture-sampling). |
| <b><span id="sbs-file"></span>SBS file</b> | SBS stands for 'SuBStance 3D file'. This file is used to store Substance 3D Designer projects. Its data uses the [XML](#xml) format. See [package](#package). |
| <b><span id="sbsar-file"></span>SBSAR file</b> | SBSAR stands for 'SuBStance 3D ARchive'. This archive file is used to store compiled Substance 3D Designer graphs and the resources they require ([bitmaps](#bitmap), fonts, etc.).   SBSAR is the main file format used to distribute Substance graphs that are ready to be consumed by other Substance 3D applications and Substance 3D plugins.   Since the graphs stored in SBSAR files are compiled, they cannot be loaded and edited in Substance 3D Designer. SBSAR files may however be opened using [7Zip](https://www.7-zip.org/) to retrieve their parameters, presets and metadata in an embedded [XML](#xml) file. |
| <b><span id="shader"></span>Shader</b> | Program that computes the appearance of a surface or volume according to its [material](#material) properties, the light it receives and where it is being viewed from. A shader is a particular implementation of a material definition.   Textures may be provided to a shader to drive its behaviour. Raw values may also be used. In the [3D view](../interface/3d-view/3d-view.md), go to the 'Materials' menu to see which shader is being used by a material in the current scene. The menu also lets you access the [shader properties](../interface/3d-view/3d-view.md) and which textures and values are currently being used by the shader.   'Shader' is sometimes used interchangeably with '[Material](#material)'. |
| <span id="sheen"></span><b>Sheen</b> | The shine or luster aspect of a fabric.   This term is widely used in the textile industry to describe a reflective property which adds a subtle colored brightness. |
| <b><span id="spline"></span>Spline</b> | Generally, a curve modelled using a mathematical function, which allows for clean and smooth shapes to be drawn at any resolution. Designer uses a lossy approximation encoded in a texture using a custom data format.   Splines offer intuitive controls for length and trajectory, include other data such as thickness and height, and provide easy access to distance and direction at any point along them.   These qualities make them a powerful tool for drawing and texturing. |
| <b><span id="static-parameter"></span>Static parameter</b> | A parameter which value may not change.   Contrarily to [dynamic parameters](#dynamic-parameter), static parameters cannot be changed on the fly when the graph is compiled into an SBSAR file. They can be exposed and modified in Designer only as the graph is being authored.   Preview Mode will hide these parameters in some cases, since it aims to match the behaviour of published SBSAR files as closely as possible.   A list of static parameters is available [here](../compositing-graphs/manage-parameters/exposing-a-parameter/exposing-a-parameter.md). |
| <b><span id="subgraph"></span>Subgraph</b> | A graph used in another graph as an [instance node](#instance-node). |
| <b><span id="substance-engine"></span>Substance Engine</b> | A proprietary technology developed by the Substance 3D team, in charge of  computing images by performing a high amount of transformations, effects and compositing of input images, very efficiently.   The Substance Engine implements and computes Designer's [atomic nodes](#atomic-node).   The engine is implemented through different backends, according to the platform it runs on: CPU, GPU and operating system. In Designer, the backends can be switched by going to [Tools &gt; Switch engine](../interface/the-main-toolbar/the-main-toolbar.md).   Some backends offer significantly better performance than others – E.g., GPU backend is much faster than CPU – and the results may be slightly different across backends. |
| <b><span id="substance-graph"></span></b><b>Substance graph</b>  (or Substance compositing graph) | A graph that outputs one or more [bitmaps](#bitmap).   A Substance graph may be used for various purproses:  - Produce a set of bitmaps that are textures describing a material;  - Perform image processing on one or more bitmap inputs, as a filter; - Generate noises, patterns or raw data, as a generator. |

## T

|  |  |
| --- | --- |
| <b><span id="tessellation"></span>Tessellation</b> | In computer graphics, tessellation is the process of subdividing a surface into more polygons, often triangles.   This process can be performed at runtime to dynamically increase the amount of polygons of a 3D model, often in combination with [displacement](#displacement) and [normal maps](#normal-map) to model finer detail using the added polygons. |
| <b><span id="texel"></span>Texel</b> | The information unit of a [texture](#texture), similarly to how a pixel is the information unit of an picture. |
| <b><span id="texture"></span>Texture</b> | An image used to represent graphics, describe the [material](#material) properties of a surface  by providing values to a [shader](#shader), and encode raw data in its [texels](#texel).   Textures are objects that can be decompressed and manipulated very efficiently by GPUs. In most cases, this efficiency requires textures to use power of two resolutions — E.g., 1024x1024, 4096x4096, 512x256, etc. |
| <b><span id="texture-sampling"></span>Texture sampling</b> | Acquiring the value of a [texture](#texture) at a specific location.   Some algorithms require many samples to be performed for comparing values, averaging them, or other operations.   If  a sample is not performed at exactly the center of a pixel, there are two options in Designer for the value which should be acquired:<ul data-preserve-html="true"> <li data-preserve-html="true"><b>Nearest:</b> The value of the nearest pixel according to its center</li> <li data-preserve-html="true"><b>Bilinear filtering:</b> The value of the interpolation between the neighbouring pixels horizontally and vertically, where closer pixels have more weight.</li> </ul> |
| <b><span id="tiling"></span>Tiling</b> | The repetition of an image horizontally, vertically, or both, without visible seams or visual discontinuity.   Designer offers a lot of [nodes](#node) that generate [noises](#noise) or [patterns](#pattern) that tile. Similarly, a lot of [filter](#filter) nodes are designed to process images while preserving tiling. |

## U

|  |  |
| --- | --- |
| <b><span id="usage"></span>Usage (output)</b> | In Substance graphs, a Usage is an attribute of an [Output](../compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md) node used to let the application know how to connect a [texture](#texture) to the [shader](#shader) in the [3D view](../interface/3d-view/3d-view.md).   When applying a Substance graph to the 3D view, all the outputs are connected to the shader based on matching usages. I.e., 'basecolor' to 'basecolor', 'roughness' to 'roughness', and so on.   Usages are also used to match connectors when using the 'Material' and 'Compact Material' [link creation modes](../interface/the-graph-view/link-creation-modes/link-creation-modes.md). |
| <b><span id="udim"></span>UDIM</b> (UV tiles) | A standard for splitting the [UV](#uv) space into tiles with a unique numeric identifier, which lets one assign a different texture to each tile.   UDIM workflows are commonplace in VFX pipelines, where high-fidelity assets require so much detail that multiple high-resolution textures are required. In that case, the asset's [UV](#uv)s are arranged across multiple UDIM (or UV tiles).   Designer supports UDIM workflows and can assign a different Substance graph per UDIM. |
| <b><span id="usd"></span>USD</b> (or OpenUSD) | The [Universal Scene Description](https://openusd.org/release/index.html) (USD) is 3D scene description format built by Pixar, built for interoperability and data exchange across applications and platforms.   USD files include the definition of data used in a scene, as well as the composition of that scene and all it involves: models, materials, cameras, animations, simulations, etc.   A USD file may include any type of data, provided that the application has access to the USD plugin which lets it read and use that data correctly.   Adobe is [involved in the Alliance for OpenUSD](https://blog.adobe.com/en/publish/2023/08/01/powering-3d-interoperability-continued-collaboration-through-openusd), a consortium of 3D industry actors which actively contribute to the development and standardization of the format. |
| <b><span id="uv"></span>UV</b> | UVs are a representation of a 3D model in 2D space. They are used to map 2D images from 2D space onto the surface of the model in 3D space.   The process of creating UVs is often described as cutting seams into the model to unfold and flatten it. |

## V

|  |  |
| --- | --- |
| <b><span id="vertex"></span>Vertex</b> | A unique point in space, often where two or more lines meet. |

## X

|  |  |
| --- | --- |
| <b><span id="xml"></span>XML</b> | The eXtensible Markup Language (XML) is a format for storing data in a human-readable format.   Similarly to HTML, data defined using tags (&lt;&gt;) and values are enclosed within tags.   The [SBS](#sbs-file) file format uses XML to arrange and store its data. |
