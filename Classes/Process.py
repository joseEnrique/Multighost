

import psutil

class Process(object) :

    def __init__(self , pid, port=None, status=None):
        self.pid= pid
        self.port= port
        self.status =status
        self.name = self.namePid(self.pid)



    def getPid(self):

        return self.pid
    def getPort(self):

        return self.port

    def getStatus(self):
        return self.status

    def getName(self):
        return self.name
    def namePid(self,pid):
        p = psutil.Process(pid)
        return p.name()



    def __str__(self):
        return " NAME = " + str(self.name)+" PID = " + str(self.pid)+ " PORT = " \
               + str(self.port) +" status = " + str(self.status)