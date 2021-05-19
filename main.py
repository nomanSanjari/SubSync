from io import StringIO
import re

FILE = #SOURCE FILE HERE
ALTERED = #NEW FILE HERE
SHIFT = #ADJUST BY SECONDS HERE
PATTERN = "\-\-\>"


def timeAdjust(hours, minutes, seconds, shift):
    # converts to int in order to apply changes
    hours = int(hours)
    minutes = int(minutes)
    seconds = int(seconds)

    # applies adjustment
    # checks for runover and applies accordingly
    seconds = seconds + shift
    if seconds == 60:
        seconds = 0
        minutes = minutes + 1
        if minutes == 60:
            hours = hours + 1
        elif minutes > 60:
            remainder = minutes - 60
            minutes = remainder
    elif seconds > 60:
        remainder = seconds - 60
        seconds = remainder
        minutes = minutes + 1
        if minutes == 60:
            hours = hours + 1
        elif minutes > 60:
            remainder = minutes - 60
            minutes = remainder

    hours = str(hours)
    minutes = str(minutes)
    seconds = str(seconds)

    if seconds == "0":
        seconds = "00"
    elif len(seconds) == 1:
        seconds = "0" + str(seconds)

    if minutes == "0":
        minutes = "00"
    elif len(minutes) == 1:
        minutes = "0" + str(minutes)

    if hours == "0":
        hours = "00"
    elif len(hours) == 1:
        hours = "0" + str(hours)

    # returns changed data
    return (hours, minutes, seconds)


source = open(FILE, "rt")
target = open(ALTERED, "wt")

for line in source:
    if re.search(PATTERN, line):
        # set start and end Times
        startTime = line[0:8]
        startTimeEnd = line[8:12]
        endTime = line[17:25]
        endTimeEnd = line[25:29]

        # Print statements for debugging
        # print(startTime, endTime)
        # print(startTimeEnd, endTimeEnd)

        # set startTime sub variables
        startTimeHours = startTime[0:2]
        startTimeMinutes = startTime[3:5]
        startTimeSeconds = startTime[6:8]

        endTimeHours = endTime[0:2]
        endTimeMinutes = endTime[3:5]
        endTimeSeconds = endTime[6:8]

        # Print statements for debugging
        # print(startTimeHours, startTimeMinutes, startTimeSeconds)
        # print(endTimeHours, endTimeMinutes, endTimeSeconds)

        startTimeHours, startTimeMinutes, startTimeSeconds = timeAdjust(
            startTimeHours, startTimeMinutes, startTimeSeconds, SHIFT
        )

        endTimeHours, endTimeMinutes, endTimeSeconds = timeAdjust(
            endTimeHours, endTimeMinutes, endTimeSeconds, SHIFT
        )

        # Print statements for debugging
        # print(startTimeHours, startTimeMinutes, startTimeSeconds)
        # print(endTimeHours, endTimeMinutes, endTimeSeconds)

        startTime = startTimeHours + ":" + startTimeMinutes + ":" + startTimeSeconds
        endTime = endTimeHours + ":" + endTimeMinutes + ":" + endTimeSeconds

        STRING = startTime + startTimeEnd + " --> " + endTime + endTimeEnd + "\n"
        target.write(STRING)
        print("Write complete")
        print("Written to file: " + ALTERED)

    else:
        target.write(line)

source.close()
target.close()

# --:--:--,--- --> 17-;--;--,---
