---
title: "GLSLFX Shaders"
description: "Use GLSLFX shaders in Substance 3D Designer 3D view to customize material rendering and preview effects."
helpx_description: Designer > Interface > 3D View > GLSLFX Shaders
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/3d-view/glslfx-shaders.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - shading
  - gradients
  - creative-effects
---




# GLSLFX Shaders

GLSLFX files make the bridge between the application and the glsl shader files.  
It allows to use any glsl shader without having to modify the code.

## File Format

GLSLFX file format is a XML file. Comments are supported.

### Header and Root node

The XML root node element is named <b>glslfx</b>.

```

<?xml version="1.0" encoding="UTF-8"?>

<glslfx version="1.0.0" author="allegorithmic.com">

    <!-- BODY -->

    <!-- ... -->

</glslfx>
```


### Body

#### Technique

XML Element that describes a technique. A technique is a variation of the current FX. A GLSLFX can contain multiple techniques but at least one technique has to be defined.

The geometry will be rendered with one of the techniques defined by the application.

+++XML element definition
<b>Name:</b> technique

<b>Attributes:</b>

* name: Any string used to name the technique

+++

The XML element can have multiples children. The elements defined in a techniques override the elements defined globally.

For example, it is used to override some uniforms values and obtain FX variation for this technique.

#### Render Pass

XML Element that describes a render pass. A render pass describes the rendering of the geometry.

A technique can contain multiple render passes that will be executed sequentially. A technique containing no render pass is equivalent to a technique containing an 'onscreen' render pass.

The elements defined in a render pass override the elements defined in the parent technique.

+++XML element definition
<b>Name:</b> pass

<b>Attributes:</b>

* output

* offscreen: The rendering will be done into user defined render targets

* onscreen: The rendering will be done into the default render target

+++

#### Shaders

Set the GLSL shader files for each type.

XML Element Definition:

+++XML element definition
<b>Name:</b> shader

<b>Attributes:</b>

* type: The GLSL shader type;

* filename: The path of the glsl shader file. Can be absolute or relative to the GLSLFX file;

* primitiveType: The method to render the primitive.


| 'type' Value | Description |
| --- | --- |
| vertex | Vertex shader |
| geometry | Geometry shader |
| tess\_control | Tessellation Control shader |
| tess\_eval | Tessellation Evaluation shader |
| fragment | Fragment shader |



| 'primitiveType' Value | Description |
| --- | --- |
| point | Render as points |
| lineloop | Render as line loop |
| patch&#91;1..N&#93; | Render as patches with &#91;1..N&#93; vertices |


+++

#### Properties

Allow to set up some part of the OpenGL state.

+++XML element definition
<b>Name:</b> property

<b>Attributes:</b>

* name: The name of the property to set. The name is based on the OpenGL function or glEnum name:  
  * Enums syntax: Without the 'GL\_' prefix, in lower case. Examples: glEnable(GL\_BLEND\_ENABLE) =&gt; """, glDisable(GL\_CULL\_FACE) =&gt; """
  * Functions syntax: without the 'gl' prefix, in lower case and with all words separated with '\_' character. Example: glBlendFunc(GL\_SRC\_ALPHA, GL\_ONE\_MINUS\_SRC\_ALPHA) =&gt; ""

* Enums syntax: Without the 'GL\_' prefix, in lower case. Examples: glEnable(GL\_BLEND\_ENABLE) =&gt; """, glDisable(GL\_CULL\_FACE) =&gt; """

* Functions syntax: without the 'gl' prefix, in lower case and with all words separated with '\_' character. Example: glBlendFunc(GL\_SRC\_ALPHA, GL\_ONE\_MINUS\_SRC\_ALPHA) =&gt; ""

* value: The value of the property.


| 'name' Values | 'value' Values | Description |
| --- | --- | --- |
| blend\_enabled | boolean | Enable/disable the blending mode |
|  | true |  |
|  | false |  |
| blend\_func | string, string | Set the sources and destination blending functions |
|  | zero | for OpenGL enum GL\_ZERO |
|  | one | for OpenGL enum GL\_ONE |
|  | src\_color | for OpenGL enum GL\_SRC\_COLOR |
|  | one\_minus\_src\_color | for OpenGL enum GL\_ONE\_MINUS\_SRC\_COLOR |
|  | dst\_color | for OpenGL enum GL\_DST\_COLOR |
|  | one\_minus\_dst\_color | for OpenGL enum GL\_ONE\_MINUS\_DST\_COLOR |
|  | src\_alpha | for OpenGL enum GL\_SRC\_ALPHA |
|  | one\_minus\_src\_alpha | for OpenGL enum GL\_ONE\_MINUS\_SRC\_ALPHA |
|  | dst\_alpha | for OpenGL enum GL\_DST\_ALPHA |
|  | one\_minus\_dst\_alpha | for OpenGL enum GL\_ONE\_MINUS\_DST\_ALPHA |
|  | constant\_color | for OpenGL enum GL\_CONSTANT\_COLOR |
|  | one\_minus\_constant\_color | for OpenGL enum GL\_ONE\_MINUS\_CONSTANT\_COLOR |
|  | constant\_alpha | for OpenGL enum GL\_CONSTANT\_ALPHA |
|  | one\_minus\_constant\_alpha | for OpenGL enum GL\_ONE\_MINUS\_CONSTANT\_ALPHA |
|  | src\_alpha\_saturate | for OpenGL enum GL\_SRC\_ALPHA\_SATURATE |
|  | src1\_color | for OpenGL enum GL\_SRC1\_COLOR |
|  | one\_minus\_src1\_color | for OpenGL enum GL\_ONE\_MINUS\_SRC1\_COLOR |
|  | src1\_alpha | for OpenGL enum GL\_SRC1\_ALPHA |
|  | one\_minus\_src1\_alpha | for OpenGL enum GL\_ONE\_MINUS\_SRC1\_ALPHA |
| cull\_face\_enabled | boolean | Enable/disable the face culling |
|  | true |  |
|  | false |  |
| cull\_face\_mode | string | Set the face culling mode |
|  | front | for OpenGL enum GL\_FRONT |
|  | back | for OpenGL enum GL\_BACK |
|  | front\_and\_back | for OpenGL enum GL\_FRONT\_AND\_BACK |
| depth\_func | string | Set the depth compare function |
|  | never | for OpenGL enum GL\_NEVER |
|  | less | for OpenGL enum GL\_LESS |
|  | lequal | for OpenGL enum GL\_LEQUAL |
|  | equal | for OpenGL enum GL\_EQUAL |
|  | notequal | for OpenGL enum GL\_NOTEQUAL |
|  | gequal | for OpenGL enum GL\_GEQUAL |
|  | greater | for OpenGL enum GL\_GREATER |
|  | always | for OpenGL enum GL\_ALWAYS |


