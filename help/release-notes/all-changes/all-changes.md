---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/release-notes/all-changes.html"
breadcrumb-title: ""
description: Review all changes and updates across Substance 3D Designer versions to track feature evolution and improvements.
helpx_creative_field: ""
helpx_description: Designer > Release Notes > All changes
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: All changes
user-guide-description: ""
user-guide-title: ""
---



# All changes

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

| 13 |  |
| --- | --- |
| <b>13.1</b> | 13.1.2    13.1.1    13.1.0 |
| <b>13.0</b> | 13.0.2    13.0.1    13.0.0 |

</td>
<td style="border: 0;" valign="top">

| 12 |  |
| --- | --- |
| <b>12.4</b> | 12.4.1    12.4.0 |
| <b>12.3</b> | 12.3.1    12.3.0 |
| <b>12.2</b> | 12.2.1    12.2.0 |
| <b>12.1</b> | 12.1.1    12.1.0 |

</td>
</tr>
</table>

<table>
<tr style="border: 0;">
<td style="border: 0;" valign="top">

| 11 |  |
| --- | --- |
| <b>11.3</b> | 11.3.3    11.3.2    11.3.1    11.3.0 |
| <b>11.2</b> | 11.2.2    11.2.1    11.2.0 |
| <b>11.1</b> | 11.1.2    11.1.1    11.1.0 |

</td>
<td style="border: 0;" valign="top">

| 10 |  |
| --- | --- |
| <b>10.2</b> | 10.2.2    10.2.1    10.2.0 |
| <b>10.1</b> | 10.1.3    10.1.2    10.1.1    10.1.0 |

</td>
</tr>
</table>

+++Previous versions

| 9 |  |
| --- | --- |
| <b>9.3</b> | 9.3.3    9.3.2    9.3.1    9.3.0 |
| <b>9.2</b> | 9.2.3    9.2.2    9.2.1    9.2.0 |
| <b>9.1</b> | 9.1.3    9.1.2    9.1.1    9.1.0 |



| 8 |  |
| --- | --- |
| <b>8.3</b> | 8.3.4    8.3.3    8.3.2    8.3.1    8.3.0 |
| <b>8.2</b> | 8.2.2    8.2.1    8.2.0 |
| <b>8.1</b> | 8.1.2    8.1.1    8.1.0 |



| 7 |  |
| --- | --- |
| <b>7.2</b> | 7.2.5    7.2.4    7.2.3    7.2.2    7.2.1    7.2.0 |
| <b>7.1</b> | 7.1.4    7.1.3    7.1.2    7.1.1    7.1.0 |



| 6 |  |
| --- | --- |
| <b>6.0</b> | 6.0.4    6.0.3    6.0.2    6.0.1    6.0.0 |



| 5 |  |
| --- | --- |
| <b>5.6</b> | 5.6.2    5.6.1    5.6.0 |
| <b>5.5</b> | 5.5.3    5.5.2    5.5.1    5.5.0 |
| <b>5.4</b> | 5.4.0 |
| <b>5.3</b> | 5.3.3    5.3.2    5.3.1    5.3.0 |
| <b>5.2</b> | 5.2.5    5.2.1    5.2.0 |
| <b>5.1</b> | 5.1.1    5.1.0 |
| <b>5.0</b> | 5.0.3    5.0.2    5.0.1    5.0.0 |


+++

## Version 15

### 15.1.2

*(Released February 3rd, 2026)*

### Fixes

* &#91;Engine&#93; Levels: Floating point values are always clamped to &#91;0, 1&#93;
* &#91;Bakers&#93; Matching geometry by parent name (Legacy) does not work for submeshes
* &#91;Bakers&#93; Color: Edits to material colors in the UI are ignored
* &#91;3D View&#93;&#91;Bakers&#93; OBJ file takes a very long time to load

### 15.1.1

*(Released January 20th, 2026)*

### ADDED

* &#91;Samples&#93; Add two samples to create sections to feed the Painter ribbon tool
* &#91;Engine&#93; Update to Substance Engine v9.3.2
* &#91;Engine&#93;&#91;Metal&#93; Improve performances
* &#91;Engine&#93; Bilinear interpolation of integer textures is now performed with increased precision (CPU backend)
* &#91;Bakers&#93; Log a warning if Vertex color is missing from high poly mesh
* &#91;Branding&#93; Update filetypes icons
* &#91;NewGraph&#93; Apply hover styles on (i) icon in 'List', 'Packages' and 'Directories' view modes

### Fixes

* &#91;3DView&#93; UDIM meshes are not rendering a single tile anymore
* &#91;3DView&#93; Crash when no renderDevice is detected
* &#91;Branding&#93; Fix icons for .SBS files on Linux
* &#91;Content&#93; RGB to HSL function: Incorrect result for near 0 inputs
* &#91;Graph&#93; Graph icon/thumbnail generator does not work
* &#91;Graph&#93; Node menu: grouped items with no thumbnail have no indentation
* &#91;Engine&#93;&#91;Content&#93; Color to mask v2: Artefacts on SSE2 engine when using Lab distance color space
* &#91;Engine&#93;&#91;Content&#93; Color to mask v2: Artefacts on arm64 GPU engines when using Lab distance color space
* &#91;Engine&#93;&#91;Metal&#93; Black irradiance output for PBR render node
* &#91;Engine&#93;&#91;Mac&#93; Incorrect result in a pixel processor function on Metal
* &#91;Engine&#93;&#91;Mac&#93; Improve accuracy for some instructions used in Pixel Processors on Apple Silicon M1/M2 GPUs
* &#91;Engine&#93; Input images (or embedded resource) resizing will no longer introduce border artefacts (CPU backend)
* &#91;Engine&#93; Levels filter will no longer clamp its floating-point input values when outputting 8I/16I textures (CPU backend)
* &#91;Engine&#93; Fixed an FxMaps bug where grayscale input images consumed by FxMaps nodes could be incorrectly sampled (CPU backend)
* &#91;Engine&#93; Fixed some artifacts in the 1-seed version of the Distance filter (GPU backends)

### 15.1.0

*(Released December 11th, 2025)*

### ADDED

* &#91;NewGraph&#93; Rework of the new graph window
* &#91;NewGraph&#93; Add materials samples and advanced samples
* &#91;NewGraph&#93; Add a new attribute for graph for the template data (category and sub-title)
* &#91;NewGraph&#93; Remove Output format option
* &#91;Content&#93; Add hash functions
* &#91;Content&#93; Add tonemappers to functions.sbs
* &#91;Content&#93; Anisotropic noise v2: add default output format, add disorder
* &#91;Content&#93; Apply sentence case to node and parameters labels
* &#91;Content&#93; BnW spots 1 v2: add default output format, no tiling support
* &#91;Content&#93; BnW spots 2 v2: add default output format, no tiling support
* &#91;Content&#93; BnW spots 3 v2: add default output format, no tiling support
* &#91;Content&#93; Cells 1,2,3,4 v2: add default output format, no tiling support, disorder options
* &#91;Content&#93; Clouds 1 v2: add default output format, no tiling support
* &#91;Content&#93; Clouds 2 v2: add default output format, no tiling support
* &#91;Content&#93; Clouds 3 v2: add default output format, no tiling support
* &#91;Content&#93; Color to mask v2
* &#91;Content&#93; Directional noise 1 v2: add default output format, no tiling support
* &#91;Content&#93; Directional noise 2 v2: add default output format, no tiling support
* &#91;Content&#93; Directional noise 3 v2: add default output format, no tiling support
* &#91;Content&#93; Directional noise 4 v2: add default output format, no tiling support
* &#91;Content&#93; Directional scratches v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 1 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 2 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 3 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 4 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt 5 v2: add default output format, no tiling support
* &#91;Content&#93; Dirt gradient v2: add default output format, new disorder options
* &#91;Content&#93; Fractal Sum Base v2: add default output format, disorder, no tiling support
* &#91;Content&#93; Fractal sum 1,2,3,4 v2: add default output format
* &#91;Content&#93; Gaussian noise v2: add default output format, no tiling support
* &#91;Content&#93; Gaussian spots 1&amp;2 v2: add default output format, no tiling support
* &#91;Content&#93; Messy fibers 1,2,3  v2: add default output format, no tiling support, disorder options
* &#91;Content&#93; Moisture noise v2: add default output format, no tiling support
* &#91;Content&#93; New 'Moisture noise 2' node
* &#91;Content&#93; Noises: update to add default outputformat
* &#91;Content&#93; Perlin noise v2: add default output format, no tiling support
* &#91;Content&#93; Shape mapper: add filtering mode
* &#91;Content&#93; UV mapper: add filtering mode
* &#91;Content&#93; Waveform 1 v2: use default output format + new options
* &#91;Content&#93; White noise v2: use default output format, add distribution options
* &#91;Bakers&#93; Display the UVs from the selected mesh only
* &#91;Bakers&#93; Add an option to select the method of matching geometry by name
* &#91;Bakers&#93; Select the closest Baker when a baker is deleted
* &#91;Bakers&#93; UDIM: define a list of UV tiles to bakes
* &#91;Bakers&#93; Update bake sdk to 3.15.4
* &#91;3D View/SceneBrowser&#93; Avoid selecting a UsdPrimitive when doing a right click on it
* &#91;ColorManagement&#93; Support ACES 2.0
* &#91;Compositing Graph&#93; Allow to set an output node as the "Default output"
* &#91;Cooker&#93; Remove warning on unconnected inputs of function instances¬†
* &#91;Functions&#93; Add isDefined operator
* &#91;Graph&#93; Group the items per 'group' attribute in the node menu
* &#91;Graph&#93; Improve thumbnail rendering

### Fixes

* &#91;3D View&#93; L16 Grayscale texture is displayed with a red tint when plugged to the environment or the baseColor
* &#91;3D View&#93; Changing the material binding of a scene with no material creates a new "default" material
* &#91;3D View&#93; Computed normals are not correct for specific OBJ meshes
* &#91;3D View&#93; Custom environment from SBSSCN is not visible on load in Pathtracer
* &#91;3D View&#93; Errors in the Console when rotating a disabled environment
* &#91;3D View&#93; Specular level is not applied correctly
* &#91;3D View&#93; Specular edge color doesn't work when using Eclair rasterizer
* &#91;3D View&#93; User added material is not applied on default scenes
* &#91;3D View&#93;&#91;Bakers&#93; Material color is too dark once overridden or when using a "Color" baker
* &#91;3D View&#93;&#91;Bakers&#93; No material color from FBX file
* &#91;Bakers&#93; Material colors in FBX files are not correctly detected
* &#91;Bakers&#93; 'recompute\_tangents' option is always 'false' in JSON preset exports
* &#91;Bakers&#93; CLI: Crash when running the same baker consecutively through JSON file
* &#91;Bakers&#93; Updating the 'color-generator' parameter does not work for 'Grayscale'
* &#91;Content&#93; Mask to paths: Failure in non-square ratios
* &#91;Content&#93; PBR Render/Icon renderer: Incorrect specular lobe function
* &#91;Content&#93; Paths to spline: Set the 'Output size' to 'Relative to parent' by default'
* &#91;Content&#93; Point list: Points are not in the correct order when data texture is non-square
* &#91;Content&#93; Spline mapper: 1px line glitch in random cases
* &#91;Content&#93; Spline mapper: stretched UVs in some cases when thickness is 0
* &#91;Graph&#93; Crash when deleting the output of a function subgraph
* &#91;Graph&#93; Input node color type can be changed in read-only packages
* &#91;Graph&#93; Primary input can be changed in read-only packages
* &#91;Properties&#93; The color of the color preview widget does not match the sRGB button state
* &#91;Scene&#93; Cannot load an OBJ file larger than 2 GB
* &#91;UI&#93; The Console and Dependency manager docking states are not restored after restart

### 15.0.3

*(Released October 23rd, 2025)*

### Fixes

* &#91;Content&#93; Preview output of Spline tools nodes is not displayed by default
* &#91;Graph&#93; Crash when deleting the output of a function subgraph

### 15.0.2

*(Released September 18th, 2025)*

### Added

* &#91;3D View/OpenGL&#93; Remove the wireframe effect applied on the selected Mesh
* &#91;3D View&#93; Allow using the 'F' key to focus on a selected mesh when the Scene Browser has focus
* &#91;3D View&#93; Render not refreshed when changing normal map format
* &#91;BakersCLI&#93; Add option to control surface cache size
* &#91;BakersCLI&#93; Rename "use\_cache" option to "keep\_meshes\_in\_cache"
* &#91;UI&#93; Refresh icon for 3D scenes in Library

### Fixes

* &#91;3D View&#93; Crash when assigning a material node to a multi-material scene
* &#91;3D View&#93; Graph created from texture inputs is always viewed in 3D View regardless of preferences
* &#91;3D View&#93; Incorrect usage in a 'Viewed in 3D View' badge tooltip in a specific case
* &#91;3D View&#93; Lots of USD errors when overriding specific scenes
* &#91;3D View&#93; Shadow artefacts when using displacement on a flat Scene in the rasterizer
* &#91;3D View&#93; Some specific scenes are not visible when using OpenGL renderer
* &#91;3D View&#93; The Dialog used to "Select the destination Substance Graph" always have the "Pending" Graph icon
* &#91;3D View&#93; The viewport contextual menu is not displayed for specific scenes
* &#91;3D View&#93; 'Viewed in 3D View' badges are not cleared when switching scenes in a specific case
* &#91;3D View&#93; Washed out color in 3D View when using Adobe ACE color management
* &#91;3D View&#93;&#91;Linux&#93; Several scenes render black in the OpenGL renderer
* &#91;3D View&#93;&#91;Scene Browser&#93; Arrow keys move the selection at the root
* &#91;BakerCLI&#93; Can't override some parameters
* &#91;Bakers&#93; Artifacts in dilation when using normal bakers with antialiasing
* &#91;Bakers&#93; Baking process abruptly stopped in CLI while baking a high amount of UDIMs at 4K
* &#91;Bakers&#93; Crash when pushing baker down in baker list in specific case
* &#91;Bakers&#93; Format selection switches from .surface to .dds
* &#91;Bakers&#93; Freeze while baking high amount of UDIMs at 4K
* &#91;Bakers&#93;&#91;macOS&#93; Crash when baking Texture transfer with antialising
* &#91;Content&#93; Point list: Points are not in the correct order when data texture is non-square
* &#91;Content&#93; View color palette: Internal nodes are computed at too high resolutions
* &#91;Data&#93; Crash when renaming output to fix ghost output in instance
* &#91;Engine&#93; Distance: input mask luminance is altered
* &#91;FxMap&#93; $tiling has no effect if the FX-Map is inside a subgraph
* &#91;Graph&#93; Fuzzy search returns irrelevant results
* &#91;Python Editor&#93; Loaded scripts are not reopened across sessions

### 15.0.1

*(Released July 22nd, 2025)*

### Added

* &#91;3D View&#93; Allow to texture USD Meshes that have displayColor and no Material bindings
* &#91;3D View&#93; Do not automatically create one material per mesh that does not have a material binding
* &#91;3D View&#93; Rename "Converged pixel samples" to "Samples"
* &#91;3D View&#93; Rename the "UV Scale Enabled" parameter to "Enable Physical Size from Graph"
* &#91;3D View&#93; Scale down the displacement intensity according to the 'Tiling' parameter
* &#91;3D View/OpenGL/Iray&#93; Add a message in the viewport when the default environment is disabled
* &#91;Bakers&#93; Use icons for buttons to reorder lines in the Bakers render list
* &#91;Preferences&#93; Add an option to define the default 3D View renderer
* &#91;Properties&#93; Make 'Reset to default' use the authored default values if any

### Fixes

* &#91;3D View&#93; Artefacts on specific scene when rendered with OpenGL
* &#91;3D View&#93; Default environment is not disabled when loading a USD 3D scene resource that contains one
* &#91;3D View&#93; Displaying the viewport contextual menu takes several seconds in large scenes
* &#91;3D View&#93; 'Emissive intensity' is 0 when overriding non-USD materials using 'Emissive color' only
* &#91;3D View&#93; Red and Blue channels are swapped in 8-bit texture used as environment
* &#91;3D View&#93; RMB drag&amp;drop does not work consistently because of right click register
* &#91;3D View&#93; 'Show only' on subset hides its parent mesh
* &#91;3D View&#93; The default Scenes loaded from a files appears with a wrong base color
* &#91;3D View&#93; 'UV Scale' property is reset when switching from OpenGL to another renderer and back
* &#91;3D View&#93;&#91;Iray&#93; Renders are often blurry and pixelated
* &#91;Bakers&#93; Artifacts when using diffusion on an AMD GPU
* &#91;Bakers&#93; Baking fails with some scenes for UV sets other than 0
* &#91;Bakers&#93; 'Transferred texture': The 'UV Set' list does not take 'Use low as high poly' option into account
* &#91;Bakers&#93; UV tiles selection is always reset to 'All'
* &#91;Graph&#93; Crash when deleting a node in context
* &#91;Mac OS&#93;&#91;3D View&#93; Incorrect render resolution on mac displays
* &#91;Parameters&#93; Modified parameters are not stylized on first display
* &#91;UX&#93; Disabled items in dropdown menu are invisible

### 15.0.0

*(Released July 15th, 2025)*

### Added

* &#91;3D View&#93; Brand new renderer, with rasterizer and pathtracer modes
* &#91;3D View&#93; Add a selection tool to pick an object in the 3D scene
* &#91;3D View&#93; Add new "Export scene with layers..." action in the "Scene" menu
* &#91;3D View&#93; Add new toolbar buttons
* &#91;3D View&#93; Add the possibility to switch between multiple cameras contained in a USD scene
* &#91;3D View&#93; Allow to focus on the selected object when pressing 'F' in the viewport
* &#91;3D View&#93; Allow to generate a Substance Compositing Graph from an existing material
* &#91;3D View&#93; Allow to send a SBS Comp Graph in the 3D View and assign its unique output to the Environment/Panorama usage
* &#91;3D View&#93; Clear the current selection by pressing the Escape key
* &#91;3D View&#93; Display an imported 3D scene with textures
* &#91;3D View&#93; Distinguish X and Y texture repetition controls
* &#91;3D View&#93; Enable / Disable shadows
* &#91;3D View&#93; Enable / Disable ground plane
* &#91;3D View&#93; In the "Materials" menu, add the "Remove" only for the Material that have been added manually and are unused
* &#91;3D View&#93; In the "Materials" menu, remove the action "Remove All"
* &#91;3D View&#93; Make exported USDZ files self-contained
* &#91;3D View&#93; Make the renderer properties persistent when switching the renderer mode
* &#91;3D View&#93; Preserve the existing material inputs when overriding a Material
* &#91;3D View&#93; Rearrange Camera properties
* &#91;3D View&#93; Remove actions "Camera/Save screenshot..." and "Camera/Copy screenshot to clipboard"
* &#91;3D View&#93; Remove the Menu action "Material/Rebuild all"
* &#91;3D View&#93; Remove the prefix "Default" of the label of the default camera
* &#91;3D View&#93; Set the menu action "Reset to default value" as the last one in the material input property hamburger menu
* &#91;3D View&#93; Shortcut adjustments
* &#91;3D View&#93; Support shadows and translucency in real time mode
* &#91;3D View&#93; Support MaterialX shaders from an imported USD scene
* &#91;3D View / OpenGL&#93; Rename the "UV Scale Enabled" parameter to "Enable Physical Size from Graph"
* &#91;3D View / Post effects&#93; Bloom
* &#91;3D View / Post effects&#93; Depth of field
* &#91;3D View / Post effects&#93; Tone mapping
* &#91;3D View / Scene Browser&#93; Allow to display the Material properties when selecting it in the SceneBrowser
* &#91;3D View / Scene Browser&#93; Hide the column "Material"
* &#91;3D View / Scene Browser&#93; Put in bold the USD Primitives that are controlled by a Predefined entity
* &#91;Bakers&#93; Add a contextual menu in the treeview with "Select all"/"Deselect all" actions
* &#91;Bakers&#93; Add an option to control bitangent interpolation
* &#91;Bakers&#93; Add horizontal splitter in GUI
* &#91;Bakers&#93; Add UDIM macro by default in output name when the scene is udim
* &#91;Bakers&#93; Allow to recompute tangent
* &#91;Bakers&#93; Allow to rename a baker without breaking links
* &#91;Bakers&#93; Change the default size of the middle panel
* &#91;Bakers&#93; Input texture for UDIM workflow
* &#91;Bakers&#93; Make 2D View maps list order match Bakers render list order
* &#91;Bakers&#93; Make the baking window modal
* &#91;Bakers&#93; Manage tonemapping parameters
* &#91;Bakers&#93; Remove tangent space plugin selection
* &#91;Bakers&#93; Save status "enabled" or "disabled" for Bakers when saving a Preset
* &#91;Bakers&#93; Select material by default in select widget
* &#91;Bakers&#93; Set default orientation of Normal output texture relative to the preference
* &#91;Bakers&#93; Set UV tiles to All by default
* &#91;Bakers&#93; WordSpaceDirection add option FromTexture/FromValue
* &#91;Bakers&#93; World to tangent: set default input to "from texture"
* &#91;SBSBaker&#93; Create an option to control the backend order
* &#91;SBSBaker&#93; Improve use of StringList argument
* &#91;SBSBaker&#93; Rename "match\_source\_instance" to "match\_mesh\_name"
* &#91;SBSBaker&#93; Rename "Submesh" to "GeomSubset"
* &#91;SBSBaker&#93; Rename to substance3d\_baker
* &#91;Content&#93; Add 'Hemisphere' shape to generator nodes exposing Quadrant shapes
* &#91;Interop&#93; Support GLTF file format
* &#91;Interop&#93; Support PLY file format
* &#91;Interop&#93; Support STL file format
* &#91;Library&#93; Uniformize tooltips for atomic nodes
* &#91;Mac&#93; Stop supporting MacIntel platform
* &#91;Nodes&#93; Add richtooltips for atomic nodes
* &#91;Parameters&#93; Close 'Attributes' section by default
* &#91;Parameters&#93; Let the user specify base parameter default values for new instances
* &#91;Preferences&#93; Bakers: add a boolean option to compute the tangent space per fragment
* &#91;Preferences&#93; Remove the tangent space plugins
* &#91;Preferences&#93; Store the preferences per minor version of SD (XX.X)
* &#91;VFX&#93; Update Boost to 1.85.0
* &#91;VFX&#93; Update MacOS minimal version to 12.0
* &#91;VFX&#93; Update OpenColorIO to 2.4.2
* &#91;VFX&#93; Update OpenColorIO to 2.4.x
* &#91;VFX&#93; Update OpenExr to 3.3.x
* &#91;VFX&#93; Update Qt to 6.5.8

### Fixes

* &#91;3D View&#93; Textures in exported USD scene are not correctly applied
* &#91;3D View&#93; &#91;UDIM&#93; Cannot view UDIM graph outputs in 3D View when automatic viewing on graph opening is turned off in graph preferences
* &#91;Bakers&#93; 'Anti-alias.' and 'Avg. normals' cells for non-applicable bakers are blank and editable
* &#91;Bakers&#93; 'Refresh' action uses raytracing backend when it is disabled in preferences
* &#91;Bakers&#93; Bakers blocked as busy after failure during 'Refresh all baked maps' process
* &#91;Bakers&#93; Crash at 180+ UDIMs when baking OpenGL Position map on specific mesh
* &#91;Bakers&#93; Crash when opening 'Bake model information' dialog multiple times in a row (macOS only)
* &#91;Bakers&#93; In JSON preset export, 'udim' value is replaced by '1001' when it was set to 'All'
* &#91;Bakers&#93; Memory is not correctly detected on Linux
* &#91;Bakers&#93; Missing map input dependency does not trigger warning and/or block rendering
* &#91;Bakers&#93; No error label when output name is empty
* &#91;Bakers&#93; Switching high poly mesh from file has no effect
* &#91;Bakers&#93; Target baker is not selected by default when using 'Rebake' action
* &#91;Engine&#93; Distance: visible "cut" in some situations
* &#91;Engine&#93; Fx-Map: Negative colors are not supported when bitdepth is 8-bit (GPU engines only)
* &#91;Localization&#93; Character input switches back from Japanese to Latin in node menu
* &#91;Security&#93; USDC File Parsing Out Of Bound Write Vulnerability
* &#91;Security&#93; Out-of-Bound WRITE Vulnerability II, when parsing NEF file
* &#91;Security&#93; Out-of-Bound Read Vulnerability III, when parsing DNG file
* &#91;Preferences&#93; UX issues in project settings for read-only projects
* &#91;Resources&#93; Multiple UV sets are not displayed when opening FBX files
* &#91;UI&#93; Overlapping labels in status bar
* &#91;UI&#93; Tooltips of the 'Link creation mode' drop down menu are not displayed

## Version 14

### 14.1.2

*(Released April 15th, 2025)*

### Added

* &#91;Graph&#93; Use the default GPU engine to generate thumbnails for the current graph
* &#91;Library&#93; Use the default GPU engine to generate thumbnails for the library

### Fixes

* &#91;Graph&#93; Cannot move connections in some cases in 'Standard' link creation mode
* &#91;Content&#93; Artifacts in MLV filter output in a specific case
* &#91;Content&#93; Atlas splitter/scatter: only first cell is drawn correctly (macOS + GPU engine only)
* &#91;Content&#93; Bevel Smooth: format is absolute 32f
* &#91;Content&#93; Fibers 1: visual artefacts when converting to normal map
* &#91;Content&#93; RT AO, Shadows, Bent Normal render incorrectly in some cases
* &#91;Bakers&#93; Menu items with submenus miss some margin on the right of the text
* &#91;MacArm&#93;&#91;sbsrender&#93; Wrong CPU engine when GPU engine not found
* &#91;Mac/Linux&#93;&#91;sbsrender&#93; Wrong default GPU engine

### 14.1.1

*(Released February 20th, 2025)*

### Added

* &#91;Graph&#93; Node alignment tools: Reinstate keyboard shortcuts, enable stacking by default
* &#91;MDL&#93; Warn users that "MDL graphs" will be deprecated in a future version
* &#91;Preferences&#93; Warn users that "Custom tangent space plugins" will be deprecated in a future version

### Fixes

* &#91;2D View&#93; Display center pixel coordinates instead of top-left
* &#91;Content&#93; Anisotropic Kuwahara Grayscale: Cooker warning for missing 'ignore\_alpha' variable
* &#91;Content&#93; Cooker warnings in some Grunge nodes
* &#91;Content&#93; Cooking errors for missing parameter in 'Auto Levels' node
* &#91;Content&#93; Cooking errors in Console when rendering thumbnails of some packages
* &#91;Content&#93; Edge Notch: Cooking warning in the Console
* &#91;Content&#93; MLV Color: Color bleed despite using No Tiling in a specific case
* &#91;Content&#93; Mask to Paths: Paths can be too many, too few or of zero length in specific cases
* &#91;Content&#93; PBR Render v1: Some utility graphs are exposed in Library
* &#91;Content&#93; Scatter on spline: one pattern is drawn even though there is no spline input
* &#91;Parameters&#93; 'Ghost value' label when pasting list parameter with mismatching index
* &#91;UI&#93; Crash when closing Designer through 'Quit' action in macOS dock (macOS only)
* &#91;UI&#93; Texture paths in shader properties are not cropped to the dock's width

### 14.1.0

*(Released January 14th, 2025)*

### Added

* &#91;2D View&#93; Add pinned pixel display in Information panel
* &#91;API&#93; Expose the nodes BBox size in the Graph View scene
* &#91;Content&#93; 'Material Height Blend': Add 'Height Mask' output
* &#91;Content&#93; 'Path Vertex Processor': Use 'Edit function' button for 'Per Vertex Function' parameter
* &#91;Content&#93; Auto Levels: Clean unused parameter, adjust labels and tooltip
* &#91;Content&#93; Mask to paths v2
* &#91;Content&#93; New Mean of Least Variance node (MLV)
* &#91;Content&#93; New Median Filter node
* &#91;Content&#93; Quantize Color: add a 'Nearest' filtering option
* &#91;Content&#93; Spline Bridge List: Add random spline offset parameters
* &#91;Content&#93; Spline Tools: New Spline (Quadratic) node
* &#91;Content&#93; Triangle grid: change triangulation method and use loops
* &#91;Content&#93; New Scatter Splines on Splines node
* &#91;Cooker&#93; Expose 'Pixel ratio' base parameter as '$pixelratio' static variable
* &#91;CrashReport&#93; Integrate new crash report window
* &#91;Engine&#93; Add the Vulkan/Metal version of the blend engine
* &#91;Graph&#93; Material Mode: allow connection to input without usage when a single link is selected
* &#91;Graph&#93; Material link: allow standard connections when connection is not ambiguous
* &#91;Graph&#93; Node alignment tools: add horizontal/vertical distributions, left/right/top/bottom alignments, and support stacked nodes
* &#91;Library&#93; Fix text color in contextual menus
* &#91;Parameters&#93; Copy parameters from a node to another
* &#91;Properties&#93; "Reset all": Remove the confirmation pop up window
* &#91;Resources&#93; Set the format to "All format" in the "Link Bitmap" dialog
* &#91;Search&#93; Add a way to enable/disable a recursive mode
* &#91;Search&#93; Add a way to enable/disable the fuzzy search
* &#91;Search&#93; Always show and set focus on search term field when enabling Node Finder using its keyboard shortcut
* &#91;Search&#93; Rework the filter option
* &#91;Shortcuts&#93; Allow 'V', 'H' and 'S' keys to be assigned
* &#91;ThirdParty&#93; Upgrade to Qt 6.5.7
* &#91;UX&#93; Modal dialogs should not be minimisable
* &#91;UX&#93; Remove horizontal scroll on alert dialog

### Fixes

