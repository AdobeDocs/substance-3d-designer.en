---
title: "Crash when rendering graphs"
description: ""
helpx_description: "Designer > Technical issues > Crash when rendering graphs"
---

# Crash when rendering graphs

This page lists crashes occurring during the graph rendering process in Substance 3D Designer, and offers troubleshooting steps for each.

## TDR (Windows only)

<b>&#91;!&#91;(error)&#93;(error.svg)&#93;(https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-drivers-crash-with-long-computations-tdr-crash.html) Issue</b>

The system's <b>Timeout Detection &amp; Recovery (TDR)</b> timer is *too short* to let Substance 3D Designer finish its current computations before the graphics driver is *restarted*.

Computations performed by Substance 3D Designer can be very intensive and use the graphics drivers to a degree which it *does not respond* to the operating system for a while.  
As a stability and security measure, the operating system *restarts the graphics driver*, cutting the computations short and resulting in Substance 3D Designer *crashing*.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

The TDR timer values needs to be *increased* to prevent such crashes. You can do this by following the instructions in [this page](https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-drivers-crash-with-long-computations-tdr-crash.html) of Substance 3D Painter's documentation, which apply to Substance 3D Designer as well.
