# reading and writing file practice for logging

#importing datetime library to get today's date
# for now, the user manually have to enter their tiem of arrival and departure
# but will be automated later on

import TimePuncherGUI
import datetime

date = datetime.date.today()

def returnTime():
    with open('Manual Time Log.txt', 'a+') as logger:
        logger.write('{}: {} : {} : {} \n'.format(datetime.datetime.today(), TimePuncherGUI.time.strftime("%H"), TimePuncherGUI.time.strftime("%M"),TimePuncherGUI.time.strftime("%S")))


TimePuncherGUI.clock()