* &#91;Content&#93; Bevel: Normal Format is not affected by the global preference
* &#91;Content&#93; Color to Mask node does not ignore alpha
* &#91;Content&#93; Directional distance: Incorrect result when input has vertical image ratio
* &#91;Content&#93; Flood Fill Mapper: Warning raised for absent variable
* &#91;Content&#93; Histogram Compute: result is 16 times what it should be
* &#91;Content&#93; RT caustics doesn't work in non square resolution
* &#91;Content&#93; Spline Bridge List: Incorrect result when using Start/End offsets
* &#91;Content&#93; Spline Select: output spline amount can be greater than the input spline amount
* &#91;Content&#93; Spline Warp produces a black result with SSE engine
* &#91;Content&#93; Triangle Grid: pattern is not tiling properly
* &#91;Content&#93; Triangle grid: Tiling is broken in a specific case
* &#91;Data&#93; Crash when changing graph input identifier in a specific case
* &#91;Function Graph&#93; Long values appear overlapped on 'Float' nodes
* &#91;Fx-Map&#93; Crash when displaying Quadrant node properties
* &#91;Graph&#93; &#91;UDIM&#93; Having a scrollbar in the UDIM list results in 1..1 1..2 entries
* &#91;Graph&#93;&#91;Shortcuts&#93; Node created using a shortcut is not placed on existing link after node duplication
* &#91;Properties&#93; Incorrect parameter display when value is invalid
* &#91;Publish&#93; Reciprocal dependencies result in an infinite loop when publishing a package
* &#91;Publish&#93; Silent failure when using 'Publish' action on package with unloaded dependency
* &#91;UI&#93; 'Parent size' widget is not displayed correctly when expanded and may block the interface (macOS only)
* &#91;UI&#93; Main window falls behind other applications in some cases (Windows only)

### 14.0.2

*(Released October 10th, 2024)*

<b>Added:</b>

* &#91;Function graph&#93; Improve text alignment within nodes
* &#91;MacOS&#93; Reallow installation on BigSur version (11.0)
* &#91;Windows&#93; Reallow installation on Windows 10 19H2

<b>Fixed:</b>

* &#91;Bitmap&#93; Paint strokes on bitmap resource do not mark host package as modified
* &#91;Function Graph&#93; Crash when closing package with function graph hosting an instance node
* &#91;Function graph&#93; Crash when undoing two Sample Color node tweaks in a row

### 14.0.1

*(Released September 24th, 2024)*

<b>Added:</b>

* &#91;Engine&#93; Update to Substance Engine 9.1.4
* &#91;Content&#93; Triangle grid: change triangulation method and use loops

<b>Fixed:</b>

* &#91;API&#93; Unloaded plugins cannot be loaded again
* &#91;Content&#93; Histogram Compute: result is 16 times what it should be
* &#91;Content&#93; Triangle Grid: pattern is not tiling properly
* &#91;Data&#93; Crash when changing graph input identifier in a specific case
* &#91;Engine&#93; Distance node produces artifacts when using very low pixel sizes
* &#91;Engine&#93; Incorrect Distance node result at 8K resolution on SSE2 engine
* &#91;Function Graph&#93; Long values appear overlapped on 'Float' nodes
* &#91;Graph&#93;&#91;Shortcuts&#93; Node created using a shortcut is not placed on existing link after node duplication
* &#91;Properties&#93; Incorrect parameter display when value is invalid

### 14.0.0

*(Released July 30th, 2024)*

<b>Added:</b>

* &#91;Content&#93; New Anisotropic Kuwahara filter
* &#91;Content&#93; New Bevel Smooth Node
* &#91;Content&#93; New Curvature Smooth v2 node
* &#91;Content&#93; New Directional Distance node
* &#91;Content&#93; New Histogram Tools: Compute, Equalize, Render
* &#91;Content&#93; New ID to Mask node
* &#91;Content&#93; New Normal Uncombine node
* &#91;Content&#93; New Palette nodes: Create, Apply, Modify, View
* &#91;Content&#93; New Quantize Color node
* &#91;Content&#93; Non-Uniform Directional Warp: Set default Intensity Map Value to 1
* &#91;Content&#93; Add 'Color' or 'Grayscale' suffix to all node labels which have these versions
* &#91;Content&#93; Deprecate "White Noise" only keep "White Noise Fast"
* &#91;Content&#93; Deprecate 'Negate Float1' node in Substance function graph
* &#91;Content&#93; Rename "Quantize Color" to "Quantize Color (Simple)"
* &#91;2D View&#93; Display values in Information panel for pixels outside of 0-1 range
* &#91;Engine&#93;&#91;Text&#93; New kerning for some fonts
* &#91;Graph&#93; Improve invalidation time when editing deep subgraphs while using in-context edition
* &#91;Linker&#93; Do not duplicate bitmaps in SBSASM
* &#91;Parameters&#93; Add a new "function" widget for all input parameter types
* &#91;Properties&#93; Improve display of inherited parameters
* &#91;UX&#93; Improve Trackpad support (Mac only)
* &#91;UX&#93; Modernize panning when reaching border of graph while selecting
* &#91;UX&#93; Remove 'Disable High DPI' functionality
* &#91;Branding&#93; New branding for Splash Screen and About window
* &#91;Gradient Map&#93; Add a way to shift all keys and loop
* &#91;Library&#93; Switch all default filters to sentence case
* &#91;API&#93; Add method to frame a specific node in the Graph View viewport
* &#91;API&#93; Add method to open a package resource in its editor (E.g., a Substance graph in the Graph View)
* &#91;API&#93; Add method to select a package resource in the Explorer (E.g., a Substance graph)
* &#91;API&#93; Add methods to get and set the graph type of a Substance compositing graph
* &#91;ThirdParty&#93; Follow 2023 VFX platforms recommendations
* &#91;ThirdParty&#93; Follow 2024 VFX platforms recommendations
* &#91;ThirdParty&#93; Update Boost to 1.82.0 + USD to 23.08
* &#91;ThirdParty&#93; Update NGL to 1.38
* &#91;ThirdParty&#93; Update OpenColorIO to 2.3.x
* &#91;ThirdParty&#93; Update OpenExr to 3.2.x
* &#91;ThirdParty&#93; Update OpenSubdiv to 3.6.x
* &#91;ThirdParty&#93; Update Python to 3.11.x
* &#91;ThirdParty&#93; Update Qt to 6.5.x
* &#91;ThirdParty&#93; Update gcc to 11.2.1
* &#91;ThirdParty&#93; Update glibc to 2.28
* &#91;ThirdParty&#93; Update libstdc++ ABI to C++11 one
* &#91;Documentation&#93; New 'Glossary' page

<b>Fixed:</b>

* &#91;Bakers&#93; Crash when rebaking a scene which filename was changed
* &#91;Bakers&#93; Crash when saving bakers preset to JSON file
* &#91;Content&#93; 'Scatter on spline': Expose Input image alpha parameter
* &#91;Content&#93; 'Tile Sampler Color': missing visibleif expression
* &#91;Content&#93; Anisotropic Noise: negative value for X/Y amount produces wrong result
* &#91;Content&#93; Anisotropic Noise: tiling issue when using odd value as X amount and no smoothness
* &#91;Content&#93; Normal Distrib function: incorrectly placed max() can lead to NaN
* &#91;Content&#93; RTAO, Bent Normal and RT Shadows do not work correctly on some platforms
* &#91;Content&#93; Shape Splatter Blend Color: OpenGL normal maps are not blended correctly
* &#91;Content&#93; Unwarranted space after 'Multi' prefix in node labels
* &#91;Dependencies&#93; Crash when moving graph within or across packages
* &#91;Engine&#93; Precision error in Warp nodes impacting the Slope Blur nodes
* &#91;Engine&#93; SBSAR layer in SD is unable to read SBSAR with SBSASM content &gt; 2GB
* &#91;Function graph&#93; Incorrect result for 0^n
* &#91;Graph&#93; 'Display node size' option is mislabelled
* &#91;Graph&#93; Crash when copying a parented comment to another graph
* &#91;Graph&#93; Freeze when alt-dragging a Dot node
* &#91;Graph&#93; Node search can miss obvious matches in some cases
* &#91;Graph&#93; Performance issue when editing a function graph instanciated multiple times with supergraph opened
* &#91;Graph&#93; Too many invalidations when creating an output
* &#91;Security&#93; ICO Parsing Out-Of-Bounds Write Vulnerability
* &#91;Security&#93; Deprecate some unused image format
* &#91;Parameters&#93; Bitmap PKG Resource Path should not be editable
* &#91;Parameters&#93; Fix issues related to exposing/batch exposing the parameter of a value processor
* &#91;Parameters&#93; String parameters are ignored when batch exposing
* &#91;Properties&#93; Performance issue when editing a function graph instanciated multiple times with properties opened
* &#91;SVG&#93; Edits to shapes are not applied in rasterised image
* &#91;UI&#93; Fix some bugs/inconsistencies with scrollable widgets (Windowss only)
* &#91;UI&#93; Inconsistent order of 3D scene file formats in import/export lists
* &#91;UI&#93; Window's actions are duplicated in the UI
* &#91;Version Control&#93; 'perforce.py' script does not work on Python 3

## Version 13

### 13.1.2

*(Released April 16th, 2024)*

<b>Added:</b>

* &#91;Graph&#93; Do not place duplicated nodes on top of the original node
* &#91;Graph&#93; Improve alignment of comments attached to nodes
* &#91;Graph&#93; Improve comments move
* &#91;Graph&#93; Snap pasted/duplicated frames and comments to the grid
* &#91;Frames&#93; Snap new frames and comments to the grid
* &#91;Content&#93; 'Curvature smooth': Add a note about tiling support in the description
* &#91;3DView&#93;&#91;IRay&#93; Allow int output to be assigned to enum parameter
* &#91;AxF&#93; Add properties about the clear coat model
* &#91;AxF&#93; Improve errors management during export
* &#91;AxF&#93; Improve GLSLFX and MDL materials for "SVBRDF" representation as stored in a AXF file
* &#91;AxF&#93; Remove 'CC No Refraction' property from 'AxF to AxF' template
* &#91;AxF&#93; Rename properties "properties.has\_xxx" to "characteristics.has\_xxx"
* &#91;AxF&#93; Update template to include all properties used by our SVBRDF shaders

<b>Fixed:</b>

* &#91;3D View&#93; Crash when resetting an Int MDL parameter mapped to an MDL enum
* &#91;3D View&#93; Incorrect widgets for SVBRDF shader properties when material is reset after changing 3D scene
* &#91;3D View&#93; Incorrect widgets for SVBRDF shader properties when no graph is applied
* &#91;3D View&#93; 'Show environment' button is disabled for new views with no default SBSSCN file
* &#91;3D View&#93; Switching from Iray to OpenGL renderer disconnects a graph output
* &#91;AxF&#93; Fresnel variant is not updated by graph output
* &#91;AxF&#93; Labels of AxF shader properties are formatted inconsistently
* &#91;AxF&#93; Warning about unchanged resources only appears in Console
* &#91;Content&#93; 'Non-Uniform' is not written consistently in all nodes
* &#91;Content&#93; Scatter on spline: Missing patterns on bridge splines
* &#91;Content&#93; Spline Mapper: Freeze when setting a negative 'Segment Amount' value
* &#91;Content&#93; 'Symmetry': Labels are missing and inconsistent
* &#91;Graph&#93; Existing comments are slightly offset
* &#91;Security&#93; RAS File Parsing Out-Of-Bounds Read Vulnerability

### 13.1.1

*(Released February 8th, 2024)*

<b>Added:</b>

* &#91;AxF&#93; Add boolean properties hasClearCoat, hasSheen etc.
* &#91;AxF&#93; Add some missing properties
* &#91;AxF&#93; Allow importing EP-SVBRDF
* &#91;AxF&#93; Rename properties "anisotropic", "fresnel" and "fresnel variant"
* &#91;AxF&#93; Update to AxF-Editing 1.0.0
* &#91;Graph&#93; Paste on mouse position if position inside Graph View
* &#91;UX&#93; Increase height of Frame and Comment's 'Description' text field
* &#91;UX&#93; Set focus on text edition fields when creating Frames, Comments or Pins

<b>Fixed:</b>

* &#91;AxF&#93; 'Specular Color' map values are incorrect when exported
* &#91;AxF&#93; Preview and textures are not displayed correctly in 'Import AxF' dialog
* &#91;AxF&#93; Property 'CC No Refraction' is not injected correctly in 'AxF to AxF' template
* &#91;Content&#93; 'Flood Fill to Position' is absent from the Library
* &#91;Content&#93; 'Splatter Circular': Negative 'Pattern Amount' values result in very long and intensive computations
* &#91;Content&#93; 'Spline Merge List': Incorrect input order
* &#91;Dependencies&#93; Dependency is remapped to its copy after being saved as a copy
* &#91;Frames&#93; 'Enable HTML markup' button is not toggled when undoing its use
* &#91;Frames&#93; Marquee-selecting a frame and its content leads to entire frame contents being moved while auto-expanding
* &#91;Graph&#93; Comments duplicated from parented comments are always placed at graph origin
* &#91;Graph&#93; Line breaking in Comment is harsher on creation
* &#91;Publish&#93; Set default path for SBSAR publishing to "My Documents" folder
* &#91;SBSAR&#93; Redoing SBSAR load makes it editable and its data can be lost

### 13.1.0

*(Released December 12th, 2023)*

<b>Added:</b>

* &#91;Frames&#93; Auto Expand
* &#91;Frames&#93; Change rules to define when an object belongs to a frame
* &#91;Frames&#93; Disable text scaling for frames description
* &#91;Frames&#93; Fit size to content
* &#91;Frames&#93; New default, hover and selected states
* &#91;Frames&#93; Snap to Large Grid
* &#91;Frames&#93; Support HTML code for Frames description
* &#91;Frames&#93; Update interaction zones
* &#91;Frames&#93; Update visual aspect
* &#91;Graph&#93; Create the node at the middle of the visible link instead of middle of the link
* &#91;Graph&#93; Display properties of an item if it is the only one item with properties available in a selection
* &#91;Graph&#93; Remove "Scaling" option for comments in the graph
* &#91;Graph&#93; Snap nodes on the main grid when doing copy/paste
* &#91;UX&#93; Allow fuzzy search in Node menu and Library search
* &#91;UX&#93; Make the Node menu list loop
* &#91;AxF&#93; Support AxF export
* &#91;AxF&#93; Disable AxF on Linux
* &#91;API&#93; Set the 'Visible if' property of graph parameters, inputs and outputs using the Python API
* &#91;API&#93; Set the order of graph I/O using the Python API
* &#91;Dependencies&#93; Update Boost to 1.80.0
* &#91;Dependencies&#93; Update OpenSubdiv to 3.5.x
* &#91;Dependencies&#93; Update gcc to 11.2.1 - Iray/MDL C++20 issue
* &#91;Dependencies&#93; Update FBX SDK to 2020.3
* &#91;Dependencies&#93; Update NGL to 1.35.0.20
* &#91;Color management&#93; Add support for OCIO ICC displays
* &#91;Levels&#93; Add a way to reset the histogram
* &#91;Python&#93; Warn users if QtForPython cannot be imported
* &#91;2D view&#93; Save the state of the view options
* &#91;3D View&#93; Add Position technique to the mesh info shader
* &#91;Export&#93; Add a 'Save settings' button to save changes to export options

<b>Fixed:</b>

* &#91;3D View&#93; Cannot assign a texture to an input of type texture\_2d of a MDL Material
* &#91;AxF&#93; Graph identifiers in templates list can be blank
* &#91;AxF&#93; Substance graph template field is blank by default
* &#91;Content&#93; Atlas Scatter: incorrect behavior in specific cases
* &#91;Content&#93; Flood Fill Mapper: blank output when all shapes have same Bbox size
* &#91;Content&#93; FloodFill to Position: Imprecision artefacts in some situations
* &#91;Content&#93; Incorrect 'Specular' output in 'BaseColor/Metallic/Roughness converter' node
* &#91;Content&#93; Mask to Path doesn't work in non square vertical
* &#91;Content&#93; Missing description for Input value, Input Grayscale, Input Color and Output nodes
* &#91;Content&#93; Missing description for Set and Sequence nodes
* &#91;Content&#93; Shape Splatter: Imprecision artefacts in 'Splatter data 2' output
* &#91;Engine&#93; Booleans in Value Processors always evaluate to 'False' (Apple Silicon only)
* &#91;Explorer&#93; Order of toolbar buttons is inconsistent between OS
* &#91;Frames&#93; Do not grab nodes when moving a frame with CTRL modifier
* &#91;Gradient Map&#93; reset all option should also reset the gradient widget
* &#91;GraphRender&#93; Some nodes are rendered black when tweaking in preview mode
* &#91;Graph&#93; 'Input value' preview is stuck to 'False' when tweaking default boolean value (Apple Silicon only)
* &#91;Graph&#93; Dot nodes close to Frame edge are not moved by the Frame
* &#91;Interoperability&#93; Resend icon is not updated after sending to Substance 3D Stager
* &#91;MDL&#93; Impossible to change Roughness in nodes where this param is available
* &#91;MDL&#93; Invalid connections in 'AxF to Metallic Roughness' template
* &#91;UI&#93; 'Export outputs' window can be minimised (Windows only)
* &#91;UI&#93; Images appear pixelated in About screen when using display scaling
* &#91;UI&#93; Node align tools in graph toolbar create multiple undo steps

### 13.0.2

*(Released July 27th, 2023)*

<b>Added:</b>

* &#91;Function graph&#93; Add $getPhysicalSize system variable
* &#91;Home Screen&#93; Support opening SBS files by drag and drop
* &#91;Content&#93; Spline Mapper/Spline Flow Mapper : Add 'Non-Square Correction' parameter

<b>Fixed:</b>

* &#91;Home Screen&#93; Do not display Home Screen when a file is sent from another software
* &#91;Home Screen&#93; Wrong status for Designer icon in the Windows toolbar
* &#91;Content&#93; Atlas Splitter: Description is incorrect
* &#91;Content&#93; Incorrect reference value in 'Linear to sRGB (luminance)' function
* &#91;Content&#93; Numbers display tool does not support non-square resolutions
* &#91;Content&#93; Point List: 'Point number' parameter has incorrect minimum value
* &#91;Content&#93; Shape Drop Shadow: Shadow can disappear when tiling is disabled
* &#91;Content&#93; Spline (Poly Quadratic): Incorrect preview tangents and thickness in non-corrected non-square resolutions
* &#91;Content&#93; Spline (Poly Quadratic): Points labels are not hidden when using connect start/end options
* &#91;Content&#93; Spline Bridge (List): 'Non-Square Correction' parameter has no effect
* &#91;Content&#93; Spline Cubic: Non-Square Correction parameter has no effect on Preview output
* &#91;Content&#93; Spline Mapper: Incorrect render when the spline has a very small thickness
* &#91;Content&#93; Spline nodes: Inverted alpha sign description in Spline Coords tooltip
* &#91;Content&#93; Spline nodes: 'Non-Square Correction' parameter has no effect on Preview output
* &#91;Content&#93; Spline Render: Output format is absolute 32F
* &#91;Content&#93; Spline Render: Output is clamped in &#91;0, 1&#93; range
* &#91;Content&#93; Spline Sample Thickness: Spline can be subtracted into negative values
* &#91;Content&#93; Spline Select: Splines are closed with a single segment by default
* &#91;Crash&#93;&#91;Cooker&#93; Crash when loading specific graphs
* &#91;Crash&#93;&#91;UI&#93; Crash when enabling menus after loading package from Home Screen
* &#91;API&#93; 'User documentation' link in scripting reference is outdated
* &#91;Properties&#93; Value processor function can't be opened on a locked graph
* &#91;Publish&#93; Cannot publish packages containing MDL graphs
* &#91;UI&#93; 'Manage My Account...' option is disabled in Help menu
* &#91;UI&#93; Missing entries in Help menu when opening Designer through a file

### 13.0.1

*(Released June 27th, 2023)*

<b>Added:</b>

* &#91;Content&#93; Spline (Poly Quadratic), Point List: add name of points in the Preview output
* &#91;Content&#93; Spline Mapper: add a parameter to offset the cylinder profile center
* &#91;DotNode&#93; Sort the list of input portals alphabetically

<b>Fixed:</b>

* &#91;Content&#93; Incorrect result in several Spline nodes when using uniform distribution
* &#91;Content&#93; Minor errors in Spline &amp; Path nodes' tooltips
* &#91;Content&#93; Quad Transform on Path: p01 and p10 default values are switched
* &#91;Content&#93; Quad Transform: result is incorrect in a specific situation
* &#91;Content&#93; Spline Circle: 'Flip direction' result is incorrect when not using Uniform distribution
* &#91;Content&#93; Spline Circle: tangents are incorrect when adjusting the spiral and size parameters
* &#91;Content&#93; Spline Flow Mapper: black streaks in result when using high spiral power in Spline Circle
* &#91;Content&#93; Spline Mapper / UV Mapper: background Color does not work
* &#91;Content&#93; Spline Mapper: base height is 0, resulting in clipping
* &#91;Content&#93; Spline Mapper: spline height is modified by input multiplier even when that input is not connected
* &#91;Content&#93; Spline Mapper: splines extremities meeting an image edge are not mapped
* &#91;Content&#93; Spline Mapper: UV Scale Y has no effect when using non-Plane shape
* &#91;Content&#93; Spline Mapper: Z-fighting when rendering overlapping splines of same height
* &#91;Content&#93; Spline Poly Quadratic: 'Flip direction' result is incorrect when not using Uniform distribution
* &#91;Content&#93; Spline Render: joints are not handled consistently across Spline Style options
* &#91;Content&#93; Spline Render: last segment is not drawn
* &#91;Content&#93; Spline Render: non-square correction is not applied correctly
* &#91;Content&#93; UV Mapper color appears twice in Library
* &#91;DotNode&#93; Connection snapping area is not updated after disabling text scaling limit
* &#91;DotNode&#93; Creation via contextual menu is broken
* &#91;DotNode&#93; Input portal name position is not adjusted after undoing/redoing a name change
* &#91;GraphRender&#93; Too many invalidations when modifying a function graph
* &#91;Graph&#93; Transformation widget position is not visually updated correctly
* &#91;Localization&#93; 'Soft range' and 'Hard range' are not localized in MDL graphs
* &#91;Parameters&#93; Consecutive text changes are not logged in history stack
* &#91;Parameters&#93; Hitbox for moving graph input parameters in the list is unreliable
* &#91;Properties&#93; Simple click is considered as double on spin-box widget on heavy projects
* &#91;Publish&#93; Order of resources in package is not preserved in published asset

### 13.0.0

*(Released June 6th, 2023)*

<b>Added:</b>

* &#91;Graph&#93; Portal node
* &#91;Onboarding&#93; New Home Screen
* &#91;Content&#93; Spline (Cubic) node
* &#91;Content&#93; Spline (Poly Quadratic) node
* &#91;Content&#93; Spline Circle node
* &#91;Content&#93; Point List node
* &#91;Content&#93; Spline Bridge (2 splines) node
* &#91;Content&#93; Spline Bridge (List) node
* &#91;Content&#93; Spline Append node
* &#91;Content&#93; Spline Select node
* &#91;Content&#93; Spline Merge List node
* &#91;Content&#93; Spline 2D Transform node
* &#91;Content&#93; Spline Warp node
* &#91;Content&#93; Spline Sample Height node
* &#91;Content&#93; Spline Sample Thickness node
* &#91;Content&#93; Spline Render node
* &#91;Content&#93; Scatter on Spline Color node
* &#91;Content&#93; Scatter on Spline Grayscale node
* &#91;Content&#93; Spline Mapper Color node
* &#91;Content&#93; Spline Mapper Grayscale node
* &#91;Content&#93; Spline Bridge Mapper Color node
* &#91;Content&#93; Spline Bridge Mapper Grayscale node
* &#91;Content&#93; Spline Flow Mapper node
* &#91;Content&#93; UV Mapper Color node
* &#91;Content&#93; UV Mapper Grayscale node
* &#91;Content&#93; Paths to Splines node
* &#91;Content&#93; Masks to Paths node
* &#91;Content&#93; Paths 2D Transform nodenode
* &#91;Content&#93; Paths Polygon node
* &#91;Content&#93; Preview Paths node
* &#91;Content&#93; Paths Warp node
* &#91;Content&#93; Paths Select node
* &#91;Content&#93; Paths Vertex Processor node
* &#91;Content&#93; Paths Vertex Processor Simple node
* &#91;Content&#93; Quad Transform on Path node
* &#91;Content&#93; Raytraced Ambient Occlusion v2
* &#91;Content&#93; Raytraced Bent Normal v2
* &#91;Content&#93; Raytraced Shadows v2
* &#91;Engine&#93; Update to version 9
* &#91;Engine&#93; Loop node in function graphs
* &#91;Engine&#93; Add solid mode to Gradient
* &#91;Engine&#93; Atomic pow() node in Function Graph
* &#91;Engine&#93; Add border wrapping options (clamp to edge / repeat) in Sampler node
* &#91;Engine&#93; Nearest sampling in Warp and Directional Warp node
* &#91;Engine&#93; Add a "punchthrough alpha" mode to the Sharpen filter for color inputs
* &#91;Engine&#93; FxMap: Hemisphere morphlet
* &#91;Engine&#93; Atomic Get/Set operations in function graphs
* &#91;Engine&#93; Functions: use precise function of log/log2/exp, 2pow - Unify functions between cooker and engine
* &#91;Engine&#93; Add an "intensity offset" parameter to the Directional Warp filter
* &#91;API&#93; Support preset management for compositing graphs
* &#91;Functions&#93; Change input name for functions atomic nodes
* &#91;Localization&#93; Add Portuguese (Brazil), Italian (Italy) and Spanish (Spain) languages
* &#91;Localization&#93; Respect rule "Language (Country)" in the list of languages
* &#91;Presets&#93; Disable 'Preview' and 'Presets' panels in graph properties when using in-context editing
* &#91;Substance models graph&#93; End of support of Substance models graphs

<b>Fixed:</b>

* &#91;3D View&#93; Display of long strings in scene statistics is cut off (macOS only)
* &#91;API&#93; 'structure::Structure' module is still included in the API reference
* &#91;API&#93; Dot nodes in MDL graphs have no definition nor properties
* &#91;API&#93; Incorrect behavior when setting the parameter of function nodes
* &#91;Content&#93; 3D Voronoi and 3D Voronoi Fractal nodes generate a cooking warning
* &#91;Engine&#93; 'Intensity Map Offset' parameter has no effect on grayscale data in SSE2 engine
* &#91;Explorer&#93; Graph i/o can be deleted
* &#91;Graph&#93; Bitmap is ignored when used in instances
* &#91;Graph&#93; Incorrect dot node position when created node from a node
* &#91;Graph&#93; Incorrect focus in 'Expose parameter' dialog when using 'Enter' key
* &#91;Graph&#93; Wrong result in histogram scan with bitmap in context editing
* &#91;Localization&#93; Fix various clipping issues
* &#91;Parameters&#93; Crash when deleting an input parameter
* &#91;Publish&#93; Graphs in folders are moved to root in published package
* &#91;Resources&#93; Crash when updating a loaded resource on disk
* &#91;VisibleIf&#93; Fix regression in conditional visibility evaluation

## Version 12

### 12.4.1

*(Released: March 30, 2023)*

**Added:**

* &#91;Cooker&#93;&#91;Graph&#93; Take in account EXIF transformation tags in JPEG file
* &#91;Security&#93; Upgrade to USD 23.02
* &#91;Security&#93; Remove the support of file format import Collada (.dae)
* &#91;Substance models&#93; Warning about the end of life of Substance model graphs in the next major version

**Fixed:**

* &#91;3D View&#93;&#91;ASM&#93; Coating roughness artefact when using a CoatNormal
* &#91;Content&#93; 'Gradient Filled Cells' parameter of Alveolus node is inverted
* &#91;Content&#93; Input Number of Multi-Switch nodes is not clamped
* &#91;Content&#93; Cooking warning in Scratches Generator Normal node
* &#91;Data&#93; Crash when loading package manually after undoing its previous load
* &#91;Data&#93; Crash when quickly undoing a multiple graph operations up to the package load

### 12.4.0

*(Released: January 31, 2023)*

**Added:**

* &#91;3D View&#93; Add all options in Display menu as toolbar buttons
* &#91;API&#93; Allow adding actions to graph view toolbars
* &#91;API&#93; Allow to create/edit/evaluate a Substance model graph from the API
* &#91;Color management&#93; Improve quality of baked 3D LUTs in ACE mode
* &#91;Documentation&#93; Sample projects for Substance compositing graphs
* &#91;Documentation&#93; Sample project for function graphs
* &#91;Explorer&#93; Allow moving Graph and Resources from one parent to another without closing or invalidating widgets
* &#91;Gradient Editor&#93; Select clicked pin when displaying the gradient editor
* &#91;Graph&#93; Add option in a node's contextual menu to select all its children
* &#91;Graph&#93; Clean graph tool to detect and remove unused nodes in all graphs types and property graphs
* &#91;Graph&#93; Transform image input to color/greyscale
* &#91;Parameters&#93; Add a lock on integer2 widgets
* &#91;Parameters&#93; Allow to type basic formulas as a parameter
* &#91;Substance model&#93; Toggle to switch between values and icons for value nodes
* &#91;UI&#93; Button to generate a random value when a random seed is required
* &#91;UI&#93; Focused item is not highlighted in Scene browser
* &#91;UX&#93; Reset slider ranges when their value is reset

**Fixed:**

