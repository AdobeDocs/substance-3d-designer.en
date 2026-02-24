---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/application-callbacks.html"
breadcrumb-title: ""
description: Learn how to use application callbacks in Substance 3D Designer Python plugins to respond to application events.
helpx_creative_field: ""
helpx_description: Designer > Scripting > Application callbacks
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: Application callbacks
user-guide-description: ""
user-guide-title: ""
---


# Application callbacks

It is possible to register <b>Python callbacks</b> with the application object that Designer will call when specific events happen.

User interface objects, such as menus and buttons, can trigger callbacks using the <b>Qt for Python</b> library. For more information, see [Creating user interface elements](../../help/scripting/creating-user-interface/creating-user-interface-elements.md).

```

import sd 

 

## Our callbacks.

def onBeforeFileLoadedCallback(filePath): 

    print("Before file loaded, file: %s" % filePath) 

 

def onAfterFileLoadedCallback(filePath, succeed, updated): 

    print("After file loaded, file: %s, succeed: %s, updated: %s" % (filePath, succeed, updated)) 

     

def onBeforeFileSavedCallback(filePath, parentPackagePath): 

    print("Before file saved, file: %s, parentPackage: %s" % (filePath, parentPackagePath)) 

 

def onAfterFileSavedCallback(filePath, succeed): 

    print("After file saved, file: %s, succeed: %s" % (filePath, succeed)) 

 

## Get the application.

app = sd.getContext().getSDApplication() 

 

## Register our callbacks.

beforeFileLoadedCallbackID = app.registerBeforeFileLoadedCallback(onBeforeFileLoadedCallback) 

afterFileLoadedCallbackID = app.registerAfterFileLoadedCallback(onAfterFileLoadedCallback) 

beforeFileSavedCallbackID = app.registerBeforeFileSavedCallback(onBeforeFileSavedCallback) 

afterFileSavedCallbackID = app.registerAfterFileSavedCallback(onAfterFileSavedCallback) 

 

## Unregister callbacks when no longer needed.

app.unregisterCallback(beforeFileLoadedCallbackID) 

app.unregisterCallback(afterFileLoadedCallbackID) 

app.unregisterCallback(beforeFileSavedCallbackID) 

app.unregisterCallback(afterFileSavedCallbackID)
```
