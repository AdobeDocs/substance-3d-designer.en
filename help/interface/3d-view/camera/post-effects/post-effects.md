---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/3d-view/camera/post-effects.html"
breadcrumb-title: ""
description: Apply post-processing effects to the 3D view camera for enhanced material preview and visualization.
helpx_creative_field: ""
helpx_description: Designer > Interface > 3D view > Camera > Post effects
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Post effects
user-guide-description: ""
user-guide-title: ""
---


# Post effects

![Post effects](postEffects.png "Post effects"){zoomable="yes"}

In the camera properties, you can enable post effects to enhance renders or check specific material properties.

These effects are developed in-house and are only available for the Rasterizer and GPU Pathtracer [renderers](../../../../interface/3d-view/3d-renderers/3d-renderers.md).

Any post effect enabled at the time of saving [3D scene resources](../../../../resources/3d-scene-resource/3d-scene-resource.md) or [scene state files](../../../../working-with-3d-scenes/working-with-3d-scenes.md) will be saved as part of the scene state.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

## Tone mapping

</td>
<td style="border: 0;" valign="top">

### Bloom

</td>
<td style="border: 0;" valign="top">

### Depth of field

</td>
<td style="border: 0;" valign="top">



</td>
</tr>
</table>

## Tone mapping

Remaps the colors of the render according to specific algorithms and/or look-up tables (LUT).

This lets you improve color consistency between applications. For instance, the AgX tone mapper is also available in Blender.

+++Reinhard


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXReinhard.jpg" alt="PostFXReinhard">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXReinhard](PostFXReinhard.jpg "PostFXReinhard")

+++

+++Atan


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXAtan.jpg" alt="PostFXAtan">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXAtan](PostFXAtan.jpg "PostFXAtan")

+++

+++Exp


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXExp.jpg" alt="PostFXExp">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXExp](PostFXExp.jpg "PostFXExp")

+++

+++Log


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXLog.jpg" alt="PostFXLog">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXLog](PostFXLog.jpg "PostFXLog")

+++

+++Aces


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXAces.jpg" alt="PostFXAces">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXAces](PostFXAces.jpg "PostFXAces")

+++

+++Hejl


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXHejl.jpg" alt="PostFXHejl">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXHejl](PostFXHejl.jpg "PostFXHejl")

+++

+++Neutral


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXNeutral.jpg" alt="PostFXNeutral">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXNeutral](PostFXNeutral.jpg "PostFXNeutral")

+++

+++Agx


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXAgx.jpg" alt="PostFXAgx">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXAgx](PostFXAgx.jpg "PostFXAgx")

+++

+++Pbr neutral


<table>
  <tr>
    <td>
      <img src="PostFXDisabled.jpg" alt="PostFXDisabled">
      <br><i>Before</i>
    </td>
    <td>
      <img src="PostFXPbrNeutral.jpg" alt="PostFXPbrNeutral">
      <br><i>After</i>
    </td>
  </tr>
</table>



![PostFXDisabled](PostFXDisabled.jpg "PostFXDisabled")

![PostFXPbrNeutral](PostFXPbrNeutral.jpg "PostFXPbrNeutral")

+++

## Bloom

Simulates the in-camera effect of fringes of lights bleeding outward from very bright areas onto areas receiving less light.

The effect is influenced by the scene's lighting, camera exposure and emissive materials.

+++Threshold
The luminance value above which bloom should be visible.

*Left: 1.0 / Right: 4.0*



<table>
  <tr>
    <td>
      <img src="bloomThreshold1.jpg" alt="bloomThreshold1">
      <br><i>Before</i>
    </td>
    <td>
      <img src="bloomThreshold4.jpg" alt="bloomThreshold4">
      <br><i>After</i>
    </td>
  </tr>
</table>



![bloomThreshold1](bloomThreshold1.jpg "bloomThreshold1")

![bloomThreshold4](bloomThreshold4.jpg "bloomThreshold4")

+++

+++Falloff
The bloom attenuation ramp, where a lower value results in a shorter bloom radius.

*Left: 1.0 / Right: 0.6*



<table>
  <tr>
    <td>
      <img src="bloomFalloff1.jpg" alt="bloomFalloff1">
      <br><i>Before</i>
    </td>
    <td>
      <img src="bloomFalloff0-6.jpg" alt="bloomFalloff0-6">
      <br><i>After</i>
    </td>
  </tr>
</table>



![bloomFalloff1](bloomFalloff1.jpg "bloomFalloff1")

![bloomFalloff0-6](bloomFalloff0-6.jpg "bloomFalloff0-6")

+++

+++Level
The intensity of the bloom. A higher value results in brighter, more pronounced light fringes.

*Left: 8.0 / Right: 2.0*



<table>
  <tr>
    <td>
      <img src="bloomLevel8.jpg" alt="bloomLevel8">
      <br><i>Before</i>
    </td>
    <td>
      <img src="bloomLevel2.jpg" alt="bloomLevel2">
      <br><i>After</i>
    </td>
  </tr>
</table>



![bloomLevel8](bloomLevel8.jpg "bloomLevel8")

![bloomLevel2](bloomLevel2.jpg "bloomLevel2")

+++

+++Color shift
Offsets the hue of the areas affected by the bloom towards warmer colors.

*Left: 0.0 / Right: 0.8*



