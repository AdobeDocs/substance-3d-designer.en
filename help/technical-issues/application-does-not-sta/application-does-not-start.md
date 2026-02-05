---
title: "Application does not start"
description: ""
helpx_description: "Designer > Technical issues > Application does not start"
---

# Application does not start

This page lists common causes for Substance 3D Designer failing to start correctly, and offers troubleshooting steps for each, grouped by operating system:

## Designer 15.0 and higher

<b>!&#91;(error)&#93;(error.svg) Issue</b>

Versions 15.0 and higher of Designer fail to start on systems with both an integrated GPU (iGPU) and a discrete GPU (dGPU).

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

Update the iGPU's graphics drivers. You can find the latest drivers here:  [Intel](https://downloadcenter.intel.com/product/80939/Graphics-Drivers)  |  [AMD](https://www.amd.com/en/support/download/drivers.html)

## Windows 10/11

**![(error)](error.svg) Issue**

Substance 3D Designer fails to start on systems using Windows 10 or Windows 11.

**![(tick)](check.svg) Recommended steps**

Older versions of Designer may fail to start on Windows 10 or Windows 11 because of an *outdated* `libeay32.dll` library used in the license validation process.

You may try to replace the library with an *updated version*, such as the one distributed [here](https://support.networkoptix.com/hc/en-us/articles/115015730007-Nx-Software-crashes-due-to-libeay32-dll-on-Windows) (select the file for 32-bit Windows), by following these steps:

1. Locate the `libeay32.dll` file in Designer's installation directory
1. Back up the file in a safe location if you need to restore it in the future
1. Replace the file by the updated version
1. Start Designer

>[!WARNING]
>
> Unsupported configurations
> 
> Windows 10 is not supported. You can learn more on the [System requirements](../../getting-started/system-requirements/system-requirements.md) page.
> 
> Versions of Designer that are out of their maintenance period are not supported. These versions may not run reliably anymore if significant changes are done to the system, such as OS upgrades.

## Windows 7/8/8.1

**![(error)](error.svg) Issue**

Substance 3D Designer fails to start on systems using Windows 7, Windows 8 or Windows 8.1.

**![(tick)](check.svg) Recommended steps**

As part of the version **11.3.0** update, we upgraded multiple librairies, tools and SDKs which *broke compatibility* with versions of Windows lower than Windows 10.

We *strongly* recommend upgrading to Windows 10, as Microsoft itself does not support previous versions of Windows anymore for mainstream use (see [here](https://www.microsoft.com/en-us/windows/windows-7-end-of-life-support-information) and [here](https://docs.microsoft.com/en-us/lifecycle/faq/windows#windows-8.1)). Thus, the continued use of these versions presents a *security issue*.  
 If upgrading to Windows 10 is not possible, *do not update* your installation of Designer *past* version **11.2.2**.

>[!WARNING]
>
> Unsupported configurations
> 
> Please note Windows 7, Windows 8 and Windows 8.1 are *not officially supported*. You can learn more on the [System requirements](../../getting-started/system-requirements/system-requirements.md) page.

## Linux

<b>!&#91;(error)&#93;(error.svg) Issue</b>

Crash when closing the Home screen and displaying the main window.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

Designer fails to load Python components because it loads the system's <b>libffi.so</b> library instead of its own.

To make sure Designer loads its own library, use this command at Designer's installation directory, replacing `%command%` with your command to run Designer:

```

LD_PRELOAD=./plugins/pythonsdk/lib/python3.11/lib-dynload/libffi.so.6 %command%
```


Please note the Python version number depends on the version of Designer being run:

* Lower than 14.0.0: python3.9
* Lower than 12.1.0: python3.7

+++Steam launch options
Linux users starting Designer from Steam may set the LD\_PRELOAD command in Designer's launch options, as shown below.

Once this is done, Designer may be started from Steam normally for all future sessions.

![Steam launch options](steam_linux_launch_option.jpg "Steam launch options")



+++

**![(error)](error.svg) Issue**

The Steam edition of Designer fails to start with and produces no error message.

**![(tick)](check.svg) Recommended steps**

You can acquire error messages by logging the Steam application instead.

As recommended [here](https://github.com/ValveSoftware/steam-for-linux/issues/7114#issuecomment-629634260), completely close Steam then run the following command from a terminal (or create a shortcut for this command):

```

steam 2>&1 | tee /path/to/logfile
```


<b>!&#91;(error)&#93;(error.svg) Issu</b><b>e</b>

The `<b>xcb</b>` plugin cannot be loaded. The following message is displayed in the command line:

```

qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found. 

This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem. 

 

Available platform plugins are: minimal, offscreen, xcb. 

 

Aborted (core dumped)
```


**![(tick)](check.svg) Recommended steps**

Some required packages are missing. Run the following command from Designer's installation directory :

```

ldd libQt5XcbQpa.so.5
```


Check the printed list for any packages reported as `not found`, then run the following command for each of these missing packages:

```

apt-get install <package-name>
```


E.g.

```

apt-get install libxcb-xinput0
```


<b>!&#91;(error)&#93;(error.svg) Issue</b>

This error is raised when starting Designer:

```

error while loading shared libraries: libcrypt.so.1: cannot open shared object file: No such file or directory
```


A system library loaded by Designer is incompatible with Designer's own <b>libcrypto.so.1.1</b> library.

<b>!&#91;(tick)&#93;(check.svg) Recommended steps</b>

Remove the <b>`libcrypto.so.1.1`</b> library from Designer's installation directory, so that the system's library is used instead.

>[!NOTE]
>
> This workaround only works when the system has its own libcrypto.so.1 library. On recent distributions, a compatibility package such as <b>libxcrypt-compat</b> may need to be installed.

<b>!&#91;(error)&#93;(error.svg) Issue</b>

Substance 3D Designer fails to start on systems using *Arch-based* distributions of Linux.

**![(tick)](check.svg) Recommended steps *(![(warning)](warning.svg) Unstable, AMD GPUs only!)***

Try installing **progl** (part of the [AMDGPU-PRO](https://wiki.archlinux.org/title/AMDGPU_PRO "https://wiki.archlinux.org/title/AMDGPU_PRO") drivers) and start Designer through it. You may do this by using the `progl` prefix in the application launch command:

```

progl <designer-application-path>
```


Be mindful that `progl` may be unstable. This should therefore be attempted as a *last resort*.

>[!WARNING]
>
> Please note Arch-based distributions of Linux are *not supported*. You can learn more on the [System requirements](../../getting-started/system-requirements/system-requirements.md) page.
