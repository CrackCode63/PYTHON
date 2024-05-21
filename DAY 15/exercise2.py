from datetime import datetime
# importing time ans using python modules.

time = datetime.strptime('12:00:00', '%H:%M:%S')  # convert the time string to a datetime object

if datetime.now() <= time:
    print("It's before noon!")
else:
    print("It's after noon!")