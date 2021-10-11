

import sqlite3

conn = sqlite3.connect('python.db')#name of the database


with conn: #Created table with column name
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_filelist( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()


conn = sqlite3.connect('python.db')

data_tuple =('information.docx', 'Hello.txt', 'myImage.png', \
             'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')#Tuple containing all the files.

with conn: #for loop runs through and will only print out docs that end in .txt into the col_filename
    cur = conn.cursor()
    for i in data_tuple: #runs through all the files inside the tuple, looks only for files ending in .txt
        if i.endswith('.txt'): #will only pull files that end in .txt
            cur.execute("INSERT INTO tbl_filelist (col_filename) VALUES (?)", (i,)) #missing tailing comma after (i,)) will result in in string data type not a tuple         
            print(i)#prints files ending in .txt
conn.close()

        
