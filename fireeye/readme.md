## HBIs - File system
Host based indicator

1. There might be executable 
2. May use registry keys
3. Mutex to not allow multiple instances toexecute at the same time
 in strings output -  create mutex

## Network based indicator

1. Domain ip
2. http header 

# Basic static analysis

## hashing -

the hash search
virustotal

hashmyfiles
sigcheck.exe -h (sysinternals)
CFF explorer and PE analysis tools

## strings

what can be there

filenames
registry path/keys
PDB strings
service configuration ingo
HTTP user agent
domain names, ip addressses URLs
command line help
debug messages
function names
third party software
keylogger

This program cannot be run in DOS mode - it means windows
???? - CPP string
exception handling -cpp string
wsastartup - it means interenet connectino
useragent - Mozzila firefox
windows api function
paths - registry pat
IExplore internet explore
registry path 
debugging strings
service dll

hiding strings 
encrypt
obfuscate
encode

common encoding methods
hexadecimal
XOR
can be used with one line of python code
decoding XOR, anything with XOR is 0

Base64
    6 bit interval uses = for padding

ADVAPI.DLL 
KERNEL32.DLL -  AAPI to write file

google.com - anti sandboxing, connectivity

FLOSS - given by fireye
emulator

floss -q | rank_strings> ranked.txt

commander - commander emulator

string sifter - machine learning based propogating the nice tools to the top


### Tools for strings
strings.exe 
/use/bin/strings


### encoding in strings
ascii
utf  a lot of 00

### Using cyberchef

you can also get a file
gives a hexdump
use head to lookat cyberchef

How magic wand works?
 1. tries all the encoding and then checks for the typeof malware 

Floss


## open source intelligence

xm-rig for crypto currency virus
search for unique strings

capa for capabilities in malware
yara - tool for scanning signature of a malware
capa is better than yara

PE file format
Packing

# Dynamic analysis

## PE File Format

Portable executable is the standard binary file format

Common Object file format (COFF)

EXE -  on execution it gets its own address space
DLL - Dynamic Link Library referred to as module
Loaded into virtual address space of a process, can be loaded or unloaded
SYS - kernel driver, executes in kernel-mode 

see page 39

winexec tries to create a process

PE magic sequence
4D 5A MZ in ascii

Rich header

## exploring CFF explorer

> file header
 characteristics section

> optional header
 imagebase
 dll characteristics

> section header

.text - exectanle code
.rdate -  read only dat
.data - read and write data
.reloc - for relocation of data

> raw size vs virtual size

    when raw size is small and the virtual size is more it means packing

> resource editor
we can save individual resources

> import directory we can look at the dlls

1. kernel32 to create file movefile, and create process

2. might call ntdll.dll - does the system call to write to the disk

2. advapi32  registry and service for advance api

3. WS2_32.dll socket api 

4. WININET.dll - internet protocol library

5. MSVCRT.dll - c runtime

> exports

### Linking

1. Static linking - entire linking is put on file
 zlib compression librayr is always statically linked
 openssl encryption library is another one

2. Loadtime Dynamic linking
 load time import via import table
 cannot run if DLL dependencies are missing

3. euntime linking

loadlibrary and runtime linking


### Packing

unpacking stub that unpacks data

detected by cff explorer
peid
upx

might have used UPX

### 

3. Run time Dynamic linking


Questions

1. what do you use your bing credits for?
2. is the practical malware book the best for malware analysis
3. What was you rpath in cyber security.
4. machine learning in cyber security in things like floss



# Flare vm

practival malware analysis
inside tools

flare vm can be used for doing a lot of stuff


# notes 

consolidated list of windows api 
practical malware analysis tool book

do in malware labs
shady rabbit 32