<table>
  <tr>
    <td>
      <img src="bloomColorShift0.jpg" alt="bloomColorShift0">
      <br><i>Before</i>
    </td>
    <td>
      <img src="bloomColorShift0-8.jpg" alt="bloomColorShift0-8">
      <br><i>After</i>
    </td>
  </tr>
</table>



![bloomColorShift0](bloomColorShift0.jpg "bloomColorShift0")

![bloomColorShift0-8](bloomColorShift0-8.jpg "bloomColorShift0-8")

+++

## Depth of field

Simulates the optical phenomenon caused by camera lenses where objects nearer and farther than the focus distance are blurred.

The effect is impacted by both the camera’s ‘F-Stop’ and ‘Focus distance’ parameters.

>[!TIP]
>
> To quickly adjust the camera focus, place the cursor on the location of a scene you want in focus and press Ctrl+LMB (Windows) or Cmd+LMB (macOS) to automatically set the focus distance to that location.

+++Max radius
The maximum radius of the blurring effect.

*Left: 32.0 / Right: 4.0*



<table>
  <tr>
    <td>
      <img src="depthOfFieldMaxRadius32.jpg" alt="depthOfFieldMaxRadius32">
      <br><i>Before</i>
    </td>
    <td>
      <img src="depthOfFieldMaxRadius4.jpg" alt="depthOfFieldMaxRadius4">
      <br><i>After</i>
    </td>
  </tr>
</table>



![depthOfFieldMaxRadius32](depthOfFieldMaxRadius32.jpg "depthOfFieldMaxRadius32")

![depthOfFieldMaxRadius4](depthOfFieldMaxRadius4.jpg "depthOfFieldMaxRadius4")

+++

+++Composite strength
The magnitude of the blurring effect from the focus distance outward.

*Left: 0.2 / Right: 0.05*



<table>
  <tr>
    <td>
      <img src="depthOfFieldCompositeStrength0-2.jpg" alt="depthOfFieldCompositeStrength0-2">
      <br><i>Before</i>
    </td>
    <td>
      <img src="depthOfFieldCompositeStrength0-05.jpg" alt="depthOfFieldCompositeStrength0-05">
      <br><i>After</i>
    </td>
  </tr>
</table>



![depthOfFieldCompositeStrength0-2](depthOfFieldCompositeStrength0-2.jpg "depthOfFieldCompositeStrength0-2")

![depthOfFieldCompositeStrength0-05](depthOfFieldCompositeStrength0-05.jpg "depthOfFieldCompositeStrength0-05")

+++

+++Longitudinal aberration
The intensity of the aberration occurring away from the focus distance.

Aberration simulates how different wavelengths of light have a slightly different focal lengths, resulting in colors appearing to be offset and having sublte differences in focus.

*Left: 0.0 / RIght: 1.0*



<table>
  <tr>
    <td>
      <img src="depthOfFieldLongitudinalAberration0.jpg" alt="depthOfFieldLongitudinalAberration0">
      <br><i>Before</i>
    </td>
    <td>
      <img src="depthOfFieldLongitudinalAberration1.jpg" alt="depthOfFieldLongitudinalAberration1">
      <br><i>After</i>
    </td>
  </tr>
</table>



![depthOfFieldLongitudinalAberration0](depthOfFieldLongitudinalAberration0.jpg "depthOfFieldLongitudinalAberration0")

![depthOfFieldLongitudinalAberration1](depthOfFieldLongitudinalAberration1.jpg "depthOfFieldLongitudinalAberration1")

+++

+++Achromatic aberration
Specifies whether the aberration should be achromatic, meaning that some or all colors have the same focal length.

This makes the blurring effect appear to be more equally distributed.

*Left: True / Right: False*



<table>
  <tr>
    <td>
      <img src="depthOfFieldAchromaticAberrationYes.jpg" alt="depthOfFieldAchromaticAberrationYes">
      <br><i>Before</i>
    </td>
    <td>
      <img src="depthOfFieldAchromaticAberrationNo.jpg" alt="depthOfFieldAchromaticAberrationNo">
      <br><i>After</i>
    </td>
  </tr>
</table>



![depthOfFieldAchromaticAberrationYes](depthOfFieldAchromaticAberrationYes.jpg "depthOfFieldAchromaticAberrationYes")

![depthOfFieldAchromaticAberrationNo](depthOfFieldAchromaticAberrationNo.jpg "depthOfFieldAchromaticAberrationNo")

+++

+++Cat's eye
Enables the cat’s eye effect in the scene, which simulates how light entering at an oblique angle does not enter a disc, but a uneven oval, causing distortion.

This effect is more pronounced at higher apertures – I.e., lower F-Stop values.

*Left: True / Right: False*



<table>
  <tr>
    <td>
      <img src="depthOfFieldAchromaticCatsEyeYes.jpg" alt="depthOfFieldAchromaticCatsEyeYes">
      <br><i>Before</i>
    </td>
    <td>
      <img src="depthOfFieldAchromaticCatsEyeNo.jpg" alt="depthOfFieldAchromaticCatsEyeNo">
      <br><i>After</i>
    </td>
  </tr>
</table>



![depthOfFieldAchromaticCatsEyeYes](depthOfFieldAchromaticCatsEyeYes.jpg "depthOfFieldAchromaticCatsEyeYes")

![depthOfFieldAchromaticCatsEyeNo](depthOfFieldAchromaticCatsEyeNo.jpg "depthOfFieldAchromaticCatsEyeNo")

+++
