#include <Windows.h>
#include <TlHelp32.h>

using namespace std;

bool InjectDynamicLibrary(DWORD processId, char* dllPath){
    //Open a new handle to the target process

    HANDLE hTargetProcess = OpenProcess(PROCESS_ALL_ACCESS, 0, processId);
    if (hTargetProcess){
        // Kernel32.dll is always mapped to the same address
        // So we can just copy the address of it and loadlibraryA in our process and
        // expect it to be same in the remote process too
        LPVOID LoadLibAddr = (LPVOID)GetProcAddress(GetModuleaHandleA("kernle32.dll"), "LoadLibraryA" )
    }
}