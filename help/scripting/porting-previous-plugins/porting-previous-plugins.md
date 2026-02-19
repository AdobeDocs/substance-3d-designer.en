---
title: "Porting previous plugins"
description: "Learn how to port plugins from previous versions of Substance Designer to the current Python API."
helpx_description: Designer > Scripting > Porting previous plugins
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/porting-previous-plugins.html"
helpx_creative_field:
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - interface
  - component
  - automation
---




# Porting previous plugins

Because of the changes done to support Qt for Python, **previous plugins won't work anymore**.  
In particular, please note the following:

## Plugin loading and unloading

Plugins are now loaded when the application <b>starts</b> and are unloaded when it <b>exits</b>.  
As such, it's *not necessary* for plugins to inherit from '*sdplugins.Plugin*' anymore.

For more information, check the [Plugin basics](../plugin-basics/plugin-basics.md) section.

## Creating user interface elements

Plugins *don't need* to define a '*sdplugins.PluginDesc*' anymore.  
Instead, plugins can use the<b> new &#91;UI manager&#93;(https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/scripting-api-next-172825023.html) object</b> and <b>Qt for Python</b> to create any user interface elements they need.

You can find small code samples in the [Creating user interface elements](../creating-user-interface/creating-user-interface-elements.md) section.

## Replacing uses of location context

The '*SDLocationContext*' class has been *removed* from the Python API.  
Plugins can use the <b>&#91;UI manager&#93;(https://helpx.adobe.com/substance-3d/unlisted/documentation/sddoc/scripting-api-next-172825023.html) object</b> to access the currently active graph and selection.

You can find some examples in the [Accessing graphs and selections](../accessing-graphs-and-sel/accessing-graphs-and-selections.md) section.
