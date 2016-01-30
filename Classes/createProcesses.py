import psutil
from Classes.Process import Process

def allProcess():
    allproces = []
    for process in psutil.net_connections():
        a = Process(process[-1],process[-4][1],process[-2])
        allproces.append(a)
    return allproces

def filterByname(namesearched):
    #python without lambda expresions
    #processesfiltered = []
    #for process in allProcess():
    #    if process.getName().lower() == namesearched.lower():
    #        processesfiltered.append(process)


    #return processesfiltered
    #lambda expresion

    return list(filter(lambda process:process.getName().lower() == namesearched.lower() , allProcess()))