* &#91;API&#93; SDProperty.getDefaultValue() almost always returns None
* &#91;3D View&#93; 'DirectX Normal' property value is not shared across renderers
* &#91;3D View&#93; Scene statistics display is stretched when viewport is small
* &#91;3D View&#93; Wireframe display property is not saved
* &#91;Content&#93; Radial Blur Color parameters have no effect on the alpha channel
* &#91;Localization&#93; Additional sliders and buttons are displayed in Enviroment OpenGL Properties.
* &#91;MDL&#93;&#91;Substance model&#93; Crash when deleting exposed nodes
* &#91;Preferences&#93; Default\_config file is never recreated if deleted
* &#91;Substance model&#93; Crash reordering parameter that doesn't appears at instance level

### 12.3.1

*(Released: November 24, 2022)*

**Added:**

* &#91;3DView&#93; Optimized rendering for scenes with many materials
* &#91;3DView&#93; View a Substance model graph's outputs when dropping it from Explorer
* &#91;License&#93; Clean legacy system for Linux users
* &#91;Onboarding&#93; Update background transparency
* &#91;Substance models&#93; Display warning in Graph View when input and output share the same identifier

**Fixed:**

* &#91;3D Assets&#93; 'Help &gt; Substance 3D assets' mistakenly targets Creative Cloud Desktop on Linux
* &#91;3D View&#93; Materials are not built when mesh is loaded
* &#91;3D View&#93; Materials list opens when dropping Substance model graph in viewport
* &#91;Explorer&#93; Cannot delete selection with keyboard if a Substance model graph is included
* &#91;Explorer&#93; Crash when opening the contextual menu of a mesh resource's material item on Mac
* &#91;Graph&#93; Instances whose Input images depends on Values generates wrong result in subsequent nodes
* &#91;Graph&#93; Wrong result when using chain of subgraphs with contextual graph editing enabled
* &#91;MDL&#93; Crash when loading MDL graph referencing a compositing graph with outdated outputs
* &#91;MDL&#93; Texture 2D node does not work anymore
* &#91;Onboarding&#93; Cropped and unlocalized texts
* &#91;Onboarding&#93; Panels are not correctly displayed when launching the app via opening a file
* &#91;Preferences&#93; Image cache ignores the temporary files location set by the user
* &#91;Properties&#93; Tweak performed in preview/preset panels are merged in undo stack
* &#91;Shortcut&#93; Shortcut assigned on deprecated nodes create conflicts and can't be cleaned
* &#91;Substance models&#93; Crash when closing a package after performing specific actions
* &#91;Substance models&#93; Instance nodes and links from relocated packages are not refreshed correctly
* &#91;Substance models&#93; Undoing deletion of subgraphs does not refresh instance nodes and links consistently
* &#91;Substance models&#93; Value suddenly increases too fast on transform node
* &#91;UI&#93; "Visible if" property warning icons does not have a tooltip
* &#91;UI&#93; Image information text is too dark in 2D View's viewport
* &#91;Undo&#93; Moving a position widget in preview mode stores all intermediate values

### 12.3.0

*(Released: October 06, 2022)*

**Added:**

* &#91;General&#93; Onboarding panel to welcome new users
* &#91;General&#93; What's new panel to improve new features discoverability
* &#91;Substance model&#93; Support of sub graphs and instances
* &#91;Substance model&#93; Support Visible If for exposed parameters
* &#91;Substance model&#93; Add support of Output nodes
* &#91;Substance model&#93; Curve offset node
* &#91;Substance model&#93; Curve revert node
* &#91;Substance model&#93; Curve smoothing node
* &#91;Substance model&#93; Curve subdivide node
* &#91;Substance model&#93; Graft node
* &#91;Substance model&#93; Update "Filter Scene" node
* &#91;Substance model&#93; Make non-atomic nodes discoverable in Node menu
* &#91;Substance model&#93; Add the action "Open Reference" in the contextual menu of an instance node
* &#91;Substance model&#93; Add a "View in 3DView" action in the contextual menu of nodes that can be sent to the 3DView
* &#91;Substance model&#93; Automatically display a node's properties after exposing it
* &#91;Substance model&#93; Create 'New Substance model graph' window with templates list
* &#91;UI&#93; Improve consistency of image saving options in 2D View and 3D View
* &#91;UI&#93; Rename 'Link &gt; 3D Mesh' to 'Link &gt; 3D Scene' in Explorer's contextual menu
* &#91;UI&#93; Reset layout now apply to all floating windows
* &#91;UI&#93; Use 'View outputs in 3D View' label in contextual menus for graphs
* &#91;Library&#93; Support non-atomic Substance model graphs
* &#91;SBSAR&#93; Support graph outputs' description in the SBSAR
* &#91;Shader&#93; Set the default Tessellation Factor value to 1 for all shaders
* &#91;UI&#93; Expose 2-buttons widget for boolean parameters
* &#91;Engine&#93; Update to Version 8.6.4
* &#91;Steam&#93; Optimized build for Apple Silicon chipset (Apple M1 / M2)

**Fixed:**

* &#91;UI&#93; Resolve scaling issues for high-DPI screens
* &#91;UI&#93; '$(udim)' template missing from list in baking window
* &#91;UI&#93; Crash when displaying the Node menu on the screen's right border (macOS only)
* &#91;UI&#93; Extension button in 3D view menu is not visible
* &#91;UI&#93; Graph toolbar's extension menu is incomplete
* &#91;UI&#93; Incorrect parameter widget value after undoing hard range activation
* &#91;3D view&#93; Non default shader setting is lost on Iray from a session to another
* &#91;Bakers&#93; Crash when loading baking window with a scene without meshes
* &#91;Function&#93; Crash when copying an instance into its referenced graph
* &#91;Function&#93; Fix possible crash when manipulating nodes
* &#91;Globalization&#93; Italic is not always correctly disabled in japanese/korean/chinese
* &#91;Graph&#93; Incorrect fallback identifier for new MDL and Substance model graphs
* &#91;Graph&#93; Inherited parameters driven by values are sometimes computed incorrectly
* &#91;GraphRender&#93; Crash when switching engines while computing high resolution graph (macOS only)

### 12.2.1

*(Released: August 04, 2022)*

**Fixed:**

* &#91;Graph&#93; Wrong results when changing the parent size of the graph
* &#91;Crash&#93; Crash when computing Substance compositing graph at very high resolution
* &#91;Crash&#93; Crash when running out of memory while loading package
* &#91;Crash&#93; Crash when using bracket in exposed parameter's annotations in a Substance model graph
* &#91;Crash&#93; Improve stability of rendering Substance compositing graphs
* &#91;Iray&#93; Update to version 2021.1.6

### 12.2.0

*(Released: July 19, 2022)*

**Added:**

* &#91;Apple&#93; Native Apple silicon (M1) support (Creative Cloud version only)
* &#91;Substance model graph&#93; Display node tooltips in Graph View
* &#91;Substance model graph&#93; Display node tooltips in Library
* &#91;Substance model graph&#93; Add a contextual menu entry to preview nodes
* &#91;Substance model graph&#93; Allow user to create shortcuts for nodes creation
* &#91;UI&#93; Add "View output in 2D View" option in compositing graph's contextual menu
* &#91;UI&#93; Split the "Automatic display of outputs" setting into 2D View/3D View specific settings
* &#91;UI&#93; Add dropdown arrow and tooltip to "View output" button in 2D View toolbar
* &#91;UI&#93; Reword and reorder items in Explorer's Information panel
* &#91;Color Management&#93; Add "Linear Adobe RGB (1998)" and "Adobe RGB (1998)" export color spaces for Adobe ACE
* &#91;Color Management&#93; Add "Linear Adobe RGB (1998)" working color space for Adobe ACE
* &#91;Color management&#93; Add suport for OCIO ICC displays
* &#91;Color Management&#93; Hide Adobe RGB working color space from ACE preferences
* &#91;Color management&#93; Improve quality of baked 3D LUTs in ACE mode
* &#91;Color Management&#93; Use new GPU backend in 3D viewer
* &#91;Localization&#93; Full update of Korean language
* &#91;Engine&#93; Update to version 8.6.0
* &#91;Graph&#93; Assign a default graph identifier when that property is left blank
* &#91;Library&#93; Disable tooltip hyperlinks for non-instance nodes
* &#91;NewProject&#93; Update default resolution
* &#91;Templates&#93; Add CLO template
* &#91;API&#93; Expose the defaultParentSize property for SDSBSCompGraph objects
* &#91;Dependencies&#93; Update Alembic to version 1.8.3
* &#91;Dependencies&#93; Update AXF to version 1.9.0
* &#91;Dependencies&#93; Update Boost to version 1.76
* &#91;Dependencies&#93; Update FBX to version 2020.2.1
* &#91;Dependencies&#93; Update IRay to version 2021.1.0
* &#91;Dependencies&#93; Update OpenColorIO to version 2.1.1
* &#91;Dependencies&#93; Update OpenEXR to version 3.1.5
* &#91;Dependencies&#93; Update TBB to version 2020.3
* &#91;Dependencies&#93; Update USD to version 0.22.3
* &#91;Remove&#93; Disable the post effects feature (Yebis)
* &#91;Remove&#93; Remove "Save render to Artstation" command from the 3D View menu

**Fixed:**

* &#91;Substance models&#93; Hard range set on exposed parameter is saved when unexposing
* &#91;Substance models&#93; Identifier is not user friendly on constant nodes
* &#91;Substance models&#93; Improve search based on node compatibility
* &#91;UI&#93; 'New' submenu order is incorrect for Folder resources
* &#91;UI&#93; Default size of main window is very small
* &#91;UI&#93; Toolbars are not affected by 'Reset layout' option
* &#91;UI&#93; Visible transparency grid on font resource icon in Explorer
* &#91;Cooker&#93; Compositing graphs instanced in MDL graph are always entirely recooked
* &#91;Graph&#93; Crash when pasting a node copied from a graph with blank identifier
* &#91;MDL&#93; Crash when closing a specific MDL graph
* &#91;Performances&#93; Application is unresponsive when loading very large packages
* &#91;Resources&#93; 3D Scene resource can be imported in a specific case

### 12.1.1

*(Released: June 07, 2022)*

**Fixed:**

* &#91;Content&#93; "bluenoise\_256" resource has a defined "colorspace" attribute in some nodes
* &#91;Content&#93; "Get size" nodes do not appear in Library and grayscale version is mislabeled
* &#91;Content&#93; "Random Color Seed" parameter in 2D Voronoi nodes has no effect
* &#91;SBSRender&#93; Exporting a graph to EXR do not generate the same bpc as Designer
* &#91;Substance models&#93; "Gamma type" should not appear in exposed parameter's properties
* &#91;Substance models&#93; Crash when using bracket in exposed parameter's annotations

### 12.1.0

*(Released: April 26, 2022)*

**Added:**

* &#91;Main&#93; New Content for material graphs
* &#91;Main&#93; Send Materials to Stager
* &#91;Main&#93; Support of USD files
* &#91;Main&#93; Improve the error reporting in the UI
* &#91;Main&#93; Scene Management nodes for model graphs
* &#91;Content&#93; Add more options to 3D Perlin Noises (tiling, absolute...)
* &#91;Content&#93; New 3D Ridged Noise Fractal node
* &#91;Content&#93; New 3D Texture Offset node
* &#91;Content&#93; New 3D Texture Position node
* &#91;Content&#93; New 3D Texture Render Surface node
* &#91;Content&#93; New 3D Texture Render Volume node
* &#91;Content&#93; New 3D Texture Signed Distance Field node
* &#91;Content&#93; New Auto Crop node
* &#91;Content&#93; New Easing functions
* &#91;Content&#93; New Extend Shape nodes
* &#91;Content&#93; New Grunge Maps
* &#91;Content&#93; New Non-Uniform Rotation node
* &#91;Content&#93; New Summed Area Table filter
* &#91;Content&#93; New Tile Random 2 generator
* &#91;Content&#93; New Triangle Grid pattern generator
* &#91;Content&#93; New version of the Quantize Grayscale node
* &#91;Content&#93; New Voronoi and Voronoi Fractal Noises (2D/3D)
* &#91;Content&#93; Threshold: add 'Lower' and 'Lower and equal' comparison mode
* &#91;Content&#93;&#91;3D View&#93; Add a mesh fit for displaying fabrics to the shipped resources
* &#91;Substance models&#93; New Expand Group Instances node
* &#91;Substance models&#93; New Fuse node
* &#91;Substance models&#93; New Rename node
* &#91;Substance models&#93; New Reparent node
* &#91;Substance models&#93; New Set Pivot node
* &#91;Substance models&#93; Update to SDK 1.6.0
* &#91;UI&#93; Improve Node menu behavior when misclicking
* &#91;UI&#93; Open subgraphs in the same tab even if pinned
* &#91;UI&#93; Remove Pin button from Explorer panel's title bar
* &#91;UI&#93; Save "Do not display again" option on Welcome screen across versions
* &#91;ThirdParty&#93; Upgrade Qt (and QtForPython) to 5.15.8
* &#91;ThirdParty&#93; Upgrade Python to 3.9.9
* &#91;ThirdParty&#93; Upgrade OpenSSL to 1.1.1m
* &#91;3D View&#93; Display the Grid unit in the viewport when the "Axis" helper is enabled
* &#91;Automation&#93; Provide sbsbaker command line tool with Designer
* &#91;Color Management&#93; Implement new GPU backend for Adobe ACE
* &#91;Cooker&#93; Add an option to cook a package without a timestamp
* &#91;Graph&#93; Add badges in the FxMap graph
* &#91;Library&#93; Add new filter for Easings functions
* &#91;Player&#93; USD support
* &#91;Properties&#93; Add a warning error on the "PKG Resource Path" parameter of a Bitmap node when the resource is not found
* &#91;Substance Engine&#93; Upgrade to 8.4.1
* &#91;Yebis&#93; Warn the user that Yebis post effects will be removed in the next version
* &#91;Documentation&#93; New "Warnings and errors" page
* &#91;Documentation&#93; New page describing inheritance in Substance compositing graphs
* &#91;Documentation&#93; Update 'Iray' section
* &#91;Documentation&#93; Update 'MDL graphs' section

**Fixed:**

* &#91;UI&#93; Clipping issues in templates tooltips in the new graph window
* &#91;UI&#93; Hard to read white text in nodes when using Dark Mode in macOS
* &#91;UI&#93; Layout issue in some dialog boxes
* &#91;UI&#93; Warning message is appearing truncated while creating Substance function graph in Explorer.
* &#91;UX&#93; Color picker is moving downward on each new opening
* &#91;UX&#93; Gradient editor window moves up each time it is spawned
* &#91;UX&#93; Graph properties are not automatically displayed for loaded packages
* &#91;Content&#93; Flood Fill Mapper: Incorrect input selection in a specific case
* &#91;Content&#93; Flood Fill: Text bleed in boolean parameters' buttons
* &#91;Content&#93; Incorrect range for Multi-Angle to Normal node's First Sample Light Angle parameter
* &#91;Substance models&#93; Properties of node shows identifier instead of label
* &#91;Substance models&#93;&#91;3D view&#93; Refresh problem when reopening a project
* &#91;Substance models&#93;&#91;3Dview&#93; Refresh issue when using wireframe preview
* &#91;Parameters&#93; Crash when deleting graph inputs in quick succession in a specific case
* &#91;Parameters&#93; Crash when resetting an instance parameter while editing its reference description
* &#91;Bitmap&#93; UDIM detection is not triggered for bitmap files dropped in graph
* &#91;Graph&#93; Bitmap/SVG nodes are not invalidated when resource is modified on disk after loading the package
* &#91;GraphRender&#93; Memory leak when Substance graph evaluation get cancelled
* &#91;Localization&#93; String "Rebake all maps for this resource" is appearing unlocalised
* &#91;MDL&#93; Exposed parameter initialised to 0 if input is connected to unconnected Dot node
* &#91;Preferences&#93; Tooltips are displayed even when the cursor is in an empty space
* &#91;Properties&#93; Undoing a color space value change sets the default value instead in a specific case
* &#91;Text&#93; Cannot Undo font switch to missing font resource

## Version 11

### 11.3.3

*(Released: February 01, 2022)*

**Fixed:**

* &#91;Substance models&#93; Ranges can be lost in some cases
* &#91;Substance models&#93;&#91;Export&#93; Scale is different depending of the file type
* &#91;Substance models&#93;&#91;Export&#93; Meshes are duplicated

### 11.3.2

*(Released: January 25, 2022)*

**Added:**

* &#91;Documentation&#93; Update 'Iray' section

**Fixed:**

* &#91;Substance models&#93; Can't publish package that contains Substance models graphs
* &#91;Substance models&#93; Impossible to export a model graph in some specific cases
* &#91;Substance models&#93; Make parameters ranges more coherent
* &#91;MDL&#93; Crash when exporting MDLE file
* &#91;MDL&#93; Wrong .mdl file generated when a MDL graph contains Dot nodes connected to Exposed parameters
* &#91;2D View&#93; Optimize display of painting tools
* &#91;Content&#93; Inconsistent Output size parameter setup in template's source graphs
* &#91;Properties&#93; Labels of Soft/Hard ranges are wrong in the Property Panel for MDL and Substance models exposed nodes
* &#91;Templates&#93; Update default values of inputs in 'Sampler filter' template

### 11.3.1

*(Released: December 13, 2021)*

**Added:**

* &#91;Graph&#93; Add a warning when deleting a graph used in another graph/package

**Fixed:**

* &#91;UI&#93; Color editor is too small when using a specific UI layout
* &#91;UI&#93; Crash when updating the list of recently used templates
* &#91;UI&#93; Incorrect highlighting in Shortcuts preferences
* &#91;UI&#93; Main window size is too small after restarting a windowed session (macOS only)
* &#91;UI&#93; Maximised dock is not minimised on exit (Windows only)
* &#91;UI&#93; Missing space in 'Level Out High' parameter tooltip&#91;3DView&#93; Axis in 3D view are too small when the scene bounding box is thin
* &#91;UI&#93; Style issue on some text in Project settings for French language
* &#91;Substance models&#93; Clamp on exposed parameters are not saved across sessions
* &#91;Substance models&#93; Shift modifier is still enabled after using node preview shortcut
* &#91;Substance models&#93; Some deleted nodes remain in the exported SBSM
* &#91;Substance models&#93; Target nodes of the evaluation accumulate and are not deleted&#91;API&#93; Crash when rendering Curve node which properties were set through API
* &#91;Bakers&#93; 'Material color' widget is not visible and does not work as expected
* &#91;Content&#93; PBR Render Node: internal computation not performed at the node's resolution
* &#91;Function Graph&#93; Messages displaying the expected types are wrong in some cases
* &#91;Graph&#93; Input relative to input: inherited parameters are incorrect with connected instances
* &#91;MDL&#93; Substance graph instances are not reliably updated in MDL graphs
* &#91;Publish&#93; Fail publishing graph that contains circular dependencies
* &#91;Shortcuts&#93; Shift+Space should not be an assignable keyboard shortcut for nodes
* &#91;Templates&#93; Output format of custom templates is ignored

### 11.3.0

*(Released: November 24, 2021)*

**Added:**

* &#91;Substance models&#93; Add tooltips for nodes parameters
* &#91;Substance models&#93; Allow to display in overlay in the 3D viewport the result of an intermediate node
* &#91;Substance models&#93; Improve how Basis are displayed
* &#91;Substance models&#93; Preserve the objects' hierarchy when exporting a Substance Model graph to .fbx
* &#91;Substance models&#93; Support multiple materials in FBX/OBJ export from Substance Model graph
* &#91;Substance models&#93;&#91;Content&#93; Particle node
* &#91;Substance models&#93;&#91;Content&#93; Generative Transform node
* &#91;Substance models&#93;&#91;Content&#93; Organic Pattern node
* &#91;Substance models&#93;&#91;Content&#93; Particles from Instances node
* &#91;Substance models&#93;&#91;Content&#93; Particle Pruning node
* &#91;Substance models&#93;&#91;Content&#93; Lathe node
* &#91;Substance models&#93;&#91;Content&#93; Shell node
* &#91;Substance models&#93;&#91;Content&#93; Projection node
* &#91;Substance models&#93;&#91;Content&#93; Curve Trim node
* &#91;Substance models&#93;&#91;Content&#93; Update Curve Sampler node
* &#91;Substance models&#93;&#91;Content&#93; Update Mesh Sampler node
* &#91;Substance models&#93;&#91;Content&#93; Update Jitter node
* &#91;UX&#93; Button to maximize current view
* &#91;UX&#93; Update the New Graph window
* &#91;UX&#93; Add 'Download Player' option in Tools menu and aggregate with 'Locate Player'
* &#91;UX&#93; Add 'Close All' entry to the file menu
* &#91;UX&#93; Apply consistent casing throughout the main menu
* &#91;UX&#93; Automatically display the properties of duplicated graph items
* &#91;UX&#93; Add buttons in the graph toolbar to disable constant screen size for Frame titles / Comments / Pins
* &#91;UX&#93; Buttons to copy versions information to the clipboard in the About dialog
* &#91;Materials&#93; Inputs relative to inputs
* &#91;Content&#93; Add 'Tiling' option on 3D Perlin Noises
* &#91;Content&#93; New Diffusion process node
* &#91;Content&#93; New PBR Render node version
* &#91;Interoperability&#93; Receive SBS and SBSAR from Sampler
* &#91;Interoperability&#93; Send SBSM To Stager
* &#91;3D View&#93; Add an option to disable backface culling
* &#91;3D View&#93; Add an option to display Vertex tangent space
* &#91;Explorer&#93; Highlight graph in the Explorer when double clicking the Graph View's background
* &#91;Explorer&#93; Remove the 'Explore' option in contextual menus
* &#91;Bakers&#93; Hide deprecated bakers
* &#91;Color Management&#93; Add support for OCIO v2 config file rules
* &#91;Library&#93; Rename categories according to graph types
* &#91;Preferences&#93; Auto-disable the CPU in Iray hardware preferences if supported CUDA GPU is detected

**Fixed:**

* &#91;Substance models&#93; Crash on Mac when using "as sudb" option on .fbx
* &#91;Substance models&#93; Crash when exporting to SBSM in a specific case
* &#91;Substance models&#93; Export failure when exporting exposed parameters which widgets were never built
* &#91;Substance models&#93; Random crash when opening a graph that refers to multiple .fbx files
* &#91;Substance models&#93; Ranges are not applied dynamically in exposed parameters' widgets
* &#91;Substance models&#93; Reload mesh option doesn't work on resources used in Substance models graph
* &#91;Substance models&#93; Scenes are not displayed in an available 3D View in a specific case
* &#91;UI&#93; Disable area is too large in material options
* &#91;UI&#93; Style issue in 'Package File not Saved' dialog
* &#91;UI&#93; Tab key has to be pressed twice to navigate across values
* &#91;UI&#93; Zooming with mouse drag is inversed between 3D View and other Viewports
* &#91;UI&#93; Loading an already open SBS using the 'Recent files' list incorrectly triggers a 'Package Not Found' prompt
* &#91;UI&#93;&#91;macOS&#93; Incorrect default interface layout after starting the application
* &#91;UI&#93; Packages cannot be saved to a drive's root (Windows only)
* &#91;Graph&#93; 'Automatically display in 2D View' option is inconsistent in a specific case
* &#91;Graph&#93; 'Open Reference' option is available for SBSAR instance nodes
* &#91;Graph&#93; Pin properties are only displayed when item is created
* &#91;Graph&#93; Pin string rules are inconsistently enforced
* &#91;Graph&#93; Crash when saving an empty graph
* &#91;3D View&#93; Anisotropy angle is inverted in ASM shader
* &#91;3D View&#93; ASM Shader: linearization issues with SSS related maps
* &#91;3D View&#93; Broken OpenGL rendering after closing additional 3D Views in a specific case
* &#91;3D View&#93; The predefined cameras positions are not correct in the 3D View with some .fbx files
* &#91;MDL&#93; 'Add Node' from the contextual menu is not working for MDL Graphs
* &#91;MDL&#93; Bug: Connection of node fails when using float2.x components and alike (SD 11.1.2)
* &#91;MDL&#93; Crash upon opening specific.sbs file
* &#91;MDL&#93; Scene units per meter in Iray not set at render session start
* &#91;MDL&#93; Freezes when tweaking a lerp node in the MDL graph
* &#91;MDL&#93; Order of parameters in exported MDL code
* &#91;Explorer&#93; empty resource folder is created after canceling resource creation
* &#91;Explorer&#93; Only the first element of a package can be moved to the bottom of the list
* &#91;Content&#93; RT Bent Normal and RT AO triggers node computation in nested graphs
* &#91;Input Node&#93; Bitmap in Input Nodes is not updated when UDIM change
* &#91;Iray&#93; Long time is taken when trying to display a Substance models Scene with lots of instances
* &#91;Preferences&#93; Empty line when cancelling the addition of a project file
* &#91;Python editor&#93; 'Close' option stays enabled after closing last script and still includes its name æ

### 11.2.2

*(Released: September 28, 2021)*

**Added:**

* &#91;Properties&#93; Add new graph types for Decals, Atlases, Environment lights and Light textures

**Fixed:**

* &#91;UI&#93; Incorrect interface layout after starting the application
* &#91;Stability&#93; Fix crashes when going out of sleep mode on Windows and when plugging/unplugging screens
* &#91;3D View&#93; Creating a 3D Scene resource from Substance model graph Scene has no effect
* &#91;Blend&#93; Enum values are missing when exposing blending mode
* &#91;Export&#93; Scene export of Substance models results in duplicated geometry
* &#91;MDL&#93; Crash when opening a specific SBS file
* &#91;Mesh&#93; Crash when linking specific mesh with flawed geometry
* &#91;Substance models&#93; Export fails when exposed parameter's default value is out of soft range

### 11.2.1

*(Released: July 27, 2021)*

**Added:**

* &#91;Substance model&#93; Update to version 1.0.3
* &#91;Substance model&#93; Complete and improve the Substance model graphs documentation
* &#91;Substance model&#93; Display logs in the console
* &#91;Substance model&#93;&#91;ScatterOnCurves&#93; Change default value for spacing
* &#91;Substance model&#93;&#91;ScatterOnCurves&#93; Remove unneeded HalfSpaceOddEven parameter
* &#91;Substance model&#93;&#91;Transform&#93; Update Euler rotation soft range
* &#91;Publish&#93; Remember settings in the Publish window
* &#91;Publish&#93; Warn the user when at least one dependency has unsaved changes
* &#91;Publish&#93; Initialize "File Path" field
* &#91;Publish&#93; Add visual feedback during publishing
* &#91;Interoperability&#93; Add "Send to Player" command to the "Send to" menu
* &#91;Interoperability&#93; Simplify send/resend workflow to Sampler and Painter
* &#91;API&#93; Add SDApplication.getVersion() to allow retrieve the version of the host application
* &#91;Explorer&#93; Add an Open action to Substance model graph items
* &#91;Graph&#93; Disable "View in 3d view" actions for ghost instance nodes

**Fixed:**

* &#91;Substance model&#93; Crash when deleting a sequence
* &#91;Substance model&#93; Basis are not drawn correctly in some cases
* &#91;Substance model&#93; Fail to export specific projects
* &#91;Substance model&#93; Material assignment broken when opening a project with Iray enabled
* &#91;Substance model&#93; Min hard range doesn't work correctly in certain circumstances
* &#91;Substance model&#93;&#91;Primitive&#93; Icosphere first level of subdivision doesn't work
* &#91;Substance model&#93;&#91;RandomFloat&#93; Correctly handle the case where Min &gt;= Max
* &#91;3D view&#93; Crash when drag and dropping maps
* &#91;3D View&#93; Exposed strings in MDL materials use color space widget
* &#91;3D View&#93;&#91;Bakers&#93; Parented objects are not handled correctly
* &#91;3D View&#93; Warning message about the "heightScale" usage name for legacy .glslfx file
* &#91;Content&#93; Cooking warnings in Height extrude node
* &#91;Content&#93; RT Irradiance node does not appear in Library
* &#91;Content&#93; RT Shadows: cooking warning messages in the console
* &#91;Graph&#93; Crash when opening a file with some disabled nodes
* &#91;Graph&#93; Dot node doesn't work correctly in MDL Graph when a link is selected
* &#91;Graph&#93; Graph view is not automatically re-opened after reloading a package
* &#91;Interoperability&#93; Error dialog when selecting 'Download...' while sending to Player
* &#91;Interoperability&#93; Resending after deleting all outputs results in API errors
* &#91;Interoperability&#93; Resending just after closing target application results in API errors
* &#91;Explorer&#93; &#91;Graph&#93; After reloading a package, the first graph opened is not the first graph of the package
* &#91;Explorer&#93; New graphs in a package are not placed the same way depending on their type
* &#91;Explorer&#93; Unable to open a Substance Model graph or a Scene Resource after moving it in the explorer
* &#91;Explorer&#93; Crash/freeze when moving a Substance model graph into package hierarchy
* &#91;Library&#93; SBSAR files remain in the temporary files location
* &#91;Library&#93; XML files remain in the temporary files location
* &#91;Player&#93; Material has no impact in 3D View when language is set to Japanese
* &#91;Player&#93; Substance Player download link is outdated
* &#91;Color widget&#93; Color editor window moves to the top of the screen
* &#91;IRay&#93; Fix IRay module loading on Windows when app directory contains non ascii chars
* &#91;Preferences&#93; MDL panel is displayed twice in Project
* &#91;API&#93; FxMap nodes don't support getPropertyGraph()

### 11.2.0

*(Released: June 23, 2021)*

**Added:**

