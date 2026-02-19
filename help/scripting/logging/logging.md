---
title: "Logging"
description: "Learn how to implement logging in Substance 3D Designer Python plugins for debugging and monitoring."
helpx_description: Designer > Scripting > Logging
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/logging.html"
helpx_creative_field:
  - video
  - graphic-design
  - 3d-immersive
  - painting-illustration
helpx_experience_level:
  - any
helpx_learn_topic:
  - preflight
  - output
  - automation
---




# Logging

We recommend using the standard Python's logging module for logging.

The <b>sd</b> module contains helper classes to redirect logging to Designer's console.

## Logging to Designer's console panel

```

import logging 

import sd 

 

 

## Create a logger.

logger = logging.getLogger("MyLogger") 

 

 

## Add a handler to redirect logging to Designer's console panel.

ctx = sd.getContext() 

logger.addHandler(ctx.createRuntimeLogHandler()) 

 

 

## Do not propagate log messages to Python's root logger.

logger.propagate = False 

 

 

## Set the default log level if needed.

logger.setLevel(logging.DEBUG) 

 

 

## Use the logger

logger.info("Info message") 

logger.warning("Warning message") 

logger.error("Error message")
```
