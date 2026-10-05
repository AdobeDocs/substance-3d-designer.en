---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/getting-started/system-requirements.html"
breadcrumb-title: ""
description: Review system requirements for Substance 3D Designer to ensure your computer meets the necessary specifications.
helpx_creative_field: ""
helpx_description: Designer > Getting started > System requirements
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: System requirements
user-guide-description: ""
user-guide-title: ""
---

# System requirements

Below is a list of hardware and systems supported by the application:

## System configuration by platform

### Windows

|             | Minimum                                                                                                  | Recommended                                                                                         | Optimal                                                                                                            |
|:------------|:---------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| **OS**      | Windows 11 64-bit Version 23H2                                                                           | Windows 11 64-bit Version 24H1                                                                      | Windows 11 64-bit Version 24H2                                                                                     |
| **CPU**     | Intel Core i5<br>AMD Ryzen 5                                                                             | Intel Core i7<br>AMD Ryzen 7                                                                        | Intel Core i9<br>AMD Ryzen 9                                                                                       |
| **GPU**     | NVIDIA GeForce RTX 2060 Super<br>NVIDIA Quadro RTX 4000<br>AMD Radeon RX 5700 XT<br>AMD Radeon Pro W5700 | NVIDIA GeForce RTX 3080<br>NVIDIA Quadro RTX A4000<br>AMD Radeon RX 6800 XT<br>AMD Radeon Pro W7700 | NVIDIA GeForce RTX 4090<br>NVIDIA Quadro RTX 5000 Ada Generation<br>AMD Radeon RX 7900 XTX<br>AMD Radeon Pro W7800 |
| **VRAM**    | 8 GB                                                                                                     | 16 GB                                                                                               | 24 GB                                                                                                              |
| **RAM**     | 16 GB                                                                                                    | 32 GB                                                                                               | 64 GB                                                                                                              |
| **Storage** | SSD with 30 GB of available space                                                                        | SSD with 50 GB of available space                                                                   | SSD with 70 GB of available space                                                                                  |

### macOS

|             | Minimum                           | Recommended                       | Optimal                           |
|:------------|:----------------------------------|:----------------------------------|:----------------------------------|
| **OS**      | macOS 14 Sonoma                   | macOS 26 Tahoe                    | macOS 26 Tahoe                    |
| **CPU**     | Apple M1                          | Apple M2 Pro                      | Apple M4 Pro                      |
| **GPU**     | Apple M1                          | Apple M2 Pro                      | Apple M4 Pro                      |
| **RAM**     | 16 GB                             | 32 GB                             | 64 GB                             |
| **Storage** | SSD with 30 GB of available space | SSD with 50 GB of available space | SSD with 70 GB of available space |

### Linux

| Enterprise        | Steam        |
|:------------------|:-------------|
| RHEL 8</br>RHEL 9 | Ubuntu 22.04 |

## General recommendations

* For working in comfortable conditions we recommend a monitor with a resolution greater than 1 Mega Pixel and wider than 1280 pixels.
* Many Substance Apps depend on OpenSSL 1.1.1 for RHEL8/9 compatibility. For systems with newer OpenSSL versions, you will need to provide it manually.
* *Only* versions **2019.x** and above have been notarized in order to run on **macOS 10.15 Catalina**.
* **Remote Desktop** connection is possible if an OpenGL 3.3 context is available. It will work on **Nvidia Quadro** but *not* on Nvidia GeForce because it provides only an OpenGL 1.4 context. If this is an issue, we recommend using alternative solutions such as **VNC/Teamviewer**.
* **Steam** version users should *disable* the **Steam Overlay** for Designer, as it may cause performance issues when active.

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
> For the best overall stability while performing heavy computations on the GPU – e.g. rendering complex graphs, rendering in the 3D view, exporting a scene from the 3D view, etc. – it is strongly recommended to make sure the **Timeout Detection and Recovery (TDR)** values match the recommendations in [this page](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/technical-support/technical-issues/gpu-issues/gpu-drivers-crash-with-long-computations-tdr-crash) of our documentation.

## Unsupported configurations

**Windows**

* Virtual machine are not supported.
* Windows Server is not supported.

**macOS**

* Intel-based macOS systems are not supported.
* Only official Apple configurations are supported.
* eGPUs are not currently supported and may have stability issues.

**Linux**

* Mesa drivers on Linux are not supported.

**Any platform**

* Integrated GPUs are not supported on x86-64 (Intel, AMD) CPUs.
* Using Designer in combination with third-party software that intercepts Designer calls to the graphics drivers is not supported. Such software includes:
  * Post-process injectors such as re-shaders that apply color grading, camera effects, ...
  * On-screen overlays such as custom crosshairs, GPU performance metrics, skins for video streaming...

## Minimum GPU driver versions

Below is a list of the minimum GPU driver versions required for the application to run without issue. This list is subject to changes as new versions release.

To download new drivers see: [GPU has outdated drivers](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/technical-support/technical-issues/gpu-issues/gpu-has-outdated-drivers).

| OS          | NVIDIA                       | AMD                                      | Intel       |
|:------------|:-----------------------------|:-----------------------------------------|:------------|
| **Windows** | GeForce 451.48 Quadro 451.48 | Radeon 19.7.1 Radeon Pro / FirePro 18.Q4 | 15.33       |
| **Linux**   | 535.129.03                   | Radeon 23.20 Pro 23.Q3                   | Unsupported |

>[!NOTE]
>
> On **macOS** the GPU driver is provided by the operating system itself. Update to the latest version of your OS to access the newest driver.

## GPU raytracing for baking

To enable GPU Raytracing via Optix or DXR the drivers recommended above must be installed.

**DXR** requires the following minimum configuration :

* **Windows 10** version 1809, see [this page](https://experienceleague.adobe.com/en/docs/substance-3d/bakers/features/gpu-raytracing) for more information
* **GPU with Pascal architecture** (Nvidia GeForce 10XX)

>[!TIP]
>
> GPU raytracing runs optimally on dedicated ray tracing hardware such as NVIDIA GeForce RTX or NVIDIA Quadro RTX GPUs.

## Using tablets

Tablet users on **Windows** should apply the settings described in the following page to get the most reliable experience: [Configuring pens and tablets](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/technical-support/configuring-pens-and-tablets).

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
