import datetime

now = datetime.datetime.now()

ms = format(now.timestamp(), ",.4f") # ,. are used to format the string 4f stands for 4 decimal points
scientific = format(now.timestamp(), ".2e") # e stands for scientific notation

print("Seconds since January 1, 1970:", ms, "or", scientific, "in scientific notation")
print(now.strftime("%b %d %Y"))