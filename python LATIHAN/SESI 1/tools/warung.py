import main
from services import db

def add():
    kode_barang = input("KODE BARANG :")
    nama_barang = input("NAMA BARANG :")
    harga_barang =int(input("HARGA BARANG :"))
    stok_barang = int(input("STOK BARANG :"))
    
    
    
    save =db.insert_item(kode_barang,nama_barang,harga_barang,stok_barang)
    print(save)
def check():
    items = db.fetch_item()
    for items in items:
        kode_barang =items[1]
        nama_barang =items[2]
        harga_barang =items[3]
        stok_barang =items[4]
        
        print(f'''
kode: {kode_barang}
{nama_barang} |Rp {harga_barang}
stok:{stok_barang}
''')   

def start ():
    while True: 
        menu =int( input("MENU:\n\n1. Tambah Barang\n2. Check Barang\n3. Kembali\n\nSihlahkan Pilih :"))
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break
       
    
if __name__ =="__main__":
    start()
    
