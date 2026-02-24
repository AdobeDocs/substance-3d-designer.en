---
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/debugging-plugins-using-visual-studio-code.html"
breadcrumb-title: ""
description: Learn how to debug Substance 3D Designer Python plugins using Visual Studio Code for efficient development.
helpx_creative_field: ""
helpx_description: Designer > Scripting > Debugging plugins using Visual Studio Code
helpx_experience_level: ""
helpx_learn_topic: ""
helpx_tags: ""
title: Debugging plugins using Visual Studio Code
user-guide-description: ""
user-guide-title: ""
---



# Debugging plugins using Visual Studio Code

As a workflow standard for many developers, the **Visual Studio Code IDE** is available to debug Python plugins.

>[!WARNING]
>
> The <b>debugpy.listen()</b> method may let anyone who can connect to the specified port execute arbitrary code within the debugged process.
> 
> Therefore, debugging should *<b>only</b>* be set up and performed on *secure networks*.

In order to set up the synergy between Visual Studio Code and Substance 3D Designer, please follow these steps:

1. Install **[Visual Studio Code](https://code.visualstudio.com/)** and the **[Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)**.
1. Install the **[debugpy Python module](https://github.com/microsoft/debugpy)**.

   >[!NOTE]
   >
   > Make sure that the Python interpreter in Designer can find the '*debugpy*' module. The easiest way to do it is to add the directory where the '*debug*' module is to the **PYTHONPATH** environment variable. An alternative could be to modify sys.path in your script to add the path to the debugpy module.
1. Launch the application, open the Python Editor and **run the following code**:

   ```

   import sys 

    

   debugpy_path = '/path/to/debugpy/module' 

   debugpy_port = 5678 

   designer_py_interpreter = '/path/to/python/executable/bundled/in/designer' 

    

   if not debugpy_path in sys.path: 

       sys.path.append(debugpy_path) 

    

   import debugpy 

    

   debugpy.configure(python=designer_py_interpreter) 

   debugpy.listen(debugpy_port)
   ```

1. In Visual Studio Code, open your project and create a **launch.json** file. Add the following into the file:

   ```

   { 

       "name": "Attach to Designer", 

       "type": "python", 

       "request": "attach", 

       "port": <port number used in the script above>, 

       "host": "127.0.0.1" 

   }
   ```

1. Click on the <b>Debug</b> icon, create or edit your debugger configuration, if needed.
1. Select the **Python: Attach to Designer** configuration and click on **Start Debugging**.

   You should now be able to set breakpoints, step trough the code, and use all the other features of Visual Studio Code's debugger.
