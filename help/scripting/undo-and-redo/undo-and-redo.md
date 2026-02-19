---
title: "Undo and redo"
description: "Learn how to implement undo and redo functionality in Substance 3D Designer Python scripts for user actions."
helpx_description: Designer > Scripting > Undo and redo
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/undo-and-redo.html"
helpx_creative_field:
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - behaviors
  - snapshots
  - organization
---




# Undo and redo

With the <b>SDHistoryUtils.UndoGroup</b> class, users  can *group actions* in order to *undo or redo* them all in one command.

These groups are *named* by users, and will appear by that name in the undo/redo list in the user interface.  This makes large numbers of actions more manageable.

```

import sd 

from sd.api.sdhistoryutils import * 

 

## Get the application and package manager objects.

cxt = sd.getContext() 

app = cxt.getSDApplication() 

pkgMgr = app.getPackageMgr() 

 

## Group one or more changes into an undo group.

with SDHistoryUtils.UndoGroup("My Undo Group"): 

## Create two new packages.

    pkgMgr.newUserPackage() 

    pkgMgr.newUserPackage()
```
