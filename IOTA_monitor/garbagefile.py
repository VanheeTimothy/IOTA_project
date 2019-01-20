from model.Logreader import LogReader

readFlaskLog = LogReader("updatedatabase.log").readlog()

duration, samples = [], []
for line in readFlaskLog:
    if line[42:50] == "duration":
        duration.append(float(line[52:58]))
    elif line[42:49] == "samples":
        samples.append(int(line[50:]))


print(duration)