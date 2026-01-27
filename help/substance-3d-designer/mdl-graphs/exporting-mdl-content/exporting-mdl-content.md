---
title: "Exporting MDL content | Substance 3D Designer"
description: "Designer > MDL graphs > Exporting MDL content"
---

# Exporting MDL content

This page describes the export processes related to [MDL graphs](../mdl-graphs.md) and materials in Substance 3D Designer.

## Overview

Once an MDL material is authored in Designer, it needs to be exported into a format which can *carry the material's definition* and be read by renderers which support MDL. MDL uses proprietary formats to carry material definitions, called MDL modules, written and packaged in different formats which can all be exported from within Designer.

>[!NOTE]
>
> All of these formats can be opened directly with a *text editor* – sometimes after unpacking them with an archive manager – to inspect the material definition they hold.

## MDL module (\*.mdl)

This is the fundamental exchange file format for material definitions. An MDL module defines the following:

* the material's characteristics and behaviour
* its exposed parameters and default values
* its annotations (i.e., metadata): author, tags, categories, ...

Exporting an MDL module is performed at the *package* level. To export an MDL module for a given package, click the ![](mdl-export-module-icon.png) <b>Export MDL Module</b> button in the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) or select that same option in the *package's contextual menu*. Select a target location and name for the exported MDL module, and the <b>Export Report</b> dialog is displayed with the list of messages logged during the export process.

The exported module will contain the definitions of *all* the MDL materials defined by an [MDL graph](../mdl-graphs.md) in the package.

>[!NOTE]
>
> Learn more about MDL modules in sections 4 and 15 of NVIDIA's [MDL Specification](https://developer.download.nvidia.com/designworks/mdl-sdk/secure/MDL_spec_1.6.1_16Dec2019.pdf?xBg5Km0pdI4vC4iQw4ADtIaJOe6U90WHUfJYs-WxGykGo3fdCqKP2Iw4AktgKPyx-z4mPfCRoQgU3GbbSXrZei8JCPLkYrLWfSUfaecroUdXSLv-UOWq41t20eWP7hRuMoc7oj5bJWEs_EXVmLkCd4uiqlZ_UQ&amp;t=eyJscyI6ImdzZW8iLCJsc2QiOiJodHRwczpcL1wvd3d3Lmdvb2dsZS5jb21cLyJ9).

>[!NOTE]
>
> Warnings following this template: `x appears to be invalid whereas it was expected to be an mdl::call` are caused by the way MDL materials are processed in MDL graphs, and are *safe to ignore*.

![MDL export pathway](mdl-export-module.png "MDL export pathway")

*The "Export MDL Module" pathways in the Explorer, and the resulting Export Report dialog*

### MDL preset (\*.mdl)

An MDL module preset is largely identical to the module it is based on, with the only difference being it carries a different set of default values – learn more [here](https://www.migenius.com/doc/realityserver/latest/resources/general/iray/api_reference/iray/html/classmi_1_1neuraylib_1_1IMdl__factory.html#details).

A preset for an MDL material assigned to a scene material `my_material` may be exported from the following locations:

* The [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) panel, by clicking <b>RMB</b> on the MDL graph resource and selecting the <b>Export Preset...</b> option in the contextual menu
* The [3D View](../../interface/3d-view/3d-view.md) panel, using the <b>Materials &gt; my\_material &gt; Export preset...</b> menu option

The menu option opens the <b>Export MDL Material Preset</b> dialog, which offers the following options:

* <b>Directory</b>: The target location the MDL module is exported to
* <b>MDL File Name</b>: The name of the MDL module
* <b>Embed Imported MDL Modules</b>: If the MDL module relies on imported modules – i.e., has any module dependencies, checking this option results in the module dependencies to be *embedded* into the exported MDL module, making it effectively *self-sufficient* at the cost of file size and dynamic inheritance

The exported preset will use the material's parameters' *current values* in the 3D View as the *new default* values. These values may be modified using the <b>Materials &gt; my\_material &gt; Edit</b> option, which will display the material's exposed parameters in the [Properties](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/parameters-ui-129368153.html) panel.

>[!WARNING]
>
> While exporting an MDL module from the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) panel results in an MDL module holding *all* MDL materials defined by an MDL graph in the package, exporting an MDL preset from the [3D View](../../interface/3d-view/3d-view.md) results in an MDL module holding *only* the definition of the MDL materials applied to the *selected material* in the menu – `my_material` in this example.

