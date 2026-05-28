# colon-three

## Disclaimer
This project was only made for the purpose of learning tkinter (and PyInstaller) and for me to learn how to make a program that forks itself.
**I do not condone using this project for any malicious purposes whatsoever.**

## How it works
The application creates a window containing an image and nothing else, closing it afterwards creates forks of itself which does the same thing as its parent.
On close, the parent spawns two child processes, and the parent process reappears, multiplying the process count by 3 `(1 > 3 > 9 > 27 > 81...)`.
The `while True` loop in the `colon_three` function serves two purposes, it makes each process resistant to termination, and the PyInstaller binary keeps the shared `_MEIPASS` extraction directory alive so the child processes don't lose their dependencies.

# On Windows:

### Running the `.pyw` file (Recommended):
**NOTE: If the `.exe` file is present in the same path as the `.pyw` file, the `.pyw` file will instead run the `.exe` file instead of itself when closed. If this behavior is undesired, delete the `.exe` file before running the `.pyw` file.**

Closing it normally will create **two** copies of itself and reappear. Task Manager's "End Task" will terminate it since Windows sends `WM_CLOSE` through tkinter's event loop, but sometimes the `WM_DELETE_WINDOW` override may occasionally win the race condition and spawn children before the process dies. This is inconsistent and is considered the safe version, thus it is actually recommended to use this instead.

### Running the `.exe` file (PyInstaller binary):
**IT IS HIGHLY RECOMMENDED TO RUN IN A VM INSTEAD OF YOUR LOCAL MACHINE, YOU HAVE BEEN WARNED!**

This is the dangerous version. Closing it normally does the same behavior as the `.pyw` file. What makes it dangerous is that Task Manager's `End Task` is unreliable due to the fact that the parent spawns **two** orphaned child processes when killed (the parent process won't reappear). `End Task` is unreliable due to:
1. `DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP` flags fully decoupling children from the parent.
2. The `while True` loop creating child processes faster than the kill signal can be processed.
3. PyInstaller's `_MEIPASS` shared extraction directory creating interdependencies between processes.

### Stopping it on Windows:
The only reliable method are the force kill scripts which are also found in the `kill-scripts` directory:
- `kill-pyw.bat`
- `kill.bat`
- `kill.ps1`

As a last resort, reboot your machine. Detached processes do not survive a restart.

# On Linux:

### Running the `.pyw` file:
Both `SIGTERM` and `SIGKILL` stop it. This means a tool like `System Monitor` on Linux Mint can end the process without much problem.

```bash
# Either of these work
pkill -f colonthree.pyw
pkill -9 -f colonthree.pyw
```

### Running the `.exe` under Wine:
Wine runs all `.exe` processes under a shared `wineserver` session. Killing it via the `System Monitor` terminates the entire Wine session, taking all instances simultaneously. This makes it the easiest environment to stop it in.