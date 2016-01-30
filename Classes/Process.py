

import psutil

class Process(object) :

    def __init__(self , pid, port=None, status=None):
        self.pid= pid
        self.port= port
        self.status =status
        self.name = self.__namePid(self.pid)



    def getPid(self):
        return self.pid


    def getPort(self):

        return self.port



    def getStatus(self):
        return self.status



    def getName(self):
        return self.name
    def __namePid(self,pid):
        p = psutil.Process(pid)
        return p.name()

    def __hash__(self):
        if not self:
            return 0 # empty
        value = ord(self[0]) << 7
        for char in self:
            value = 1000003*value ^ ord(char)
        value = value ^ len(self)
        if value == -1:
            value = -2
        return value


    def __str__(self):
        return " NAME = " + str(self.name)+" PID = " + str(self.pid)+ " PORT = " \
               + str(self.port) +" status = " + str(self.status)