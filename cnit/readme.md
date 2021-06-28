- Program Address Space

- Stack LIFO- 

- Heap -
    Holds dynamic variables, which is FIFo
    grows in address space

- Program layout in ram

    kernel space

    stack grows down towards higher address

    memory mappign segment grows down towards higher address

    heap grows aup towards the lower address

    BSS segment - uninitialised static variables filled with zeros

    Data Segment - static variables initialized by the programmer

    Text Segment - stores binary image of the process

- asswmbly langugae

    x86 - 32 bit intel
    x64 - 64 bit intel

    other processesors - SPARC, PowerPC, MIPS, ARM 

    Windows runs on x86, x64

    x64 machines can eun x86 programs

    Most malware is designed for x86

- Mnemonic followed by operands

    mov ecx  0x42 is translated as 0xB942000000

- big Endian - Most significant byte first

- small Endian - least significant byte first

- network data uses big endian

- x86 uses little endina

- Operands

    Immediate - fixed value like 0x42

    Register - eax, ebx, ecx and so on

    memory address - denotes with brackets [eax]

## Registers

    General Registers - all 32 bits in size
    E stands for extended, EDX would contain 32 bits while DX -  16 bits
    AH and AL would have 8 bit value

        EAX (AX, AH, AL) - CS
        EBX = SS
        ECX - DS
        EDX - ES
    
    - EAX contains the return value for function calls

    Segment Registers-  track memory -  

        EBP -  FS
        ESP - GS
        ESI - SI
        EDI - DI

    Status Flags - 
        EFLAGS status registers set(1) or cleared(0)

        ZF , CF, SF, TF 

    Instruction pointer - 
        EIP - 

## Simple instructions

    - AT &T is opposit eto intel mov operations

    MOV  EBP, ESp -> movl %esp, %ebp

###  mov instructions examples

mov eax, ebx

mov eax, 0x42

mov eax, [0x4037C4]

mov eax, [ebx]

mov eax, [ebx + esi*4]

### lea 

- lea eax, [ebx + 8]

### arithematic operations

- sub, add, inc, dec, mul, div

### NOP

Does nothign, 0x90

### The stack - 

    - esp - top of the stack

    - ebp - bottom of the stack

    - push puts data on the stack

    - POP takes data off the stack

### Other stack instructions

    - Call

    - leave

    - Enter

    - Ret

### FUnction calls

    - Small programs that do one thing and return like printf()

    - Prologue - instructions at the start of a function that prepate stack and regusters for the function to use

    - Epilogue -  instructions at the end of the function that restore the stack and the registers to their stat before the function was called

### Conditionals

    - test - compares the two values liek and does but does not alter them, test eax, ebx

    - cmp eax, ebx - sets zero flag if the arguments are equal

### Branching

    - jz loc -  jump to loc if the zero flag is set

    - jnz loc - jump to loc if the zero flag is cleared

### C Main() method

    - int main (int argc, char ** argv) -
     argc contrains the nnumber of arguments on the command line
     argv is a pointer to an array of names containing the arguments

### Example

cp foo bar
argc =  3
argv[0] = cp
argv[1] = foo
argv[2] = bar

### Recognizing C constructs in the assembly

int number > number dw 0 # dw define word
number++    > mov eax, number
            > inc eax
            > mov number, eax

int number          > number dw 0

if (number < 0){    > mov eax, number
                    > or eax, eax
                    > jge label
                    > label :
    ...
}

### Arrat 

int array[4]    > array dw 0,0,0,0

array[2] = 9    > mov ebx, 2
                > mov array[ebx] , 9

### Triangle

int triangle(int width, int height){
    int array[5] =  {0,1,2,3,4}

    int area

    area = width * height/2

    return (area)
}

push ebp
mov  ebp, esp

push edi
push esi

sub esp, 0x30

lea edi, 0xffffffd8
mov $0x8049508, %esi

cld
mov esp, 0x30

repz movsl 
mov 0x8(ebp), edx
mov edx, eax
imul 0xc, edx
mov edx, eax
sar 0x1f, eax
shr 0x1f, eax
lea %eax, edx, 1, eax
sar eax
mov eax, d4(ebp)
mov ebp, eax
mov eax, eax
add 0x30, esp

pop esi
pop edi
pop ebp
ret