* &#91;Branding&#93; Substance Designer becomes Adobe Substance 3D Designer
* &#91;Substance Models&#93; New Substance model graphs to create procedural 3D models
* &#91;Content&#93; Add new HDR environment maps
* &#91;Content&#93; New Bent Normal node
* &#91;Content&#93; New RT Ambient Occlusion node
* &#91;Content&#93; New RT Caustics node
* &#91;Content&#93; New RT Caustics node
* &#91;Content&#93; New RT Irradiance node
* &#91;Content&#93; New RT Shadows node
* &#91;Interoperability&#93; Send asset to Painter, will launch Painter and add or update your asset in the library (requires a Adobe Substance 3D plan)
* &#91;Interoperability&#93; Send asset to Sampler, will launch Sampler and add or update your asset in the library (requires a Adobe Substance 3D plan)
* &#91;Interoperability&#93; Browse your asset in Adobe Bridge, will launch Bridge at the location of the asset (requires a Adobe Substance 3D plan)
* &#91;ASM&#93; Support of the new Adobe Standard Material (ASM) in Substance Graph and MDL Graph
* &#91;ASM&#93; Add ASM templates
* &#91;ASM&#93; Add OpenGL Shader for ASM
* &#91;ASM&#93; Set ASM shader as the default Shader
* &#91;General&#93; Aggregate all temporary files to the user-set temporary directory
* &#91;General&#93; New 'Save a Copy as' command
* &#91;General&#93; Update File Menu
* &#91;General&#93; Update Help Menu
* &#91;Publish&#93; New publish window
* &#91;Publish&#93; Add option in the preferences in order to not save the SBS file while publishing a SBSAR file
* &#91;Properties&#93; Add graph type field to the graph properties
* &#91;Properties&#93; Reorder properties of graphs in a more relevant way
* &#91;Branding&#93; New About window
* &#91;Branding&#93; Update application Style
* &#91;GLSLFX&#93; Add a label to techniques
* &#91;GLSLFX&#93; Add the possibility to set the label of a GLSLFX shader
* &#91;Metadata&#93; Add Metadata on the package resources
* &#91;Metadata&#93; Allow Metadata edition for graphs, inputs, outputs and resources
* &#91;Localization&#93; New translations in German, French and Simplified Chinese
* &#91;UX&#93; Reverse zoom in the 3D view in the case of a Mouse Drag
* &#91;AXF&#93; Update to version 1.8.0
* &#91;Logs&#93; Add installed plugins to the logs
* &#91;VFX&#93; Add ACES 1.2 OpenColorIO config
* &#91;Python API&#93; Add a method to query the tmp dir specified in the settings
* &#91;Python API&#93; Add an isModified method to SDPackage to check if a pkg is saved
* &#91;Python API&#93; Add some color conversion methods to SDColorManagementEngine
* &#91;Python API&#93; Delete graph objects (Comments, pins, frames, ...)
* &#91;Python API&#93; Expose Physical Size property for graph instance nodes
* &#91;Python API&#93; Expose save a copy as
* &#91;Python API&#93; Fix SDPackageMgr.savePackage method
* &#91;Python API&#93; Get a list of selected graph objects
* &#91;Python API&#93; Introduce new method names to work with graph selections
* &#91;Python API&#93; Plugins cannot add actions to the first created explorer panel

**Fixed:**

* &#91;Parameters&#93; Negative values on drop down Integer1 parameters result in incongruous behaviour in instance
* &#91;Parameters&#93; Problem when incrementing a value on an angle widget
* &#91;Graph&#93; Timing problems when output are displayed in the 2D or 3D view.
* &#91;Internationalisation&#93; Some specific characters are changed into spaces in file identifiers
* &#91;Preferences&#93; 'User project' file label is not translated back from Japanese
* &#91;Python API&#93; RecursionError when running SDUIMgr.getCurrentGraphSelectedNodes() method
* &#91;Python API&#93; SDApplication.getPath(SDApplicationPath.InstallationDir) returns nothing
* &#91;Python API&#93; SDSBSARExporter does not send file save notifications

### 11.1.2 (2021.1.2)

*(Released: March 17, 2021)*

**Fixed:**

* &#91;Library&#93; Thumbnails do not refresh consistently
* &#91;Content&#93; 'Vector morph' graphs' 'Pixel ratio' property is set to 'Stretch (Absolute)'
* &#91;Content&#93; Bitmaps used in painting tools appear in Node menu
* &#91;Content&#93; NaN output for flat color input in Auto Levels node at floating point precision
* &#91;Engine&#93;&#91;SSE2&#93; 'Level in mid' value other than 0.5 results in 1.0 output
* &#91;Thumbnail&#93; Input maps are downscaled to 256
* &#91;UI&#93; Atomic nodes tooltips have incorrect line break

### 11.1.1 (2021.1.1)

*(Released: February 10, 2021)*

**Fixed:**

* &#91;3D view&#93; Render issue when using sbs that have high frequencies in normal map
* &#91;3D View&#93; Images are not applied if 'Component' output property is not set to RGBA or RGB
* &#91;3D View&#93; Scenes are not loaded correctly in some specific situation
* &#91;UI&#93; 'Texture file' input field in Brush Editor scales vertically
* &#91;UI&#93; Pin and Dock buttons disappear from tab when active tab is closed
* &#91;Bakers&#93; Incorrect result when high poly meshes' global Bbox does not include the scene origin
* &#91;Color Management&#93; sRGB Base Color Texture material property is not overridden in custom Scene state
* &#91;Console&#93; 'Available GPUs' log message does not list GPUs and appears randomly
* &#91;Console&#93; Incorrect string logged when using Batch export
* &#91;Content&#93; Atlas splitter's 'Input normal format' parameter impacts Red channel instead of Green
* &#91;Cooker&#93; Crash or NaN output when using \*.surface bitmaps in SBSAR
* &#91;Engine&#93; Gradient map's out of range output values loop around to 0 when Output format has 0-1 range
* &#91;Parameters&#93; Min/Max/Default sliders do not auto-adjust in Expose parameter window
* &#91;SBSAR&#93; Crash when importing some SBSAR
* &#91;SVG&#93; Crash when cancelling resource import

### 11.1.0 (2021.1.0)

*(Released: January 28, 2021)*

**Added:**

* &#91;Spot colors&#93; Support Pantone colors in Designer
* &#91;Graph&#93; Disable nodes
* &#91;3D View&#93; Export Tessellated Meshes from the Viewport
* &#91;Internationalisation&#93; Update Japanese version
* &#91;3D View&#93; Optimize memory consumption when not using Iray
* &#91;Python API&#93; Add method SDResource.delete() to delete a SDResource
* &#91;Python API&#93; Add support for Spot Colors to Python API
* &#91;Python API&#93; New callback to trigger when a package is closed
* &#91;2D View&#93; Convert brush database from SQLite to Json format
* &#91;2D View&#93; Improve rendering performances and reliability (CPU computation)
* &#91;Library&#93; Add 'Exclude pattern' option in project settings
* &#91;Library&#93; Rename 'Exclude pattern' to Exclude file extensions' in project settings
* &#91;UX&#93; Remove '?' button in window title bars on Windows
* &#91;UX&#93; Move the Ctrl+E shortcut to 'Open Reference' when in-context editing is disabled
* &#91;Bakers&#93; Delete Preview cache when deleting a baker in the bake list
* &#91;Performances&#93; Improve image cache budget on hardware with GPU with shared memory
* &#91;Preferences&#93; Adapt 'GPU cache limit' value to available memory pool
* &#91;Properties&#93; Display Physical Size attribute on node instance
* &#91;Scripting&#93; Mark external scripting system as deprecated
* &#91;Share&#93; Remove "Export to Substance Share" features

**Fixed:**

* &#91;Content&#93; Inconsistent I/O order on Material nodes
* &#91;Content&#93; Primary input on Warp nodes is inconsistent
* &#91;Content&#93; Solve Cooker warnings from Radial Blur node
* &#91;Export&#93; Batch export with CPU engine uses VRAM for determining memory budget
* &#91;Export&#93; Exporting to a path that does not exist will create the folders
* &#91;Export&#93; Memory budget is too low when using Batch export
* &#91;2D View&#93; Artifacts / banding when copying HDR images to the clipboard
* &#91;2D View&#93; Exporting images from resources always export 8 bits
* &#91;3D View&#93; Iray: changing the normal value using the editor gives a strange result
* &#91;3D View&#93; Iray: disabling the normal channel does not produce the right result
* &#91;Library&#93; Filtering by URL does not work correctly
* &#91;Library&#93; Resources matching a Library excluded pattern cannot be imported manually
* &#91;Bakers&#93; Renaming a baker does not impact its entry in the 2D View preview list
* &#91;Explorer&#93; Loss of synchronisation between Explorer and graph data
* &#91;Function graph&#93; Crash when setting function node with mismatching output type as output
* &#91;MDL&#93; SBS instance nodes have no preview, output 0 and do not trigger graph computation
* &#91;Python API&#93; Input parameter's 'editor' property cannot be modified
* &#91;Python&#93; Reset layout does not correctly reset Python created docks
* &#91;Resources&#93; Cannot link/import 32-bit PSD document

## Version 10

### 10.2.2 (2020.2.2)

*(Released: December 17, 2020)*

**Added:**

* &#91;3D View&#93; Restore camera position stored in a Scene resource
* &#91;Graph&#93; Remove "input nodes" in the contextual menu for FXMap and value processor

**Fixed:**

* &#91;Content&#93; Inconsistent I/O order on Material nodes
* &#91;Content&#93; PBR Render: incorrect IBL sampling for the specular contribution
* &#91;Content&#93; PBR Render: some pixels are always transparent
* &#91;Content&#93; PBR Render: UV output is incorrect for the Cylinder shape
* &#91;Content&#93; Splatter Circular's 'Pattern Specific' parameter has no effect
* &#91;MDL&#93; Crash when creating and connecting a node
* &#91;MDL&#93; Crash when duplicating a color&#91;&#93; array constructor with its exposed value input connected
* &#91;MDL&#93; Crash when reconnecting an invalid connection
* &#91;MDL&#93; Exported MDLs have duplicated parameters
* &#91;MDL&#93; Exposed parameters are not exported to a .mdl file
* &#91;Parameters&#93; A node parameter can be defined twice in the SBS in a specific case
* &#91;Parameters&#93; Crash when fetching the Output Type of a parameter's Function Graph
* &#91;Parameters&#93; Crash when selecting 'Edit exposed graph input' option where no matching input exists
* &#91;3D View&#93; "Environment" usage is not correctly taken into account by the OpenGL renderer
* &#91;3D View&#93; IOR is 0 and needs to be reset in a specific case
* &#91;3D View&#93; UVs of Plane/Plane Hi-res are offset
* &#91;Bitmap&#93; Crash when canceling resource import
* &#91;Bitmap&#93; Crash when creating a new Bitmap node with an unsupported file type
* &#91;Dependencies&#93; Crash when undoing 'Relocate' for solving a Ghost Instance
* &#91;Function Graph&#93; Crash when opening Function graph for a parameter
* &#91;Gradient Editor&#93; Moving sliders and keys logs too many actions in history stack
* &#91;License&#93; Crash when parsing an invalid license.key file
* &#91;SBSAR&#93; SBSAR instance nodes cannot be created from Library if exposed graphs are in folders

### 10.2.1 (2020.2.1)

*(Released: November 04, 2020)*

**Fixed:**

* &#91;General&#93; Crash when going out of Windows Sleep mode
* &#91;General&#93; Crash on Undo after loading a 3D Scene resource
* &#91;Engine&#93; Artefact lines appear in Distance node output on Direct3D
* &#91;Engine&#93; Crash when selecting Gradient Map node in an updated graph
* &#91;Engine&#93; No warning when Input default value other than 0 in Engine v7 compatibility mode
* &#91;3D View&#93; 'Remove All' leaves meshes with predefined materials with no material applied
* &#91;3D View&#93; 'Reset Scene' removes all textures from mesh in Iray
* &#91;3D View&#93; OpenGL: modifying the default value of a sampler in a .glslfx file is not correctly reflected in the UI
* &#91;3D View&#93; Red and black pixels on rightmost edge of OpenGL rendered images
* &#91;Dependencies&#93; Cannot relocate missing dependencies of 'Other' type
* &#91;Dependencies&#93; Crash on exit when Dependency Viewer is open
* &#91;Graph&#93; Crash when duplicating a Ghost Instance node
* &#91;Graph&#93; In-Context Editing is available through keystroke when it is disabled in Preferences
* &#91;UI&#93; 'Locate Player' warning window has incorrect title
* &#91;UI&#93; Activation wizard has some incorrect behaviour
* &#91;Explorer&#93; Bundled packages are always editable on Windows
* &#91;MDL&#93; Crash when loading graph from previous version with now invalid connections
* &#91;Properties&#93; Default color of input node not updated when undoing
* &#91;SBSRender&#93; ICC profiles of injected bitmaps are not used

### 10.2.0 (2020.2.0)

*(Released: October 12, 2020)*

**Added:**

* &#91;Content&#93; Add "Cross Section" node
* &#91;Content&#93; Add "Cross product vec2" function to functions.sbs
* &#91;Content&#93; Add "Get Size" value node
* &#91;Content&#93; Add "Orthogonal vec2" function to functions.sbs
* &#91;Content&#93; Add Average functions to functions.sbs
* &#91;Content&#93; Add Threshold filter
* &#91;Content&#93; Color Match: add a mask input to specify where to apply the filter
* &#91;Content&#93; Tile Generator/Sampler: add new options to control the pattern size
* &#91;Content&#93; Update PBR Render node with default value for image inputs
* &#91;Parameters&#93; Add warning icons to highlight issues in Instance Parameters
* &#91;Parameters&#93; Ignore Visible If statements for Inputs/Outputs involving parameters which have a Function applied
* &#91;Parameters&#93; Improve the UX for group association
* &#91;Parameters&#93; Rework of the way to expose a single parameter
* &#91;Parameters&#93; Highlight exposed parameters
* &#91;Parameters&#93; Improve Clean up of unused parameters
* &#91;Engine&#93; Curve node: new option to output the curve texture
* &#91;Engine&#93; Default values on input images
* &#91;Engine&#93; Distance node: new distance modes (Manhattan and Chebyshev distances)
* &#91;Engine&#93; Gradient node: new interpolation mode to have more natural mix between colors
* &#91;UX&#93; Some parameters are now grayed out depending on other parameters
* &#91;UX&#93; Accept 6-digits RGB colours in Color Picker's hexadecimal field
* &#91;UX&#93; Avoid showing comments properties as soon as they are selected
* &#91;UX&#93; Display relevant groups when starting to write a group name
* &#91;UX&#93; Shortcut to Reexport graph outputs
* &#91;UX&#93; Make all Dropdown-textfield-comboboxes look different from regular comboboxes
* &#91;GraphRender&#93; Display nodes thumbnails one by one and not only when they are all computed
* &#91;GraphRender&#93; Improve cancellation delay during graph rendering
* &#91;GraphRender&#93; Improve the accuracy of the rendering progress bar
* &#91;Thumbnails&#93; Automatic thumbnail (icon) computation
* &#91;Thumbnails&#93; Rework of the UX to add a thumbnail (icon) to a package
* &#91;Preferences&#93; Enable GPU raytracing by default for new users
* &#91;Preferences&#93; 3DView / OpenGL / Quality: replace slider for sample counts by a more intuitive list of choices
* &#91;Bakers&#93; Improve post processes performances
* &#91;Color Management&#93; Show current working color space in preferences dialog.
* &#91;Iray&#93; Automatically switch to CPU mode when there is no compatible GPU
* &#91;Performances&#93; Improve response time to compute the node we are interested in (now computed first)
* &#91;Python API&#93; New Method addActionToExplorerToolbar to add icons to the explorer toolbar
* &#91;Resources&#93; Upgrade to FBX 2020.0.1
* &#91;iRay&#93; Update to Iray 2020.1.0
* &#91;API&#93; Add Python access to color management settings and properties

**Fixed:**

* &#91;Graph&#93; Changing the parent size or uv tile does not cancel the current render
* &#91;Graph&#93; Crash when moving an output connection then pressing Alt+LMB
* &#91;Graph&#93; Crash when moving connections in Material or Compact Material mode
* &#91;Graph&#93; Input nodes cannot preview Bitmap resources
* &#91;Graph&#93; Node compatibility broken on instances
* &#91;Graph&#93; Too many nodes are invalidated when changing a graph parameter
* &#91;Content&#93; 'Shape Extrude' output shape is flipped in specific cases: new version needed, old one is deprecated
* &#91;Content&#93; Incorrect result using Custom Color Variation in Color Match node
* &#91;Content&#93; Size by X/Y Amount Ratio in Atlas Scatter has the opposite effect
* &#91;Content&#93; Size by X/Y Amount Ratio in Shape Splatter has the opposite effect
* &#91;3D View&#93; Crash on Undo operation after loading a Scene resource from a package
* &#91;3D View&#93; Custom environment not saved in SBSSCN if path has alias with special characters
* &#91;3D View&#93; Switching Normal Format in Material settings results in flipped states
* &#91;UI&#93; 'Set as Primary' button text is overflowing from display area
* &#91;UI&#93; Main window position is not correctly restored when working in windowed mode
* &#91;UI&#93; Status bar text is offset when window is fullscreened or dragged near screen edge
* &#91;Iray&#93; Crash with "Invalid Tag" message when switching back and forth between renderers
* &#91;Iray&#93; Visible faces on non-opaque surfaces
* &#91;Presets&#93; Crash when applying presets in instances of some Substance Source graphs
* &#91;Presets&#93; wrong name displayed after undo on sbs instance
* &#91;Render&#93; Wrong render when tweaking a parameter in preview mode
* &#91;Bakers&#93; Refreshing multiple baked maps results in warnings blocking some bakes
* &#91;Cooker&#93; Tweaking SBSAR nodes in SBS instances results in 0 output from the instance
* &#91;Explorer&#93; Custom aliases are not passed along when using 'Save and open in Substance Player'
* &#91;Gradient Editor&#93; Absolute color selection does not impact all selected keys

### 10.1.3 (2020.1.3)

*(Released: June 11, 2020)*

**Added:**

* &#91;Content&#93; Expose 'Matte Color' parameter in Safe Transform Grayscale node
* &#91;Content&#93; PBR Render: Add a custom Background Input option
* &#91;Content&#93; Panorama Light nodes: new option to sample the color from the background image
* &#91;Parameters&#93; Hide parameters with 'not-supported' flag from the Expose Parameters window list

**Fixed:**

* &#91;3D View&#93; Crash when switching custom meshes in a specific case
* &#91;3D View&#93; Normal format is always DirectX on startup
* &#91;Content&#93; 3D Worley noise: render artefact when using a high grid size value
* &#91;Content&#93; Dissolve node blending is incorrect
* &#91;Content&#93; PBR Render: remove Cooker warning
* &#91;Content&#93; PBR Render: result contains negative colors in some cases
* &#91;Cooker&#93; Cache injection issue for multi-output instance nodes
* &#91;Explorer&#93; Crash when closing a Package that contains a displayed MDL Graph
* &#91;Graph&#93; 2 pass cooking: node type change does not trigger a recook
* &#91;Graph&#93; Crash when deleting inputs while using its connection
* &#91;Graph&#93; Link endpoints can be moved to empty space
* &#91;MDL&#93; Crash when cancelling MDL export from MaterialX graph
* &#91;MDL&#93; Error when cancelling export to MDLE
* &#91;Presets&#93; Crash in Presets tab after changing type of parameter included in preset
* &#91;Resources&#93; Material list is empty in graph contextual menu for meshes linked as non-UDIM

### 10.1.2 (2020.1.2)

*(Released: April 27, 2020)*

**Added:**

* &#91;Content&#93; Add Alchemist Filter template
* &#91;Content&#93; PBR Render: add parameters to control the diffuse/specular shadows intensities
* &#91;Content&#93; Shape Light nodes: add camera position parameter
* &#91;News&#93; Group 'Arrow' style is broken the first time the window is displayed
* &#91;Bakers&#93; Add the Z shortcut to the 2D View to see the image at 1:1
* &#91;Project&#93; Hide $(PROJECT\_DIR) alias from the list
* &#91;Explorer&#93; Do not create Custom Resource for resources that are not a file on disk

**Fixed:**

* &#91;Player&#93; Report missing aliases when loading SBS packages
* &#91;Player&#93; Display the Random Seed value in decimal base
* &#91;Player&#93; Bundle all environment maps included with Substance Designer
* &#91;Player&#93; Crash on exit in macOS High Sierra
* &#91;Player&#93; Packages using the sbs:// cannot be loaded
* &#91;Content&#93; 3D Worley noise: render artefact when using a high grid size value
* &#91;Content&#93; 'greaterThanZero' input in 'Wave' node is not used
* &#91;Content&#93; Plane Light: World space position mode does not work
* &#91;Content&#93; Sphere Light: internal light position does not work correctly
* &#91;Bakers&#93; Crash when baking with the baking window while a 'Refresh all baked maps' is running
* &#91;Bakers&#93; Baking fail on Optix for AO from Mesh using Low as High with a Normal map
* &#91;Bakers&#93; The resolution of the preview of the UVTiles does not match the size of screen
* &#91;3D View&#93; Assigned bitmap is overridden when loading a MDL if default value is not a texture2d
* &#91;3D View&#93; Materials Properties widgets change after a property is reset
* &#91;3D View&#93; Normal Format global preference no longer works
* &#91;MatX&#93; Library: MaterialX Graph category does not display all the available nodes
* &#91;MatX&#93; The contextual menu of a Custom Graph can contain empty subfolders in the 'Add Node' folder
* &#91;SBSAR&#93; Primary Input is reverted to the first input in the list
* &#91;Library&#93; Only first graph is included from SBSAR with multiple graphs
* &#91;CustomGraph&#93; Nodes, that are not part of the current graph type, are created automatically in some cases
* &#91;Iray&#93; Box projection 'Depth' parameter does not work correctly
* &#91;Preferences&#93; Improve layout in the project settings
* &#91;Parameters&#93; Crash when moving a position widget after having deleted a parameter
* &#91;UI&#93; Crash when changing usages hierarchy in outputs node
* &#91;Graph&#93; Crash while using a Selection Box on comment and a badged node

### 10.1.1 (2020.1.1)

*(Released: April 10, 2020)*

**Fixed:**

* &#91;3D View&#93; Memory usage is too high when working on compositing graph
* &#91;Content&#93; Unexpected shapes in non-square output of 'Polygon' nodes
* &#91;Content&#93; PBR Render: Orthographic camera doesn't work correctly when using non square resolution
* &#91;Content&#93; PBR Render: Swirly bokeh increases the image border brightness
* &#91;Color Management&#93; Color picker in New Bitmap dialog is not color managed.
* &#91;Color Management&#93; Color pickers in paint and vector tools in the 2d view are not color managed.

### 10.1.0 (2020.1.0)

*(Released: April 09, 2020)*

**Added:**

* &#91;Shortcuts&#93; Shortcuts manager for node creation
* &#91;Content&#93; New PBR Render Node
* &#91;Content&#93; New FXAA filter
* &#91;Content&#93; New Hald CLUT filter
* &#91;Content&#93; Expose filtering in 'Crop' nodes
* &#91;3D View&#93; Improve Shader parameters / texture assignment workflow
* &#91;3D View&#93; New Unlit shader
* &#91;3D View&#93; Add a "Scalar Zero Value" to the displacement shaders
* &#91;3D View&#93; Add an option to downscale viewport resolution when High DPI is enabled
* &#91;3D View&#93; GLSLFX: Allow to set gui information on sampler (default, min, max, guiMin, guiMax, guiStep, guiWidget, guiName, guiGroup)
* &#91;3D View&#93; Add 'Load State With Mesh...' option in the Scene menu
* &#91;3D View&#93; Add the ACES tonemapped output transform in Legacy color management mode
* &#91;Bakers&#93; New Sampling method in AO, Curvature, Bent Normal, Thickness bakers
* &#91;Bakers&#93; New Normalization options in Height and Thickness bakers
* &#91;Color Management&#93; Integrate Adobe ACE (Adobe Color Engine)
* &#91;Color Management&#93; Add options to set default behavior when ICC profile is missing
* &#91;Parameters&#93; Make sliders incrementing consistent with Substance Painter
* &#91;Packaging&#93; Bundle as many Qt dlls as we can for Python scripts
* &#91;Project&#93; Disable settings for read-only project files and communicate that state clearly
* &#91;Preferences&#93; Hide specific unclear settings related to responsiveness and computation periods
* &#91;UI&#93; Rename Pow2 -&gt; 2Pow
* &#91;Properties&#93; Optimize compositing graph properties display
* &#91;AXF&#93; Update to AXF SDK 1.7.1

**Fixed:**

* &#91;3D View&#93; Ambient Light parameters are not visible eventhough it is enabled
* &#91;3D View&#93; glslfx: Color widget is always a vec3 without alpha
* &#91;3D View&#93; Environment map set from a resource is not saved in the scene resource
* &#91;3D View&#93; Iray: Ambient light is converted to a point light at scene origin
* &#91;3D View&#93; glslfx: Color widget is always a vec3 without alpha
* &#91;Parameters&#93; Instance Package URL is not correct in the attribute group
* &#91;Parameters&#93; Crash when exposing parameters
* &#91;Parameters&#93; Icons are not correctly aligned in parameters of Curve nodes
* &#91;Parameters&#93; 'Text' node string is only displayed in 'Preview' mode when exposed
* &#91;Parameters&#93; Crash when renaming an input parameter used in 'Visible If' statement
* &#91;Parameters&#93; Crash when deleting a Levels node which has a function set in any of its parameters
* &#91;UI&#93; Warning icon in input parameters list is placed on top on an existing button
* &#91;UI&#93; Warnings are not cleared on correct input parameter item in a specific case
* &#91;UI&#93; Prevent the "Is mesh UDIM ?" popup to appear when the mesh UVs are strictly in the &#91;0,1&#93; tile
* &#91;UI&#93; Presets drop down lists can be scrolled with mouse wheel with a simple mouse hover
* &#91;UI&#93; 'Output(s) computation' option in graph attributes is incorrectly named
* &#91;MDL&#93; Crash when placing a SBS graph resource into a MDL graph
* &#91;MDL&#93; SBS node with image input does not work correctly
* &#91;MDL&#93; Incorrect texture bindings &amp; usage names
* &#91;Graph&#93; Input value group and usage are ignored in 'Material' Link Creation Mode
* &#91;Graph&#93; Input Values use the default value instead of input data for Booleans
* &#91;Bakers&#93; Incorrect normals in World Space Normals baker using a tangent Normal map in specific cases
* &#91;Bakers&#93; Excessive memory usage when baking with the Preview window opened
* &#91;Presets&#93; corrupted preset make rendering crash
* &#91;Presets&#93; Boolean parameter from old SBS is not impacted by preset
* &#91;Library&#93; Resources from the first open package are listed in the node creation floating menu
* &#91;Publish&#93; Publishing to SBSAR returns Error code 13 in SBSCooker on macOS
* &#91;Publish&#93; Deprecated argument warning in SBSCooker when publishing to SBSAR
* &#91;API&#93; Can't get the Metadata from a package that comes from a .sbsar file
* &#91;Export&#93; In Legacy mode, colorspace option reverts back to defaults for specific outputs
* &#91;2D View&#93; Copy to clipboard does not take the Color Management state into account
* &#91;Unix&#93; Designer ignores system signals
* &#91;Library&#93; Some filters in the library don't work properly because of translated tags
* &#91;Cooker&#93; Square Root of negative numbers should return 0 instead of NaN
* &#91;2D View&#93; Red and blue channels are swapped after undoing the first paint stroke
* &#91;Console&#93; Too many warning message in the console "QPixmap::scaled: Pixmap is a null pixmap"
* &#91;Content&#93; "Shape Glow": cooking warning
* &#91;Dependencies&#93; Assigning a graph located in a different package to a mesh does not create dependencies
* &#91;Iray&#93; Material properties becomes inactive after switching geometry

## Version 9

### 9.3.3 (2019.3.3)

*(Released: February 14, 2020)*

**Added:**

* &#91;Batchtools&#93; Ship default OCIO profiles with batch tools

**Fixed:**

* &#91;Content&#93; Atlas Scatter: issues when using random color/normal in some situations

### 9.3.2 (2019.3.2)

*(Released: February 04, 2020)*

**Added:**

* &#91;SBSRender&#93; Add Color Management support

**Fixed:**

* &#91;Content&#93; Linear sRGB to ACEScg node: I/O labels are incorrect
* &#91;Content&#93; ACEScg to sRGB node: Output labels is incorrect
* &#91;Content&#93; Panorama Light nodes: adjust Temperature range
* &#91;Graph&#93; Severe performance drop and freezes when tweaking a nested graph with 'In-Context Editing' active
* &#91;Graph&#93; Crash when deleting multiple nodes in FX-Map
* &#91;Performances&#93; Designer's process may stay alive after quitting

### 9.3.1 (2019.3.1)

*(Released: January 27, 2020)*

**Fixed:**

