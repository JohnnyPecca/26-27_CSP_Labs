starting_ms = 10000123
print("starting milliseconds: " + str(starting_ms))
hours = starting_ms // 3600000
print("hours:    \t\t\t\t\t " + str(hours))
msfirst = starting_ms % 3600000
minutes = msfirst // 60000
print("minutes: \t\t\t\t\t" + str(minutes))
mssecond = msfirst % 60000
seconds = mssecond // 1000
print("seconds: \t\t\t\t\t" + str(seconds))
milli_seconds = mssecond % 1000
print("milli seconds: \t\t\t\t" + str(milli_seconds))
