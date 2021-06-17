import ctypes
User32 = ctypes.WinDLL('User32.dll')

print("Checking if dll loaded: ")
print(User32.GetSystemMetrics(1))

print(win32com.client.combrowse)