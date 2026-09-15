import sqlite3
connection=sqlite3.connect("database.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS VACANCIES(  
          id TEXT PRIMARY KEY,
          title TEXT,
          company TEXT,
          url TEXT,
          level TEXT,
          match_percent INTEGER,
          timestamp TEXT)  """)
connection.commit()

def add_cv_skill(skill_name):
    cursor.execute("""INSERT INTO CV_SKILLS (skill_name) VALUES (?)""",(skill_name,))
    connection.commit()

def clear_cv_skills():
    cursor.execute("""DELETE FROM CV_SKILLS """)
    connection.commit()


cursor.execute("""CREATE TABLE IF NOT EXISTS CV_SKILLS(
                skill_name TEXT) """)
connection.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS VACANCY_SKILLS(
                    skill_name TEXT,
                    vacancy_id TEXT,
                    FOREIGN KEY(vacancy_id) REFERENCES VACANCIES(id))""")
connection.commit()

#cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' """)
#answer=cursor.fetchall()
#print(answer)