* &#91;Graph&#93; Severe performance drop and freezes when tweaking a nested graph with "In-Context Editing" active
* &#91;Graph&#93; Cannot enter enum value out of &#91;0, 99&#93; in Integer1 tweak
* &#91;Graph&#93; Comment is not moved when the corresponding frame is displaced
* &#91;Graph&#93; Input names are missing on custom instance node
* &#91;Graph&#93; Thumbnails may be rendered when loading graph even if the corresponding option is disabled in the Preferences
* &#91;2D View&#93; Negative alpha shows checker no matter the display option
* &#91;2D View&#93; Surface conversion from 32f to 8bits fails with high values
* &#91;2D View&#93; Top/left skew and 'Make Square' set some coordinates to huge values in forward transformation matrices
* &#91;2D View&#93; UVs of all mesh objects are not displayed on UV sets other than "0"
* &#91;Content&#93; Bevel: Angular mode does not work correctly on tiling mask
* &#91;Content&#93; Flood Fill To Gradient: slope image value is not sampled in the middle of the shape
* &#91;Content&#93; Function; "Equality Boolean" is broken
* &#91;Bakers&#93; Artefacts when using automatic tonemapping in "Curvature From Mesh" baker in specific cases
* &#91;Bakers&#93; Crash in DXR when baking while no material is selected
* &#91;Bakers&#93; Performances issue in the 2D View when enabling the "info"
* &#91;Engine&#93; 'Pow' function outputs huge values when using very low input value and high exponent on SSE2 engine
* &#91;Engine&#93; Crash when using a high jpg compression on bitmap resources
* &#91;Engine&#93; Value Processor returns wrong $size value when inside a subgraph
* &#91;Parameters&#93; Empty pop-up appears when selecting an instance node with high number of parameters
* &#91;Parameters&#93; Integer value is not shown in drop-down parameter items
* &#91;Parameters&#93; Transform Matrix 'Edit' button is not available in Preview mode
* &#91;Cooker&#93; $size in ValueProcessor is wrong when inside a graph instance
* &#91;Cooker&#93; Outputsize is incorrect when value link passes through a dot node to an atomic node
* &#91;UI&#93; Button to display all items in the 2D View bottom bar is not visible
* &#91;UI&#93; Preview of picked RGB values display incorrect numbers when using Color Management
* &#91;Export&#93; 16f RGBA images are exported as grayscale
* &#91;3D View&#93; Cannot import OBJ with multiple spaces
* &#91;Color Management&#93; OCIO config is not taken into account when publishing sbsar
* &#91;Color Widget&#93; Color sliders ranges can expand exponentially in a specific case
* &#91;Doc&#93; "paramValue" section is incomplete in Sbs format reference
* &#91;MDL&#93; Color Widget in sbsar instances are not correct
* &#91;Presets&#93; Crash when updating presets in a specific case
* &#91;PSD&#93; FreeImage error when loading PSD files from recent versions of Photoshop
* &#91;Resources&#93; Crash when undoing Bitmap linking directly into graph
* &#91;SVG&#93; SVG nodes do not update automatically when using the vector tools

### 9.3.0 (2019.3.0)

*(Released: December 19, 2019)*

**Added:**

* &#91;General&#93; Support Color Management using OpenColorIO configuration file
* &#91;Presets&#93; Improve presets management
* &#91;Presets&#93; Synchronize 2D View Gizmos and Preview Sliders
* &#91;Presets&#93; Restore preview values when switching back to Preview mode
* &#91;Presets&#93; Keep preview mode active when editing other nodes, resources or graph
* &#91;Presets&#93; Undo works smoothly when navigating between the 3 presets tabs
* &#91;Presets&#93; Allow to Reset parameters to Graph's default or Preset's value in Preview mode
* &#91;Presets&#93; Improve pinning of parameters
* &#91;Presets&#93; Import/Export all Presets of a graph to a file
* &#91;Bakers&#93; New 'Curvature from mesh' baker based on ray tracing
* &#91;Bakers&#93; Add ground plane option in 'AO from Mesh' baker
* &#91;Bakers&#93; Add match by name option to ignore backface in 'AO from Mesh' baker
* &#91;Content&#93; New Atlas Scatter node
* &#91;Content&#93; New Color Space Conversion nodes and functions (ACEScg)
* &#91;Content&#93; Improve naming consistency for nodes with Color/Grayscale versions
* &#91;Graph&#93; Improve performances in Presets Preview mode
* &#91;Graph&#93; Add $(colorspace) macro to export graph outputs option
* &#91;Parameters&#93; When a parameter is set to invisible, hide the corresponding gizmo in the 2D View
* &#91;Parameters&#93; Do not add 'Graph input group' as a prefix when exposing parameters
* &#91;Parameters&#93; Add tooltip for VisibleIf in Graph parameters
* &#91;AXF&#93; Update AXF SDK to v1.6

**Fixed:**

* &#91;Linux&#93; Designer does not launch on CentOS 8 due to Qt platform loading failure.
* &#91;Linux&#93; WARNING: Freetype library has been removed from SD application: Users with CentOS version &lt;= 7.5 has to install it manually.
* &#91;AxF&#93; Crash when importing files created with newer AxF versions
* &#91;2DView&#93; Brush textures fed by a resource are not applied
* &#91;2DView&#93; Crash when modifying inputs of instanced graph with position tweak
* &#91;3DView&#93; Crash when canceling the "Load..." action
* &#91;3DView&#93; Add Color Space option for emission textures in GLSLFX Shaders
* &#91;Bakers&#93; Maps fed through resources are ignored during baking
* &#91;Bakers&#93; 'World Space Direction' options are incorrectly locked
* &#91;Bitmap&#93; EXR bitmaps with floating point values are rendered as a black image
* &#91;Content&#93; Flood Fill to index: shape detection fails in a particular case
* &#91;Content&#93; Crop: sampling issue when the crop node has a lower resolution than the input
* &#91;General&#93; Crash when closing Designer while generating the Library
* &#91;Graph&#93; Bitmap nodes do not reflect the compression of the associated bitmap
* &#91;Graph&#93; Cache is not cleared when clearing node thumbnails after first render
* &#91;Graph&#93; Node size incorrectly invalidated
* &#91;Graph&#93; Crash when im some cases when changing input connections on a Pixel Processor Node
* &#91;MDL Graph&#93; Failure when restoring a function call default value
* &#91;Properties&#93; 'Edit' and 'Matrix' buttons in transform matrix parameters are confusing

### 9.2.3 (2019.2.3)

*(Released: November 26, 2019)*

**Added:**

* &#91;MacOS&#93; Notarize the software to follow new MacOS Catalina distribution requirements

**Fixed:**

* &#91;Bakers&#93; Crash when baking using a skew map resource with an invalid link
* &#91;Bakers&#93; UV sets other than 0 are not taken into account on Embree
* &#91;Bakers&#93; 'Bent Normals from Mesh' outputs incorrect results with UV sets other than 0 on DXR
* &#91;Bakers&#93; 'UV Set' parameters are reset to '0' value when reopening baking window
* &#91;Bakers&#93; 'Position' outputs a black image with UV sets other than 0
* &#91;Content&#93; Smart Auto Tile: sampling issue in 8k
* &#91;Content&#93; Atlas Splitter: Shape Detection fails in some cases, precision parameter should be exposed
* &#91;Content&#93; Pow does not return the right value in some cases
* &#91;Content&#93; Flood Fill to index: incorrect result when published to sbsar
* &#91;Library&#93; Crash while loading the session's first SBS package
* &#91;Library&#93; 'Show Resources in the Library by Default' setting is ignored for resources imported directly into the Explorer panel
* &#91;Console&#93; Unexpected message in the console when using the node menu
* &#91;Parameters&#93; Cannot remove single entry in Output usage list
* &#91;3DView&#93; the scene is not reloaded correctly when the scene file is modified on disk&#91;Graph&#93; Node menu filtering is incorrect when using Value outputs

### 9.2.2 (2019.2.2)

*(Released: October 23, 2019)*

**Fixed:**

* &#91;Graph&#93; Node menu filtering is incorrect when using Value outputs
* &#91;Graph&#93; Crash when displaying the node menu
* &#91;Graph&#93; Search tool appears when using shift shortcut
* &#91;Graph&#93; Crash when consecutively spawning node menus from value input connector
* &#91;Graph&#93; Comments containing long strings are cropped
* &#91;Graph&#93; Flow highlight is incorrect when creating a node using the drag from connector menu
* &#91;Graph&#93; Crash when removing all graph items from scene while loading a different graph
* &#91;Graph&#93; Crash when using to create node while using click and drag from connector
* &#91;Graph&#93; Crash while using the 'Node Finder' tool
* &#91;Graph&#93; Output pin color is incorrect in 'Material Compact' mode
* &#91;Cooker&#93; Nodes downstream of multi-outputs nodes do not update correctly
* &#91;Cooker&#93; Issue with Value outputs and passthrough nodes
* &#91;Cooker&#93; Value Processor outputs wrong results when only a 'Get' node is used
* &#91;Content&#93; 'Contrast/Luminosity' node outputs an Alpha value of 1.0
* &#91;Content&#93; 'Studio Panorama' template has no description
* &#91;Content&#93; Flood Fill to index: incorrect result when the input contains a wrapping shape
* &#91;Content&#93; 'HDR Merge': internal exposure computation is incorrect
* &#91;Dot Node&#93; Crash when using a level and a dot node
* &#91;Dependency Manager&#93; 'Go to' action does not work anymore
* &#91;PSD&#93; Crash when undoing deletion of multiple nodes which were included in the PSD Exporter
* &#91;UI&#93; Crash when closing graph using the 'Window' menu and opening one again while one is pinned
* &#91;Gradient Editor&#93; The 'Remove Key' button is too large
* &#91;Engine&#93; Precision issue with sqrt() acos() and asin()
* &#91;Bakers&#93; AO From Mesh: 'Spread Angle' slider has an incorrect value range when tweaked

### 9.2.1 (2019.2.1)

*(Released: September 20, 2019)*

**Added:**

* &#91;Templates&#93; Add default input nodes to Specular/Glossiness and to other templates
* &#91;Templates&#93; Add PBR Anisotropy template
* &#91;3D View&#93; Increase the Automatic Clip Plane Far distances
* &#91;3D View&#93; PBR Coated: change default value for Coat normal inheritance
* &#91;Content&#93; Atlas Splitter: add option for the "Auto Crop" feature
* &#91;Node Menu&#93; Don't filter nodes without input

**Fixed:**

* &#91;Content&#93; Atlas Splitter: some outputs are not cropped correctly when using the "Auto Crop" option
* &#91;Content&#93; Material Height Blend: cooking error related to inexistent parameter
* &#91;Content&#93; "Plane Light": pattern UV Mode does not work correctly
* &#91;Content&#93; "Height to Normal World Unit": input is forced to 16bit
* &#91;Content&#93; Unexpected shapes when using angular 'Bevel' node with no tiling on small shapes
* &#91;Library&#93; Icons for sbsar are not visible in library
* &#91;Library&#93; Using "\" for filtering Url no longer works
* &#91;Library&#93; Filter values are case sensitive
* &#91;Library&#93; Search filter does not work when "Compositing" is checked
* &#91;Bakers&#93; Double-clicking specific cells and dismissing the change reverts them to incorrect values
* &#91;Bakers&#93; The backend state text in the bakers window always shows 'GPU acceleration : enable'
* &#91;Cooker&#93; Crash when processing an 'impostor' dependency in a graph
* &#91;Cooker&#93; grayscale conversion has wrong output size when using value
* &#91;Explorer&#93; Crash when processing "Publish on Share"
* &#91;Graph&#93; Crash when opening a specific package
* &#91;MDL&#93; Crash when using cast operator
* &#91;Templates&#93; Output identifiers are not correct in the PBR coated template

### 9.2.0 (2019.2.0)

*(Released: August 29, 2019)*

**Added:**

* &#91;Content&#93; New 'Panorama Light' shapes
* &#91;Content&#93; New 'Panorama Nadir Patch' filter
* &#91;Content&#93; New 'Panorama Nadir Extract' filter
* &#91;Content&#93; New 'Panorama Straighten Horizon' filter
* &#91;Content&#93; New 'Panorama Rotation' filter
* &#91;Content&#93; New 'Panorama Position' node
* &#91;Content&#93; New 'Panorama Physical Sun and Sky' node
* &#91;Content&#93; New 'Panorama Gradients' nodes
* &#91;Content&#93; New 'HDR Merge' filter
* &#91;Content&#93; New 'HDR Preview' filter
* &#91;Content&#93; New 'Color Temperature Adjustment' filter
* &#91;Content&#93; New 'Blackbody' node
* &#91;Content&#93; New 'Exposure' filter
* &#91;UI&#93; Node Creation Menu: display and manage Favorites in the menu
* &#91;UI&#93; Add/Remove a node from the favorites from the Node Creation Menu
* &#91;UI&#93; Node Creation Menu: spawn the menu when clicking/dragging a link from an output
* &#91;UI&#93; Node Creation Menu: filter the content according to the current selection type
* &#91;3D View&#93; Support Anisotropy
* &#91;3D View&#93; Support Coating effect
* &#91;3D View&#93; Support Subsurface Scattering
* &#91;Graph&#93; Dot node
* &#91;Graph&#93; Optimize graph rendering by caching cooking results
* &#91;Preferences&#93; Change the 'Cooking Size Limit' default value to 8192
* &#91;Preferences&#93; Add a toggle to turn the new 'Tab' key functionality on/off
* &#91;API&#93; Add SDResource.getPackage() method
* &#91;Iray&#93; Update to NVIDIA Iray RTX 2019.1.3 SDK (317500.3714)
* &#91;Explorer&#93; Allow to link any type of file as a resource in the Package
* &#91;GradientNode&#93; Press ESC to cancel the gradient picking
* &#91;Parameters&#93; Remove automatic Upper case on identifiers
* &#91;Project&#93; Add an option to specify if graphs and resources are 'Visible in Library' by default
* &#91;Presets&#93; Automatically pin modified parameters

**Fixed:**

* &#91;MDL&#93; Can't export module due to parameter type issue
* &#91;MDL&#93; Exposed int is not visible when loading
* &#91;MDL&#93; Crash occurring during MDL export
* &#91;MDL&#93; Crash when modifying color of a material surface node
* &#91;MDL&#93; void MDLGraphNodeControllerSelector::updateSelectorCurrentMember(const DataMessage&amp; msg) is broken
* &#91;Graph&#93; Incorrect link thickness in graph display
* &#91;Graph&#93; Too many invalidations are triggered when tweaking parameters
* &#91;Graph&#93; Crash when closing a package while two windows of it are open, and using in-context editing
* &#91;Function Graph&#93; Warning doesn't appear when closing function view
* &#91;3D View&#93; Crash on 3D View initialization when camera projection is set as 'orthographic' as a default scene state
* &#91;3D View&#93; Post-FX DOF stays enabled in Iray
* &#91;2D view&#93; Brush selection window disappears when changing brush size
* &#91;2D View&#93; Information panel: values are cropped with a specific layout
* &#91;2D View&#93; The image is offset when minimizing and restoring the main window
* &#91;Bakers&#93; 'From Resource' selection list is not filtered correctly
* &#91;Bakers&#93; Crash when chaining 'Color Map from Mesh' and 'Normal Map from Mesh' bakers on Embree
* &#91;Bakers&#93; Curvature Per Vertex baking results in severe artefacts
* &#91;Explorer&#93; Can't import UDIM resources drag and dropping it in explorer
* &#91;Explorer&#93; Explorer window is not filtered correctly when linking meshes and fonts after linking unusual file formats
* &#91;Explorer&#93; Resources are visible when graph has 'show in Library' set to 'no'
* &#91;Content&#93; 'Pow' and 'clamp' inputs are not in the correct order
* &#91;Content&#93; 'RGBA Merge' node inputs are not labelled
* &#91;Cooker&#93; Invalid connections of numeric values evaluate anyway
* &#91;Cooker&#93; Assert when connecting an image input to an input value
* &#91;UI&#93; Mouse cursor gets stuck in the 'resize' state in some particular cases
* &#91;UI&#93; Right click in package view doesn't display the correct menu on Linux
* &#91;Dependencies&#93; File path of temporary resources is not correct
* &#91;Dependencies&#93; Missing bitmap resource warning stays active after relocation
* &#91;Library&#93; Some thumbnails are not generated
* &#91;Library&#93; MDL files are displayed in the library
* &#91;Parameters&#93; Crash when exposing parameters
* &#91;Parameters&#93; Crash after recreating a new element in drop down list
* &#91;Export&#93; 8K batch export fails
* &#91;Presets&#93; Crash when applying a preset involving booleans in SBS instances
* &#91;Scripting&#93; 'Welcome' screen still appears when using '--quit' command line argument

### 9.1.3 (2019.1.3)

*(Released: August 19, 2019)*

**Fixed:**

* &#91;Bakers&#93; Crash in DXR when aspect ratios of bake output and skew map are mismatched
* &#91;Bakers&#93; 'Ambient Occlusion From Mesh' baker outputs wrong results with Optix or DXR when using a Normal map
* &#91;Bakers&#93; 'Curvature' baker outputs wrong results when using 'Per Vertex' setting
* &#91;Bakers&#93; Error messages state the backend which failed instead of the cause of the error
* &#91;Bakers&#93; Crash when processing a detail map baker without a high poly mesh
* &#91;Bakers&#93; Skew map does not appear to affect all the output with DXR enabled
* &#91;Content&#93; mg\_leaks: typo in parameters name
* &#91;Content&#93; "Shape" returns a cooking warning
* &#91;Content&#93; Polygon 1 and 2 don't support random functions
* &#91;Content&#93; Polygon 1 and 2 can have less than 3 sides
* &#91;Content&#93; Normal to Height HQ does not work correctly in non square
* &#91;Parameters&#93; Integer input parameters: the drop down list does not show the values

### 9.1.2 (2019.1.2)

*(Released: July 02, 2019)*

**Fixed:**

* &#91;3D View&#93; 3D View export with depth of field enabled looks incorrect
* &#91;3D View&#93; Alpha channel of PSD images is wrong when using save render
* &#91;3D View&#93; PNG and PSD are broken when using save render option with Iray
* &#91;3D view&#93; dds format doesn't work when saving render
* &#91;Graph&#93; Nodes get offset when combining right and left click drag in specific ways
* &#91;Graph&#93; Modifying a Function instances no longer updates the node result
* &#91;Graph&#93; Crash when displaying the Space Bar menu
* &#91;Content&#93; Shape Extrude: quality issue when shape has no rotation
* &#91;Content&#93; Shape Drop Shadow (and Grayscale) does not produce shadow without H and V tiling
* &#91;Content&#93; Material Crop normal issue
* &#91;Bakers&#93; JSON bakers presets are not loaded correctly
* &#91;Bakers&#93; Crash when baking heavy meshes using Optix or DXR (now it may fail because of insufficient Vram but it won't crash)
* &#91;Bitmap Editor&#93; Bitmap painting tools offset strokes and redraws in the stroke bounding box
* &#91;Bitmap Editor&#93; Bitmap painting tools broken in OSX
* &#91;UI&#93; Some button's menu are barely reachable
* &#91;UI&#93; Crash while drag and dropping a baker instance
* &#91;SVG&#93; Embedded SVG edit tools are unreliable
* &#91;Parameters&#93; Crash when applying a preset with boolean parameters in a SBSAR instance
* &#91;Network&#93; Crash sometimes when an error occurred in an SSL encrypted connection

### 9.1.1 (2019.1.1)

*(Released: May 28, 2019)*

**Added:**

* &#91;PythonIntegration&#93; Save and restore plugin manager state
* &#91;Preferencies&#93;&#91;Dependencies&#93; Add an option to determine how dependencies file path are stored
* &#91;Content&#93; Flood Fill Mapper: Add a "Fit Shape BBox" option

**Fixed:**

* &#91;Content&#93; Flood Fill Mapper: "Rotation Auto Scale" does the opposite effect
* &#91;Content&#93; "luminance\_offset\_map" input is not used by "Flood Fill Mapper Color"
* &#91;Content&#93; 'Flood Fill Mapper Grayscale' node generates stepping artifacts
* &#91;Content&#93; Cannot publish Height Extrude
* &#91;Parameters&#93; Embedded presets in sbsar are not loaded in Designer
* &#91;Bakers&#93; Baker name is not correctly displayed in the baker list
* &#91;3D View&#93; "View outputs in 3d View" does not work for values
* &#91;Cooker&#93; Crash when correcting a wrong parameter type
* &#91;API&#93; SDResource.setInputPropertyFromId function don't work on SDSBSCompGraph input parameters
* &#91;Updater&#93; some sbs can't be updated in 2019
* &#91;Explorer&#93; Crash when importing a specific .obj file
* &#91;PythonIntegration&#93; Backslashes not properly escaped on windows when initializing PYTHONPATH
* &#91;UI&#93; value issue with some sliders in bakers
* &#91;Linux&#93; Designer cannot be run on CentOS &lt; 7.6

### 9.1.0 (2019.1.0)

*(Released: May 09, 2019)*

**Added:**

* &#91;API&#93; Add 'updatePackages' parameter to the SDPackageMGR.loadUserPackage() method to control if the updaters should be applied or not on load
* &#91;API&#93; Add the ability to disconnect a SDConnection
* &#91;API&#93; Add class SDSBSARExporter to publish a SDPackage
* &#91;API&#93; Add SDHistoryUtils class to manage undoable commands
* &#91;API&#93; Add grayscale input node definition in Substance Compositing Graph (sbs::compositing::input\_grayscale)
* &#91;API&#93; Add value input node definition in Substance Compositing Graph (sbs::compositing::input\_value)
* &#91;API&#93; Add SDProperty.isFunctionOnly() method
* &#91;API&#93; Add support of custom input parameter on SDSBSCompNode
* &#91;API&#93; Add 'reloadIfModified' parameter to the SDPackageMGR.loadUserPackage() method to control if a package has be reloaded if modified
* &#91;API&#93; Add SDPackageMgr.getPackages() method
* &#91;API&#93; Add possibility to get/add/remove root paths from SDModuleMgr
* &#91;API&#93; Allow getting the pointer of the pixels buffer and the pitch of a SDTexture
* &#91;API&#93; Allow to retrieve the pointer of the MainWindow
* &#91;API&#93; Allow to create custom menus in the main menu
* &#91;API&#93; Allow to create custom DockWidgets in the main window
* &#91;API&#93; Use object names to find menus in toolbars
* &#91;API&#93; Provide system to manage application notifications to the API
* &#91;PythonIntegration&#93; Add default environment variable to look for python plugins
* &#91;PythonIntegration&#93; Add text search and replace to the Python editor
* &#91;PythonIntegration&#93; Instanciate Python plugins at startup
* &#91;PythonIntegration&#93; Take in account PYTHONPATH environment variable
* &#91;PythonIntegration&#93; Allow creating toolbars in graph widgets
* &#91;PythonIntegration&#93; Support Python threads
* &#91;PythonIntegration&#93; Add a Plugin Manager (in the 'Tools' menu)
* &#91;Content&#93; Normal Vector Rotation: add an optional image input to drive the angle
* &#91;Content&#93; New Min/Max filter
* &#91;Content&#93; New "Flood Fill to Index" filter
* &#91;Content&#93; New "Flood Fill Mapper" filter
* &#91;Content&#93; New Atlas Splitter filter
* &#91;Content&#93; Improve Tri Planar filter
* &#91;Content&#93; New Non Uniform Directional Warp filter
* &#91;Content&#93; New Multi Directional Warp
* &#91;Content&#93; New Height Extrude filter
* &#91;Engine&#93; Fxmap: new "Gradation with offset" pattern
* &#91;Engine&#93; Support For Uniform value processing (New Value Processor node)
* &#91;3D View&#93;&#91;Bakers&#93; Improve OBJ loader performances
* &#91;3D View&#93; Increase the camera clip plane distances
* &#91;Preferences&#93; Add settings for Bakers
* &#91;Graph&#93; Make invalidation faster by avoiding string comparisons
* &#91;MDL&#93; Support MDL Arrays
* &#91;UI&#93; Engine selection UI improvements
* &#91;IRay&#93; Upgrade to IRay SDK 2018.1.4
* &#91;Dependency Manager&#93; Use "last path" when relocating a resource
* &#91;Cooking&#93; Add support of Boolean Labels in the sbsar
* Integrate Qt 5.12.2

**Fixed:**

* &#91;Graph&#93; Connections are broken when changing the name of the input
* &#91;Graph&#93; Too many invalidations are triggered when tweaking parameters
* &#91;Graph&#93; "Copy to Clipboard" action don't work if we do the right click on a badge
* &#91;Graph&#93; Moving a frame using Alt is not stored in the .sbs
* &#91;MDL&#93; Color profile is not automatically updated in MDL editor
* &#91;MDL&#93; crash when exporting module that contains a specific setup
* &#91;MDL&#93; Fail to export a MDL Graph that contains a LightProfile or a MBSDF resource
* &#91;UI&#93; Shortcuts are no longer displayed in context menus
* &#91;UI&#93; Floating window becomes dockable after restart
* &#91;Scripting&#93; Cancel option doesn't work in python editor
* &#91;Scripting&#93; "yes to all" option in save menu doesn't work
* &#91;Parameters&#93; drop down list are not displayed correctly after copy
* &#91;Explorer&#93; Relocating resources should open the last relocated path by default
* &#91;Library&#93; The content of the library is always rebuilt when switching from one version to another
* &#91;Library&#93; Imported Bitmaps are invalidated on save
* &#91;IRay&#93; Tangent space is not computed correctly / incorrect normal mapping
* &#91;Function&#93; Crash or fail when creating new graph from selection
* &#91;API&#93; default value of properties is not defined

## Version 8

### 8.3.4 (2018.3.4)

*(Released: April 12, 2019)*

**Added:**

* &#91;Content&#93; Normal Transform/Material Transform: add an option to enable Scale and Skew transformation

**Fixed:**

* &#91;Content&#93; Swirl filter does not work correctly when random functions are used in parameters functions
* &#91;Content&#93; Normal Transform/Material Transform: Normal is not normalized after a scale transformation
* &#91;Content&#93; Swirl gives incorrect results when amount is random
* &#91;Graph&#93; Crash when shift-dragging an output then switching to ctrl-dragging
* &#91;Graph&#93; Crash while manipulating split points
* &#91;Graph&#93; Performance drop when displaying node badges
* &#91;Scripting&#93; Using custom actions could crash after 30secs
* &#91;Preferences/Projects&#93; Enabled scripts from all projects should be executed (in the 'Scripting' section)
* &#91;MDL&#93; crash when linking a MDL graph into another MDL graph
* &#91;Parameters&#93; Nodes do not update after setting the graph random seed to an exposed parameter
* &#91;PSD&#93; Assigning colour node changes layer thumbnail size, assigning a grayscale node does not
* &#91;API&#93; Unhandled exception with SDNode.getPropertyValueFromId()

### 8.3.3 (2018.3.3)

*(Released: February 19, 2019)*

**Fixed:**

* &#91;Content&#93; PBR Base Material outputs does not have the right group name

### 8.3.2 (2018.3.2)

*(Released: February 19, 2019)*

**Added:**

* &#91;Bakers&#93; Add a label indicating the current suffix setting for "Match By Name"

**Fixed:**

* &#91;Graph&#93; Crash while manipulating split points
* &#91;Graph&#93; Invalidation issue when input node bitdepth is changed
* &#91;Graph&#93; Thumbnail computation options no longer work
* &#91;Graph&#93; Empty space is displayed under the breadcrumb with a specific UI layout
* &#91;Graph&#93; Link style is incorrect in context
* &#91;Graph&#93; Thumbnails are not correctly displayed in function/mdl graphs on Hi DPI screens
* &#91;Content&#93; Shape Splatter Blend Color: no option to specify the normal map format
* &#91;Content&#93; Spelling mistake in linear interpolation tooltip
* &#91;Content&#93; Normal Transform does not handle mirror and skew transformation correctly
* &#91;Content&#93; Gradient Axial, Radial, Circular do not support random functions
* &#91;Content&#93; Gradient Radial does not work correctly in non square
* &#91;API&#93; output\_exporter.sbs always needs to be updated when using export\_output script
* &#91;API&#93; Crash after using export\_output script
* &#91;API&#93; Fail to set numerical value of annotations on Compositing Graph inputs
* &#91;Explorer&#93; Random crash when saving a project
* &#91;Explorer&#93; Can't open sbs with uppercase extension
* &#91;UI&#93; "New Substance" window size is not persistent
* &#91;UI&#93; Right click menu on function instance is not consistent with compositing graph
* &#91;Bakers&#93; Crash when opening the bakers on a specific mesh
* &#91;Bakers&#93; Wrong computation for DXR bakers when UVs have a 0 ordinate value
* &#91;Updater&#93; Crash when canceling updater
* &#91;3D View&#93; Sphere primitive has its UVs offset by 1 unit
* &#91;Cooker&#93; Random dithering when cooking bitmaps
* &#91;Player&#93; Window control buttons are small
* &#91;Player&#93; Button icons are broken

### 8.3.1 (2018.3.1)

*(Released: December 20, 2018)*

**Added:**

* &#91;API&#93; Add SDConnection.getOutputProperty() and SDConnection.getOutputPropertyNode()
* &#91;API&#93; Add doc about all resources definitions
* &#91;API&#93; Change SDSBSCompNode annotation property 'visibleif' to 'visible\_if' for consistency

**Fixed:**

* &#91;Graph&#93; Hitting the TAB key a second time does not close the Node menu
* &#91;Graph&#93; 3D View badges does not work correctly in some situations
* &#91;Graph&#93; Read-only packages can be modified
* &#91;Bakers&#93; Progress bar acts in a weird manner when loading a very high poly mesh
* &#91;Bakers&#93; Artifacts on mesh with in-facing normals
* &#91;Bakers&#93; Bakers output and parameters widget can't be uncollapsed
* &#91;Explorer&#93; 3D resources are loaded when a package is opened
* &#91;CmdLineArgs&#93; "--news hide\_changelog:true" does not work anymore

### 8.3.0 (2018.3.0)

*(Released: December 05, 2019)*

**Added:**

* &#91;Graph&#93; Add a Breadcrumb when editing sub-graphs / functions
* &#91;Graph&#93; Add TAB as a shortcut to spawn the "node menu"
* &#91;Graph&#93; Node highlighter for parent nodes of selection
* &#91;Graph&#93; Add Ctrl+E as shortcut to open Pixel Processor function and subgraphs
* &#91;Graph&#93; Connect new node to first visible output of selected node
* &#91;Graph&#93; Add node 'Badges'
* &#91;Graph&#93; Add warning on compositing nodes through badges
* &#91;Graph&#93; Add the possibility to search a node by its name, attributes or UID
* &#91;API&#93; Allow to create and modify data
* &#91;API&#93; Allow to export SDPackage and SDMDLGraph to MDL Modules (see SDMDLExporter)
* &#91;API&#93; Allow to retrieve all nodes, enums and struct definitions (see SDModuleMgr)
* &#91;3D View&#93; Switch to cubemaps for the OpenGL renderer
* &#91;3D View&#93; Export linear hdr image when saving to .exr or .hdr
* &#91;Bakers&#93; Integrate DXR raytracing technology
* &#91;IRay&#93; Integrate IRay SDK 2018.1
* &#91;Engine&#93; SSE (CPU) Engine support for hdr floating point image processing
* &#91;Engine&#93; Add a command line option (--gpu x) to specify the GPU device dedicated to the Substance engine
* &#91;Content&#93; New PBR render node
* &#91;UI&#93; Rework tabs and title bar
* &#91;Dependency Manager&#93; Prevent updating the dependency list when user actions don't affect dependencies

