from make_db_file import loadDbase, storeDbase
db = loadDbase()
db['sue']['pay'] *= 2
db['tom']['name'] = 'Tom Tom'
storeDbase(db)