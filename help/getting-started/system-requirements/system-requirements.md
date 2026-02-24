---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/getting-started/system-requirements.html"
breadcrumb-title: ""
description: Review system requirements for Substance 3D Designer to ensure your computer meets the necessary specifications.
helpx_creative_field: ""
helpx_description: Designer > Getting started > System requirements
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
solution: ""
title: System requirements
user-guide-description: ""
user-guide-title: ""
---


# Supported systems

Below is a list of hardware and systems supported by the application:

## Windows

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | Windows 11 64-bit Version 23H2 | Windows 11 64-bit Version 24H1 | Windows 11 64-bit Version 24H2 |
| <b>CPU</b> | Intel Core i5 AMD Ryzen 5 | Intel Core i7 AMD Ryzen 7 | Intel Core i9 AMD Ryzen 9 |
| <b>GPU</b> | NVIDIA GeForce RTX 2060 Super NVIDIA Quadro RTX 4000 AMD Radeon RX 5700 XT AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080 NVIDIA Quadro RTX A4000 AMD Radeon RX 6800 XT AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090 NVIDIA Quadro RTX 5000 Ada Generation AMD Radeon RX 7900 XTX AMD Radeon Pro W7800 |
| <b>VRAM</b> | 8 GB | 16 GB | 24 GB |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### macos

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | macOS 12 Monterey | macOS 13 Ventura | macOS 14 Sonoma |
| <b>CPU</b> | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| <b>GPU</b> | Apple M1 | Apple M2 Pro | Apple M4 Pro |
| <b>RAM</b> | 16 GB | 32 GB | 64 GB |
| <b>Storage</b> | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### Linux

|  | Minimum | Recommended | Optimal |
| --- | --- | --- | --- |
| <b>OS</b> | <b>Enterprise ETLA</b>  RHEL 8.6 or later or RHEL 9.2 or later <b>Steam</b> Ubuntu 22.04.1 LTS | <b>Enterprise ETLA</b>  RHEL 8.6 or later  or RHEL 9.4 or later  <b>Steam</b> Ubuntu 22.04.1 LTS or later | <b>Enterprise ETLA</b>  RHEL 8.6 or later  or RHEL 9.4 or later  <b>Steam</b> Ubuntu 22.04.1 LTS or later |

## General recommendations

* For working in comfortable conditions we recommend a monitor with a resolution greater than 1 Mega Pixel and wider than 1280 pixels.
* Many Substance Apps depend on OpenSSL 1.1.1 for RHEL8/9 compatibility. For systems with newer OpenSSL versions, you will need to provide it manually.
* *Only* versions <b>2019.x</b> and above have been notarized in order to run on <b>MacOS 10.15</b> (Catalina).
* <b>Remote Desktop</b> connection is possible if an OpenGL 3.3 context is available. It will work on <b>Nvidia Quadro</b> but *not* on Nvidia GeForce because it provides only an OpenGL 1.4 context. If this is an issue, we recommend using alternative solutions such as <b>VNC</b>/<b>Teamviewer</b>.
* <b>Steam</b> version users should *disable* the <b>Steam Overlay</b> for Designer, as it may cause performance issues when active.

## Supported GPUs

Below is a list of the GPU compatible with the application :

* NVIDIA GeForce GTX 1060 and above
* NVIDIA Quadro P2200 and above
* AMD Radeon RX 580 and above
* AMD Radeon Pro 5300 M

>[!TIP]
>
> **TDR (Windows only)**
> 
> For the best overall stability while performing heavy computations on the GPU – e.g. rendering complex graphs, rendering in the 3D view, exporting a scene from the 3D view, etc. – it is strongly recommended to make sure the <b>Timeout Detection and Recovery (TDR)</b> values match the recommendations in [this page](https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-drivers-crash-with-long-computations-tdr-crash.html) of our documentation.

## Unsupported configurations

<b>Windows</b>

* Virtual machine are not supported.
* Windows Server is not supported.

<b>macOS</b>

* Intel-based macOS systems are not supported.
* Only official Apple configurations are supported.
* eGPUs are not currently supported and may have stability issues.

<b>Linux</b>

* Mesa drivers on Linux are not supported.

<b>Any platform</b>

* Integrated GPUs are not supported on x86-64 (Intel, AMD) CPUs.
* Using Designer in combination with third-party software that intercepts Designer calls to the graphics drivers is not supported. Such software includes:
  * Post-process injectors such as reshaders that apply color grading, camera effects, ...
  * On-screen overlays such as custom crosshairs, GPU performance metrics, skins for video streaming...

## Minimum GPU driver versions

Below is a list of the minimum GPU driver versions required for the application to run without issue. This list is subject to changes as new versions release.

To download new drivers see: [GPU has outdated drivers](https://helpx.adobe.com/substance-3d-painter/technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers.html).

| OS | NVIDIA | AMD | Intel |
| --- | --- | --- | --- |
| <b>Windows</b> | GeForce 451.48 Quadro 451.48 | Radeon 19.7.1 Radeon Pro / FirePro 18.Q4 | 15.33 |
| <b>Linux</b> | 535.129.03 | Radeon 23.20 Pro 23.Q3 | Unsupported |

>[!NOTE]
>
> On **Mac OS** the GPU driver is provided by the operating system itself. Update to the latest version of your OS to access the newest driver.

## GPU raytracing for baking

To enable GPU Raytracing via Optix or DXR the drivers recommended above must be installed.

<b>DXR</b> requires the following minimum configuration :

* <b>Windows 10</b> version 1809, see [this page](https://helpx.adobe.com/substance-3d-bake/features/gpu-raytracing.html) for more information
* <b>GPU with Pascal architecture</b> (Nvidia GeForce 10XX)

>[!TIP]
>
> GPU raytracing runs optimally on dedicated ray tracing hardware such as NVIDIA GeForce RTX or NVIDIA Quadro RTX GPUs.

## Using tablets

Tablet users on <b>Windows</b> should apply the settings described in the following page to get the most reliable experience: [Configuring pens and tablets](https://helpx.adobe.com/substance-3d-painter/technical-support/configuring-pens-and-tablets.html).

## Languages

The software interface is available in the following languages:

* Deutsch (Deutschland)
* English (United States)
* Español (España)
* Français (France)
* Italiano (Italia)
* Português (Brasil)
* 日本語（日本）
* 한국어(한국)
* 简体中文（中国)