**Fixed:**

* &#91;Graph&#93; Crash when instantiating a graph into itself
* &#91;Graph&#93; Duplicated node is not selected
* &#91;Graph&#93; computing problem when using a same node instance in 2 different MDL graph
* &#91;Graph&#93; the Z key should center the view at the scene bbox center
* &#91;Graph&#93; Ignore colorspace in the connection rules when using material link
* &#91;Graph&#93; Avoid opening outputs in 3D view when opening a graph in conli
* &#91;Graph&#93; Paste nodes is slow when "Open newly created node" is enabled
* &#91;3D view&#93; Assert when drag and dropping a specific mesh
* &#91;3D view&#93; UV scale enabled option doesn't work on height map
* &#91;Content&#93; Tri-Planar: Various Issues regarding axis and transforms
* &#91;Content&#93; Slope Blur Grayscale: one of the samples does not have the right blending mode when using min or max
* &#91;Content&#93; Gradient linear 2 wrong result at low resolution
* &#91;API&#93; SDPackage.findResourceFromUrl() could also retrieve resources located in another SDPackage
* &#91;API&#93; SDPackage.getChildrenResources() always returns the first element in non recursive mode
* &#91;API&#93; &#91;Documentation&#93; Enums, structs located in 'generated' folder are not reflected in the documentation
* &#91;UI&#93; 2D view width should not be constrained
* &#91;Gradient&#93; Crash when picking on Mac
* &#91;Explorer&#93; Crash when closing and re opening a graph
* &#91;Mac&#93; Color picker does not work on multiple screen
* &#91;Parameters&#93; Spin box on integer parameters doesn't work
* &#91;Cooker&#93; Crash when creating certain nodes on OSX 10.13
* &#91;Curve Filter&#93; Keys and control points can end up with a -0.0 or a weird "almost zero" value in the Curve editor
* &#91;2D View&#93; Position widget are not available for graphs coming from sbsar
* &#91;PSD&#93; Layer issue after exporting with dependencies

### 8.2.2 (2018.2.2)

*(Released: October 04, 2019)*

**Fixed:**

* &#91;Content&#93; Shape Shadow does not work correctly when tiling is off
* &#91;Content&#93; Floodfill to Random grayscale / color doesn't work correctly in some cases
* &#91;Content&#93; Flood Fill is incorrect in non-square
* &#91;Content&#93; Flood fill to Color / Grayscale is broken
* &#91;Content&#93; QuadTransform is jaggy in CPU
* &#91;Content&#93; Star Shape outputs a "No Tiling" tiling mode
* &#91;Content&#93; Shape Splatter Blend Color output absolute 32f bitdepth
* &#91;Content&#93; Shape Splatter Blend Color is long to compute if its format is not set to 32F
* &#91;Graph&#93; Crash when linking image as Input of a Fx-Map while Iterate properties are displayed
* &#91;Graph&#93; Timings seems wrong while editing graph in-context
* &#91;Graph&#93; Random crash when saving graph
* &#91;Graph&#93; material mode doesn't work with sbsar
* &#91;3D View&#93; Material assignment is not restored correctly
* &#91;3D View&#93; Some 3Dview state file settings are not loaded correctly
* &#91;2D View&#93; Alpha display always displays black
* &#91;2D View&#93; Display Image to grayscale button does not work for images with alpha
* &#91;UI&#93; dependency manager spawn on start even when not activated on Mac
* &#91;UI&#93; Some buttons perform actions even when releasing the mouse outside
* &#91;API&#93; Crash when trying to keep an array item outside the scope of the array where he comes from
* &#91;MDL Graph&#93; Node preview is upside down
* &#91;MDL Graph&#93; Displacement of the preview node is different than in the 3DView
* &#91;Console&#93; Performances gets very slow when the console contains many message
* &#91;Console&#93; Qt warnings when launching Designer on CentOS
* &#91;FX-Map&#93; Crash while deleting links between inputs and FX-map
* &#91;Functions&#93; Can't set a string type node as output in Function Resource
* &#91;Preferences&#93; There is no focus in the preferences menu, user can accidentally change a value while scrolling
* &#91;FX-Map&#93; Input Image Index combobox not updated correctly when adding/removing inputs
* &#91;Dependencies&#93; Crash when deleting UDIM resources used in a graph
* &#91;API&#93; SDLocationContext.getCurrentGraph() always return null
* &#91;Publish&#93; Wrong URL to Substance Player downloading page

### 8.2.1 (2018.2.1)

*(Released: August 17, 2018)*

**Added:**

* &#91;UI&#93; Add a message in the taskbar when the "In context editing" is enabled
* &#91;Preferences&#93; Rephrase the "In context editing" option label

**Fixed:**

* &#91;Graph&#93; Paste without link shortcut doesn't work in compositing graph
* &#91;Graph&#93; Invalidation is very long when in context editing is enabled
* &#91;Graph&#93; Crash when linking nodes
* &#91;Graph&#93; Crash relinking nodes
* &#91;Graph&#93; Crash moving frames
* &#91;Graph&#93; Crash when switching UVTile in graph and mesh is not udim anymore
* &#91;Graph&#93; Crash when using ctrl+z after pasting nodes
* &#91;Graph&#93; Select Parent Nodes is very slow
* &#91;Bakers&#93; Moving maps up/down allow user to resize the row
* &#91;Bakers&#93; Path for saving or loading preset is never saved
* &#91;Bakers&#93; Cage is used even when not selected in the baking window
* &#91;Bakers&#93; Skew correction is not working correctly
* &#91;Bakers&#93; Very slow performance when negative UV space is in the view
* &#91;Bakers&#93; Clicking the Cancel button does not cancel the mesh loading
* &#91;Bakers&#93; Can't bake using a cage if the skew map is empty and set as true
* &#91;Content&#93; Flood Fill is slow in 4K
* &#91;Content&#93; Linear to sRGB function is broken
* &#91;Content&#93; Tile Random Grayscale background is driven by a float4 instead of a float, prevents cooking
* &#91;Content&#93; Shape Splatter: Position/Vector Map Multiplier does not work properly
* &#91;Scripting&#93; Ctrl + o doesn't work in python editor
* &#91;Scripting&#93; The Python editor keeps prompting even after closing
* &#91;Scripting&#93; Freeze when creating multiple new scripts
* &#91;UI&#93; Icons in Library are pixalated
* &#91;UI&#93; Panels that are floating by default misbehave
* &#91;Explorer&#93; Crash importing a mesh on CentOS
* &#91;Explorer&#93; UDIM mesh is loaded twice
* &#91;Cooker&#93; No timing for nodes in context
* &#91;Cooker&#93; Stack overflow when cooking
* &#91;License&#93; Bad authentication with valid credentials
* &#91;License&#93; Floating license reported more than once for the same user
* &#91;3D view&#93; UV tile material default V value is wrong
* &#91;3D View&#93; Performance regression compared to 2018.1.x
* &#91;Preferences&#93; Crash while using a configuration file from a server
* &#91;Library&#93; Crash deleting a filter inside the library
* &#91;SVG&#93; Dependency issue when using alias
* &#91;Levels&#93; 32bits HDR bitmaps make the level editor blink while moving widgets position
* &#91;PSD&#93; Linked import PSD window is displayed twice
* &#91;Iray&#93; Scene is updated when a disabled light is modified
* &#91;MDL&#93; Crash when deleting all nodes of an MDL template
* &#91;Engine&#93; Huge offset amount in FX-Map can freeze SD
* Crashpad Crashes at startup
* Python environnent variable makes Designer crash at launch

### 8.2.0 (2018.2.0)

*(Released: July 19, 2018)*

**Added:**

* &#91;UI&#93; New Style
* &#91;UI&#93; New Sliders
* &#91;UI&#93; Make floating windows really floating
* &#91;UI&#93; Change Preferences Window layout
* &#91;UI&#93; Library: remove filter bar
* &#91;UI&#93; Library: remove selection display overlay
* &#91;UI&#93; Add a message in the taskbar when the application is Autosaving a package
* &#91;UX&#93; Properties: merge "function" and "reset to default" menus
* &#91;Content&#93; New Shape Splatter (+ companion filters) nodes
* &#91;Content&#93; Add Flood Fill to Color/Grayscale filters
* &#91;Content&#93; New Flood Fill support: support shapes with holes
* &#91;Content&#93; Flood Fill to Gradient: add Slope and Angle image input
* &#91;Content&#93; Optimize the Auto Level filter
* &#91;Content&#93; New Shape Extrude filter
* &#91;Content&#93; Material Transform: add support for rotated normal maps
* &#91;Content&#93; New Normal Vector Rotation and Normal Transform filters
* &#91;Content&#93; Normal Normalize: improve result quality.
* &#91;Content&#93; New Trapezoid Transform filter
* &#91;Content&#93; New Quad Transform filter
* &#91;Content&#93; Add Hemisphere pattern to Shape node
* &#91;Content&#93; Add new Gradients with controls in the 2D View
* &#91;Content&#93; Add UV output to "Cube GBuffers" node
* &#91;Graph&#93; Frame: ignore title text larger than the frame bbox for selection
* &#91;Graph&#93; Add support for in context edition of sub graphs (experimental)
* &#91;Graph&#93; Creating Frame/Comment should affect the node under the cursor when using RMB
* &#91;Graph&#93; Frame: ignore title text larger than the frame bbox for selection
* &#91;Graph&#93; Reuse existing tab when opening a function already opened
* &#91;Graph&#93; Create a new tab when "Open Reference" is used
* &#91;Graph&#93; Function: don't display function properties when clicking on the background
* &#91;Parameters&#93; Remove "Expose" button from fxmap graphs
* &#91;Parameters&#93; Level: Add an "Invert" button
* &#91;Parameters&#93; Expand the "Input Parameters" group when creating a new input parameter
* &#91;Properties&#93; Add the package url info in the graph attributes
* &#91;Properties&#93; Increase the description field size for output nodes
* &#91;Properties&#93; Allow to enter Per Pixel Function of Pixel Processor even for read-only packages
* &#91;Scipting&#93; New Python API / Python editor (first iteration)
* &#91;Bakers&#93; Optimize geometry transfer during rendering
* &#91;3D View&#93; Switch to OpenGL Core Profile
* &#91;3D View&#93; Support tesselation/displacement on Mac
* &#91;Functions&#93; Function Resource: list image inputs in sampler nodes

**Fixed:**

* &#91;Graph&#93; crash when linking a node to another
* &#91;Graph&#93; getting variables in graph random seed function does not work
* &#91;Graph&#93; crash when drag and dropping noise in a graph
* &#91;Graph&#93; crash when opening a specific graph
* &#91;Content&#93; Result is different between Tile Random Color and Grayscale
* &#91;Content&#93; Tile Random: Result changes when modifying the "Symmetry Random Mode"
* &#91;Content&#93; Edge detect doesn't work with non-square resolutions
* &#91;Bakers&#93; Artifacts while baking curvature using a UDIM mesh
* &#91;Bakers&#93; Ambient Occlusion map from mesh is inverted while using a normal map
* &#91;Bakers&#93; UV sets list should be restricted to available UV sets
* &#91;Explorer&#93; crash when deleting resources while baking
* &#91;Transform2D&#93; Crash when exposing Mip map level and Background Color parameters
* &#91;Transform2D&#93; Misbehavior while exposing a Transform MipMap level
* &#91;PSDExport&#93; PSD exporter doesn't export grayscale 32F correctly
* &#91;2D View&#93; Histogram computation not working with 16F nodes
* &#91;PSD&#93; Linked PSD are broken
* &#91;Cooker&#93; Function in outputsize parameter is not correctly evaluated
* &#91;Export&#93; Export outputs path should be the same as the package path
* &#91;Export&#93; Export path is not saved using an empty pattern
* &#91;Templates&#93; Missing group for Position in Painter template
* &#91;Help&#93; command line help does not display --news on Mac
* &#91;Dependencies&#93; Exporting twice after modifying a folder name doesn't work

### 8.1.2 (2018.1.2)

*(Released: May 31, 2018)*

**Added:**

* &#91;3D View&#93; Allow to set the default light state in the Project settings
* &#91;Version Control&#93; Remove the timeout of 30s when calling the python scripts

**Fixed:**

* &#91;Content&#93; Fractal Sum Base: wrong result with the third level (new graph has been added)
* &#91;Content&#93; 3D Perlin Noise Fractal is forced to 32bit
* &#91;Content&#93; Gradient Linear 3 does not give the right result when using non uniform size
* &#91;Content&#93; Normal Sobel does not support tiling options
* &#91;Content&#93; Checker\_1 is forced to 8bit
* &#91;Content&#93; Multiangle to Normal: internal computation issue
* &#91;Content&#93; Stripes Pattern does not support negative "Shift" values (engine crash)
* &#91;MDL&#93; Crash when trying to open a specific MDL project
* &#91;MDL&#93; MDL Graph is not computed after a closed/reopened operation
* &#91;Export&#93; Outputs from unassigned graphs are exported using the batch tool
* &#91;Export&#93; Exporting C16F in exr generates grayscale image
* &#91;Bakers&#93; Skew features are not disabled in UI when baking with a cage
* &#91;Bakers&#93; Crash when cage doesn't have corresponding UV set
* &#91;Cooker&#93; sbscooker: cooking error related to "blend\_switch.sbs"
* &#91;Cooker&#93; Published graph does not render correctly
* &#91;Engine&#93; Transformation 2D: matte color is not correct
* &#91;Explorer&#93; Crash when re-importing a FBX mesh
* &#91;Color Widget&#93; Grayscale color picker only picks red channel value
* &#91;3D View&#93; Usage "textcoordN" doesn't work anymore
* &#91;Iray&#93; Normal Map is applied twice for dielectrics

### 8.1.1 (2018.1.1)

*(Released: April 12, 2018)*

**Added:**

* &#91;3D View&#93; Set default range of "Tesselation factor" to &#91;0, 16&#93;

**Fixed:**

* &#91;3D View&#93; Weird visual artefact with specific AMD GPU
* &#91;3D View&#93; Freeze with specific AMD GPUs
* &#91;3D View&#93;&#91;Bakers&#93; Generated normals from .obj have hard edges on UV seam
* &#91;3D View&#93; Crash while computing spherical harmonics
* &#91;Bakers&#93; Can't set resource as "embedded"
* &#91;Bakers&#93; crash when baking
* &#91;Bakers&#93; Baking 2 different versions of a map from UDIM mesh is broken
* &#91;Bakers&#93; crash when switching between contextual and non contextual graph
* &#91;Bakers&#93; Having the same baker twice will make them synchronized
* &#91;Bakers&#93; renaming the $(custom) macro prevents baking correctly
* &#91;Bakers&#93; Refreshing a baked map should blocks the UI
* &#91;Bakers&#93; Refresh All baked maps creates empty resources
* &#91;Bakers&#93; Pressing "Enter" to confirm a parameter value removes the high poly
* &#91;Content&#93; Tile Generator: Rotation Random error when X and Y Amount are different
* &#91;Content&#93; some grunge maps contains ghost instances
* &#91;Content&#93; Cube 3d: using random functions in parameters does not give expected result
* &#91;Content&#93; Fractal noises are not rendered correctly when Non Square Expansion is off
* &#91;Content&#93; Cells 2 and Cells 4 don't behave correctly when Non Square Expansion is off
* &#91;Graph&#93; Updating a sbsar instance creates a ghost graph
* &#91;Graph&#93; Assignment through right click should not display UV tiles sub menu for non UDIM meshes
* &#91;Graph&#93; Republished sbsar is not correctly updated
* &#91;Graph&#93; Nodes not invalidated correctly when resource changes
* &#91;Cooker&#93; Premult alpha blending parameter is not correctly retrieved from sbsar
* &#91;Cooker&#93; levels filter does not clamp values when cooked in a sbsar
* &#91;Cooker&#93; Implicit transform are performed before FX-Map nodes
* &#91;Explorer&#93; Pressing del key on a package asks the user if he wants to delete it
* &#91;Explorer&#93;&#91;Bakers&#93; Relocate issue
* &#91;Curve&#93; Random crash when manipulating keys in the curve editor
* &#91;MDL&#93; Gamma Type not correctly set for custom usage
* &#91;Parameters&#93; Crash exposing a parameter with the same identifier as an existing input
* &#91;Properties&#93; Output usage is edited with insensitive case

### 8.1.0 (2018.1.0)

*(Released: March 09, 2018)*

**Added:**

* &#91;Bakers&#93; Optimize high-poly baking
* &#91;Bakers&#93; Improve result on seams for Curvature baker
* &#91;Bakers&#93; Bake maps for UDIM based mesh
* &#91;Bakers&#93; Add a dedicated 2D view in the Baker window
* &#91;Graph&#93; Support for UDIMs
* &#91;Graph&#93; Optimize cooker performances
* &#91;Graph&#93; Improve node thumbnails generation speed
* &#91;Graph&#93; Keep node cache only for opened graphs
* &#91;Graph&#93; Add toolbar in the compositing graph to control the Thumbnail generation mode
* &#91;3D View&#93; Add a geometry cache to optimize high definition meshes display
* &#91;3D View&#93; Support UDIM display (display the current tile)
* &#91;3D View&#93; Update Rounded Cube with uniform topology
* &#91;3D View&#93; Avoid saving scene all the time
* &#91;Content&#93; Add 3D Noises (Perlin, Perlin Fractal, Worley, Simplex) nodes
* &#91;Content&#93; Add 3D Volume Mask node
* &#91;Content&#93; Add 3D Linear Gradient node
* &#91;Content&#93; Add 3D Cube Gbuffers node (useful to previsualize 3D based nodes)
* &#91;Content&#93; Add 3d Planar Projection node
* &#91;Content&#93; Add Radial Blur filter
* &#91;Parameters&#93; Display image input/output properties in the graph properties
* &#91;Parameters&#93; Allow the edition of resources path
* &#91;Engine&#93; Support up to 8k textures with the CPU (SSE2) engine
* &#91;Engine&#93; Allow Grayscale Converter to use HDR weights for HDR engine
* &#91;Preferences&#93; Add an option to disable the automatic conversion node creation
* &#91;Preferences&#93; Set the default compression for png to 'best speed'
* &#91;UI&#93; support html link in Graph properties
* &#91;UI&#93; Center the "Yes / No / Cancel" Buttons in the save confirmation dialog
* &#91;Explorer&#93; Enhance Mesh hierarchy display
* &#91;IRay&#93; Integrate IRay SDK 2017.1.4

**Fixed:**

* &#91;Bakers&#93; Adding a macro in the output name field does not add it on the cursor position
* &#91;Bakers&#93; No materials are displayed in the list if the object has no material
* &#91;Bakers&#93; Pressing Enter to confirm baker parameters open a drop-down menu
* &#91;Bakers&#93; Baking textures should not generate commands in the undo stack
* &#91;Bakers&#93; Crash baking a Transferred Texture From Mesh without specifying a texture
* &#91;Explorer&#93; "Save as" should use the existing file name instead of the first resource name
* &#91;Explorer&#93; Wrong behavior when drag and dropping a resource from one package to another
* &#91;Explorer&#93; Right mouse click should not open the data in the properties
* &#91;Explorer&#93; Icon of Scene items don't have the correct background
* &#91;Graph&#93; Ctrl + D doesn't work on Linux
* &#91;Graph&#93; Multi relink function sometimes plug only one link
* &#91;Graph&#93; Ctrl+Shift+D should remove only external links, not internal links
* &#91;Graph&#93; Link between grayscale and color isn't correct
* &#91;3D View&#93; Cannot set a resource as an env map
* &#91;3D View&#93; Mesh info shader don't display results in the right color space
* &#91;Parameters&#93; Non exposable parameters are still exposable using CTRL+P
* &#91;Parameters&#93; Text fields are not updated correctly on undo/redo
* &#91;Content&#93; Artifacts in Grunge Map 003
* &#91;Content&#93; Vector morph grayscale primary input seems incorrect
* &#91;Cooker&#93; sbscooker generates an error when a resource is missing
* &#91;Cooking&#93; Crash with stack overflow when node chain is too long
* &#91;UI&#93; 'Quit' button in license management doesn't work

## Version 7

### 7.2.5 (2017.2.5)

*(Released: February 19, 2018)*

**Added:**

* &#91;Content&#93; Typos in function.sbs
* &#91;Content&#93; Reduce default range of perlin noise and gaussian noise
* &#91;3D View&#93; Adjust default range for "Height Scale" Parameter
* &#91;AXF&#93; Update mdl templates

**Fixed:**

* &#91;3D View&#93;&#91;Bakers&#93; Normals are not recomputed if the model has no normals
* &#91;Graph&#93; Non Square bitmap resource is empty once instantiated
* &#91;Content&#93; Perlin noise gives different result between CPU and GPU engine

### 7.2.4 (2017.2.4)

*(Released: February 08, 2018)*

**Added:**

* &#91;AXF Import&#93; Allow to specify the filtering mode on input bitmaps
* &#91;2D View&#93; Don't change the ratio of the image in the 2D view when the physical size is enabled

**Fixed:**

* &#91;Library&#93; crash when enable/disable path in preferences
* &#91;Baker&#93; Match by name ignore some meshes with specific names
* &#91;Content&#93; Premult to Straight filter removes alpha channel

### 7.2.3 (2017.2.3)

*(Released: January 19, 2018)*

**Fixed:**

* &#91;Content&#93; typo in "PBR Basecolor Validate" node
* &#91;Content&#93; Disorder parameter is broken in Cells 2
* &#91;Content&#93; Cells 3 is inverted when using specific values in parameters
* &#91;Content&#93; Polygon 2: Visual artefacts with specific settings
* &#91;Content&#93; Tile generator grayscale is in 8 bit by default
* &#91;Content&#93; Tile sampler: pattern specific random parameter doesn't work
* &#91;Content&#93; Shape Mapper: random functions can't be used to drive Pattern Amount, Radius, Width..etc
* &#91;Content&#93; Polygon 2: random functions can't be used to drive Sides amount
* &#91;Content&#93; Some noises/pattern generators generate warnings in the console
* &#91;Content&#93; Non-Square-Transform-Grayscale generates a wrong Pixel Size
* &#91;Content&#93; Swirl filter does not take the tiling mode into account
* &#91;Graph&#93; Drag and dropping bitmap resource to image Input node no longer works
* &#91;Graph&#93; CTRL+R (reload) doesn't work anymore
* &#91;Graph&#93; Problem when using frame in another frame
* &#91;Graph&#93; Crash when moving frames containing Pins
* &#91;Graph&#93; "Shape (Legacy)" instance gets transformed into "Shape" on save
* &#91;Baker&#93; crash when using non power of 2 images
* &#91;Bakers&#93; Color from mesh: Polygroup, Submesh ID always return a black image
* &#91;Bakers&#93; AO from Mesh: Occluder distance is clamped to 1 no matter the input value
* &#91;Iray&#93; Crash switching to Iray
* &#91;Iray&#93; Tiling value should affect the heighScale intensity
* &#91;Iray&#93; Fail to load IRay on windows machine where VCCOMP110.dll was not present
* &#91;3D View&#93;&#91;Bakers&#93; UVs can't be decoded from obj exported from Modo
* &#91;3D View&#93; Displacement intensities are not consistent between Opengl and Iray
* &#91;3D View&#93; Displacement/Parallax Occlusion intensity is twice what it should be
* &#91;2D View&#93; offset when displaying image alpha
* &#91;Cooker&#93; Constant parameter ($tiling) is not found when used inside a graph instance
* &#91;Cooker&#93; Wrong evaluation of variable in chained instances
* &#91;Parameters&#93; Bitmap PKG Resource Path should not be editable
* &#91;Parameters&#93; Parameters in a same group are invisible if only one parameter has its visibility to false
* &#91;PSD&#93; Can't import/link a PSD file from a folder named with special characters
* &#91;Functions&#93; Parameters in functions shouldn't have a visibility option
* &#91;LicenseService&#93; Exception thrown when getting information on nodes
* &#91;UI&#93; Selecting text in description field keeps it highlighted

### 7.2.2 (2017.2.2)

*(Released: November 23, 2017)*

**Fixed:**

* &#91;Content&#93; Typos in "Directional ..." nodes
* &#91;Content&#93; Various Typos
* &#91;Content&#93; Tile Sampler is set to "Absolute 32 bit"
* &#91;Content&#93; Shape Mapper: visible artefacts on the shape border in some cases
* &#91;Content&#93; tiling and "Non-Square Expansion" parameters in Polygon 1 are broken
* &#91;Content&#93; "Random Seed" and "Non-Square Expansion" don't work on Anisotropic Noise
* &#91;Content&#93; Broken "Shape" instance in some Grunge Maps
* &#91;3D View&#93; UV scaling is not applied if the height scale is 0
* &#91;3D View&#93; Reflection with shader blinn don't work anymore
* &#91;2D View&#93; Information window has its layout broken
* &#91;Graph&#93; issue when controling output size with function on a linked bitmap instanced in a graph
* &#91;Function&#93; Graph not invalidated when a link is deleted
* &#91;Library&#93; Favorites don't work
* &#91;PSD Export&#93; PSD file content change each time an export is done
* &#91;Gradient&#93; Crash when manipulating keys in the gradient editor
* &#91;Templates&#93; Position map for Substance Painter templates is incorrect
* &#91;AxF&#93; Wrong physical height
* &#91;MDL&#93; UVW scaling from physical size is inverted in MDL SBS nodes
* &#91;Bakers&#93; $custom doesn't work anymore
* &#91;Preferences&#93; crash on start on Mac

### 7.2.1 (2017.2.1)

*(Released: October 20, 2017)*

**Fixed:**

* &#91;Engine&#93; Crash when rendering text with GPU engine
* &#91;Content&#93; Tile Sampler: Row/Column ID does not work properly with non square
* &#91;Content&#93; Tile Sampler Color: Color parametrization is wrong
* &#91;Content&#93; Tile Sampler: wrong default value for X / Y pattern amount
* &#91;Export&#93; Exported PSD are missing metadata

### 7.2.0 (2017.2.0)

*(Released: October 19, 2017)*

**Added:**

* &#91;Content&#93; Add Floodfill and associated filters (convert a black and white mask to gradients, random colors..etc)
* &#91;Content&#93; Add new Noises, Grunge Maps and Pattern generators that support non square format (old version are marked as "Legacy")
* &#91;Content&#93; Added new Splatter Circular with a lot more features
* &#91;Content&#93; Add new Scratches Generator
* &#91;Content&#93; Add Swirl filter
* &#91;Content&#93; Add Histogram Select
* &#91;Content&#93; Add Star pattern
* &#91;Content&#93; Add Shape Mapper filter
* &#91;Content&#93; Add Vector Morph filter
* &#91;Content&#93; Add Gradient Linear 3
* &#91;Content&#93; Tile Random / Tile Generator: add symmetry mode (h+v, h, v)
* &#91;Content&#93; Tile Generator: Add multiple image input
* &#91;Content&#93; Rename "RGB-A Merge" to "Alpha Merge"
* &#91;2D View&#93; switch node output display using the C key
* &#91;2D View&#93; Optimize Histogram / info layout depending on their display ratio
* &#91;2D View&#93; Add a button to enable/disable the tiling display
* &#91;3DView&#93; Optimize computation speed of Spherical harmonics
* &#91;3D View&#93; Update PBR shaders to use Fibonacci sampling instead of Hammersley
* &#91;3D View&#93; Add an option to save the current scene state as default
* &#91;3D View&#93;&#91;Bakers&#93; Serialize Data in human readable format
* &#91;Bakers&#93; Add presets export/import (json)
* &#91;Publish&#93; Create the sbsar archive as non solid
* &#91;Publish&#93; Store the graph image/thumbnail into the sbsar
* &#91;Publish&#93; Display a progress bar when a package is being published
* &#91;Dependencies&#93; Display the .sbs file requesting a dependency in the "Missing dependency window"
* &#91;Dependencies&#93; Report window: display green icon when the problem has been resolved
* &#91;Dependencies&#93; Add an option to open the package custom dependencies in the package explorer
* &#91;Preferences&#93; Add an option to set the default scene state in the project settings
* &#91;Preferences&#93; Add an option to enable/disable path for the library
* &#91;Graph&#93; Add an option to make a screenshot (at 1:1 scale) of the graph
* &#91;Graph&#93; Remove tooltip from the background of compositing graphs
* &#91;Scripting&#93; Add onBeforeFileLoaded and onAfterFileLoaded callbacks
* &#91;Engine&#93; Add a Base Parameter to adjust Pixel Ratio mode
* &#91;Console&#93; Improve Console performances
* &#91;Parameters&#93; New Position (XY) widget
* &#91;Iray&#93; Upgrade to IRay SDK 2017.1
* &#91;PSD&#93; Save PSD widget state as text instead of binary
* &#91;Library&#93; Use thumbs from sbsar if it exists
* &#91;Explorer&#93; Rename "Dependencies.." entry to "Dependency Manager"
* AXF files Import

**Fixed:**

