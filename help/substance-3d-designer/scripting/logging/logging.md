---
title: "Logging | Substance 3D Designer"
description: "Designer > Scripting > Logging"
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