+++

#### Uniforms

Allow to override some uniforms defined globally or in the parent technique. This allow to change shader behavior for this technique or render pass.

See the <b>Uniforms</b> section below for more details about their definition.

+++Example


+++

## Render Targets

For 'offscreen' render passes, render targets must be defined in the render pass.

+++XML element definition
<b>Name:</b> output

<b>Attributes:</b>

* attachment: The OpenGL attachment point, inspired by the OpenGL names:  
  GL\_COLOR\_ATTACHMENT&#91;0..3&#93; =&gt; 'color&#91;0..3&#93;'  
  GL\_DEPTH\_ATTACHMENT =&gt; 'depth'

attachment: The OpenGL attachment point, inspired by the OpenGL names:  
GL\_COLOR\_ATTACHMENT&#91;0..3&#93; =&gt; 'color&#91;0..3&#93;'  
GL\_DEPTH\_ATTACHMENT =&gt; 'depth'

* name: the name of the render target.  
  It can be used in a later render pass to bind this render target as a sampler.

name: the name of the render target.  
It can be used in a later render pass to bind this render target as a sampler.

* format: the internal format of the render target.

format: the internal format of the render target.

* clear: optional attribute that defines a clear value.  
  If present, the render target will be cleared to this value at the beginning of the render pass.  
  If missing, the render target will keep its previous content.

+++