* &#91;MDL&#93; Fail to export MDL Module if texture is connected to an exposed parameter
* &#91;MDL&#93; Try to register dependency for MDL string variables (constant node)
* &#91;MDL&#93; crash after closing the package
* &#91;MDL&#93; crash when connecting a float 3 to a color node
* &#91;MDL&#93; can't open nodes library when releasing a link node in a frame
* &#91;MDL&#93; crash when using a file texture
* &#91;MDL&#93; Dependency behaviour register too many operands
* &#91;Graph&#93; Connector names are disabled after FX-Map editing
* &#91;Graph&#93; crash when undo
* &#91;Graph&#93; Strange behavior with links between nodes
* &#91;Graph&#93; Collapsed nodes scatter and detach when undo
* &#91;Graph&#93; Function instance are not updated when reference is changed
* &#91;Version Control&#93; Package is reloaded when a Version Control custom action is triggered
* &#91;Version Control&#93; Disabled version control workspaces are still available in the context menu of a package
* &#91;Version control&#93; Remove custom action don't remove it from the contextual menu of a package
* &#91;Properties&#93; Parameter preview is not updated when using the gizmo
* &#91;Iray&#93; Max time display problem
* &#91;Iray&#93; Pause option issue
* &#91;Bakers&#93; crash when baking convert UV to SVG using Korean/Japaneses translation
* &#91;Bakers&#93; changing the path after a first baking doesn't work
* &#91;PSD Exporter&#93; undo issue
* &#91;PSD&#93; folder and layers are locked in Photoshop CS5
* &#91;UI&#93; color cursor is always set to white when uniform color node is created
* &#91;UI&#93; Opening an existing tab should display it instead of duplicating it.
* &#91;Presets&#93; crash when changing parameter type used in a preset
* &#91;3D View&#93; samplers with same usage are merged
* &#91;2D View&#93; Pixel information does not work for images whose resolution is not a power of 2
* &#91;Library&#93; issue when renaming filters
* &#91;Data&#93; Fix various typo in SBS files
* &#91;Parameters&#93; level node - auto level precision issue
* &#91;Preferences&#93; Templates Directories buttons should be disabled for "Default Project"

### 7.1.4 (2017.1.4)

*(Released: October 02, 2017)*

**Added:**

* &#91;Bakers&#93; Add the Curvature from mesh back
* &#91;New Version checker&#93; Add a command line option to disable the check for new version (--news hide\_changelog:true)
* &#91;Scripting&#93; Disable Qprocess time out

**Fixed:**

* &#91;Bakers&#93; can't change material color in UV to SVG
* &#91;UI&#93; can't close graph view using wheel click
* &#91;Content&#93; Some noises are in 8 bits instead of 16 bits
* &#91;Content&#93; Curvature Smooth gives wrong result when tiling is disabled
* &#91;Text&#93; crash when resizing specific fonts

### 7.1.3 (2017.1.3)

*(Released: August 31, 2017)*

**Fixed:**

* &#91;3D View&#93; crash when trying to display 3D view options on Mac 10.10.5
* &#91;3D View&#93; Text Info is not displayed in the 3D view when using High dpi screen
* &#91;3D View&#93; Global preference for OpenGL/DirectX is not taken into account when the material is reset
* &#91;Content&#93; Height to normal: normal is inverted when using Sobel sampling
* &#91;Content&#93; Ambient Occlusion (hbao\_2) does not behave correctly when set to non square
* &#91;Content&#93; Mask generators inputs are not in the same order as "Mesh Data Combiner"
* &#91;2D View&#93; Histogram: selection information is not updated on image change
* &#91;2D View&#93; Histogram: Used range information is not displayed for grayscale images
* &#91;Presets&#93; crash when renaming a preset of a graph used in another graph
* &#91;Graph&#93; X and Y are inverted in the Parent Size Toolbar

### 7.1.2 (2017.1.2)

*(Released: August 03, 2017)*

**Fixed:**

* &#91;Content&#93; Filtering Problem in "Smart Auto Tile" and "Crop Grayscale" Filters
* &#91;Content&#93; Library Filters don't take the OpenGL/DirectX preference into account
* &#91;Content&#93; Can't cook SBSAR with non\_square\_transform
* &#91;Content&#93; Panorama Shape: Hotspot is mirrored in RGB channel
* &#91;Content&#93; Tile Sampler: Position Color parametrization is not normalized
* &#91;Content&#93; Tile Sampler: Patterns are invisible if the the tiling is disabled
* &#91;Graph&#93; $normal\_map\_format switch does not work when we use the library/space bar menu
* &#91;Graph&#93; Wrong format in the bitmap node when drag and dropping a RGBxxF resource
* &#91;Bakers&#93; Color from mesh with material color is broken
* &#91;3D View&#93; every change in 3D view generate actions in undo stack
* &#91;Dependencies&#93; crash when a graph has missing resources in custom library
* &#91;Iray&#93; crash on start on OSX version is older than 10.11

### 7.1.1 (2017.1.1)

*(Released: July 18, 2017)*

**Added:**

* &#91;Bakers&#93; Add a "Reset" action" on resource fields
* &#91;Bakers&#93; Use black color when no vertex color is found
* &#91;Presets&#93; Hide the preset widget on instances when no presets are available
* &#91;Preferences&#93; Remove the "Compute binormal by fragment" option in the project settings (now this option is handled in the tangent frame plugin)
* sbsupater.exe adjustments

**Fixed:**

* &#91;Bakers&#93; The "error" system no longer works
* &#91;Bakers&#93; options serialization: old keys remain
* &#91;Bakers&#93; crash when changing the name of a baker
* &#91;Bakers&#93; UI glitches
* &#91;Content&#93; Color Match filter - difference between CPU/GPU
* &#91;Content&#93; Some GrungeMaps output 8bits images instead of 16bits
* &#91;Graph&#93; Crash when using the X "switch links" on fx-map node
* &#91;3D View&#93; Random crash when opening 3D View
* &#91;3D View&#93; Binormal are always computed by fragment, no matter the tangent space plugin
* &#91;Updater&#93; XML error when using specific font
* &#91;Cooker&#93; modulo on negative number does not return the same result as the engine
* &#91;UI&#93; interface issue when using pick gradient on high DPI screen
* &#91;MDL&#93; Color node doesn't keep his value
* &#91;Packaging&#93; Mikkt Unreal tangent space plugin is missing

### 7.1.0 (2017.1.0)

*(Released: June 29, 2017)*

**Added:**

* &#91;Bakers&#93; New UI
* &#91;Bakers&#93; Keep a high def mesh cache until the baker window is closed
* &#91;Bakers&#93; Add an option to correct skew deformation using a grayscale mask
* &#91;Bakers&#93; Support use-high-poly-as-low-poly in from-mesh bakers
* &#91;Bakers&#93; Make the Bakers window non modal
* &#91;Bakers&#93; Store state to .sbs file in human readable format
* &#91;Parameters&#93; Copy/Paste parameters from one graph to another
* &#91;Parameters&#93; Add an option to copy a single Input Parameter (and paste it afterward)
* &#91;Parameters&#93; Remove the function button on "Color Mode" parameter
* &#91;Parameters&#93; Edit/Save/Display embedded parameter presets
* &#91;Parameters&#93; Allow the user to copy parameters attributes when a package is locked
* &#91;3D View&#93; No longer store last session 3d view settings in the registry
* &#91;3D View&#93; Create new 3d resource from current scene
* &#91;3D View&#93; No longer store the 3D view state from one session to another in the registry
* &#91;3D View&#93; Merge the "Scene" and "Geometry" menus
* &#91;3D View&#93; Seperate sRGB conversion from the fragment shader (you will need to update your custom shaders!)
* &#91;3D View&#93; Add an option to create a new 3d resource from the current state
* &#91;3D View&#93; Improve error message generated when #include fail into a shader code
* &#91;3D View&#93;&#91;Explorer&#93; Create 3D scene from primitives
* &#91;3D View&#93; Display correct line number when GLSL shader compilation failed and code contains #include directives
* &#91;Graph&#93; Be able to resize a frame from all corners/borders
* &#91;Graph&#93; Store the Parent Size information on the graph resource instead of local registry
* &#91;Graph&#93; optimize Node thumbnails generation speed
* &#91;Graph&#93; Expose the memory cache budget in the Preferences
* &#91;Graph&#93; Add a "Reset and View in 3D View" option on nodes
* &#91;Content&#93; PBR Converter: Add new Arnold 4/5, Corona 1.6 and Renderman Presets
* &#91;Content&#93; Optimize AutoLevel node and support HDR input
* &#91;Content&#93; Optimize HBAO filter when GPU Optimization is off, add 16 samples version
* &#91;Cooker&#93; output SVG unsupported feature to the log
* &#91;Cooker&#93; Don't discard all the SVG resource if only one feature is not supported
* &#91;UI&#93; Increase Description block size
* &#91;UI&#93; Add file path information on graph instances
* &#91;Functions&#93; Add "Open Reference" on function instances
* &#91;Functions&#93; Display function graphs list when drag anddroping .sbs into a function graph
* &#91;Explorer&#93; Create new 3d resource from primitive
* &#91;Engine&#93; Add $tiling variable
* &#91;Curve&#93; Add options to flip horizontally/vertically the curve
* &#91;Color Management&#93; Read ICC profile on bitmaps
* &#91;Export&#93; Add "Label", "Group" and "User Data" in the Pattern macro list
* &#91;Preferences&#93; add the possibility to change the path for temp files
* &#91;Doc&#93; Add MDL Graph format to the SBS format documentation

**Fixed:**

* &#91;Graph&#93; Cache issue: view outputs in 3D View no longer works
* &#91;Graph&#93; Clear cache issue
* &#91;Graph&#93; Node thumbnails generation requests are not canceled when graph is invalidated
* &#91;Graph&#93; Resolution issues after using F5
* &#91;Graph&#93; graph view missing at launch
* &#91;Graph&#93; Modifying a parameter generates multiple render call
* &#91;Graph&#93; crash when using custom template which contains baked maps
* &#91;Graph&#93; Crash when linked nodes in a graph function
* &#91;3D View&#93; Parallel loading mess up with ProgressManager
* &#91;3D View&#93; Rendering with iray at custom resolution image not full frame
* &#91;3D View&#93;&#91;Iray&#93; Material Definition is not kept
* &#91;2D View&#93; Histogram is empty on LDR images
* &#91;2D View&#93; Display issue when tiling mode is enabled
* &#91;MDL&#93; parameters not exposed
* &#91;MDL&#93; crash when moving a MDL from a package to another while rendering
* &#91;MDL&#93; Don't ask where to assign the MDL when double clicking on graph
* &#91;Bakers&#93; Crash when baking specific .obj file
* &#91;Bakers&#93; Transferred texture from mesh / normal gives a wrong result
* &#91;Transformation 2D&#93; Can't use arrow keys to change offset in 2D transform node
* &#91;Transformation 2D&#93; artefact issue with low resolution
* &#91;Updater&#93; Update report doesn't appear using when Ctrl+o/open
* &#91;Properties&#93;&#91;Format&#93; Some characters are escaped twice in UserTags
* &#91;Bitmap node&#93; Ctrl Z doesn't work on 2D View
* &#91;Preference&#93; Useless empty space in the Aliases tab
* &#91;Installer&#93; Installing a previous version doesn't work the first time
* &#91;Parameters&#93; drop down list: putting some spaces to the last value label freezes SD indefinitely
* &#91;UI&#93;&#91;MAC&#93; "about Substance" displays Iray info
* &#91;SVG&#93; crash when importing a specific SVG
* &#91;Content&#93; HBAO filter: Radius parameter behaves differently in function of the resolution (a new hbao\_2.sbs has been added, old hbao.sbs is now deprecated)

## Version 6

### 6.0.4

*(Released: June 21, 2017)*

**Fixed:**

* &#91;Graph&#93; crash using X shortcut
* &#91;Graph&#93; crashes after deleting a link between nodes
* &#91;Graph&#93; Deleting a split point makes SD crash
* &#91;Content&#93; Typo in mg\_surface\_brush
* &#91;Content&#93; Lower quality on HBAO compared to 6.0.2
* &#91;Library&#93; Custom filter's icons are not saved
* &#91;Explorer&#93; Crash when opening a 3d resource referencing a missing file
* &#91;Bakers&#93; Transfer Texture From Mesh is mirrored if "Normal" option is enabled

### 6.0.3

*(Released: June 01, 2017)*

**Added:**

* &#91;Export&#93; Save physical size as dpi in exported textures
* &#91;2D View&#93; Display the matrix parameter label in the Transformation menu

**Fixed:**

* &#91;Content&#93; Tile Sampler: Position Color parametrization is not normalized
* &#91;Content&#93; Crop: Ghost graph in pixel processor
* &#91;Content&#93; Panorama Shape: Hotspot is mirrored in RGB channel
* &#91;Content&#93; HBAO filter can generate negative resolution
* &#91;Content&#93; Color Match filter renders incorrectly in some situations
* &#91;Content&#93; "Pre-Multiplied to Straight" removes alpha channel
* &#91;Content&#93; Typos in various Labels
* &#91;Graph&#93; Bit depth information is cut when DPI scaling is set to 125,1520 or 175%
* &#91;Graph&#93; When a selection containing a frame is pasted, the frame it not selected
* &#91;Graph&#93; When a selection contains a comment, the pasted elements will be shifted in the graph
* &#91;Graph&#93; split points issue
* &#91;Graph&#93; Some Pin Connectors don't snap when hovered
* &#91;Graph&#93; graph view missing at launch
* &#91;Export&#93; missing bitmaps after export
* &#91;Export&#93; Doesn't export the dependencies on steam version
* &#91;Bakers&#93; crash with mesh which has too much UV sets
* &#91;Bakers&#93; UV map baker crash when baking meshes without UV sets
* &#91;Engine&#93; Sampler bug with Fxmap+HDR
* &#91;Engine&#93; crash with high resolution jpeg images
* &#91;2D View&#93; Transform widget missing in 2D View when tiling preview mode enabled
* &#91;3D View&#93; Graph instance with custom usage is not correctly sent to the 3D View
* &#91;Preferences&#93; Wrong path for mikktspace.dll
* &#91;Explorer&#93; moving a bitmap resource in a package makes the "link/embed" menu popping up
* &#91;Parameters&#93; crash when using 'tiling' as parameter name
* &#91;MDL&#93; no colored links between nodes
* &#91;Linker&#93; Pixel Processor: Incorrect GLSL shaders generation
* &#91;Cooker&#93; Bit depth issue

### 6.0.2

*(Released: March 17, 2017)*

**Added:**

* &#91;Engine&#93; Integrate latest engine with jpeg decompression optimization

**Fixed:**

* &#91;Content&#93; Clone patch not working anymore
* &#91;Content&#93; Height output is not part of the material group in templates
* &#91;MDL&#93; Crash when deleting a graph instance
* &#91;MDL&#93; No warning between conflicting nodes
* &#91;MDL&#93; Useless warning messages when exporting
* &#91;Curve&#93; Adressing parameter exposition should not be exposable
* &#91;Engine&#93; Crash importing a sbsar which contains a HDR bitmap
* &#91;Text Node&#93; Font specification generates invalid XML file
* &#91;Gradient editor&#93; Values are not clamped correctly
* &#91;3D View&#93; Crash when using a custom (high resolution) HDRi as environment

### 6.0.1

*(Released: March 03, 2017)*

**Added:**

* &#91;Bakers&#93; Improve progress task management
* &#91;Bakers&#93; Change the error tooltip when no mesh is selected
* &#91;Properties&#93; 3DView Post Effect parameters should be disabled when "Post Process" are disabled in Preferences
* &#91;License&#93; Allow specifying a custom path for Substance Designer 6 license
* &#91;Gradient&#93; Disable the "precision" slider if no gradient picking has been made
* &#91;Cooker&#93; Ignore missing resource in image input to prevent cooking fail
* &#91;3D View&#93; Change handling of specular reflections leaks
* &#91;Graph&#93; Add more parameters for the engine v6 compatibility

**Fixed:**

* &#91;Bakers&#93; Normal Map from mesh (world space) is flipped on Y axis
* &#91;Bakers&#93; Baking a mesh with no UV fails to report error
* &#91;Bakers&#93; Average normal doesn't work
* &#91;Bakers&#93; SD crashes when baking AO with a specific mesh
* &#91;Bakers&#93; Output format is not restored properly
* &#91;Text&#93; custom font doesn't work in player
* &#91;Text&#93; invalid font warning when re opening a package with font in resources
* &#91;Text&#93; text input does not work in preview mode
* &#91;Text&#93; Font parameter can be exposed
* &#91;Text&#93; freeze/crash when creating a function in the text parameter
* &#91;Text&#93; Crashes when exposing font size
* &#91;2D View&#93; Zoom percentage is not displayed correctly when using the "F" key
* &#91;2D View&#93; Image is shifted when the size is changed
* &#91;2D View&#93; Discontinuity when displaying the tiling
* &#91;2D View&#93; Transformation guizmo is not visible/editable in preview mode
* &#91;3D View&#93; Physical Size not taken into account by PBR Parralax shader
* &#91;3D View&#93; Refresh rate setting is not correctly restored from one session to another
* &#91;Graph&#93; multiangle\_to\_normal prevent publishing
* &#91;Graph&#93; Output size of pow filter is locked
* &#91;Graph&#93;Cannot instantiate .sbsar files
* &#91;Curve&#93; UI cropped
* &#91;Curve&#93; Numbers display is slightly cropped
* &#91;Curve&#93; Widget disappear when the toolbar gets resized
* &#91;Content&#93; Glow node is broken
* &#91;Content&#93; Tile Sampler: Patterns are invisible if the the tiling is disabled
* &#91;Content&#93; MG Mask Builder - Inverted Curvature contrast parameters
* &#91;Content&#93; Color Equalizer: custom\_color\_variation group parameters not connected
* &#91;Content&#93; Clone Patch: patch area not visible when positioned in corners
* &#91;Explorer&#93; Reloading a package while its dependency is opened breaks the dependency package
* &#91;Explorer&#93; Can't import a 32bit psd resource
* &#91;Publish&#93; cooking fail (ERR:No inheritance (absolute))
* &#91;Gradient&#93; Gradient should be displayed as Linear when sRGB is unchecked
* &#91;Transformation2D&#93; Offset impression when moving a guizmo with axis constraint
* &#91;Parameters&#93; Mouse focus is stolen by dropdown
* &#91;Engine&#93; No Tiling has no effect on distance node on GPU engine
* &#91;Export&#93; Crash when exporting outputs as TGA
* &#91;MDL&#93; export preset doesn't work

### 6.0.0

*(Released: February 14, 2017)*

<b>Added:</b>

* &#91;Engine&#93; New Curve Node
* &#91;Engine&#93; New Text Node
* &#91;Engine&#93; 16f/32f bit depth compositing
* &#91;Engine&#93; instancing for GPU FX-maps
* &#91;Engine&#93; Add log2 function
* &#91;Bakers&#93; 8k map baking
* &#91;Bakers&#93; Bake by Material / "Texture Set"
* &#91;Bakers&#93; Display loading message when the bitmap output is being encoded/written on disk
* &#91;Bakers&#93; Add a cancel option during baking
* &#91;Gradient node&#93; add global adjustments for multiple selected keys
* &#91;Gradient Node&#93; Simplify Gradient Picker options
* &#91;Graph&#93; Add an option to modify default parent size
* &#91;Graph&#93; Display Image pixel depth under the node
* &#91;Preferences&#93; Global preferences for DirectX/OpenGL
* &#91;Preferences&#93; Use tabs in Preferences/Project UI
* &#91;Preferences&#93; remove parameter MaxTextureSize located in the "3DView" preferences
* &#91;Preferences&#93; Display short help about the autosave
* &#91;Preferences&#93; Expose image format options
* &#91;Preferences&#93; Add an option to hide the Environment map in 3D View by default
* &#91;Preferences&#93; Add an option for the normal map filter default alpha option
* &#91;2D View&#93; Add the possibility to pan away from texture bounds
* &#91;2D View&#93; Interpret the physical size X/Y ratio
* &#91;3D View&#93; Improve Texture management
* &#91;3D View&#93; Disable Post Effects by default (to prevent crash on lowend gpu)
* &#91;MDL Graph&#93; Manage the hidden flag on IRay parameter
* &#91;MDL Graph&#93; Allow to set the constructor 'material()' as Root Node
* &#91;MDL Graph&#93; Create SBS Graph instance node preview
* &#91;Content&#93; Add new Scan Processing filters
* &#91;Content&#93; Add new Adjustment filters (Clamp, Pow, HDR Range Viewer)
* &#91;Content&#93; Add Blue Noise (Fast approximation)
* &#91;Content&#93; Add new Shape effects (Glow, Drop shadow, Stroke)
* &#91;Publish&#93; Add an action "Export as previous" to republish the last selected package
* &#91;Publish&#93; Improve SBSAR generation when using high resolution bitmaps
* &#91;Publish&#93; Warn user about non "relative to parent x1" graph setting when publishing or uploading on Share
* &#91;Properties&#93; Add "Physical Size" attribute on SBS Graphs
* &#91;Parameters&#93; Remove function actions on PKG Resource paths
* &#91;Parameters&#93; Remove "Preview values changed" pop up

<b>Fixed:</b>

* &#91;Graph&#93; Memory usage grows up regulary each time right-click menu is open
* &#91;Graph&#93; &#91;In SSE2&#93; Polygon's nodes doesn't displays shapes when the "Scale" parameter is in negative
* &#91;Graph&#93; Crash when switching from "Integer" to "Float" on a exposed parameter
* &#91;Graph&#93; Moving nodes while a splitpoint is selected will recompute the nodes
* &#91;Graph&#93; Split Points do not support "Undo"
* &#91;Graph&#93; empty tooltip displayed when graph description contains non printable characters
* &#91;MDL Graph&#93; Crash when the current node displayed in property view is deleted
* &#91;MDL Graph&#93; MDL Graph that uses material() constructor function as root are not rendered correctly in the 3D View
* &#91;MDL&#93; Cannot export MDL module when using conditional operator with uniform boolean expose parameter
* &#91;MDL&#93; Crash when Loading a MDL Graph Template two times
* &#91;MDL Archive&#93; Materials that are using a texture are not correctly managed
* &#91;3D View&#93; IRay Material is not changed when the MDLGraph's root node change
* &#91;3D View&#93; random crash when closing the 3D View while a mesh loading is in progress
* &#91;3D View&#93; Yebis isn't reactivated after saving render
* &#91;3D View&#93; Invalid PSD File generated when saving render result of iray scene
* &#91;3D View&#93; point light 1 will not illuminate
* &#91;UI&#93; Detection area of Checkboxes is too wide in "Bakers from Mesh" Parameters
* &#91;UI&#93; Aesthetic issue in "Bakers from Mesh" Parameters
* &#91;Mac&#93; Opening SD by double clicking on a sbs does not send output to 3d view
* &#91;Mac&#93; &#91;Iray&#93; Photoreal Cluster render doesn't work on MacOS
* &#91;Engine&#93; Atan2(0, 0) makes the engine crash
* &#91;Engine&#93; Critical synchronization issue
* &#91;Bakers&#93; Can't disable automatic normalization for Height baker
* &#91;Parameters&#93; when converting grayscale to rgba, alpha should be 255
* &#91;Functions&#93; It is possible to set a function as the output node even if not compatible
* &#91;Export&#93; Invalid dependencies after exporting a Package with PSD's Resources
* &#91;Console&#93; Clearing the console makes SD crash

## Version 5

### 5.6.2

*(Released: February 08, 2017)*

**Fixed:**

* &#91;Preferences&#93; Default shader is not taken into account
* &#91;3D View&#93; Crash if the default shader is changed at runtime
* &#91;Engine&#93; get $size issue

### 5.6.1

*(Released: January 17, 2017)*

**Added:**

* &#91;3D View&#93; Set primitives size to 100cm
* &#91;Content&#93; Add "Image Input Filtering" to "Splatter Circular" and "Splatter"
* &#91;Bakers&#93; "Curvature From Mesh" Add Console Warnings under Channel "Mesh Sanity Check"

**Fixed:**

* &#91;3D View&#93; Disappear when undocked
* &#91;Graph&#93; Gradient Map "Noise" and "Precision" parameters don't work anymore
* &#91;3D View&#93; ALT+R doesn't work after saving render
* &#91;Bakers&#93; "Curvature From Mesh" crash with some ZBrush meshes

### 5.6.0

*(Released: December 15, 2016)*

**Added:**

* &#91;Content&#93; Added new "AO (Horizon Base Ambient Occlusion)" filter
* &#91;Content&#93; Added new "Height Blend" Filter
* &#91;Content&#93; Added new "Height to Normal (world units)" filter
* &#91;Content&#93; Added new "Material Height Blend" filter
* &#91;Content&#93; Added new "Snow Cover" filter
* &#91;Content&#93; Added new "Water Level" filter
* &#91;Content&#93; Added new "Color Match" filter
* &#91;Content&#93; Added new "Histogram Scan (Non Uniform)" filter
* &#91;Preferences&#93; &#91;UI&#93; Add an option in Preferences to disable the High-DPI detection
* &#91;3d View&#93; Add a "reset camera position" option
* &#91;Iray&#93; Integrate IRay SDK 2016.2 for Pascal architecture Support
* &#91;Graph&#93; Add "Copy Node information to the clipboard" option on contextual menu

**Fixed:**

* &#91;MDL&#93; alg material root is not removed on exported preset
* &#91;MDL Graph&#93; links for missing resource are not deleted in the MDL graph
* &#91;Library&#93; Creating a new filter creates two base conditons
* &#91;Library&#93; Folders doesn't filters anymore library's content
* &#91;Bakers&#93; Progress Bar does come and go
* &#91;Bakers&#93; Non existant cage resource prevents to bake
* &#91;Content&#93; Various errors in "Functions.sbs"
* &#91;Export&#93; File format is always reset to png
* &#91;UI&#93; Substance Designer UI Scaling Issue
* &#91;Graph&#93; Crash when moving the original package of a graph instance
* &#91;Preferences&#93; if the default shader/tangent plugin/.. are not found use the ones defined in the default project
* &#91;Parameters&#93; Sliders have to much precision on Mac
* &#91;Explorer&#93; Move 3D mesh from a folder to another corrupts this resource
* Closing the window doesn't kill SD process
* File open dialog does not display files with the "All format" filter

### 5.5.3

*(Released: October 28, 2016)*

**Fixed:**

* &#91;Shelf&#93; Crash when creating folder
* &#91;Bakers&#93; World\_Space\_Direction doesn't work anymore

### 5.5.2

*(Released: October 18, 2016)*

**Added:**

* &#91;MDL Graph&#93; Propagate SBS Graph default values to SBS Graph Node instance in MDL Graph
* &#91;MDL&#93; Support Drag&amp;Drop of SBSAR graph
* &#91;IRay&#93; upgrade to SDK 2016.1.6 (261500.16187)
* &#91;sbsrender&#93; Optimise the memory management of sbsrender to match of Player performances
* &#91;3D View&#93; Allow the widget size to be smaller than the top menu bar
* &#91;Console&#93; Allow to copy some lines to the clipboard

**Fixed:**

* &#91;Player&#93; Crash when playing a Package directly in Designer by the "play button"
* &#91;Startup&#93; popup display missing nvcuvid.dll file
* &#91;Environment init&#93; double clicking an .sbs file does not load it in SD
* &#91;Export&#93; Export with dependencies crash
* &#91;MDL&#93; Synchronization issue in between a Graph an its Instance
* &#91;MDL&#93; sbsar instance nodes are outputing texture\_return instead of values
* &#91;IRay 3D View&#93; In Iray Renderer the "Height Channel" isn't updated properly when you change of height map
* &#91;IRay 3D View Undocked&#93; "Camera&gt;Save Render" Doesn't work after hiding app in the Windows's Taskbar
* &#91;Mac IRay&#93; NVIDIA GPU no more detected by IRay
* &#91;Bakers&#93; Transferred Texture from Mesh Crash when baking Non POT textures
* &#91;Crash&#93; Crash when exporting a graph on Substance Share
* &#91;Graph&#93; Crash when selecting a ghost instance
* &#91;3D View&#93; Can't dolly (Zoom In or Zoom Out) the orthographic camera in Iray mode
* &#91;UI&#93; Color Picker doesn't manage High DPI display
* &#91;Graph&#93; (MacOS 10.11.06) Infinite computation with multi-material blend node
* &#91;Graph&#93; Copy/Paste Graph's content ==&gt; paste in the content and also a reference to that graph
* &#91;Graph&#93; Several multi material blends in scene, it autoselect the wrong outputs
* &#91;Graph&#93; Metal Edge Wear locks up PC
* &#91;Library&#93; The "SBSAR" files displays "S" logo instead of thumbnails
* &#91;Library&#93; Folder inside .sbsar are displayed in library

### 5.5.1

*(Released: September 08, 2016)*

**Added:**

* &#91;Iray&#93; Add "IQ" mode for cloud rendering
* &#91;Iray&#93; Update to Iray SDK 2016.1.5

**Fixed:**

* &#91;MDL&#93; View in 3D View does not work properly the first time
* &#91;MDL&#93; gradient\_interpolation\_linear is not exported with the full path
* &#91;MDL&#93; newly created frame bottom right corner is exactly aligned with the related node
* &#91;MDL&#93; Root material thumbnail does not update in some cases
* &#91;MDL&#93; Crash when delete all nodes and redo
* &#91;MDL&#93; Sluggish performances in the graph display compared to Substance Graph
* &#91;MDL&#93; Can't export MDL module because of IOR parameter
* &#91;MDL&#93; Displayed parameters don't correspond to the selected node
* &#91;3D View&#93; MDL Material that comes from an MDL Graph is not reseted when root node is deleted
* &#91;3D View&#93; Default camera framing is lost after loading fbx's mesh
* &#91;3D View&#93; Texture assignment is not kept when switching to Iray
* &#91;Iray&#93; Warning message from IRay when moving camera
* &#91;Iray&#93; Crash when switching to Iray
* &#91;Iray&#93; VCA password is not saved
* &#91;Graph&#93; Crash when deleting nodes
* &#91;Graph&#93; Pressing CTRL to copy link doesn't work with Material mode
* &#91;Graph&#93; Crash when deleting output node in an instance node material
* &#91;Bakers&#93;&#91;3D View&#93; Can't load high definition mesh
* &#91;Mac&#93;&#91;3D View&#93; Crash when trying to restore detached windows on secondary monitor
* &#91;Parameters&#93; Cannot edit a value in a spinboxedit without removing the suffix
* &#91;UI&#93; Use "Cancel" when closing SD should stop message box
* Crash when opening two 3D Views
* Crash in Alg::Scripting::Engine when using lots of VisibleIf condition
* Files get deleted by autosave if a .algautosave file exists

