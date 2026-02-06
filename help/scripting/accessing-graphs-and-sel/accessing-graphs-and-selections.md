---
title: "Accessing graphs and selections"
description: ""
helpx_description: "Designer > Scripting > Accessing graphs and selections"
---

# Accessing graphs and selections

The <b>SDApplication</b> class contains some helpful methods that let you access the *currently active* graph, and the *current selection* within it.

```

import sd 

 

## Get the application and UI manager object.

ctx = sd.getContext() 

app = ctx.getSDApplication() 

uiMgr = app.getQtForPythonUIMgr() 

 

## Get the current graph.

g = uiMgr.getCurrentGraph() 

print("The current graph is %s" % g) 

 

## Get the currently selected nodes.

selection = uiMgr.getCurrentGraphSelectedNodes() 

for node in selection: 

 print("Node %s" % node)
```


A graph displayed in a *specific* Graph view can be accessed using a <b>graphViewID</b>.

This method is useful when creating custom graph view toolbars. The <b>Creating toolbars in Graph views</b> sample in the [Creating user interface elements](../creating-user-interface/creating-user-interface-elements.md) chapter provides further details.
