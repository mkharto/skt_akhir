import mysql.connector
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

db = mysql.connector.connect(
  host="localhost",
  user="root",
  database="skt"
)
cursor = db.cursor()

server = SimpleXMLRPCServer( ("0.0.0.0", 8889) )
client = xmlrpc.client.ServerProxy("http://127.0.0.1:8890")

def show_all():
	global db
	global cursor
	sql = "SELECT * FROM produk"
	cursor.execute(sql)
	results = cursor.fetchall()
	return results

def input_new(a,b):
	global db
	global cursor
	sql = "INSERT INTO produk (name, quantity) VALUES (%s, %s)"
	val = (a, int(b))
	cursor.execute(sql, val)
	db.commit()
	
	return "{} data ditambahkan".format(cursor.rowcount)

def update_quantity(a, b):
	global db
	global cursor
	sql = "UPDATE produk SET quantity=%s WHERE name=%s"
	val = (int(b),a)
	cursor.execute(sql, val)
	db.commit()
	
	return "{} data diubah".format(cursor.rowcount)
	
def delete(a):
	global db
	global cursor
	sql = "DELETE FROM produk WHERE name=%s"
	val = (a, )
	cursor.execute(sql, val)
	db.commit()
	return "{} data dihapus".format(cursor.rowcount)

# Daftarkan fungsinya
server.register_function( show_all, "data" )
server.register_function( input_new, "input" )
server.register_function( update_quantity, "update" )
server.register_function( delete, "hapus" )

# Jalankan servernya
server.serve_forever()