### 5.5.0

*(Released: August 25, 2016)*

<b>Added:</b>

* Substance Designer is now available on Linux
* New MDL (Material Definition Language) Editor
* &#91;Bakers&#93; New Curvature from mesh baker
* &#91;Library&#93; Use SVG icons instead of bitmap files
* &#91;Library&#93; Add an option to filter the result for MDL, Compositing, Function and Fxmap
* &#91;Graph&#93; Extend the "Display newly created node" to copy/pasted / duplicated nodes
* &#91;New Document&#93; Create a Template selection widget when creating a new MDL Graph
* &#91;3D View&#93;&#91;Iray&#93; Display Render Mode + VCA nodes next to iterations/time
* &#91;3D View&#93; Improve "material" menu performances on opening
* &#91;3DView&#93;&#91;Bakers&#93; Update to FBX SDK 2017
* &#91;3D View&#93; Add the ability to show/hide rendering information (resolution, iterations, etc.) in the display menu of 3D View
* &#91;Iray&#93; Expose tesselation parameters back to scene edit
* &#91;Project&#93; Add auto-generated alias for project file directory
* &#91;Project&#93; Specify the default environment texture in the project settings
* &#91;Content&#93; Added new studio HDRi
* &#91;Content&#93; Add non-square transform node to the library
* Launch SD with a specific .sbscfg file

<b>Fixed:</b>

* ﻿&#91;Graph&#93; Inputs does not automatically connect to outputs with same usage.
* &#91;Graph&#93; Inserted node inputs are not plugged correctly
* &#91;Graph&#93; Unselecting should also select a node under the mouse
* &#91;Graph&#93; Node insert doesn't connect to all links
* &#91;Bakers&#93; Incorrect diffusion in curvature baker
* &#91;Bakers&#93; "Transferred texture from mesh" crashes if high def mesh has no UVs
* &#91;UI&#93; Function Icon on parameters is not modified when a function is defined
* &#91;UI&#93; Tooltips for parameters are cut
* &#91;3D View&#93; more than 1000 lights are displayed in the scene
* &#91;3D View&#93; GLSL Lambert shader don't manage srgb texture correctly
* &#91;3D View&#93; Tiling parameters missing when connecting substances in Iray
* &#91;Iray&#93; Preset export of mdl not working when spaces in name
* &#91;Iray&#93; Subdvision parameters are not taken into account
* &#91;Parameters&#93; Parameter identifier is no more displayed
* &#91;Parameters&#93; Crash when changing resource url from the "From Resource..." action
* &#91;Parameters&#93; Incorrect conversion of &amp; character
* &#91;Explorer&#93; double clicking on a 'big' graph often fail to open it in the graph view
* &#91;Explorer&#93; Embedded SVGs are shown as missing in the Explorer
* &#91;Explorer&#93; Crash when renaming an item with the '&amp;' character
* &#91;Content&#93; Gradient 1 tiling is wrong when using 90/180° rotation
* &#91;Perforce&#93; Integration does not seem to work if the workspace is located at the HDD root
* &#91;Data&#93; UID generated for nodes are not unique
* &#91;Preferences&#93; Adding an alias targeting HDD root messes up paths in sbsprj
* &#91;MEMORY LEAK&#93; Some QDialogs are not destroyed when they are closed

### 5.4.0

*(Released: April 29, 2016)*

**Added:**

* Add a link to Substance Store
* &#91;UI&#93; Support for High-DPI resolutions
* &#91;UI&#93; Allow to reorder tabs
* &#91;3D View&#93; Allow to export render to ArtStation
* &#91;3D View&#93; Add the default shader in the shader list
* &#91;Graph&#93; Display the resource name on top of bitmap node
* &#91;Graph&#93; Improve the listing order of the space bar search menu
* &#91;Bakers&#93; New baker "Position from Mesh"
* &#91;Bakers&#93; New "normal map" setting for Texture Transfert baker
* &#91;Bakers&#93; New setting "Tangent" &amp; "Binormal" for World Space Normal baker
* &#91;Scripting&#93; Allow to execute scripts during Save, Export and Publish actions
* &#91;Dependencies&#93; Add a Collapse/Expand option based on selection
* Added a warning regarding shell extension conflicts

**Fixed:**

* Crash on exit
* Substance Designer process can still be running after exit
* &#91;Iray&#93; Outputs are not sent to mdl materials when switching renderer
* &#91;Content&#93; Tile sampler: pattern rotation random should not rotate the shape

### 5.3.5

*(Released: April 06, 2016)*

**Fixed:**

* &#91;2D View&#93; Transformation 2D right click menu option is available on any node
* &#91;2D View&#93; transformation 2d gizmo still editable after transformation node deletion
* &#91;3D View&#93; Environment path should not be displayed in the Environment Parameters
* &#91;3D View&#93; Post effects parameters are not saved in 3D resources
* &#91;3D View&#93; Toolbar menu does not behave like a regular menu
* &#91;Preferences&#93; Can't set the "Engine Cache limite" higher than 4095
* &#91;Preferences&#93; Setting a default shader is not taken into account
* &#91;Iray&#93; Color parameters are not correctly retrieved
* &#91;Iray&#93; MDL material colors are reset
* &#91;Iray&#93; Bitmaps are not exported along with the MDL preset
* &#91;IRay/Mac&#93; Resizing 3D View makes Mac workstation crash
* &#91;Graph&#93; PSD Document fails to export
* &#91;Graph&#93; Incorrect displayed node size
* &#91;Function Graph&#93; Sample node input image is not editable if only one image is plugged
* &#91;Engine&#93; Crash when computing Fxmap graph
* &#91;Engine OGL&#93; Error in pixel processor generation
* &#91;Gradient&#93; Gradient Picker does not work on mac
* &#91;PSD&#93; 8bit image not correctly converted to 16bit
* &#91;Parameters&#93; Level histogram widget does not have the same height in color and grayscale
* &#91;Console&#93; Clicking on a cell scrolls the view horizontally
* &#91;Explorer&#93; Relocated 3d resource are not correctly opened in 3d view

### 5.3.4

*(Released: January 16, 2016)*

**Fixed:**

* &#91;Iray&#93; tangent/binormal are not correctly taken into account
* &#91;Explorer&#93; Package is marked as to be saved just after being opened
* &#91;3D View&#93; IBL Diffuse reflection is too strong
* &#91;3D View&#93; Crash when drag&amp;droping 8bit image from explorer to 3D View
* Application crashes since 2016 January 1st

### 5.3.3

*(Released: November 10, 2015)*

**Added:**

* &#91;Content&#93; Add "White Noise Fast" (based on pixel processor)
* &#91;Content&#93; Add "Offset global horizontal/vertical" on Tile Samplers

**Fixed:**

* Crash when creating new Substance in some situations
* &#91;Bakers&#93; Crash when baked maps are updating the graph
* &#91;Bakers&#93; OBJ coming from zbrush should use filename for Match By name
* &#91;Parameters&#93; Crash when doing Undo/Redo/Undo in function graph
* &#91;Graph&#93; Split points are not pasted at the correct location

### 5.3.2

*(Released: October 30, 2015)*

**Added:**

* &#91;Content&#93; Add filtering control for pattern input on Tile Generators

**Fixed:**

* &#91;3D View&#93; Focus point not correctly initialized
* &#91;3D View&#93; Wrong far clip plane when switching several times of 3D mesh resources
* &#91;3D View&#93; Brief rendering artefact when loading a mesh
* &#91;3D View&#93; Environment map is black when file can't be found -&gt; fallback to default envmap
* &#91;3D View&#93; Crash after using a custom Latitude/Longitude image
* &#91;3D View&#93; Crash when loading specific obj file
* &#91;3D View&#93; mesh autoreload does not work properly
* &#91;Iray&#93; Can't assign texture on external mdl
* &#91;Iray&#93; Can't assign textures to anisotropy channel after material reset
* &#91;UI&#93; Windows popup menu appears when right mouse button is released after moving in 3DView
* &#91;2D View&#93; Info tool does not return the color value of the pixel under the cursor
* &#91;Bakers&#93; Grayscale images are saved as indexed with tga format
* &#91;Graph&#93; View outputs in 3d view should reset the channels before sending the outputs to 3d view
* &#91;Parameters&#93; Param input name is empty when exposed from "Expose node parameters"
* &#91;Performances&#93; Set the onSubstanceCallbackProfileEvent callback on engine ONLY if timings are enabled

### 5.3.1

*(Released: October 21, 2015)*

**Added:**

* &#91;3D View&#93; Display the mesh name in the scene/edit instead of "Entity"
* &#91;3D View&#93; Reset to default color when a new 3D View is opened
* &#91;3D View&#93; Focus camera when switching from scene to primitive
* &#91;3D View&#93; Display the render viewport resolution when custom resolution is used
* &#91;Iray&#93; Adjust Subdivision parameters presentation
* &#91;Iray&#93; Output IRay log info to SD log
* &#91;Bakers&#93; Read OBJ files properly to make matching by name compatible

**Fixed:**

* &#91;3D View&#93; Incorrect display of meshes having a scale different than 1.0
* &#91;3D View&#93; Automatic near clip plane computation doesn't work well for big objects
* &#91;3D View&#93; Wireframe mode displays too thick wires
* &#91;3D View&#93; Save render window does not show up if post effects are disabled
* &#91;3D View&#93; Crash when switching geometry
* &#91;3D View&#93; "QOpenGLWidget: Cannot make uninitialized widget current" message in log
* &#91;3D View&#93; Lighting is not computed if the environment map is changed while Iray is running
* &#91;3D View&#93; Crash when viewing 3d mesh
* &#91;3D View&#93; Very bad OpenGL performances after having used Iray
* &#91;3D View&#93; Clip planes not correctly computed
* &#91;3D View&#93; Changing the environment map does not refresh the 3d View
* &#91;3D View&#93; Textures are not updated on graph change
* &#91;3D View&#93; GLSLFX hidden samplers are still displayed in the selection menu
* &#91;3D View&#93; Material not restored properly when opening mesh resource
* &#91;3D View&#93; RAM/VRAM Memory leak when opening various meshes and assigning multiple graphs on them
* &#91;3D View&#93; Focus does not take focal length into account
* &#91;Iray&#93; nvcuvid.dll is missing (uninstall previous version to get rid of the message)
* &#91;Iray&#93; Preset Export dialog '...' button don't spawn the dialog window
* &#91;Iray&#93; Refraction/Scattering does not work correctly in physically\_diffuse\_specular
* &#91;Iray&#93; Default mdl can't be found (magenta color)
* &#91;Iray&#93; Do not plug default textures to mdl material to enable value mode in edit material
* &#91;Iray&#93; Descale is not triggered when a texture is updated
* &#91;Bakers&#93; Worldspace normal baker renders a black image
* &#91;Bakers&#93; Crash when baking normal map with undocked 3d view
* &#91;Bakers&#93; Baking with "Embedded" method while an invalid path is set for "link" prevents saving the resource
* &#91;Bakers&#93; Baking with "Embedded" method and changing the file format does not change the extension on disk
* &#91;Bakers&#93; Random names for embedded ressources all have an XXX.. name
* &#91;Bakers&#93; Multiple objects in .obj are not correctly imported
* &#91;Content&#93; Material Blend: basecolor output is not hidden when channel is disabled
* &#91;Content&#93; White\_noise and derivated are not rendered correctly at 8k
* &#91;Graph&#93; Sluggish performances in the graph
* &#91;Graph&#93; Crash when drag&amp;drop function item from Library to Function Graph
* &#91;Graph&#93; "View outputs in 3d view" should only send the node's visible output in the 3d View
* &#91;Preferences&#93; Default user\_project has empty "Name Suffix" for match by name baker feature
* &#91;Engine&#93; Color -&gt; grayscale conversion produces precision lost
* &#91;Console&#93; Console/Log is poluted by lots of messages
* &#91;Share&#93; Crash when trying to share a package
* &#91;UI&#93; Tooltip is stuck on top of Recent Files menu
* Crash on exit

### 5.3.0

*(Released: October 01, 2015)*

<b>Added:</b>

* &#91;3D View&#93; Add Nvidia Iray renderer
* &#91;3D View&#93; Rotate environment using CTRL+Shift+RMB
* &#91;3D View&#93; Render the 3D viewport at a custom resolution (Ogl / Iray)
* &#91;3D View&#93; Make the loading of the scene asynchronous
* &#91;3D View&#93; Display the global scene in the scene Browser
* &#91;3D View&#93; Disable the grid by default
* &#91;3D View&#93; Add inverse squared distance attenuation for point lights
* &#91;3D View&#93; Display color parameter in RGB instead of RGBA
* &#91;3D View&#93; Separate Lights/Camera/Environment settings
* &#91;Share&#93; Improvements for the Substance Share upload window

<b>Fixed:</b>

* &#91;3D View&#93; Error in normalization of PBR shaders
* &#91;3D View&#93; Crash when right-clicking on the root in the scene browser
* &#91;3D View&#93; PBR shaders : diffuse vs spec energy conservation and pointlights
* &#91;3D View&#93; Make "Material/Reset" also reset the channels to default color
* &#91;Bakers&#93; Position with Bsphere normalization in not centered
* &#91;UI&#93; Windows floating state not saved when closing the application
* &#91;Cooker&#93; Can't publish when the sbs is located in a path containing special character
* &#91;Publishing&#93; Pressing "enter" in the name field after publish will cancel the dialog
* &#91;Share&#93; Export sbs does not keep the sbs:// alias

### 5.2.5

*(Released: September 15, 2015)*

**Added:**

* &#91;Share&#93; Publish a package to Substance Share
* &#91;UI&#93; Add Substance Share link in the Help menu

**Fixed:**

* &#91;Cooker&#93; "Size out of bounds" is an error instead of a warning
* &#91;Cooker&#93; "Can't find subgraph output" is an error instead of a warning
* &#91;3D View&#93; PBR diffuse/spec prefers basecolor instead of diffuse
* &#91;3D View&#93; Tiling does not work correctly with tesselation shaders
* &#91;Engine&#93; Crash when instantiating specific sbsar file
* &#91;Engine&#93; Sizelog2 / pow2 functions does not work properly
* &#91;Engine&#93; "set" in output size does not work
* &#91;Engine&#93; Mipmap level is not clamped for negative values
* &#91;Content&#93; Can't publish a graph containing tri planar filter

### 5.2.1

*(Released: August 27, 2015)*

**Fixed:**

* &#91;Graph&#93; Crash when computing specific sbsar
* &#91;Graph&#93; Crash when instantiating fxmap with multiple image inputs
* &#91;Engine&#93; Crash with sizelog2
* &#91;Engine&#93; Exposed parameter default value is ignored with DX10 Engine
* &#91;Library&#93; Thumbnail computation is broken when project contains invalid alias
* &#91;Cooking&#93; Set "unknown\_parameter" and "duplicated parameter" as warning instead of errors
* &#91;Preferences&#93; Engine Cache limit is blocked at 4095 Mb
* &#91;Function&#93; input parameter label is interpreted as identifier

### 5.2.0

*(Released: August 18, 2015)*

**Added:**

* &#91;Library&#93; Add an option in the preferences to hide/display PSD layers
* &#91;Parameters&#93; Allow user data to be on multiple lines
* &#91;Graph&#93; Add a preference option to render comments at constant size
* &#91;Graph&#93; Add a preference option to disable new node display in 2D View
* &#91;Performances&#93; Pixel Processor performances boost on DX10 engine
* &#91;3D View&#93; Add tessellation to PBR shaders
* &#91;3D View&#93; Add simple opacity to PBR shaders (no face sorting)
* &#91;Content&#93; Add Vray/Corona/Redshift/Arnold targets to the PBR converter filter (to convert maps for these renderers)
* &#91;Content&#93; Add "Detail Oriented" technique to Normal combine filter

**Fixed:**

* Crash when opening sbs with empty dependency
* Link to PSD layers are broken after package reload
* &#91;Functions&#93; Nested functions break type safety
* &#91;Functions&#93; Labels and Groups and Descriptions are not displayed
* &#91;Functions&#93; Crash when copy/pasting from a deleted function
* &#91;Graph&#93; Material link broken with sbsar graphs
* &#91;Graph&#93; Creating multiple bitmap node from resources make the node stacked on each other
* &#91;Graph&#93; comment item not created in the right position when child of a node
* &#91;Graph&#93; Long comments block region selection
* &#91;Bakers&#93; Tangent Space Normal map bakes black on Mac
* &#91;Parameters&#93; Visible If does not work when input name contains "-"
* &#91;Parameters&#93; Step value in Input Parameters ignored if below 0.01
* &#91;Library&#93; "Visible in library" tag is not taken into acount for sbsar

### 5.1.1

*(Released: June 04, 2015)*

**Added:**

* &#91;Graph&#93; Reduce space between two nodes when using autoconnect
* &#91;Graph&#93; Disable Autoconnect when using drag&amp;drop in the graph
* &#91;Graph&#93; Make the frame snap on the grid
* &#91;Graph&#93; Disable node insert over/on selected link for material link
* &#91;Preferences&#93; Set max value for Max texture Size to 8192
* &#91;Content&#93; Add symmetry options to "Safe Transform" node

**Fixed:**

* &#91;Graph&#93; New node is not snapped on grid
* &#91;Graph&#93; Swapping links can generates loops/crash
* &#91;Graph&#93; Display glitch when nodesize/timings are disabled
* &#91;Bakers&#93; Crash when baking to a resource that uses the same name than the scene
* &#91;Bakers&#93; Default resource name is not taken from the correct project file
* &#91;Engine&#93; Pow2/log function problem
* &#91;Engine&#93; Error in function evaluation
* &#91;Fxmaps&#93; Crash when reset parameter to default
* &#91;FxMaps&#93; Bad function evaluation
* &#91;Preferences&#93; Clicking on project tab crashes SD
* &#91;3D View&#93; Custom usage is converted to lowercase
* &#91;Parameters&#93; Can't reorder elements in dropdown lists
* &#91;Explorer&#93; Crash when moving a function graph in the explorer

### 5.1.0

*(Released: May 28, 2015)*

**Added:**

* &#91;Graph&#93; Search/Display content from the library through space bar menu
* &#91;Graph&#93; Display/open newly created node
* &#91;Graph&#93; link redirection (alt+shift)
* &#91;Graph&#93; select node parents
* &#91;Graph&#93; Swap 2 links (X)
* &#91;Graph&#93; Insert node over a link using drag and drop
* &#91;Graph&#93; Create graph from a node selection
* &#91;Graph&#93; Delete link when using Alt + LMB on a node pin
* &#91;Graph&#93; Don't connect new node to previous using Shift
* &#91;Graph&#93; Add a toolbar for base filters
* &#91;Graph&#93; Improve grid (snapping and resolution)
* &#91;Graph&#93; Move the Comment/Frame/Pin to right click menu
* &#91;Graph&#93; Create node over a selected link
* &#91;Graph&#93; Add icons to function items
* &#91;Graph&#93; Change pin colors in function graph
* &#91;Graph&#93; Use shift to disable node auto connection
* &#91;Graph&#93; Make the selected link drawn over the other links
* &#91;Graph&#93; Add icons to Fxmap nodes
* &#91;Graph&#93; Add a switch to draw curved or rectangular links
* &#91;Function&#93; Make the different vector type more distinct in function graph (pin/link colors)
* &#91;Functions&#93; add icons on nodes and display values for constant / set / get
* &#91;Functions&#93; Add colors to node title
* &#91;Function&#93; Improve performances for function evaluation (use SSE generated code)
* &#91;Function&#93; Display warning if Set/Get node is empty
* &#91;Bakers&#93;&#91;Graph&#93; Dither bitmap when converting to 8bpc
* &#91;Bakers&#93; Average vertex normals in OBJ file if the mesh doesn't contain any
* &#91;Bakers&#93; Match by name: use suffix as separator
* &#91;Parameters&#93; Add option to switch between RGB and HSV on color widget
* &#91;Parameters&#93; Add eye dropper button in color widget
* &#91;Library&#93; Add a category for base content (compositing nodes, fxmap, function..)
* &#91;2D View&#93; Info: add display in &#91;0, 1&#93; range and HSV
* &#91;3D view&#93; Add mipmap support for the environment
* &#91;Dependencies&#93; Clean unused dependencies with updater
* &#91;Updater&#93; Do not save packages automatically

**Fixed:**

* &#91;Crash&#93; when closing package
* &#91;Crash&#93; when opening the dependency manager on an unsaved package
* &#91;Crash&#93; Sample Color bug
* &#91;Engine&#93; FxMap Tiling region deadlock
* &#91;Engine&#93; precision issue with SSE engine with blur and/or blend node
* &#91;Engine&#93; Computation doesn't stop when divide by 0
* &#91;Explorer&#93; crash when exporting package with dependency if containing dependency cycles
* &#91;Explorer&#93; Drag and drop of resources often fails to operate
* &#91;Bakers&#93; Baked normal is rendered black if it's higher than 256\*256
* &#91;Bakers&#93; Saving a package in the same location as the export path will break the path
* &#91;Bakers&#93; Incorrect default target path when package has not been saved yet
* &#91;Engine&#93; Bad pixelsize result when inherited from parent function
* &#91;Dependencies&#93; Unused dependency is not removed
* &#91;Dependencies&#93; crash when opening the dependencies window of package that contains package cycles
* &#91;Graph&#93; marquee selection are rescaled in function of the zoom
* &#91;Graph&#93; link don't "snap" to closest input/output
* &#91;Graph&#93; Wrong undo stack (may generate crashes)
* &#91;Graph&#93; Multiple connect with Ctrl does not work if pin is already plugged
* &#91;3D View&#93; Grid color is affected by background color
* &#91;3D View&#93;&#91;Graph&#93; output node containing multiple usage is not sent correctly to the 3d view
* &#91;3D View&#93; Tesselation shader : compilation bug on AMD GPUs
* &#91;2D View&#93; Pin system problem
* &#91;Functions&#93; Function compilation bug (if else)
* &#91;Preferences&#93; low/high suffix not correctly read from sbsprj
* &#91;Library&#93; Drag and dropping a folder over another removes it
* &#91;Windows&#93; Multiple sessions of SD can be run
* &#91;License&#93; Old license is not kept
* &#91;Content&#93; Edge Detect filter problem

### 5.0.3

*(Released: April 01, 2015)*

**Added:**

* &#91;Preferences&#93;&#91;Bakers&#93; Add an option to compute tbn by vertex or by pixel to match UE4
* &#91;Library&#93; Use bilinear filtering for thumbnails
* &#91;Bakers&#93; Allow the window to be downscale to less than 800px height
* &#91;3DView&#93; Equalize environment map exposure / normalize rotation to get consistent lightning
* Name application shortcut with major version

**Fixed:**

* &#91;Graph&#93; Crash when deleting some ghost nodes
* &#91;Graph&#93; docked node stay docked when duplicating node
* &#91;Graph&#93; Crash when deleting nodes
* &#91;Graph&#93; Export outputs settings are not stored per graph
* &#91;Graph&#93; Invalid node docking state when deleting node
* &#91;Bakers&#93; Errors are not displayed in a dialog box anymore
* &#91;Bakers&#93; Missing resource is not displayed as missing in the baking window
* &#91;Publishing&#93; failed window shouldn't be editable
* &#91;Publishing&#93; Sbsar Incorrect result
* &#91;3D View&#93; Multi-materials from updated FBX meshes are not properly reloaded
* &#91;3D View&#93; Diffuse SH can produce negative values in some cases in PBR shaders
* &#91;2D View&#93; Displayed bit depth for resource images is always 8 bpc
* &#91;Parameters&#93; Parameters are not always displayed in the graph properties
* &#91;Menu&#93; "Export log File.." action don't manage to locate the log.txt file
* &#91;Batchtools&#93; Sbsmutator error
* &#91;Explorer&#93; Loading packages keep the highlight
* &#91;Properties&#93; Crash when clearing a function on an enum parameter
* &#91;Preferences&#93; Mikkt tangent space plugin is not set to default in user\_project
* &#91;Evaluation/Activation&#93; Cannot evaluate/activate online on Windows
* Computing status bar moves the interface when refreshing
* Launch multiple SD at the same time
* Update Player URL when .exe is not found
* File modification on disk not detected correctly

### 5.0.2

*(Released: March 17, 2015)*

**Added:**

* &#91;Library&#93; Add normal control in material\_adjustment\_blend
* &#91;Library&#93; Add blending option for normal in material\_color\_blend
* Upgrade to Qt 5.4.1

**Fixed:**

* &#91;Crash&#93; OSX 10.9 and 10.10 in FreeImage
* &#91;Crash&#93; When opening a fbx file that contains elements without any vertices
* &#91;Graph&#93; Drag and Drop issues
* &#91;Graph&#93; Clear cache shortcut is broken
* &#91;Graph&#93; TGA appears black/transparent in SD
* &#91;Library&#93; TriPlanar Grayscale normal input wrong
* &#91;Library&#93; Edge detect node does not work properly with cpu engine
* &#91;Parameters&#93; Slider range incorrect for float2/3/4
* &#91;Parameters&#93; Doing "Expose Parameters" twice crashes Designer
* &#91;Console&#93; Is not resized correctly
* &#91;Console&#93; Duplication in channel list: View3D and 3DView
* &#91;3DView&#93; Parameters order defined in glslfx are not preserved in the GUI
* &#91;Explorer&#93; Crash when refreshing missing textures on the disk
* &#91;Function&#93; Change value and edit leads to crash
* &#91;Baker&#93; Crash when opening the baking window on a missing 3d ressource
* &#91;PSD&#93; Psdparse crash (missing MSVCR120.dll)
* &#91;About window&#93; Missing line break with Steam version
* &#91;Sbs&#93; Unused new engine features in sbs
* &#91;Sbsar&#93; New features not supported when used in SD
* &#91;Ui&#93; Progress bar doesn't clear once finished after an export with dependencies
* vcomp100.dll not found when launching SD on a freshly installed Windows 7

**Known Issues:**

* &#91;Windows 8&#93; Drag and drop doesn't work at first launch. Restart SD should solve it.

### 5.0.1

*(Released: March 05, 2015)*

**Fixed:**

* Fixed a bug when exporting bitmaps on Windows.

### 5.0.0

*(Released: March 04, 2015)*

**Added:**

* &#91;Export&#93; discard Alpha channel for TGA and BMP when it is full opaque
* &#91;3d View&#93; Set the PBR shader by default
* &#91;2D View&#93; Switch to view image as alpha premultiplied
* &#91;Parameters&#93; Size: Add a Width/Height lock / display values in dropdown lists
* &#91;Dependencies&#93; New dependency manager
* &#91;Dependencies&#93; display/find the node instance corresponding to a dependency
* &#91;Dependency&#93; Open a dependency package in the package explorer
* &#91;Engine&#93; Blend: support Opacity parameter when a mask is used
* &#91;Engine&#93; Blend: Add new blending modes (overlay, screen, softlight, divide)
* &#91;Engine&#93; Blend: support straight alpha blending
* &#91;Egnine&#93; New Dynamic Gradient node
* &#91;Engine&#93; New Distance node
* &#91;Engine&#93; New Pixel Processor node
* &#91;Engine&#93; Fxmap: support dynamic function for input images
* &#91;Engine&#93; Function Sampler: support bilinear sampling
* &#91;Engine&#93; Fxmap: support bilinear/nearest filtering for input images
* &#91;Engine&#93; Fxmap: support Straight/Premultiplied input image alpha
* &#91;Bakers&#93; Add an option to match geometry by mesh name between low and high def meshes
* &#91;Templates&#93; Create a template substance for Substance Painter
* &#91;Bakers&#93; New Texture Map from mesh baker
* &#91;Graph&#93; Add a "compatibility check" to highlight nodes that are not compatible with previous engine
* &#91;UI&#93; Help menu adjustments
* &#91;Preferences&#93; set Mikkt tangent space plugin the default one (reset to default in the preferences if SD4 is installed)
* &#91;Library&#93; Add new hdr maps
* New Substance from Template
* Switch to Qt5
* Update License System to SD5

**Fixed:**

* &#91;Mac Only&#93; Color picker problem with retina display
* &#91;Mac Only&#93; Drag'n'drop on the 3D view on Mac OS also rotate the view
* &#91;Bakers&#93; Baking a map without an output folder produce an empty texture
* &#91;Graph&#93; Docked nodes in frame move in a strange way
* &#91;Parameters&#93; Custom library path are not loaded from sbsprj files
* &#91;3D View&#93; CTRL+R to reload all shader also trigger the reset of the 3D View
* &#91;3D View&#93; Env. Mipmap height uniform switch to default when loading shader
* &#91;3D View&#93; PBR shader : Diffuse vs baseColor typo
* &#91;Library&#93; Non-recursive library path break linked textures in packages
* &#91;Library&#93; Environment Maps doesn't display .hdr
* &#91;Explorer&#93; "Copy/Paste" on the substance shouldn't be possible
* &#91;Explorer&#93; Right click "Paste" option still available on a graph
* &#91;Function&#93; tooltip of the sampler is wrong
* &#91;Graph&#93; In compact mode, instances don't show all the link names when they are expanded automatically to add a greyscale converter