![MDL preset export pathway](mdl-export-preset.png "MDL preset export pathway")

*The "Export preset" pathway in the 3D View, and the resulting Export MDL Material Preset dialog*

## MDL module archive (\*.mdr)

An MDL module archive combines MDL modules – see above – with resources such as *textures* and readme files into a *single transportable file*.

Exporting an MDL module archive is performed at the *package* level. To export an MDL module archive for a given package, click the ![](mdl-export-module-icon.png) <b>Export MDL Module Archive</b> button in the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) or select that same option in the *package's contextual menu*. Select a target location and name for the exported MDL module archive, and the <b>Export Report</b> dialog is displayed with the list of messages logged during the export process.

The exported module archive will contain MDL module holding the definitions of *all* the MDL materials defined by an [MDL graph](../mdl-graphs.md) in the package. If a [Substance graph](../../compositing-graphs/substance-compositing-graphs.md) is [instanced into an MDL graph](../compositing-graphs-and/substance-compositing-graphs-and-mdl-materials.md) and connected to a stream going to the [Root](../main-mdl-graph-concepts/main-mdl-graph-concepts.md) node, the textures it outputs are *saved into the archive*.

In addition to these items, the archive includes a <b>MANIFEST</b> file which describes the following metadata for the MDL module archive:

* `mdl`: the version of MDL used to export the module archive – e.g., "1.5"
* `version`: the version of the module archive – e.g., "1.0.0"
* `module`: the name of the module archive – e.g., "::pbr\_metallic\_roughness\_basic"
* `exports.material`: the name of the materials defined in the module archive – e.g., "::pbr\_metallic\_roughness\_basic::MDL\_graph"

>[!NOTE]
>
> Learn more about the MDL archive file format in Appendix C of NVIDIA's [MDL Specification](https://developer.download.nvidia.com/designworks/mdl-sdk/secure/MDL_spec_1.6.1_16Dec2019.pdf?xBg5Km0pdI4vC4iQw4ADtIaJOe6U90WHUfJYs-WxGykGo3fdCqKP2Iw4AktgKPyx-z4mPfCRoQgU3GbbSXrZei8JCPLkYrLWfSUfaecroUdXSLv-UOWq41t20eWP7hRuMoc7oj5bJWEs_EXVmLkCd4uiqlZ_UQ&amp;t=eyJscyI6ImdzZW8iLCJsc2QiOiJodHRwczpcL1wvd3d3Lmdvb2dsZS5jb21cLyJ9).

![MDR export pathway](mdl-export-archive.png "MDR export pathway")

*The "Export MDL Module Archive" pathways in the Explorer, and the resulting Export Report dialog*

## MDL encapsulated module (\*.mdle)

MDL graphs with exposed parameters can be exported as encapsulated MDL materials. Encapsulation *wraps data* into a dedicated class so that data *cannot be accessed directly*.

For instance, while you are still able to modify the values of exposed parameters to control a material's behaviour, the *definition* of these parameters is *not available* in an encapsulated MDL module.

Exporting an encapsulated MDL module is performed in the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) at the MDL graph level, by selecting the <b>Export as .mdle</b> option in an MDL graph's contextual menu. Select a target location and name for the exported MDL encapsulated module, and the <b>Export Report</b> dialog is displayed with the list of messages logged during the export process.

*Only* the material definition for the *selected MDL graph* will be included in the exported encapsulated MDL module.

>[!NOTE]
>
> Learn more about encapsulated material definitions in section 13.5 of NVIDIA's [MDL Specification](https://developer.download.nvidia.com/designworks/mdl-sdk/secure/MDL_spec_1.6.1_16Dec2019.pdf?xBg5Km0pdI4vC4iQw4ADtIaJOe6U90WHUfJYs-WxGykGo3fdCqKP2Iw4AktgKPyx-z4mPfCRoQgU3GbbSXrZei8JCPLkYrLWfSUfaecroUdXSLv-UOWq41t20eWP7hRuMoc7oj5bJWEs_EXVmLkCd4uiqlZ_UQ&amp;t=eyJscyI6ImdzZW8iLCJsc2QiOiJodHRwczpcL1wvd3d3Lmdvb2dsZS5jb21cLyJ9), and [MDL SDK API](https://raytracing-docs.nvidia.com/mdl/api/mi_neuray_example_mdle.html).

![MDLE export pathway](mdl-export-encapsulated.png "MDLE export pathway")

*The "Export as mdle" pathway in the Explorer, and the resulting Export Report dialog*
