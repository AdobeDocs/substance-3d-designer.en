---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/interface/preferences-window/project-settings.html"
breadcrumb-title: ""
description: Configure project settings in Substance 3D Designer preferences to customize default project behavior.
helpx_creative_field: ""
helpx_description: Designer > Interface > Preferences window > Project settings
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Project settings
user-guide-description: ""
user-guide-title: ""
---

# Project settings

This page presents the <b>Projects settings</b> in [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html), and the settings contained within.

Substance 3D Designer allows you to create preferences *per project*, and share them across workstations. These preferences can be found in the <b>Projects</b> tab of the [Preferences](../../../interface/preferences-window/preferences-window.md) window.

This is very helpful if you want to set up a common working environment for a team working on the same project, by using the *same* Project File on *all* systems.

>[!NOTE]
>
> For more information about setting up and integrating Substance 3D Designer in a **production pipeline**, we *strongly recommend* referring to the [Pipeline and Project Configuration](../../../pipeline-and-project-con/pipeline-and-project-configuration.md) section of the documentation.

![Project settings](../../../assets/2019-3-0-prefs-proj-01.png "Project settings"){zoomable="yes"}

## Configuration

### Project

## Configuration

### Configuration file

This allows you to set the path of the <b>Configuration File</b> for Substance 3D Designer. A configuration file uses the <b>\*.sbscfg</b> extension, and contains a list of project files along with a set Compatibility Display setting.

*Default: default\_configuration.sbscfg*

>[!NOTE]
>
> You can use the **--config-file** command line option to launch Designer with a specific config file.  
> For more information about Configuration Files, you can refer to the [Configuration List - SBSCFG](../../../pipeline-and-project-con/configuration-list-sbscfg/configuration-list-sbscfg.md) page of the documentation.

### Project files

A project file contains a number of settings which define key aspects of the working environment in Designer, arranged into tabs. These settings are listed in the Project chapter of this page. Project files use the <b>\*.sbsprj</b> extension.

You can import multiple project files to be used for your working environment in Designer. When multiple project files exist, settings which are lists (e.g. library watched paths, aliases, etc.) are *combined*, and settings which are unique set values are defined by the *last project file of the list*.

*Default: default\_project.sbsprj (read only), user\_project.sbsprj*

>[!NOTE]
>
> For more information about using Project Files in a production pipeline, you can refer to the [Project Configuration Files - SBSPRJ](../../../pipeline-and-project-con/project-configuration-fil/project-configuration-files-sbsprj.md) page of the documentation.

### Compatibility display

Some of the nodes created with a recent version of Designer are not compatible with older versions of the Substance Engine.

<b>Compatibility Mode</b> will highlight the nodes which are *not* compatible with the selected Substance Engine, with a yellow outline.

*Default: Substance Engine v7*

### 3D View

|  |  |
| --- | --- |
| <b>Default renderer</b> | This setting lets you select the [3D renderer](../../../interface/3d-view/3d-renderers/3d-renderers.md) which should be used by default when starting a *new* [3D View](../../../interface/3d-view/3d-view.md). *Default: Default (predefined renderer)* |
| <b>Default shader</b> | This setting lets you select the shader which should be used by default when starting a *new* [3D View](../../../interface/3d-view/3d-view.md).*Default: physically\_metallic\_roughness.glslfx* |
| <b>Default environment map</b> | This setting lets you select the texture which should be applied by default to the Environment when starting a *new* [3D View](../../../interface/3d-view/3d-view.md).*Default: panorama\_map.hdr* |
| <b>Default state file</b> | The [3D View](../../../interface/3d-view/3d-view.md) **Scene State file** includes a number of settings for the 3D View, such as camera position, environment exposure and mesh. It is used to store the state of the 3D View so you can quickly load a scene which is tailored to your needs. Scene State files use the **\*.sbsscn** extension.This setting lets you select the 3D View Scene State file which should be used when starting a new 3D View.  **Alert:** Some software updates can change the way scene states are saved/loaded. If the scene is *not restored correctly*, it is recommended to manually set the desired state of the scene, and *reexport* the Scene state file you use as default.  *Default: Empty (in this case, a preset scene state is used)* |
| <b>Default lighting state</b> | This setting lets you select which of the predefined available lights should be enabled when starting a new [3D View](../../../interface/3d-view/3d-view.md), *if no file is set* in the **Default State File** field.*Default: Ambient Light only* |

### Aliases

Aliases are used to *shorten* system paths and allow teams to *share* assets more efficiently. Aliases are used *throughout the software* as well as in *SBS files*.

This settings allows you to *add* and *edit* aliases. When an alias is applied, it *replaces* the mapped path using the following syntax: <b>://</b>.

