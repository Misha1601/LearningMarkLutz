"""
Сохраняет в файл базу данных. находящуюся в оперативной памяти, используя собственный фоормат записи;
предпологается что в данных отсутствуют строки 'endrec', 'enddb', '=>'; предпологается, что база данных является словарем словарей;
внимание: применение фукции eval - может быть опасным - она выполняет строки как программный код; с помощью фукции eval() можно так же реализовать сохранение словарей-записей целиком;
кроме того, вместо вызова print(key, file=dbfile) можно использовать вызов dbfile.write(key + '\n');
"""

dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = 'recsep'

def storeDbase(db, dbfilename=dbfilename):
	"сохраняет БД в файл"
	dbfile = open(dbfilename, 'w')
	for key in db:
		print(key, file = dbfile)
		for (name, value) in db[key].items():
			print(name + RECSEP + repr(value), file = dbfile)
		print(ENDREC, file = dbfile)
	print(ENDDB, file = dbfile)
	dbfile.close()

def loadDbase(dbfilename = dbfilename):
	"восстанавливает данные, реконструируя БД"
	dbfile = open(dbfilename)
	import sys
	sys.stdin = dbfile
	db = {}
	key = input()
	while key != ENDDB:
		rec = {}
		field = input()
		while field != ENDREC:
			name, value = field.split(RECSEP)
			rec[name] = eval(value)
			field = input()
		db[key] = rec
		key = input()
	return db

if __name__ == '__main__':
	from initdata import db
	storeDbase(db)