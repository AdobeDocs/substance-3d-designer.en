---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/plugin-basics.html"
breadcrumb-title: ""
description: Learn the basics of creating Python plugins for Substance 3D Designer to extend application functionality.
helpx_creative_field: ""
helpx_description: Designer > Scripting > Plugin basics
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Plugin basics
user-guide-description: ""
user-guide-title: ""
---



# Plugin basics

A plugin is a Python file or a Python module that defines an <b>initializeSDPlugin()</b> function.

The <b>initializeSDPlugin()</b> function is called when the plugin is loaded.  
In this function, you can create user interface elements, register callbacks and any other piece of functionality you might need.

Optionally, the plugin can define an <b>uninitializeSDPlugin()</b> function that will be called when the plugin is unloaded.  
You can use this function to free resources, close network connections and similar things.

```

## Plugin entry point. Called by Designer when loading a plugin.

def initializeSDPlugin(): 

 print("Hello!") 

 

## If this function is present in your plugin,

## it will be called by Designer when unloading the plugin.

def uninitializeSDPlugin(): 

 print("Bye!")
```
