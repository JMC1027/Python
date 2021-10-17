from datetime import datetime, timedelta
import shutil
import os

source = 'C:/Users/jmcke/OneDrive/Desktop/Folder A/'

destination = 'C:/Users/jmcke/OneDrive/Desktop/Folder B/'

files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)

x = datetime.now()#current time
y = datetime.now() - timedelta(hours = 24)

source = 'C:/Users/jmcke/OneDrive/Desktop/Folder C/'
destination = 'C:/Users/jmcke/OneDrive/Desktop/Folder D/'
files = os.listdir(source)

for a in files:
    z = os.path.getmtime(source+a)
    y = datetime.fromtimestamp(z)#converts timestamp to time object
    shutil.move(source+a, destination)
    
