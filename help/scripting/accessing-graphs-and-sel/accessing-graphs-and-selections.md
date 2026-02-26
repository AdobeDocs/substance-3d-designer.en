---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/accessing-graphs-and-selections.html"
breadcrumb-title: ""
description: Learn how to access and manipulate graphs and node selections in Substance 3D Designer Python scripts.
helpx_creative_field: ""
helpx_description: Designer > Scripting > Accessing graphs and selections
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Accessing graphs and selections
user-guide-description: ""
user-guide-title: ""
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

This method is useful when creating custom graph view toolbars. The <b>Creating toolbars in Graph views</b> sample in the [Creating user interface elements](../../scripting/creating-user-interface/creating-user-interface-elements.md) chapter provides further details.