Example: if a resource *myResource* in the folder *myFolder* is placed at the location *C:/Users/user/Documents*, then mapping this location to *myalias* will result in the *myalias://myFolder/myResource* path being used in the application *and* the SBS package the resource belongs to.

*Default: sbs; sd-3dview-shapes; sd-3dview-maps; sd-3dview-shaders (Default project)*

>[!WARNING]
>
> Aliases are *global to the application*. This means they will be applied to *all paths* used in the application, as well as all paths in *loaded SBSPRJ Project Settings files*. Keep that in mind when setting up your project environment!  
> Also, we recommend *not nesting* aliases – i.e. aliasing a path which is also included in another alias.

### Bakers

|  |  |
| --- | --- |
| <b> Default resource name   </b> | This setting lets you set a default **naming template** which will be used for the output image files. The aliases available in the [baking window](../../../bakers/bakers.md) can also be used here (i.e. *$(mesh)*, *$(bakername)*, *$(udim)*, *$(custom)*).*Default: $(mesh)\_$(bakername)* |
| <b> Default preset   </b> | When opening the the [baking window](../../../bakers/bakers.md), you can have it **already configured** with specific bakers and settings by using this option to point to a presets *JSON* file. This file can be exported from the baking window once it has been set up according to your needs.*Default: None* |
| <b> Name filtering mode</b> | The scene object which name should be used for matching the low poly and high poly scene objects:<ul data-preserve-html="true"> <li data-preserve-html="true">Geometry name: use the name of the mesh geometry object</li> <li data-preserve-html="true">Parent name (Legacy): use the name of the parent of the mesh geometry object (same as in Designer versions 14.1 and lower)</li> </ul>*Default: Geometry name* |
| <b> Resource name macros  </b> | Instead of the *$(bakername)* alias, you can use your own character strings for [each baker](https://helpx.adobe.com/substance-3d-bake/bakers-settings.html).  When the  ***$(custom)*** alias is used in the output image name for any baker, it will be replaced by the character string matching that baker in the list. If a cell of the list corresponding to a baker is left blank, the *$(custom)* alias will *not* be replaced for this baker.Example: The 'c-mesh' value assigned to the 'Curvature Map From Mesh' baker will automatically rename *t\_mymesh\_**$(custom)*** into *t\_mymesh\_**c-mesh*** for the output of the Curvature From Mesh baker *only*.*Default: None* |
| <b> Sub-meshes name filter  </b> | When using the **Match By Name** option in the [bakers](../../../bakers/bakers.md), the parts of the low and high definition versions of a mesh are *matched* if the name of those parts before the defined **suffixes** is *identical*. This setting lets you set your own suffixes to suit your specific workflow. Matching parts of meshes can make rays ignore undesired geometry in baking operations.Example: the *body-torso**\_low***  object in the *body.fbx* mesh would be matched to the *body-torso**\_high*** object in *body\_high.fbx,* *if these objects exist* in these meshes*.**Default: \_low (Low Poly Mesh) / \_high (High Poly Mesh)*Similarly, **backfaces** can be *selectively ignored* for the parts of a mesh which name include the defined **suffix**, for [specific bakers](https://helpx.adobe.com/substance-3d-bake/bakers-settings.html) which include the **Ignore Backface** option.*Default: \_ignorebf*  **Note:**  The Ignore Backface and Low/High Poly Mesh suffixes can be *combined in any order* (e.g. *body-torso\_low\_ignorebf*) |

### COLOR MANAGEMENT

Please refer to the [Color Management](../../../color-management/color-management.md) page.

>[!WARNING]
>
> Changes to these settings will take effect after restarting Designer.

### General

|  |  |
| --- | --- |
| <b> Substance templates   </b> | When creating a new graph, you are prompted to start working off of a **template** which can have a number of settings and content *pre-configured*, such as outputs (e.g. *PBR (Metallic/Roughness)*).This setting lets you point Designer to directories where you can store your own SBS files to use as templates. Your custom templates will then be *added to the list* when creating a new graph.*Default: None*  **Note:**  We recommend using the current templates as a reference for configuring and formatting your template SBS files.  The templates can be found in the **resources &gt; templates** folder in the Substance 3D Designer installation directory. |
| <b> 3D scenes   </b> | By default, Designer uses the **MikkT tangent space** in the 3D View. MikkT is widely used and is the default in programs such as Unity, Unreal Engine 4, Blender and xNormal.You can use **your own tangent space** for the 3D View, which you provide to Designer in the form of a *DLL file* input in this setting. The label is auto-detected from the DLL file, and you can edit the description for the plugin.*Default: mikktspace.dll*Always recompute tangent frames.*Default: Unchecked*Normal and Tangent Smoothing Angle.*Default: 180.0°* |
| <b>Misc   </b> | Normal maps can be generated or processed using either the <b>DirectX</b> or <b>OpenGL</b> format. This setting sets the value for this format in several places, such as [material properties](../../../interface/3d-view/material-properties/material-properties.md) in the [3D View](../../../interface/3d-view/3d-view.md) and the [Normal](../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md) filter node parameters. *Default: DirectX*   Regarding the [Normal](../../../compositing-graphs/nodes-reference-for-com/atomic-nodes/normal/normal.md) filter node, you can set the *default value* for the <b>Alpha Channel Content</b> parameter. You can either choose to force the alpha to 1 in all cases, or fill it with information from its input. *Default: Force Alpha to 1* |
| <b> Image formats   </b> | This lets you specify the default format settings for *exported* images.*Default: Default (BMP) / Piz-based wavelet, unchecked, unchecked (EXR) / Unchecked, unchecked, 75 (JPG) / Best Speed, unchecked (PNG) / Default (TGA) / LZW (TIF) / Unchecked, 75 (WEBP)* |
| <b>Dependencies paths</b> | SBS packages generally have **dependencies**, i.e. reliance on *external resources* such as other SBS packages, bitmaps or vector files. These dependencies, which are listed in the [Dependency Manager](../../../interface/dependency-manager/dependency-manager.md), are stored and *referenced in the SBS package* with a **path** which points to these resources.For dependencies which include the *same path* as the SBS package (i.e. they are located in the same locations or sub-folder(s) from that location), the reference path is written **relative to** the SBS package location.Example: for a SBS package *myproject/mypackage.sbs*, an image *myproject/myfolder/myimage.png* will be referenced to the *myfolder/myimage.png* path in *mypackage.sbs*).For dependencies which do *not* include the same path as the SBS package (i.e. they are located in a different location altogether from the SBS package), you can **choose** how the path is written.If it is set to **relative paths**, the resource will be referenced in the same way as described above.Example: for a SBS package *myparentfolder/* *myproject/mypackage.sbs*, an image *myparentfolder/myotherfolder/myimage.png* will be referenced to the  ***../**myotherfolder/myimage.png* path in *mypackage.sbs*.If it is set to **absolute paths**, the resource will be referenced by its full system path (i.e. its filename).Example: for a SBS package *myparentfolder/*my*myproject/mypackage.sbs*, an image *myparentfolder/myotherfolder/myimage.png* will be referenced to this same full path in *mypackage.sbs*.*Default: ...relative paths.*  **Note:**  In all cases, moving the resources will *break dependencies* , which will result in **Ghost Instance** nodes in graphs.  To *consolidate* all dependencies in a single project folder along with the SBS package, you can use the **Export with dependencies...** features in the [Explorer](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/the-explorer-129368147.html) panel. This effectively creates an *autonomous* project folder which can be moved freely. |

### Library

This section lets you <b>manage the custom content</b> of the [Library](../../../interface/the-library/the-library.md).

The content of all folders listed in the <b>Paths added</b> list will be included in the Library. Any change to the content are reflected in the Library, following a refresh period which can be set in the [Library](../../../interface/preferences-window/preferences-window.md) [tab](../../../interface/preferences-window/preferences-window.md) of the [Preferences](../../../interface/preferences-window/preferences-window.md) window.

In the columns of the list, you can find options giving you more granular control over the way the content of these folders are added to the Library:

* <b>Enabled</b>; the content of the folder is shown in the Library (*Default: Checked*)
* <b>Recursive</b>: the content of all children folders is also shown in the Library (*Default: Checked*)
* <b>Exclude pattern</b>: the content which *entire filename* matches the input Regex (regular expression) is *not* shown in the Library (e.g. *\*/excluded\_directory/\**) . Learn more about the regular expression syntax [here](https://doc.qt.io/qt-5/qregularexpression.html#wildcardToRegularExpression) (*Default: None*)
* <b>Exclude extension</b>: the content which *file extension* include the input text string is *not* shown in the Library. *Multiple* strings should be separated by semi-colons (e.g. *jpg;png;tif;fbx*). (*Default: None*)

If SBS packages are added to the Library, the <b>graphs</b> and <b>resources</b> it contains can be *shown in the Library* as separate entries, if their <b>Visible In Library</b> parameter is set to 'Yes'.  
Options are available to define if this parameter should be set to 'Yes' *by default* when creating/adding a new graph or resource in a package.

*Default: Checked*

If a [Photoshop](https://www.adobe.com/products/photoshop.html) document (\*.PSD file) included in the Library has <b>multiple layers</b>, an option lets you display the content of *each layer as a separate image entry* in the Library.

*Default: Checked*

>[!NOTE]
>
> While your custom resources will be added to the Library, it might *not be visible* because of the filtering rules set for the existing Library categories. We recommend creating *your own filters* organised in folders, to ensure your content can be reliably found while working on your projects.  
> See the [Managing custom content and filters](https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/creating-library-filters-for-projects-170459772.html) section of the documentation for more information.

### MDL

If you want to add *your own* [MDL](../../../mdl-graphs/mdl-graphs.md) modules to the <b>mdl</b> section of the Library, you can add folders which include the modules in this list.  
Note that if modules are stored in subfolders, they will added as well and the folder hierarchy will be *mirrored* in the Library.

Example: If the folder *mymdlfolder* is added to this list, two MDL modules *mymdlfolder/mymodule.mdl* and *mymdlfolder/mysubfolder/myothermodule.mdl* would be added in the Library as the *<b>mdl/</b>mymodule* and *<b>mdl/mysubfolder/</b>myothermodule* entries.

*Default: None*

### Python

Substance 3D Designer will automatically load all [plugins](../../../scripting/plugin-basics/plugin-basics.md) located in the folders you add to the <b>Url</b> list.

*Default: None*

>[!WARNING]
>
> Changes to these settings will take effect after restarting Designer.  
> [Plugin packages](../../../scripting/plugins-packages/plugins-packages.md) still need to be installed *manually* using the [Plugin Manager](../../../scripting/plugin-manager/plugin-manager.md).

### Scripting

>[!WARNING]
>
> This feature will be *retired* in a future release in favor of the more robust **Python API**. Therefore, we recommend making the switch in your scripts as soon as possible.  
> You may go to the [Application callbacks](../../../scripting/application-callbacks/application-callbacks.md) page in the [Scripting](../../../scripting/scripting.md) section of our documentation to get started.

This section lets you set up and control *scripts* to be executed when specific *events* happen in Designer. It is particularly useful when used in conjunction with the [Perforce](https://www.perforce.com/) integration which can be configured in the Version Control tab of the Project Settings.

|  |  |
| --- | --- |
| <b> Actions   </b> | Designer has pre-configured **callbacks triggers**, which will *execute the script* you provide using the interpreter set up in the **Interpreters** list described below.The included callbacks are the following:<ul data-preserve-html="true"><li data-preserve-html="true"><strong>onBeforeFileLoaded</strong> – executes the script <em>before</em> a SBS package is loaded</li><li data-preserve-html="true"><strong>onAfterFileLoaded</strong> – executes the script <em>after</em> a SBS package is loaded</li><li data-preserve-html="true"><strong>onBeforeFileSaved</strong> – executes the script <em>before</em> a SBS package is saved</li><li data-preserve-html="true"><strong>onAfterFileSaved</strong> – executes the script <em>after</em> a SBS package is saved</li><li data-preserve-html="true"><strong>getGraphExportOptions</strong> – executes the script when the [Export Outputs](../../../compositing-graphs/exporting-bitmaps/exporting-bitmaps.md) options are called</li></ul>A [Python](https://www.python.org/) script is included in the installation files, with the functions triggered by each callback *already set up* and ready to use. You can use it as a starting point and add functionality according to your needs. This script is **functions.py**, located in the **tools &gt; scripting** folder of the installation files.*Default: None*  **Note:**  Initially, selecting a script for any of the callbacks will input that script in *all* callbacks for convenience. You can freely set up different scripts for specific callbacks after that point. |
| **Interpreters** | In this list, you can provide specific *interpreters* Designer should use to execute the scripts set up in the **Actions** list described above. Interpreters are identified using a *custom alias* you can edit in the text field of each entry of the list.A [Python](https://www.python.org/) 3.6 interpreter is bundled with the installation files of Designer. You can find it in the **plugins &gt; pythonsdk** folder of the installation files.*Default: None* |

### Version Control

>[!WARNING]
>
> [Perforce](https://www.perforce.com/) is the *only* tool which is currently supported for version control.

Please refer to the [Version control](../../../interface/preferences-window/version-control/version-control.md) page.

**How should you use this?**

You should set all preferences that are *project-specific* in a Project File (\*.sbsprj) in Designer. These preferences include:

* Tangent space plugin
* Library
* Aliases
* 3D View settings
* Baking settings
* [Version Control settings](../../../interface/preferences-window/version-control/version-control.md)

All the paths are stored *relative to* the Project File (.spsprj). so you can have a **library** folder at the same location as your Project File in Perforce, with the following sub-folder tree :

* maps/
* meshes/
* sbs/
* sbsar/
* psd/
* 3Dview/
* ...

On the same level as the Project File, you may also store a tangent space plugin or default shader.

The Configuration File (\*.sbscfg) should be placed in the Perforce workspace alongside the Project File.

>[!NOTE]
>
> For more information about setting up and integrating Substance 3D Designer in a **production pipeline** , we *strongly recommend* referring to the [Pipeline and Project Configuration](../../../pipeline-and-project-con/pipeline-and-project-configuration.md) section of the documentation.
