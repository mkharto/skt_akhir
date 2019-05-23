import xmlrpc.client


client = xmlrpc.client.ServerProxy("http://127.0.0.1:8890")
client2 = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")
print("DISTRIBUSI DAN PENJUALAN PRODUK\n")
print("Main Menu :\n1. Daftar Barang\n2. Ubah Jumlah Produk\n")


while True:
	
	opt = int(input ("Pilihan :"))
	
	if opt==1:
		query = client.data()
		print("(product_id, name, quantity)")
		for data in query:
			print(data)

	elif opt==2:
		nama_barang = input("Masukkan Nama Barang :")
		jumlah_barang = int(input ("Jumlah barang :"))
		query = client.update(nama_barang,jumlah_barang)
		query2 =client2.update(nama_barang,jumlah_barang)
		print(query)

	else:
		break
