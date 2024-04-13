
from datetime import datetime
from sys import argv


def day_difference(string1, string2, time_frame = 86400):

    date1 = datetime.strptime(string1, "%d/%m/%y %H:%M:%S")

    date2 = datetime.strptime(string2, "%d/%m/%y %H:%M:%S")

    difference = (date2 - date1).total_seconds()

    return difference >= time_frame


if __name__ == "__main__":

    result = day_difference(argv[1], argv[2])

    print(result)