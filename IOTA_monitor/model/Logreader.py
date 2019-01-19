
import subprocess
class LogReader():


    def __init__(self, filename):
        self.name = filename


    def readlog(self):
        with open('logs/'+str(self.name)) as f:
            # logs = f.readlines()
            logs = [x.rstrip() for x in f.readlines()]
        return logs

    def readlog2(self):
        filename = "logs/"+self.name
        f = subprocess.Popen(['tail', '-F', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        while True:
            yield f.stdout.readline()