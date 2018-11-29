import Pyro4
import Pyro4.naming
import threading



server1 = Pyro4.Proxy("PYRONAME:server1")
server2 = Pyro4.Proxy("PYRONAME:server2")
server3 = Pyro4.Proxy("PYRONAME:server3")
serverList = []

@Pyro4.expose
class FrontEnd(object):

    def serverCheck(self):
        global serverList
        serverList = []
        try:
            server1.check()
            serverList.append(server1)
        except:
            pass
        try:
            server2.check()
            serverList.append(server2)
        except:
            pass
        try:
            server3.check()
            serverList.append(server3)
        except:
            pass
        return serverList

    def upload(self, fileName, file, reliability):
        serverList = FrontEnd.serverCheck(self)
        print("UPLOAD")
        if reliability.upper() == "YES":
            for i in serverList:
                i.upload(fileName, file)
            return True
        else:
            lists = []
            for i in serverList:
                lists.append(len(i.list()))
            minimum = min(lists)
            lowest = serverList[0]
            for i in serverList:
                if len(i.list()) == minimum:
                    lowest = i
            lowest.upload(fileName, file)




    def list(self):
        serverList = FrontEnd.serverCheck(self)
        print("LIST")
        reply = []
        for i in serverList:
            for j in i.list():
                if j not in reply:
                    if j != ".DS_Store":
                        reply.append(j)
        return reply

    def download(self, fileName):
        serverList = FrontEnd.serverCheck(self)
        print("DOWNLOAD")
        for i in serverList:
            if fileName in i.list():
                file = i.download(fileName)
        return file

    def delete(self, fileName):
        print("DELETE")
        try:
            server1.delete(fileName)
        except:
            pass
        try:
            server2.delete(fileName)
        except:
            pass
        try:
            server3.delete(fileName)
        except:
            pass
        return True



def start():
        Pyro4.naming.startNSloop()

link = threading.Thread(target=start, args=[])
link.setDaemon(1)
link.start()

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(FrontEnd)
ns.register("FrontEnd", uri)

daemon.requestLoop()
