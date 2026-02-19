---
title: "Cannot createload a project"
description: "Troubleshoot issues with creating or loading projects in Substance 3D Designer and find solutions."
helpx_description: Designer > Technical issues > Cannot createload a project
helpx_url: "https://helpx.adobe.com/substance-3d-designer/technical-issues/cannot-create-load-a-project.html"
helpx_creative_field:
  - video
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - import
  - cross-product-workflows
  - 3d
---




# Cannot create/load a project

This page lists common causes for failing to create or load projects in Substance 3D Designer, and offers troubleshooting steps for each.

## Application is too old to open URL

**![(error)](error.svg) Issue**

The **Substance 3D file (SBS)** is being loaded by a version of Substance 3D Designer which *does not support its format*. The Substance 3D file was likely *saved in a more recent version* of the software which uses an updated format for these files.

**![(tick)](check.svg) Recommended steps**

As Substance 3D Designer evolves, so does the Substance 3D file format (SBS). More often than not, a new version of the software will need to *update your files* so they can support the latest features.

You are *prompted* to perform this update when *loading the file for the first time* in a new version.

>[!WARNING]
>
> If the file is saved *after* the update was applied, its format version changes as well. At this point, it can *no longer be loaded in previous versions* of Substance 3D Designer.
> 
> This limitation also applies to the [Substance Player](https://helpx.adobe.com/substance-3d-player/home.html).

First, check that you are using the latest version of Substance 3D Designer which your current license allows. Here are the points of access to updates for each edition:

* <b>Adobe Substance 3D subscription:</b> go to the Updates section of the Apps tab in the [Adobe Creative Cloud Desktop](https://creativecloud.adobe.com/en/apps/download/creative-cloud) application
* <b>&#91;Substance3d.com&#93;(http://Substance3d.com) subscription:</b> update when prompted in Substance 3D Designer, or download the latest installer in the [My Licenses](https://store.substance3d.com/user) section of the [Substance3d.com](http://substance3d.com) website
* <b>Steam:</b> the application will auto-update by default. You can manually trigger the update by starting Substance 3D Designer, or going to the Downloads screen

>[!WARNING]
>
> Make sure you will not need to load your files in a previous version of Substance 3D Designer *before saving* a file which was updated.
> 
> Alternatively, you can *make a copy* of your file *before* loading it in a new version of Substance 3D Designer, so you always have a file to go back to if you need to use a previous version of the software.

## Crash when creating or loading a project

<b>!&#91;(error)&#93;(error.svg) Issue</b>

A crash when creating or loading a project is often caused by an error during the initialisation of the [3D View](../../interface/3d-view/3d-view.md), which occurs when the workspace is being set up.

If the system is a laptop, a third-party application may enforce a *power management plan* that stops the 3D View from using the system's GPU. This can result in a crash if no other GPU device can perform the task in its place.

A crash may also occur when the *display configuration or scaling* was changed between sessions, so that 3D View render frame is created at invalid coordinates.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

Considering the multiple possible causes for this crash, we suggest going through the following troubleshooting steps in order:

Update graphics drivers

First, make sure the graphics drivers are up to date. You can find the latest version for your GPU [here](https://www.nvidia.com/Download/index.aspx?lang=en-us) (NVIDIA), [here](https://www.amd.com/en/support) (AMD) or [here](https://downloadcenter.intel.com/product/80939/Graphics-Drivers) (Intel).

Force best performance

Look for any software that manages your system's *power plan* (E.g., ASUS Armoury Crate), especially when the system is a laptop.

Some power management applications may limit the access of other applications to the system's GPU, or hinder the GPU's performance, which may result in crashes. If a power management application exists and is active, switch to the plan that enables the best performance.

Force using discrete GPU

If your system has *switchable graphics*, consider forcing the use of the discrete GPU (dGPU) for Substance 3D applications.

In most cases, this is achieved in a dedicated application which controls GPU settings. For instance, for NVIDIA GPUs you can do this in the 'NVIDIA Control Panel' application.

Reset user interface saved in registry

If the crash is caused by a change in the display configuration or scaling, you may try deleting the existing registry entries for Designer to entirely reset the user interface, among other settings.

The procedure to perform this reset per operating system is described below:

+++Windows
* Close Designer

Close Designer

* Open the <b>Command prompt</b> application

Open the <b>Command prompt</b> application

* Enter the following command and press <b>Enter</b>:

  <b>Creative Cloud Desktop</b>

  ```

  reg delete "HKEY_CURRENT_USER\Software\Adobe\Adobe Substance 3D Designer" /f
  ```


  <b>Steam/Substance edition</b>

  ```

  reg delete "HKEY_CURRENT_USER\Software\Allegorithmic\Substance Designer" /f
  ```


Enter the following command and press <b>Enter</b>:

<b>Creative Cloud Desktop</b>

<b>Steam/Substance edition</b>

* Disconnect the second monitor from your system, and connect it back (ignore this step if you do *not* have multiple displays attached)

Disconnect the second monitor from your system, and connect it back (ignore this step if you do *not* have multiple displays attached)

* Start Designer, but do *not* create or open any project

Start Designer, but do *not* create or open any project

* In the top bar, open the <b>Windows</b> menu and select the <b>New 3D View</b> option

In the top bar, open the <b>Windows</b> menu and select the <b>New 3D View</b> option

* Check that the <b>3D View</b> is correctly initialised, and try different preview meshes in the <b>Scene</b> menu of the panel top bar

Check that the <b>3D View</b> is correctly initialised, and try different preview meshes in the <b>Scene</b> menu of the panel top bar

* Create or open a material

Create or open a material

+++

+++macOS
* Close Designer

Close Designer

* Open the <b>Terminal</b> application

Open the <b>Terminal</b> application

* Enter the following command and press <b>Enter</b>:

  <b>Creative Cloud Desktop</b>

  ```

  rm ~/Library/Preferences/com.adobe.Adobe\ Substance\ 3D\ Designer.plist
  ```


  <b>Steam/Substance edition</b>

  ```

  rm ~/Library/Preferences/com.allegorithmic.Substance\ Designer.plist
  ```


Enter the following command and press <b>Enter</b>:

<b>Creative Cloud Desktop</b>

<b>Steam/Substance edition</b>

* Disconnect the second monitor from your system, and connect it back (ignore this step if you do *not* have multiple displays attached)

Disconnect the second monitor from your system, and connect it back (ignore this step if you do *not* have multiple displays attached)

* Start Designer, but do *not* create or open any project

Start Designer, but do *not* create or open any project

* In the top bar, open the <b>Windows</b> menu and select the <b>New 3D View</b> option

In the top bar, open the <b>Windows</b> menu and select the <b>New 3D View</b> option

* Check that the <b>3D View</b> is correctly initialised, and try different preview meshes in the <b>Scene</b> menu of the panel top bar

Check that the <b>3D View</b> is correctly initialised, and try different preview meshes in the <b>Scene</b> menu of the panel top bar

* Create or open a material

Create or open a material

+++
