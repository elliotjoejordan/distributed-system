import Pyro4
import os
import serpent


@Pyro4.expose
class Server(object):
    def upload(self, fileName, file):
        fileWrite = serpent.tobytes(file)
        newFile = open("files/" + fileName, 'wb')
        newFile.write(fileWrite)
        newFile.close()
        return True

    def list(self):
        fileList = [f for f in os.listdir('./files/')]
        return fileList

    def download(self, fileToDownload):
        file = open("files/" + fileToDownload, 'rb')
        content = file.read()
        file.close()
        return content

    def delete(self, fileName):
        os.remove("files/" + fileName)
        return True

    def check(self):
        return True


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(Server)
ns.register("server1", uri)
daemon.requestLoop()