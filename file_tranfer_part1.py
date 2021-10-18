from datetime import datetime, timedelta
import shutil
import os


source = 'C:/Users/jmcke/OneDrive/Desktop/Folder D/'
destination = 'C:/Users/jmcke/OneDrive/Desktop/Folder C/'
files = os.listdir(source)

x = datetime.now()#current time
y = datetime.now() - timedelta(hours = 24)

for a in files:
    z = os.path.getmtime(source+a)
    b = datetime.fromtimestamp(z)#converts timestamp to time object
    shutil.move(source+a, destination)
    
