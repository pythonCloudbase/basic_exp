# Debugging fundamentals

https://resources.infosecinstitute.com/topic/debugging-fundamentals-for-exploit-development/#x86

 
# DLL injection

https://www.youtube.com/watch?v=g_Xx90wyk0c


# DLL search order preloading

https://www.programmersought.com/article/90665167429/

- A dynamic link library (DLL) is a module that contains functions and data that can be used by another module (application or DLL).

- When an application is opened, the Windows loader takes steps to map the executable image of the application in memory, and finally starts a process that hosts and executes its code.

- For the remaining imported modules, the loader first checks whether all the DLLs to be imported exist on the list set by the KnownDLLs registry key (HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\KnownDLLs)

- The application may need to use functions in the DLL, which are dynamically loaded when the application is running. Loading DLL in this way is called runtime DLL dynamic linking. This type of loading occurs when the application calls LoadLibrary or LoadLibraryEx.

- This can be achieved through tools that monitor API calls (such as Procmon and API Monitor). Static analysis methods include using disassembly tools such as IDA and Ghidra to identify specific API calls that occur without executing the application.

- search order 

- The DLL contains the following contents:
    The directory from which to load the application

    System catalog

    16-bit system catalog

    Windows directory

    The current directory (unless otherwise noted, the same as the first one)

    The directories listed in the PATH environment variable

