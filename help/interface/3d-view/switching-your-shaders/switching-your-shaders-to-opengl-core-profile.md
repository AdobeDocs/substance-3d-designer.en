---
title: "Switching your shaders to OpenGL Core Profile"
description: "Learn how to switch shaders to OpenGL Core Profile in Substance 3D Designer 3D view for compatibility and performance."
helpx_description: Designer > Interface > 3D View > Switching your shaders to OpenGL Core Profile
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/3d-view/switching-your-shaders-to-opengl-core-profile.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - shading
  - color
  - texture
---




# Switching your shaders to OpenGL Core Profile

Since version 2018.2.0, the 3D viewport uses OpenGL Core Profile.  
On this occasion, we updated some shaders we provide with the application from GLSL version 120 to GLSL version 330.

You may want to update your own shaders either to take advantage of the new GLSL functions available, or to make your GLSL code more modern. Please note that on MacOS, old shaders may not work anymore.  
For a complete overview of the new features, we highly recommend that you perused the official OpenGL documentation. You can for example take a look at the [OpenGL Shading Language Specification 3.30](https://www.khronos.org/registry/OpenGL/specs/gl/GLSLangSpec.3.30.pdf).  
Otherwise, here is a quick guide that will help you to convert your GLSL 1.20 shaders in GLSL 3.30:

## Update the version number

First of all, replace (or add it at the top of your file if you don't have it yet) your previous `#version` directive by `#version 330`.

### Replace your "attribute" and "varying" by "in" or "out"

Now, `attribute` and `varying` variables are explicitly declared as `in` or `out` depending on the shader stage:

In the vertex shader, `attribute`s of the vertices are declared as `in`, while `varying`s to be passed to the fragment shader are declared as `out`.  
For example:

```

## version 120



attribute vec3 vertexPosition;

attribute vec3 vertexNormal;

attribute vec2 vertexUV;



varying vec3 fragmentNormal;

varying vec2 fragmentUV;
```


becomes:

```

## version 330



in vec3 vertexPosition;

in vec3 vertexNormal;

in vec2 vertexUV;



out vec3 fragmentNormal;

out vec2 fragmentUV;
```


Likewise in the fragment shader, varying becomes in. You should also declare an out variable that will replace gl\_FracColor (which is not build-in anymore):

```

## version 120



varying vec3 fragmentNormal;

varying vec2 fragmentUV;



void main() {

...

gl_FragColor = vec4(myColor.rgb, 1.0);

}
```


becomes:

```

## version 330



in vec3 fragmentNormal;

in vec2 fragmentUV;



out vec4 outColor; //you could choose any name you want here



void main() {

...

outColor = vec4(myColor.rgb, 1.0);

}
```


### Use new texture lookup functions

With the new version of the shading language, the texture lookup API have been both simplified and augmented.

The `texture1D()`, `texture2D()`, `texture3D()`, and `textureCube()` functions all become overloads of `texture()`.  
Likewise `texture2DLod()` becomes `textureLod()`, `texture2DGrad()` becomes `textureGrad()` and so on.

You also have now access to useful functions such as `textureSize()` (to query the size of the sampler in texel), `textureOffset()` (to sample neighbours of the target location), `textureFetch()` (to provide a sample location in pixel), and more stuff.
