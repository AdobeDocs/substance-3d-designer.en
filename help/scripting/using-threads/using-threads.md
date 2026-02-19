---
title: "Using threads"
description: "Learn how to use threads in Substance 3D Designer Python scripting for parallel processing and performance."
helpx_description: Designer > Scripting > Using threads
helpx_url: "https://helpx.adobe.com/substance-3d-designer/scripting/using-threads.html"
helpx_creative_field:
  - painting-illustration
  - graphic-design
  - 3d-immersive
helpx_experience_level:
  - any
helpx_learn_topic:
  - interface
  - data-and-analytics
  - rigging
---




# Using threads

It is possible for plugins to <b>create threads</b> using Python's threading module *or* Qt for Python threading related classes.

This can be useful to perform background processing or I/O operations while Designer is running.

It is important to note that most classes and methods in Designer's Python API can *only* be called from the <b>main application thread</b>. As such, if you want to make any modification to any graph that is currently opened in Designer, you must make them from the main application thread.

One possible solution is to use <b>QThread</b> and <b>Queued connections</b>, like in the following example:

```

import time 

from PySide2 import QtCore 

 

 

## Our thread object.

class TimerThread(QtCore.QThread): 

    tick = QtCore.Signal() 

 

    def run(self): 

        for i in range(0, 7): 

            print("Emitting signal from thread %s" % QtCore.QThread.currentThread()) 

            self.tick.emit() 

            time.sleep(0.5) 

 

 

## Our receiver object, created on the main thread.

class Receiver(QtCore.QObject): 

    def __init__(self, parent=None): 

        super(Receiver, self).__init__(parent) 

 

    def onTick(self): 

## This is called on the main thread. It is safe to use the sd API here.

        print("Tick received in thread %s" % QtCore.QThread.currentThread()) 

 

 

timer = TimerThread() 

receiver = Receiver() 

 

## Use QtCore.Qt.QueuedConnection to make sure that slots are called on the main thread.

## You can also use QtCore.Qt.BlockingQueuedConnection if you need to block while the slot is called.

timer.tick.connect(receiver.onTick, QtCore.Qt.QueuedConnection) 

 

## Start out thread.

timer.start()
```
