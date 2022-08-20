# Multi-threading and Multi-processing in Python

Multithreading: I/O bound tasks-

![Multithreading](F:\College docs\Desktop\1_F8ckVaR__PlBssnf-mn76A.png)

Multithreading is a program execution technique that allows a single process to have multiple code segments (like threads) sharing the same CPU and memory. However, because of the GIL in Python, not all tasks can be executed faster by using multithreading. Multiple threads cannot execute code simultaneous, but when one thread is idly waiting, another thread can start executing code.

Multiprocessing: CPU Bound tasks-

Multiprocessing is when multiple processes are spawn from the main process, each having its own CPU and memory. These additional CPUs help increase the computing speed of the system. Processors share processes and resources amongst themselves dynamically so that no processor may sit idle or get overloaded.


