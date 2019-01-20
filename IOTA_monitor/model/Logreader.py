
import subprocess
class LogReader():


    def __init__(self, filename):
        self.name = filename


    def readlog(self):
        with open('logs/'+str(self.name)) as f:
            # logs = f.readlines()
            logs = [x.rstrip() for x in f.readlines()]
        return logs


    def getDatapointslog(self):
        duration, samples = [], []
        for line in self.readlog():
            if line[42:50] == "duration":
                duration.append(float(line[52:58]))
            elif line[42:49] == "samples":
                samples.append(int(line[50:]))
        return duration, samples
