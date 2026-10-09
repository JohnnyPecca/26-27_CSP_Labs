starting_milliseconds = 10000123
print("starting milliseconds: " + str(starting_milliseconds))
hours = starting_milliseconds // 3600000
print("hours: \t\t" + str(hours))
ms_left_1 = starting_milliseconds % 3600000
minutes = ms_left_1 // 60000
print("minutes: \t\t" + str(minutes))
ms_left_2 = ms_left_1 % 60000
seconds = ms_left_2 // 1000
print("seconds: \t\t" + str(seconds))
milli_seconds = ms_left_2 % 1000
print("milli seconds: \t" + str(milli_seconds))
