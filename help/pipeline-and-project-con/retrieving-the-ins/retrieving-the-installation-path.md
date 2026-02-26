---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/pipeline-and-project-configuration/retrieving-the-installation-path.html"
breadcrumb-title: ""
description: Learn how to retrieve the Substance 3D Designer installation path for scripting and automation purposes.
helpx_creative_field: ""
helpx_description: Designer > Pipeline and Project Configuration > Retrieving the installation path
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Retrieving the installation path
user-guide-description: ""
user-guide-title: ""
---

# Retrieving the installation path

This page regroups information on ways to retrieve the installation path of [Substance 3D Designer](https://www.adobe.com/products/substance3d-designer.html) depending on the version and platform.

## Windows

### Creative Cloud Desktop

1. Open <b>Windows registry editor</b> (regedit)
1. Navigate to the registry key: <b>HKEY\_LOCAL\_MACHINE\Software\Microsoft\Windows\CurrentVersion\App Paths\</b>
1. Open the sub-key named <b>Adobe Substance 3D Designer.exe</b>
1. The value of the key contains the path to the application executable where it is installed

>[!NOTE]
>
> This registry key is only available since version 11.2.  
> For older versions, the installation path can be retrieved from the file associations in HKEY\_CURRENT\_USER\Software\Microsoft\Windows\CurrentVersion\ Explorer\FileExts

### Substance edition (standalone)

1. Open <b>Windows registry editor</b> (regedit)
1. Navigate to the registry key: <b>HKEY\_LOCAL\_MACHINE\ SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall</b>
1. Find the sub-key matching the <b>AppID</b> of your application version (see the table below)
1. The value of the key contains the path to the application installation location

| Version | AppId |
| --- | --- |
| **Version 5.x** | {25E7D16D-1FBA-49EA-BF36-E2D6B20A9206} |
| **Version 6.x** | {09a302b1-8da8-4f62-b0cb-a208faa210f9} |
| **Version 7.x (2017.x) to 11.1** | {e9e3d6d9-3023-41c7-b223-11d8fdd691b9} |
| **Version 11.2 (or newer)** | {662bb79f-5616-44e6-a84d-b3d6abebe002} |

### Steam edition

The application is installed in the steamapps/common/ sub-folder of the Steam installation folder.

## macOS

On Mac the application is installed in the following:

| Version | Path |
| --- | --- |
| **11.2 or newer** | **/Applications/Adobe Substance 3D Designer.app** |
| **Legacy** | **/Applications/Substance Designer.app** |

## Linux

On Linux the rpm package is installed in the following path:

| Version | Path |
| --- | --- |
| **11.2 or newer** | **/opt/Adobe/Adobe\_Substance\_3D\_Designer** |
| **Legacy** | **/opt/Allegorithmic/Substance\_Designer** |
