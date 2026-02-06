---
title: "Plugin basics"
description: ""
helpx_description: "Designer > Scripting > Plugin basics"
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
