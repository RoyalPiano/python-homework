import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE `albums` ("
               "title text, "
               "artist text, "
               "release_date text, "
               "publisher text, "
               "media_type text);")
conn.commit()
albums = [('The End1', 'PAP1', '1/1/2001', 'Records1', 'mp3'),
          ('The End2', 'PAP1', '1/1/2001', 'Records2', 'mp3'),
          ('The End3', 'PAP3', '1/1/2003', 'Records3', 'mp3'),
          ('The End4', 'PAP4', '1/1/2004', 'Records4', 'mp3')]
cursor.executemany("INSERT INTO `albums` "
                   "VALUES (?, ?, ?, ?, ?);", albums)
conn.commit()
cursor.execute("SELECT * FROM `albums`")
print('Записи в таблице:', *cursor.fetchall(), sep='\n')
cursor.execute("UPDATE albums "
               "SET title = 'new Title\'")
conn.commit()
print('title всех записей был изменён на "new Title"')
cursor.execute("SELECT * FROM `albums`")
print('Записи в таблице:', *cursor.fetchall(), sep='\n')
cursor.execute("UPDATE albums "
               "SET release_date = null " 
               "WHERE release_date = \"1/1/2001\";")
conn.commit()
print('Были удалены записи 1 янв 2001')
cursor.execute("SELECT * FROM `albums`")
print('Записи в таблице:', *cursor.fetchall(), sep='\n')
cursor.execute("SELECT * FROM `albums`" "WHERE `artist` = \"PAP1\"")
print('Записи в таблице, где actor == "PAP1":', *cursor.fetchall(), sep='\n')
