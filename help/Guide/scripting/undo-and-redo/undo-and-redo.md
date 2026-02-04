---
title: "Undo and redo | Substance 3D Designer"
description: "Designer > Scripting > Undo and redo"
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
