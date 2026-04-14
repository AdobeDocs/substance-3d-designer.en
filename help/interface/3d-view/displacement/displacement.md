---
helpx_url: ""
breadcrumb-title: ""
description: Use the Displacement pop-up to quickly adjust the displacement and tessellation applied to meshes in a 3D scene.
helpx_creative_field: ""
helpx_description: ""
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: 3D View - Displacement pop-up
user-guide-description: ""
user-guide-title: ""
---

# Displacement pop-up

<table style="border: none; margin-top: 32px; margin-bottom: 32px">
    <tr style="vertical-align: top;">
        <td>
            <p>The Displacement pop-up available in the 3D View toolbar offers direct controls to the displacement and tessellation of meshes.</p>
            <p>There are three parameters:<ul>
                <li>Height scale</li>
                <li>Height level</li>
                <li>Tessellation</li></ul>
        </td>
        <td style="width: 60%; margin-left: 32px">
            <img src="./displacement.resources/3d-view-displacement-popup-mograph.gif" alt="Displacement pop-up in the 3D View" />
        </td>
    </tr>
</table>

## Height scale 

The maximum distance of displacement for the mesh vertices along their normal, in scene units.<br>
This is the distance travelled for a value of 1.0 in the height map.

When a Substance graph is connected to a material and that graph includes an [Output node](../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/output/output.md) with
the <code>heightScale</code> usage, then the Height scale parameter in the pop-up is *disabled* for that material
since it is being currently driven by the graph.

>[!TIP]
> 
>Use the [Height to normal world units](../../../compositing-graphs/nodes-reference-for-com/node-library/filters/normal-map/height-normal-world-units/height-to-normal-world-units.md) node and have its 'Height depth' parameter match the 'Height scale' value 
>to ensure correct shading when using displacement.

## Height level

The grayscale value in the height map that is used as the *midpoint* for the displacement height.
I.e. the threshold value used as 0.0 elevation.

Values below that threshold result in vertices being displaced backward, while values above the threshold result in 
vertices being displaced forward.

## Tessellation

Tessellation involves subdividing individual mesh faces by adding a vertex on their segments then connecting
all vertices to a new vertex at their center, so that 1 face becomes **6**.

The parameter defines the amount of times faces should be subdivided recursively.

The *scope* of the tessellation parameter varies according to the *renderer* being currently used: it can be applied
per mesh or per material.

### Per mesh

When using the [Rasterizer](../3d-renderers/3d-renderers.md#rasterizer) or [GPU Pathtracer](../3d-renderers/3d-renderers.md#gpu-pathtracer) renderer, each Mesh object in the scene has a *separate*
subdivision value.

Subdivision is contextual: it is optimized in such a way that only surface with a *non-uniform height value* or 
a *non-flat height map* will be subdivided, regardless of the parameter value.

[EXAMPLE: Rasterizer subdivision]

### Per material

When using the [OpenGL](../3d-renderers/3d-renderers.md#opengl) renderer, each material in the scene has a *separate* subdivision value, which 
is applied to *all faces using that material*.

Subdivision is not contextual: the surfaces are subdivided the specified amount of times regardless of their current
height value or texture. 

## Visualizing tessellation

You can visualize the result of tessellation by checking the **wireframe** of the mesh.<br>
The steps to displaying the wireframe for each renderer are described below:

### Rasterizer/GPU Pathtracer

Use the <img src="../3d-view.resources/3d-view-scene-toolbar-render-settings.png" width=16 /> **Renderer settings**
button, then in the Properties dock go to **Render settings > Diagnostic mode** and select the **Wireframe
(world space)** option.

[EXAMPLE: Rasterizer wireframe]

### OpenGL

Use the <img src="../3d-view.resources/3d-view-scene-toolbar-wireframe.png" width=16 /> **Wireframe**
button.

[EXAMPLE: OpenGL wireframe]
