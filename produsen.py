import xmlrpc.client


client = xmlrpc.client.ServerProxy("http://127.0.0.1:8889")
client2 = xmlrpc.client.ServerProxy("http://127.0.0.1:8890")
print("GUDANG PENYIMPANAN PRODUK\n")
print("Main Menu :\n1. Daftar Barang\n2. Input Produk\n3. Ubah Jumlah Produk\n4. Hapus Produk\n")


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
		query = client.input(nama_barang,jumlah_barang)
		query2=client2.input(nama_barang,jumlah_barang)
		print(query)

	elif opt==3:
		nama_barang = input("Masukkan Nama Barang :")
		jumlah_barang = int(input ("Jumlah barang :"))
		query = client.update(nama_barang,jumlah_barang)
		query2 =client2.update(nama_barang,jumlah_barang)
		print(query)

	elif opt==4:
		nama_barang = input("Masukkan Nama Barang :")
		query = client.hapus(nama_barang)
		query2 = client2.hapus(nama_barang)
		print(query)
		
	else:
		break
