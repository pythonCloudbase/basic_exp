Unlike Linux, in Windows, applications can’t directly accesss system calls. Instead they use functions from the Windows API (WinAPI), which internally call functions from the Native API (NtAPI), which in turn use system calls. The Native API functions are undocumented, implemented in ntdll.dll 

The documented functions from the Windows API are stored in kernel32.dll, advapi32.dll, gdi32.dll and others. The base services (like working with file systems, processes, devices, etc.) are provided by kernel32.dll.

ntdll.dll and kernel32.dll are so important that they are imported by every process.

![](windows_architecture.png)

We use ListDlls from sysinternals suite ro list out what are the dlss that are loaded

The shellcode I’m going to write is going to be simple and its only function will be to execute calc.exe. To accomplish this I’ll make use of the WinExec function, which has only two arguments and is exported by kernel32.dll.

