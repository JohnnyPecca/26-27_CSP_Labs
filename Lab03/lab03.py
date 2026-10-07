seconds = 10000

hours = seconds // 3600
remainder = seconds % 3600
minutes_colum = remainder // 60
seconds_colum = minutes_colum % 60
print(str(hours) + " hours, " + str(minutes_colum) + " minutes and " + str(seconds_colum) + " seconds")
