---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/substance-compositing-graphs/nodes-reference-for-substance-compositing-graphs/node-library/mesh-based-generators/mask-generators/dripping-rust.html"
breadcrumb-title: ""
description: Use the Dripping Rust node to generate rust drip patterns based on mesh geometry and gravity direction.
helpx_creative_field: ""
helpx_description: Designer > Substance compositing graphs > Nodes reference for Substance compositing graphs > Node library > Mesh Based Generators > Mask Generators > Dripping Rust
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Dripping Rust
user-guide-description: ""
user-guide-title: ""
---



# Dripping Rust

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

![](dripping-rust.png){width="128px"}

## Dripping Rust

**In:** *Mesh Based Generators**/Mask Generators*

**Intermediate**

</td>
<td style="border: 0;" valign="top">

## Description

Generates a black and white mask based on baked maps and user settings. Similar to [Smart Masks](https://support.allegorithmic.com/documentation/display/SPDOC/Smart+Materials+and+Masks) in [Painter](https://support.allegorithmic.com/documentation/display/SPDOC/Substance+Painter).

This mask represents rust flakes and specks, with leaks running down.

## Parameters

### Inputs

* **Curvature**: *Grayscale Input*   
  Baked or generated map to help with rust placement.
* **Ambient Occlusion**: *Grayscale Input*   
  Baked or generated map to help with rust placement.
* **Position**: *Grayscale Input*   
  Baked or generated map for drip directions.
* **Mask (optional)**: *Grayscale Input*   
  Mask slot used for masking the node's effects.

### Parameters

* **Rust Spreading**: *0.0 - 1.0*Main control for the amount of rust.
* **Rust Contrast**: *0.0 - 1.0*Sets the amount of contrast in generated rust specks (does not affect drips).
* **Spreading Smoothness**: *0.0 - 1.0*Amount of blurring/smearing effect to apply to the rust specks.
* **Drips Intensity**: *0.0 - 1.0*Sets strength and length of drips from flecks.
* **Drips Smoothness**: *0.0 - 1.0*Amount of blurring and smoothing to apply to drips.
* **Drips Samples Amount**: *0 - 32*Sets quality level (steps) for the drips effect. Has a slight effect on speed.

## Example Images

![](dripping-rust-ex3.gif)

</td>
</tr>
</table>
