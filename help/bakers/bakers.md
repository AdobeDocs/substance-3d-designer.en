---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/bakers.html"
breadcrumb-title: ""
description: Learn how to use Substance 3D Designer bakers to compute mesh-based information into texture files.
helpx_creative_field: ""
helpx_description: Designer > Bakers
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Bakers
user-guide-description: ""
user-guide-title: ""
---

# Bakers

Baking refer to the action of **transferring mesh based information into textures**. These information are then read by shaders and/or Substance filters to generate more advanced effects or textures.

>[!NOTE]
>
> To learn more about baking take a look at the [Baking Documentation](https://helpx.adobe.com/substance-3d-bake/home.html).

<table>
<tr style="border: 0;">
<td width="100.00%" style="border: 0;" valign="top">

The baking window can be accessed via the mesh file in the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) window. Right-Click on the mesh name and choose "**Bake Model Information**" to open the baking window.

</td>
<td width="33.33%" style="border: 0;" valign="top">

!['Bake mode information' option in 3D scene resource's contextual menu](../assets/sd-mesh-right-click.png "'Bake mode information' option in 3D scene resource's contextual menu")

</td>
</tr>
</table>

![Baking window](../assets/sd-window-overview.png "Baking window")

## Overview

The baking window of is divided into several panels which are described below.

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Elements to bake

This panel controls which part of the low-poly mesh will be used to perform the baking.

It lists the geometry found inside the low-poly mesh file. By default the list is based on the individual materials found in the file, but it can be switched to sub-meshes instead when relevant. You can uncheck elements that should be ignored during the baking process.

</td>
<td style="border: 0;" valign="top">

![](../assets/sd-mesh-selection.png)

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

### Output

This panel controls where the baked texture will be located.

</td>
<td style="border: 0;" valign="top">

![](../assets/sd-output.png)

</td>
</tr>
</table>

| *Parameter* | *Description* |
| --- | --- |
| **Method** | Controls how the baked textures will be stored with the Substance package.Possible values:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>Embedded</strong> : the baked texture are stored in a sub-folder next to the Substance package with specific naming.</li><li data-preserve-html="true"><strong>Linked</strong> (default) : the baked texture are stored in the folder defined and then referenced into the Substance packaged.</li></ul> |
| **Folder** | Location of the baked textures when saved. Click on three dots button to open a file dialog and choose the export folder.A check-mark will be visible on the right to indicate if the folder actually exist or not. |
| **Name** | Naming convention of the baked textures. Click on three dots button to open a dropdown and insert other placeholders (bakename, custom, material, mesh). |
| **Sample** | Simulate a filename to test the naming convention. |
| **Place Resource Into a Mesh Specific Folder** | If enabled, the baked textures will be saved inside a folder named as the mesh file. |

### High-definition meshes

This panel controls the high-poly mesh list and the related settings. See the [common parameters](https://helpx.adobe.com/substance-3d-bake/bakers-settings/common-parameters.html) for more information.

![High definition meshes](../assets/sd-high.png "High definition meshes")

### Default values

See the [common parameters](https://helpx.adobe.com/substance-3d-bake/bakers-settings/common-parameters.html) for more information.

![Default values](../assets/sd-default-values.png "Default values")

### Bakers render list and settings

The <b>Bakers render list</b> is where you can choose which baked texture you want to generate. By default the list is empty.

* <b>Adding a new baker:</b> Click on button "Add Baker".
* <b>Removing a baker:</b> Select the baker in the list, then click on the button "Delete baker".
* <b>Moving a baker to the top:</b> Select the baker in the list, then click on the button "Pull to top".
* <b>Moving down a baker:</b>Select the baker in the list, then click on the button "Push down".

Each baker in the inherit by default the Default Values (see above). The size (resolution) for example can be overridden by clicking on the cell on the line of the baker. This is true for the other settings on the line.

When clicking on a baker in the list, the Baker Parameters view will update with its specific parameters.

To learn more about the specific parameters, see: [Bakers Settings](https://helpx.adobe.com/substance-3d-bake/bakers-settings.html).

![Bakers render list](../assets/sd-baker-list.png "Bakers render list")