>[!NOTE]
>
> Color render targets are forbidden in an 'onscreen' render pass, but a depth render target can be shared with any render pass (but it's likely to break rendering when mixing multiple materials in the scene).

<b>About formats</b>

For depth formats, all depth-only (no stencil) OpenGL formats are supported:

* GL\_DEPTH\_COMPONENT16 =&gt; 'depth26'
* GL\_DEPTH\_COMPONENT24 =&gt; 'depth34'
* GL\_DEPTH\_COMPONENT32 =&gt; 'depth42'
* GL\_DEPTH\_COMPONENT32F =&gt; 'depth42f'

For color formats, the name is based on OpenGL enum names, without the 'GL\_' prefix, in lower case.  
Three channel formats (RGB) are not supported, use an RGBA format instead.  
Bit depth per channel supported:

* Normalized unsigned integer: 8, 16
* Floating point: 16, 32

An exception to these rules is the GL\_R11F\_G11F\_B10F format which is supported.:

* GL\_RGBA8 =&gt; 'rgba8'
* GL\_RGBA16F =&gt; 'rgba16f'
* GL\_SRGB8\_ALPHA8 =&gt; 'srgb8\_alpha8'
* GL\_R11F\_G11F\_B10F =&gt; 'r11f\_g11f\_b10f'
* GL\_RG16 =&gt; "rg16"

### Samplers

Allow to override some samplers defined globally, they cannot be defined in a technique. This allow to define a sampler usage for this render pass, or to read from a render target of a previous render pass.

See the <b>Samplers</b> section for more details about their definition.

+++Example


+++

## Input Vertex Format

This allow to define the semantic of each attributes define in the vertex shader.

<b>XML Element Definition:</b>

Name: 'vertexformat'

Attributes:

* 'name': The name of the attribute as defined in the vertex shader.
* 'semantic': The semantic of the attribute.

| 'semantic' Value | Description |
| --- | --- |
| position | Vertex position (float3) |
| normal | Vertex normal (float3) |
| texcoord&#91;0..N&#93; | Vertex texture coordinate buffer N (float2) |
| tangent&#91;0..N&#93; | Vertex tangent buffer N (float4) |
| binormal&#91;0..N&#93; | Vertex binormal buffer N (float4) |

Example:

```

<?xml version="1.0" encoding="UTF-8"?>

<glslfx version="1.0.0" author="allegorithmic.com">

     <!-- BODY -->

     <!-- ... -->



     <!-- INPUT VERTEX FORMAT -->

     <vertexformat name="iVS_Position" semantic="position"/>

     <vertexformat name="iVS_Normal" semantic="normal"/>

     <vertexformat name="iVS_UV" semantic="texcoord0"/>

     <vertexformat name="iVS_Tangent" semantic="tangent0"/>

     <vertexformat name="iVS_Binormal" semantic="binormal0"/>

</glslfx>
```


## Samplers

This allow to define the usage of each samplers.  
It is used by the application to known which texture to set in the specified samplers.

<b>XML Element Definition:</b>

Name: 'sampler'

Attributes:

* 'name': The name of the sampler variable in the shader file.
* 'usage': The usage of the sampler. It matches the usage specified in the Ouput node of the graph.

| 'usage' Value | Description |
| --- | --- |
| diffuse | Diffuse map |
| opacity | Opacity map |
| emissive | Emissive map |
| ambientocclusion | Ambient occlusion map |
| ambient | Ambient map |
| mask | Mask map |
| detailnormal | Detail Normal map |
| normal | Normal map |
| bump | Bump map |
| height | Height map |
| displacement | Displacement map |
| specularlevel | Specular level map |
| specularcolor | Specular color map |
| specular | Specular map |
| glossiness | Glossiness map |
| roughness | Roughness map |
| anisotropylevel | Anisothropy level map |
| anisotropyangle | Anisothropy angle map |
| transmissive | Transmissive map |
| reflection | Reflection map |
| refraction | Refraction map |
| environment | Environment map (cube map) |
| panorama | The Panorama Map (Latitude/Longitude Map) |
| bluenoisemask | A 256x256 dithering texture |

* Multiple usages are supported.
  * Example:

```

   <!-- SAMPLERS -->

    <sampler name="baseColorMap" usage="basecolor,diffuse"/>

     <!-- ... -->
```


'isHidden': Boolean that indicates if the sampler should appear in the GUI

* Example:

```

     <!-- SAMPLERS -->

    <sampler name="bluenoiseMask" usage="bluenoisemask" ishidden="true"/>

     <!-- ... -->
```


Wrapping Mode:

<table data-preserve-html="true"><tbody><tr><th>Name</th><th>Value</th></tr><tr><td rowspan="4">texture&#95;wrap&#95;s, texture&#95;wrap&#95;t, texture&#95;wrap&#95;r<br/><br/><br/></td><td>clamp&#95;to&#95;edge</td></tr><tr><td>clamp&#95;to&#95;border</td></tr><tr><td colspan="1">mirrored&#95;repeat</td></tr><tr><td colspan="1">repeat<br/><br/></td></tr></tbody></table>

Texture Filter

<table data-preserve-html="true"><tbody><tr><th>Name</th><th>Value</th></tr><tr><td rowspan="6">texture&#95;min&#95;filter, texture&#95;mag&#95;filter<br/><br/><br/></td><td>nearest</td></tr><tr><td>linear</td></tr><tr><td colspan="1">nearest&#95;mipmap&#95;nearest</td></tr><tr><td colspan="1">linear&#95;mipmap&#95;nearest</td></tr><tr><td colspan="1">nearest&#95;mipmap&#95;linear</td></tr><tr><td colspan="1">linear&#95;mipmap&#95;linear</td></tr></tbody></table>

Example:

```

<?xml version="1.0" encoding="UTF-8"?>

<glslfx version="1.0.0" author="allegorithmic.com">

     <!-- BODY -->

     <!-- ... -->



     <!-- SAMPLERS -->

     <sampler name="baseColorMap" usage="basecolor,diffuse"/>

     <sampler name="heightMap" usage="height"/>

     <sampler name="normalMap" usage="normal"/>

     <sampler name="detailNormalMap" usage="detailNormal"/>

     <sampler name="environmentMap" usage="environment"/>

     <sampler name="bluenoiseMask" usage="bluenoisemask" ishidden="true"/>

     <sampler name="sssDiffuseMap" usage="sssDiffuse"/>

</glslfx>
```


## Uniforms

This allows you to add additional information on each shader uniforms.

<b>XML Element Definition:</b>

Name: 'uniform'

Attributes:

'name': The name of the uniform in the shader file.

| 'semantic' Value | Description |
| --- | --- |
| world | World Matrix (float16) |
| worldinversetranspose | World Inverse Transpose Matrix (float16) |
| worldviewprojection | World View Projection Matrix (float16) |
| viewinverse | World Inverse Matrix (float16) |
| worldview | World View Matrix (float16) |
| modelview | Model View Matrix (float16) |
| projection | Projection Matrix (float16) |
| ambient | Scene Ambient Color (float3) |
| lightposition&#91;0..N&#93; | Position of the scene's Nth light (float3) |
| lightcolor&#91;0..N&#93; | Color of the scene's Nth light (float3) |
| lightintensity&#91;0..N&#93; | Intensity of the scene's Nth light (float) |
| globaltime | Current time in secs (float) |
| resolution | Viewport resolution (int2) |
| mouse | Mouse position (int2) |
| samplespostablesize | Number of samples to use to compute the environment lighting (int) |
| irradianceshcoefs | The array of spherical harmonics vectors (float3&#91;10&#93;) |
| panoramamipmapheight | Number of mipmap levels in the panorama map (float) |
| panoramarotation | Angle Rotation angle of the panorama map (float) |
| panoramaintensity | Intensity of the panorama map (float) |
| computebinormalinfragmentshader | Does the binormal be computedt per fragment ? (if not then per vertex) (bool) |
| isdirectxnormal | Is the normal map format DirectX ? (bool) |
| uvwscale | Scale values of u, v, w (float3) |
| renderuvtile | Render only 1 UV tile ? (bool) |
| uvtilecoords | UV tile coordinate to render (int2) |

'semantic': The semantic of the uniform. (All matrices are float16).

Example:

```

<?xml version="1.0" encoding="UTF-8"?>

<glslfx version="1.0.0" author="allegorithmic.com">

     <!-- BODY -->

     <!-- ... -->



     <!-- MATRICES -->

     <uniform name="worldMatrix" semantic="world"/>

     <uniform name="worldViewProjMatrix" semantic="worldviewprojection"/>

     <uniform name="worldViewMatrix" semantic="worldview"/>

     <uniform name="worldInverseTransposeMatrix" semantic="worldinversetranspose"/>

     <uniform name="viewInverseMatrix" semantic="viewinverse"/>

     <uniform name="modelViewMatrix" semantic="modelview"/>

     <uniform name="projectionMatrix" semantic="projection"/>

</glslfx>
```


Example:

```

<?xml version="1.0" encoding="UTF-8"?>

<glslfx version="1.0.0" author="allegorithmic.com">

    <!-- BODY -->

    <!-- ... -->



    <!-- SCENE PARAMETERS -->

    <uniform name="AmbiColor" semantic="ambient"/>

    <uniform name="Lamp0Pos" semantic="lightposition0"/>

    <uniform name="Lamp0Color" semantic="lightcolor0"/>

    <uniform name="Lamp1Pos" semantic="lightposition1"/>

    <uniform name="Lamp1Color" semantic="lightcolor1"/>

</glslfx>
```


### Other parameters

Other additional information can be add to each uniforms to:

* define the default value
* clamp values
* control the way the uniform will be display in the application:
* set the label
* set the widget info used to edit the value in the application:
* widget name, min, max, increment/decrement step
* group uniforms in group widgets

As the Uniforms can be override for each techniques, it allows to display a specific gui setup for each techniques.

<b>XML Element Definition:</b>

Name: 'uniform'

Attributes:

* 'name': The name of the uniform in the shader file.
* 'default': The uniform default value
* 'min': The min value of the validity range
* 'max': The max value of the validity range
* 'guiName': The name of the uniform in the GUI of the application
* 'guiGroup': The name of the group to put the uniform in the GUI of the application
* 'guiWidget': The name of the widget used to edit the uniform value in the GUI of application

| 'guiWidget' Value | Description |
| --- | --- |
| slider | Slider widget for floatN |
| angle | Angle widget for float |
| color | Color widget for float3, float4 color |
| checkbox | CheckBox widget for bool |

* 'guiMin': The min value of the widget
* 'guiMax': The max value of the widget

## Example: Tessellation/Parallax

### Parallax Vertex Shader File

Located in .\tessellation\_parallax\parallax\vs.glsl

Content:

> &#35;version 120

attribute vec4 iVS&#92;&#95;Position;  
attribute vec4 iVS&#92;&#95;Normal;  
attribute vec2 iVS&#92;&#95;UV;  
attribute vec4 iVS&#92;&#95;Tangent;  
attribute vec4 iVS&#92;&#95;Binormal;

varying vec3 iFS&#92;&#95;Normal;  
varying vec2 iFS&#92;&#95;UV;  
varying vec3 iFS&#92;&#95;Tangent;  
varying vec3 iFS&#92;&#95;Binormal;  
varying vec3 iFS&#92;&#95;PointWS;

uniform mat4 worldMatrix;  
uniform mat4 worldViewProjMatrix;

void main&#40;&#41;  
&#123;  
 gl&#92;&#95;Position &#61; worldViewProjMatrix &#92;&#42; iVS&#92;&#95;Position;  
 iFS&#92;&#95;Normal &#61; iVS&#92;&#95;Normal&#46;xyz;  
 iFS&#92;&#95;UV &#61; iVS&#92;&#95;UV;  
 iFS&#92;&#95;Tangent &#61; iVS&#92;&#95;Tangent&#46;xyz;  
 iFS&#92;&#95;Binormal &#61; iVS&#92;&#95;Binormal&#46;xyz;  
 iFS&#92;&#95;PointWS &#61; &#40;worldMatrix &#92;&#42; iVS&#92;&#95;Position&#41;&#46;xyz;  
&#125;

### Tessellation Vertex Shader File

Located in .\tessellation\_parallax\tessellation\vs.glsl  
  
Content:

> 

&#35;version 120

attribute vec4 iVS&#92;&#95;Position;  
attribute vec4 iVS&#92;&#95;Normal;  
attribute vec2 iVS&#92;&#95;UV;  
attribute vec4 iVS&#92;&#95;Tangent;  
attribute vec4 iVS&#92;&#95;Binormal;

varying vec4 oVS&#92;&#95;Normal;  
varying vec2 oVS&#92;&#95;UV;  
varying vec4 oVS&#92;&#95;Tangent;  
varying vec4 oVS&#92;&#95;Binormal;

void main&#40;&#41;  
&#123;  
 gl&#92;&#95;Position &#61; iVS&#92;&#95;Position;  
 oVS&#92;&#95;Normal &#61; iVS&#92;&#95;Normal;  
 oVS&#92;&#95;UV &#61; iVS&#92;&#95;UV;  
 oVS&#92;&#95;Tangent &#61; iVS&#92;&#95;Tangent;  
 oVS&#92;&#95;Binormal &#61; iVS&#92;&#95;Binormal;  
&#125;

### Tessellation Control Shader File

Located in .\tessellation\_parallax\tessellation\tcs.glsl  
  
Content:

> 

&#35;version 400 core  
&#35;extension GL&#92;&#95;ARB&#92;&#95;tessellation&#92;&#95;shader : enable

layout&#40;vertices &#61; 3&#41; out;

in vec4 oVS&#92;&#95;Normal&#91;&#93;;  
in vec2 oVS&#92;&#95;UV&#91;&#93;;  
in vec4 oVS&#92;&#95;Tangent&#91;&#93;;  
in vec4 oVS&#92;&#95;Binormal&#91;&#93;;

out vec4 oTCS&#92;&#95;Normal&#91;&#93;;  
out vec2 oTCS&#92;&#95;UV&#91;&#93;;  
out vec4 oTCS&#92;&#95;Tangent&#91;&#93;;  
out vec4 oTCS&#92;&#95;Binormal&#91;&#93;;

uniform float tessellationFactor;

void main&#40;&#41;  
&#123;  
 gl&#92;&#95;TessLevelOuter&#91;0&#93; &#61; tessellationFactor;  
 gl&#92;&#95;TessLevelOuter&#91;1&#93; &#61; tessellationFactor;  
 gl&#92;&#95;TessLevelOuter&#91;2&#93; &#61; tessellationFactor;  
 gl&#92;&#95;TessLevelInner&#91;0&#93; &#61; tessellationFactor;  
 gl&#92;&#95;out&#91;gl&#92;&#95;InvocationID&#93;&#46;gl&#92;&#95;Position &#61; gl&#92;&#95;in&#91;gl&#92;&#95;InvocationID&#93;&#46;gl&#92;&#95;Position;

oTCS&#92;&#95;Normal&#91;gl&#92;&#95;InvocationID&#93; &#61; oVS&#92;&#95;Normal&#91;gl&#92;&#95;InvocationID&#93;;  
 oTCS&#92;&#95;UV&#91;gl&#92;&#95;InvocationID&#93; &#61; oVS&#92;&#95;UV&#91;gl&#92;&#95;InvocationID&#93;;  
 oTCS&#92;&#95;Tangent&#91;gl&#92;&#95;InvocationID&#93; &#61; oVS&#92;&#95;Tangent&#91;gl&#92;&#95;InvocationID&#93;;  
 oTCS&#92;&#95;Binormal&#91;gl&#92;&#95;InvocationID&#93; &#61; oVS&#92;&#95;Binormal&#91;gl&#92;&#95;InvocationID&#93;;  
&#125;

### Tessellation Evaluation Shader File

Located in .\tessellation\_parallax\tessellation\tcs.glsl  
  
Content:

> 

&#35;version 400 core

layout&#40;triangles, equal&#92;&#95;spacing, ccw&#41; in;

in vec4 oTCS&#92;&#95;Normal&#91;&#93;;  
in vec2 oTCS&#92;&#95;UV&#91;&#93;;  
in vec4 oTCS&#92;&#95;Tangent&#91;&#93;;  
in vec4 oTCS&#92;&#95;Binormal&#91;&#93;;

uniform mat4 worldMatrix;  
uniform mat4 worldViewProjMatrix;

uniform sampler2D heightMap;

uniform float tiling &#61; 1&#46;0f;  
uniform float heightMapScale &#61; 1&#46;0f;

out vec3 iFS&#92;&#95;Normal;  
out vec2 iFS&#92;&#95;UV;  
out vec3 iFS&#92;&#95;Tangent;  
out vec3 iFS&#92;&#95;Binormal;  
out vec3 iFS&#92;&#95;PointWS;

vec3 interpolate3D&#40;vec3 v0, vec3 v1, vec3 v2, vec3 uvw&#41;  
&#123;  
 return uvw&#46;x &#92;&#42; v0 &#43; uvw&#46;y &#92;&#42; v1 &#43; uvw&#46;z &#92;&#42; v2;  
&#125;

vec2 interpolate2D&#40;vec2 v0, vec2 v1, vec2 v2, vec3 uvw&#41;  
&#123;  
 return uvw&#46;x &#92;&#42; v0 &#43; uvw&#46;y &#92;&#42; v1 &#43; uvw&#46;z &#92;&#42; v2;  
&#125;

void main&#40;&#41;  
&#123;  
 vec3 uvw &#61; gl&#92;&#95;TessCoord&#46;xyz;

vec3 newPos &#61; interpolate3D&#40;gl&#92;&#95;in&#91;0&#93;&#46;gl&#92;&#95;Position&#46;xyz, gl&#92;&#95;in&#91;1&#93;&#46;gl&#92;&#95;Position&#46;xyz, gl&#92;&#95;in&#91;2&#93;&#46;gl&#92;&#95;Position&#46;xyz, uvw&#41;;  
 vec3 newNormal &#61; normalize&#40;interpolate3D&#40;oTCS&#92;&#95;Normal&#91;0&#93;&#46;xyz, oTCS&#92;&#95;Normal&#91;1&#93;&#46;xyz, oTCS&#92;&#95;Normal&#91;2&#93;&#46;xyz, uvw&#41;&#41;;  
 vec3 newTangent &#61; normalize&#40;interpolate3D&#40;oTCS&#92;&#95;Tangent&#91;0&#93;&#46;xyz, oTCS&#92;&#95;Tangent&#91;1&#93;&#46;xyz, oTCS&#92;&#95;Tangent&#91;2&#93;&#46;xyz, uvw&#41;&#41;;  
 vec3 newBinormal &#61; normalize&#40;interpolate3D&#40;oTCS&#92;&#95;Binormal&#91;0&#93;&#46;xyz, oTCS&#92;&#95;Binormal&#91;1&#93;&#46;xyz, oTCS&#92;&#95;Binormal&#91;2&#93;&#46;xyz, uvw&#41;&#41;;  
 vec2 newUV &#61; interpolate2D&#40;oTCS&#92;&#95;UV&#91;0&#93;, oTCS&#92;&#95;UV&#91;1&#93;, oTCS&#92;&#95;UV&#91;2&#93;, uvw&#41;;

float heightTexSample &#61; texture&#40;heightMap, newUV &#92;&#42; tiling&#41;&#46;x &#92;&#42; 2&#46;0 &#45; 1&#46;0;  
 newPos &#43;&#61; newNormal &#92;&#42; heightTexSample &#92;&#42; heightMapScale;

vec4 obj&#92;&#95;pos &#61; vec4&#40;newPos, 1&#41;;  
 gl&#92;&#95;Position &#61; worldViewProjMatrix &#92;&#42; obj&#92;&#95;pos;

iFS&#92;&#95;UV &#61; newUV &#92;&#42; tiling;  
 iFS&#92;&#95;Tangent &#61; newTangent;  
 iFS&#92;&#95;Binormal &#61; newBinormal;  
 iFS&#92;&#95;Normal &#61; newNormal;  
 iFS&#92;&#95;PointWS &#61; &#40;worldMatrix &#92;&#42; obj&#92;&#95;pos&#41;&#46;xyz;  
&#125;

### Fragment Shader File

Located in .\tessellation\_parallax\fs.glsl  
  
Content:

> 

&#35;version 120

// &#35;define ALG&#92;&#95;NORMAL&#92;&#95;DIRECTX  
&#35;define ALG&#92;&#95;NORMAL&#92;&#95;OPENGL

&#35;ifdef ALG&#92;&#95;NORMAL&#92;&#95;DIRECTX  
 // &#35;define FLIP&#92;&#95;NORMAL&#92;&#95;X  
&#35;define FLIP&#92;&#95;NORMAL&#92;&#95;Y  
 // &#35;define FLIP&#92;&#95;NORMAL&#92;&#95;Z  
&#35;endif //&#35;ifdef ALG&#92;&#95;NORMAL&#92;&#95;DIRECTX

&#35;ifdef ALG&#92;&#95;NORMAL&#92;&#95;OPENGL  
 // &#35;define FLIP&#92;&#95;NORMAL&#92;&#95;X  
&#35;define FLIP&#92;&#95;NORMAL&#92;&#95;Y  
 // &#35;define FLIP&#92;&#95;NORMAL&#92;&#95;Z  
&#35;endif //&#35;ifdef ALG&#92;&#95;NORMAL&#92;&#95;OPENGL

varying vec3 iFS&#92;&#95;Normal;  
varying vec2 iFS&#92;&#95;UV;  
varying vec3 iFS&#92;&#95;Tangent;  
varying vec3 iFS&#92;&#95;Binormal;  
varying vec3 iFS&#92;&#95;PointWS;

uniform vec3 Lamp0Pos &#61; vec3&#40;0&#46;0f,0&#46;0f,70&#46;0f&#41;;  
uniform vec3 Lamp0Color &#61; vec3&#40;1&#46;0f,1&#46;0f,1&#46;0f&#41;;  
uniform vec3 Lamp1Pos &#61; vec3&#40;70&#46;0f,0&#46;0f,0&#46;0f&#41;;  
uniform vec3 Lamp1Color &#61; vec3&#40;0&#46;198f,0&#46;198f,0&#46;198f&#41;;  
uniform bool flipNormal &#61; true;  
uniform float TilingDetail &#61; 3&#46;0f;  
uniform float SpecExpon &#61; 50&#46;0;  
uniform float Ks &#61; 1&#46;0;  
uniform int parallax&#92;&#95;mode &#61; 0;  
uniform float tessellationFactor &#61; 4&#46;0;  
uniform float heightMapScale &#61; 1&#46;0f;  
uniform float Depth&#92;&#95;detail &#61; 0&#46;5f;  
uniform float Kr &#61; 0&#46;5f;  
uniform int KF&#92;&#95;on &#61; 1;  
uniform float KFs &#61; 1&#46;0f;  
uniform vec3 AmbiColor &#61; vec3&#40;0&#46;07f,0&#46;07f,0&#46;07f&#41;;  
uniform float tiling &#61; 1&#46;0f;  
uniform int enableTilingInFS &#61; 0;

uniform sampler2D heightMap;  
uniform sampler2D normalMap;  
uniform sampler2D detailNormalMap;  
uniform sampler2D emissiveMap;  
uniform sampler2D diffuseMap;  
uniform sampler2D specularMap;  
uniform sampler2D opacityMap;  
uniform samplerCube environmentMap;

uniform mat4 worldMatrix;  
uniform mat4 worldInverseTransposeMatrix;  
uniform mat4 viewInverseMatrix;

vec4 litFct&#40;float NdotL, float NdotH, float specExp&#41;  
&#123;  
 float ambient &#61; 1&#46;0;  
 float diffuse &#61; max&#40;NdotL, 0&#46;0&#41;;  
 float specular &#61; step&#40;0&#46;0, NdotL&#41; &#92;&#42; pow&#40;max&#40;0&#46;0, NdotH&#41;, specExp&#41;;  
 return vec4&#40;ambient, diffuse, specular, 1&#46;0&#41;;  
&#125;

vec3 lerpFct&#40;vec3 v0, vec3 v1, float percent&#41;  
&#123;  
 return v0 &#43; &#40;v1&#45;v0&#41; &#92;&#42; percent;  
&#125;

// Phong Shading  
void phong&#92;&#95;shading&#40;  
in vec3 LightColor,  
in vec3 normalWS,  
in vec3 pointToLightDirWS,  
in vec3 pointToCameraDirWS,  
inout vec3 DiffuseContrib,  
inout vec3 SpecularContrib&#41;  
&#123;  
 vec3 Hn &#61; normalize&#40;pointToCameraDirWS &#43; pointToLightDirWS&#41;;  
 vec4 litV &#61; litFct&#40;dot&#40;normalWS, pointToLightDirWS&#41;, dot&#40;normalWS, Hn&#41;, SpecExpon&#41;;  
 DiffuseContrib &#61; litV&#46;y &#92;&#42; LightColor;  
 SpecularContrib &#61; litV&#46;y &#92;&#42; litV&#46;z &#92;&#42; Ks &#92;&#42; LightColor;  
&#125;

vec3 fixNormalSample&#40;vec3 v&#41;  
&#123;  
 vec3 result &#61; v &#45; vec3&#40;0&#46;5,0&#46;5,0&#46;5&#41;;

&#35;ifdef FLIP&#92;&#95;NORMAL&#92;&#95;X  
 result&#46;x &#61; &#45;result&#46;x;  
&#35;endif // ifdef FLIP&#92;&#95;NORMAL&#92;&#95;X  
&#35;ifdef FLIP&#92;&#95;NORMAL&#92;&#95;Y  
 result&#46;y &#61; &#45;result&#46;y;  
&#35;endif // ifdef FLIP&#92;&#95;NORMAL&#92;&#95;Y  
&#35;ifdef FLIP&#92;&#95;NORMAL&#92;&#95;Z  
 result&#46;z &#61; &#45;result&#46;z;  
&#35;endif // ifdef FLIP&#92;&#95;NORMAL&#92;&#95;Z

return result;  
&#125;

vec3 normalVecOSToWS&#40;vec3 normal&#41;  
&#123;  
 return normal;  
&#125;

void main&#40;&#41;  
&#123;  
 vec3 cameraPosWS &#61; viewInverseMatrix&#91;3&#93;&#46;xyz;  
 vec3 pointToLight0DirWS &#61; normalize&#40;Lamp0Pos &#45; iFS&#92;&#95;PointWS&#41;;  
 vec3 pointToLight1DirWS &#61; normalize&#40;Lamp1Pos &#45; iFS&#92;&#95;PointWS&#41;;  
 vec3 pointToCameraDirWS &#61; normalize&#40;cameraPosWS&#41;;  
 vec3 normalOS &#61; normalize&#40;iFS&#92;&#95;Normal&#41;;  
 vec3 tangentOS &#61; normalize&#40;iFS&#92;&#95;Tangent&#41;;  
 vec3 binormalOS &#61; normalize&#40;iFS&#92;&#95;Binormal&#41;;

// &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;  
 // Make sure the TBN is Orthonormalized  
 binormalOS &#61; normalize&#40;cross&#40;normalOS, tangentOS&#41;&#41;;  
 tangentOS &#61; normalize&#40;cross&#40;binormalOS, normalOS&#41;&#41;;

vec3 cumulatedNormalOS &#61; normalOS;

// &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;  
 // Update UV  
 float a &#61; dot&#40;normalOS,&#45;pointToCameraDirWS&#41;;  
 vec3 s &#61; vec3&#40;dot&#40;pointToCameraDirWS,tangentOS&#41;, dot&#40;pointToCameraDirWS,binormalOS&#41;, a&#41;;  
 vec2 uv &#61; enableTilingInFS &#61;&#61; 0 ? iFS&#92;&#95;UV : &#40;iFS&#92;&#95;UV &#92;&#42; tiling&#41;;  
 float height &#61; texture2D&#40;heightMap,uv&#41;&#46;x &#92;&#42; 2&#46;0 &#45; 1&#46;0 ;  
 float parallax &#61; parallax&#92;&#95;mode &#61;&#61; 0 ? &#40;tessellationFactor / 100000&#46;f &#43; heightMapScale / 500&#46;f&#41; : &#40;heightMapScale / 50&#46;f&#41;;  
 uv &#43;&#61; &#40;height &#92;&#42; s&#46;xy &#92;&#42; parallax&#41; ;

// &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;  
 // Add Normal from normalMap  
 vec3 normalTS &#61; texture2D&#40;normalMap,uv&#41;&#46;xyz;  
 normalTS &#61; fixNormalSample&#40;normalTS&#41;;  
 vec3 normalMapOS &#61; normalTS&#46;x&#92;&#42;tangentOS &#43; normalTS&#46;y&#92;&#42;binormalOS;  
 cumulatedNormalOS &#61; cumulatedNormalOS &#43; normalMapOS;  
 cumulatedNormalOS &#61; normalize&#40;cumulatedNormalOS&#41;;

// &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;  
 // Add detail normalmap  
 vec3 normalDetailTS &#61; texture2D&#40;detailNormalMap,uv&#92;&#42;TilingDetail&#41;&#46;xyz;  
 normalDetailTS &#61; fixNormalSample&#40;normalDetailTS&#41;;  
 vec3 variableNormalDetailTS &#61; lerpFct&#40;vec3&#40;0&#46;0,0&#46;0,0&#46;5&#41;,normalDetailTS,Depth&#92;&#95;detail&#41;;  
 vec3 normalDetailOS &#61; variableNormalDetailTS&#46;x&#92;&#42;tangentOS &#43; variableNormalDetailTS&#46;y&#92;&#42;binormalOS;  
 cumulatedNormalOS &#61; cumulatedNormalOS &#43; normalDetailOS;  
 cumulatedNormalOS &#61; normalize&#40;cumulatedNormalOS&#41;;

if &#40;length&#40;normalTS&#41;&lt;0&#46;0001&#41;  
 cumulatedNormalOS &#61; normalOS;

vec3 cumulatedNormalWS &#61; normalVecOSToWS&#40;cumulatedNormalOS&#41;;

// &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;  
 // Compute Diffuse &amp; Specular

// Light 0 contribution  
 vec3 diffContrib &#61; vec3&#40;0, 0, 0&#41;;  
 vec3 specContrib &#61; vec3&#40;0, 0, 0&#41;;  
 phong&#92;&#95;shading&#40;Lamp0Color, cumulatedNormalWS, pointToLight0DirWS, pointToCameraDirWS, diffContrib, specContrib&#41;;

// Light 1 contribution  
 vec3 diffContrib2 &#61; vec3&#40;0, 0, 0&#41;;  
 vec3 specContrib2 &#61; vec3&#40;0, 0, 0&#41;;   
 phong&#92;&#95;shading&#40;Lamp1Color, cumulatedNormalWS, pointToLight1DirWS, pointToCameraDirWS, diffContrib2, specContrib2&#41;;

diffContrib &#43;&#61; diffContrib2;  
 specContrib &#43;&#61; specContrib2;

vec4 diffuseColor &#61; texture2D&#40;diffuseMap,uv&#41;;

vec3 specularColor &#61; texture2D&#40;specularMap,uv&#41;&#46;rgb;  
 vec3 R &#61; reflect&#40;pointToCameraDirWS,cumulatedNormalWS&#41;;  
 vec3 reflColor &#61; Kr &#92;&#42; textureCube&#40;environmentMap,R&#46;xyz&#41;&#46;bgr;

float FallofRefl;

if &#40;KFs &gt;&#61; 0&#46;0&#41;  
 FallofRefl &#61; max&#40;&#40;1&#45;dot&#40;pointToCameraDirWS/&#40;KFs&#41;,cumulatedNormalWS&#41;&#41;,0&#41;&#92;&#42;KF&#92;&#95;on;  
 else  
 FallofRefl &#61; &#40;1&#45;max&#40;&#40;&#40;1&#45;dot&#40;pointToCameraDirWS/&#40;&#45;KFs&#41;,cumulatedNormalWS&#41;&#41;&#41;,0&#41;&#41;&#92;&#42;KF&#92;&#95;on;

if &#40;KF&#92;&#95;on &#61;&#61; 0&#41;  
 FallofRefl&#61;1&#46;0;

vec3 Ambiant&#92;&#95;final &#61; diffuseColor&#46;rgb&#92;&#42;AmbiColor;

// &#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;&#45;  
 vec3 emissive &#61; texture2D&#40;emissiveMap,uv&#41;&#46;xyz;

vec3 finalcolor &#61; Ambiant&#92;&#95;final  
 &#43; specularColor&#92;&#42;specContrib  
 &#43; diffuseColor&#46;rgb&#92;&#42;diffContrib  
 &#43; &#40;reflColor&#92;&#42;specularColor&#92;&#42;FallofRefl&#41;  
 &#43; emissive;

// Final Color  
 vec4 finalColor4 &#61; vec4&#40;finalcolor, texture2D&#40;opacityMap,uv&#41;&#41;;

gl&#92;&#95;FragColor &#61; finalColor4;  
&#125;

### GLSLFX File

The glslfx file defines two techniques to render the geometry:

* One uses the hardware tessellation technique
* The other based on a parallax effect that will be used as a fall-back if the user hardware don't support the Tessellation.

Located in .\tessellation\_parallax\fs.glsl

Content:

```

<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE sbsbatchnode SYSTEM "glslfx.dtd">

<glslfx version="1.0.0" author="allegorithmic.com">



    <!-- TECHNIQUES -->

    <technique name="Tesselation">

        <!-- PROPERTIES -->

        <property name="blend_enabled" value="true"/>

        <property name="blend_func" value="src_alpha,one_minus_src_alpha"/>

        <property name="cull_face_enabled" value="true"/>

        <property name="cull_face_mode" value="back"/>



        <!-- SHADERS -->

        <shader type="vertex" filename="tessellation_parallax/tessellation/vs.glsl" primitiveType="patch4"/>

        <shader type="tess_control" filename="tessellation_parallax/tessellation/tcs.glsl"/>

        <shader type="tess_eval" filename="tessellation_parallax/tessellation/tes.glsl"/>

        <shader type="fragment" filename="tessellation_parallax/fs.glsl"/>



        <!-- UNIFORMS -->

        <uniform name="parallax_mode" guiName="Parallax Mode" min="0" max="0" />

        <uniform name="enableTilingInFS" guiName="Tiling Enabled In FS" min="0" max="0" />

        <uniform name="tessellationFactor" guiName="Tessellation Factor" default="4" min="1" max="64" guiStep="1" guiWidget="slider"/>

    </technique>



    <technique name="Parallax">

        <!-- PROPERTIES -->

        <property name="blend_enabled" value="true"/>

        <property name="blend_func" value="src_alpha,one_minus_src_alpha"/>

        <property name="cull_face_enabled" value="true"/>

        <property name="cull_face_mode" value="back"/>



        <!-- SHADERS -->

        <shader type="vertex" filename="tessellation_parallax/parallax/vs.glsl"/>

        <shader type="fragment" filename="tessellation_parallax/fs.glsl"/>



        <!-- UNIFORMS -->

        <uniform name="parallax_mode" guiName="Parallax Mode" min="1" max="1" />

        <uniform name="enableTilingInFS" guiName="Tiling Enabled In FS" min="1" max="1" />



    </technique>



    <!-- INPUT VERTEX FORMAT -->

    <vertexformat name="iVS_Position" semantic="position"/>

    <vertexformat name="iVS_Normal" semantic="normal"/>

    <vertexformat name="iVS_UV" semantic="texcoord0"/>

    <vertexformat name="iVS_Tangent" semantic="tangent0"/>

    <vertexformat name="iVS_Binormal" semantic="binormal0"/>



    <!-- SAMPLERS -->

    <sampler name="diffuseMap" usage="diffuse"/>

    <sampler name="heightMap" usage="height"/>

    <sampler name="normalMap" usage="normal"/>

    <sampler name="detailNormalMap" usage="detailNormal"/>

    <sampler name="emissiveMap" usage="emissive"/>

    <sampler name="specularMap" usage="specular"/>

    <sampler name="opacityMap" usage="opacity"/>

    <sampler name="environmentMap" usage="environment"/>



    <!-- MATRICES -->

    <uniform name="worldMatrix" semantic="world"/>

    <uniform name="worldViewProjMatrix" semantic="worldviewprojection"/>

    <uniform name="worldViewMatrix" semantic="worldview"/>

    <uniform name="worldInverseTransposeMatrix" semantic="worldinversetranspose"/>

    <uniform name="viewInverseMatrix" semantic="viewinverse"/>

    <uniform name="modelViewMatrix" semantic="modelview"/>

    <uniform name="projectionMatrix" semantic="projection"/>



    <!-- SCENE PARAMETERS -->

    <uniform name="AmbiColor" semantic="ambient"/>

    <uniform name="Lamp0Pos" semantic="lightposition0"/>

    <uniform name="Lamp0Color" semantic="lightcolor0"/>

    <uniform name="Lamp1Pos" semantic="lightposition1"/>

    <uniform name="Lamp1Color" semantic="lightcolor1"/>



    <!-- UNIFORMS -->

    <uniform name="tiling" guiName="Tiling" default="1" min="1" guiWidget="slider" guiMax="10"/>

    <uniform name="heightMapScale" guiGroup="Height" guiName="Scale" default="1" min="0" guiWidget="slider" guiMin="-50" guiMax="50" />

    <uniform name="TilingDetail" guiGroup="Detail Normal" guiName="Tiling" default="3" min="1" guiWidget="slider" guiMax="10"/>

    <uniform name="Depth_detail" guiGroup="Detail Normal" guiName="Intensity" default="0.5" min="0" max="1" guiStep="0.05" guiWidget="slider"/>

    <uniform name="SpecExpon" guiGroup="Specular" guiName="Power" default="50" min="1" guiWidget="slider" guiMax="128"/>

    <uniform name="Ks" guiGroup="Specular" guiName="Intensity" default="1" min="0" guiWidget="slider" guiMax="3"/>

    <uniform name="Kr" guiGroup="Reflection" guiName="Intensity" default="0.5" min="0" max="1" guiStep="0.01" guiWidget="slider"/>

    <uniform name="KF_on" guiGroup="Reflection" guiName="Falloff" default="1" min="0" max="1" guiStep="1" guiWidget="slider"/>

    <uniform name="KFs" guiGroup="Reflection" guiName="Falloff Size" default="1" min="-1" max="1" guiStep="0.05" guiWidget="slider"/>



</glslfx>
```
