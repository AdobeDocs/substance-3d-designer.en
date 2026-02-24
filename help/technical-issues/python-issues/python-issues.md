---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/technical-issues/python-issues.html"
breadcrumb-title: ""
description: Troubleshoot Python scripting issues in Substance 3D Designer including plugin and API problems.
helpx_creative_field: ""
helpx_description: Designer > Technical issues > Python issues
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Python issues
user-guide-description: ""
user-guide-title: ""
---



# Python issues

This page lists technical issues related to Substance 3D Designer's [Python API](../../help/scripting/scripting.md) as well as features implemented in Python, and offer troubleshooting steps for each.

Features implemented in Python include the [Publish](../../help/compositing-graphs/publishing-asset-files/publishing-substance-3d-asset-files-sbsar.md)/[Send to](../../help/interface/the-explorer-window/send-to-interoperability/send-to-interoperability.md) actions in the [Explorer](../../help/interface/the-explorer-window/the-explorer-window.md)'s toolbar, as well as the tool to remove unused nodes in graphs.

## 'QtForPython' module fails to load

<b>!&#91;(error)&#93;(error.svg) Issue</b>

The 'QtForPython' Python module fails to load, which leads to missing features implemented in Python, such as the [Publish](../../help/compositing-graphs/publishing-asset-files/publishing-substance-3d-asset-files-sbsar.md)/[Send to](../../help/interface/the-explorer-window/send-to-interoperability/send-to-interoperability.md) actions in the [Explorer](../../help/interface/the-explorer-window/the-explorer-window.md)'s toolbar, as well as the tool to remove unused nodes in graphs.

Additionally many [Python plugins](../../help/scripting/plugin-basics/plugin-basics.md) will fail to load, or not work as expected.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

There is likely a conflict between Designer's installation of QtForPython and its dependencies, and an existing installation on the system.

Remove any other system installation of [QtForPython](https://doc.qt.io/qtforpython-5/index.html) ([PySide2](https://pypi.org/project/PySide2/)) and [Shiboken2](https://pypi.org/project/shiboken2/).

Alternatively, instead of a system-wide installation of QtForPython you may consider using Python *virtual environments*, or a *package manager* such as [rez](https://github.com/AcademySoftwareFoundation/rez).
