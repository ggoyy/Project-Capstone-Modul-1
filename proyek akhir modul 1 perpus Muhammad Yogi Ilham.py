#Define database
dict_buku = [{'ID_Buku': 0, 'Judul': 'Harry Potter & The Deadly Hallows', 'Author': 'J.K Rowlings','Genre':'Fiction','Tahun':'2007', 'Halaman': '607', 'Status': 'Available'},
             {'ID_Buku': 1, 'Judul': 'Doraemon Vol. 1', 'Author': 'Fujiko F. Fujio','Genre': 'Manga','Tahun':'1998', 'Halaman': '60', 'Status': 'Borrowed'},
             {'ID_Buku': 2, 'Judul': 'How To Be a Stoic', 'Author': 'Massimo Pigliucci','Genre': 'Non-Fiction','Tahun':'2017', 'Halaman': '288', 'Status': 'Borrowed'}]

#fungsi update
def update_buku(id_buku,kolom,data_baru):
    dict_kosong = {}
    dict_kosong[kolom] = data_baru  #data baru dimasukkan ke dictionary kosong
    pilihan_update_buku = int(input(f'Yakin simpan perubahan? {dict_kosong} \n 1. Yes\n. 2.no : \n')) #konfirmasi untuk menyimpan perubahan
    if pilihan_update_buku == 1:
        dict_buku[id_buku][kolom] = data_baru   #data baru disimpan ke dictionary
        print('Update telah tersimpan \n')
    elif pilihan_update_buku == 2:
        print('data tidak berhasil disimpan\n') #pilihan data batal disimpan
    else:
        print('Pilihan tidak ada di menu\n')    
    
    return print(dict_buku) #return database yang telah atau tidak diubah

#fungsi hapus kategori
def hapus_buku(id_buku): 
    kolom = input('Silakan ketik kategori untuk dihapus\n 1. Judul\n 2. Author\n 3. Genre\n 4. Tahun\n 5. Halaman\n 6. status\n 7. Seluruh kolom :')    #pemilihan kategori untuk diapus
    pilihan_update_buku = int(input(f'Yakin hapus {kolom}? \n 1. Yes\n. 2.no : \n'))    #konfirmasi penghapusan
    if pilihan_update_buku == 1:
        global dict_buku
        del dict_buku[id_buku][kolom]       #kategori dihapus
        print('data telah terhapus \n')
    elif pilihan_update_buku == 2:      #batal dihapus
        print('data tidak dihapus\n')
    else:
        print('Pilihan tidak ada di menu\n')
    
    return print(dict_buku)    #return database yang telah dihapus
    


def menu_utama():       #menu utama
    print('\t' + 'Selamat Datang di Perpustakaan Cihuy' + '\t')

    print('\t' + 'List Menu :' '\n 1. Daftar Buku \n 2. Tambah Buku \n 3. Update Buku\n 4. Menghapus Buku\n 5. Exit Program ' )

    global pilihan_menu
    pilihan_menu = int(input(' Masukkan angka menu yang ingin dijalankan: \n'))

    if pilihan_menu == 1:
        menu_1()
    elif pilihan_menu == 2:
        menu_2()
    elif pilihan_menu ==3:
        menu_3()
    elif pilihan_menu == 4:
        menu_4()  
    if pilihan_menu == 5:
        print('Terima kasih, sampai jumpa')
        return False

    
    else:
        print('silakan pilih opsi dari menu yang ada\n')
        menu_utama()

    



def menu_1():       #menu READ buku
    while pilihan_menu == 1:       
        print('MENU DAFTAR BUKU\n 1. Tampilkan seluruh buku \n 2. Cari buku \n 3. Kembali ke Menu Utama')
        
        opsi_menu_1 = int(input(' Masukkan opsi yang dipilih: \n'))
        
        if opsi_menu_1 == 1:
            if len(dict_buku) == 0:     #cek apabila database kosong
                print('Tidak ada data')
            else:
                print(dict_buku)        #print seluruh database 
        
        elif opsi_menu_1 ==2:
            if len(dict_buku) == 0:
                print('Tidak ada data') #cek apabila database kosong
            elif len(dict_buku) != 0:
                kode_cari_buku = int(input('Masukkan kode buku: '))     #kode buku untuk dicari
                for i in dict_buku:
                    if i['ID_Buku'] == kode_cari_buku:
                        print(i)                    #print data sesuai kode buku
                else:
                    print('Buku tidak ada di database\n')
                    print()     
                

        elif opsi_menu_1 == 3:      #kembali ke menu utama
            menu_utama()
        else:                       #jika pilihan tidak sesuai, maka akan diulang
            continue

def menu_2():       #menu CREATE buku
    while pilihan_menu == 2:      
        print('MENU TAMBAH BUKU\n 1. Tambah Buku \n 2. Kembali ke Menu Utama \n')
        opsi_menu_2 = int(input(' Masukkan opsi yang dipilih: \n'))

        if opsi_menu_2 == 1:            #pilihan menambah buku
            input_kode_buku_baru = int(input('Masukkan kode buku baru: '))      #input untuk kode buku baru
            for i in dict_buku:
                if i['ID_Buku'] == input_kode_buku_baru:
                    print(dict_buku[input_kode_buku_baru])
                    print('Maaf, sudah ada buku tersimpan\n')       #jika kode buku sudah ada, maka proses batal
                    break
            else:                                                   #jika kode buku belum ada, maka lanjut ke proses penambahan buku
                dict_baru = {}
                list_baru = []
                dict_baru['ID_Buku'] = input_kode_buku_baru         #menambahkan data sesuai key-nya
                dict_baru['Judul'] = input('Masukkan Judul Buku: ')
                dict_baru['Author'] = input('Masukkan Penulis Buku: ')
                dict_baru['Genre'] = input('Masukkan Genre Buku: ')
                dict_baru['Tahun'] = int(input('Masukkan Tahun Terbit Buku: '))
                dict_baru['Halaman'] = int(input('Masukkan Jumlah Halaman Buku: '))
                dict_baru['Status'] = 'Available'
                list_baru.append(dict_baru)                         #memasukkan data buku baru ke list kosong
                print(list_baru)
                konfirmasi_tambah_buku = int(input('Yakin untuk menyimpan?\n 1 = Yes\n 2 = no \n: '))   #konfirmasi penyimpanan buku baru
                if konfirmasi_tambah_buku == 1:
                    dict_buku.extend(list_baru)         #buku baru telah disimpan
                    print('Data sudah tersimpan')
                    print(dict_buku)

                elif konfirmasi_tambah_buku == 2:       #buku baru batal disimpan
                    print('Penambahan dibatalkan')
                    list_baru.clear()
                    continue
                else:                                   
                    print('Pilihan tidak sesuai')
                    continue

        elif opsi_menu_2 == 2:                          #kembali ke menu utama
            menu_utama()

        else:
            print('silakan pilih opsi dari menu yang ada\n ')
            continue 
def menu_3():           #menu UPDATE buku
    while pilihan_menu == 3 : 
        print('MENU UPDATE\n 1. Ubah Data Buku \n 2. Kembali ke Menu Utama \n')
        opsi_menu_3 = int(input(' Masukkan opsi yang dipilih: \n'))

        if opsi_menu_3 == 1:        #proses update buku
            input_kode_buku_update = int(input('Masukkan ID Buku yang akan diupdate: '))
            for i in dict_buku:
                if i['ID_Buku'] == input_kode_buku_update:
                    print(dict_buku[input_kode_buku_update])        #cek id buku yang akan diupdate
                    konfirmasi_edit_buku = int(input('Lanjut update?\n 1. Yes\n 2.No : '))      #konfirmasi data yang akan diupdate
                    if konfirmasi_edit_buku == 1:
                        kolom = input('Silakan KETIK kategori untuk diubah\n 1. Judul\n 2. Author\n 3. Genre\n 4. Tahun\n 5. Halaman\n 6. status :')
                        kolom = kolom.capitalize()                                                        #pemilihan kategori yang akan diupdate                                              
                        data_baru = input('Silakan masukan nilai yang akan diupdate: ')                     #input data baru
                        update_buku(input_kode_buku_update,kolom,data_baru)    
                    if konfirmasi_edit_buku == 2:           #pembatalan update data
                        break
            else:
                print('data tidak ada')         #jika id_buku tidak ada di database

        elif opsi_menu_3 == 2:
            menu_utama()
        
        else:
            print('silakan pilih opsi dari menu yang ada\n ')
            continue

def menu_4():       #menu DELETE buku
    while pilihan_menu == 4 :  
        print('MENU DELETE\n 1. Hapus Data Buku \n 2. Kembali ke Menu Utama \n')
        opsi_menu_4 = int(input(' Masukkan opsi yang dipilih: \n'))
        if opsi_menu_4 == 1:        #proses hapus buku
            input_kode_buku_hapus = int(input('Masukkan ID Buku yang akan dihapus: '))
            for i in dict_buku:
                if i['ID_Buku'] == input_kode_buku_hapus:   #buku bisa dihapus jika tercatat di database
                    print(dict_buku[input_kode_buku_hapus])
                    konfirmasi_hapus_buku = int(input('Lanjut hapus?\n 1. Yes\n 2.No : '))  #konfirmasi untuk hapus data
                    if konfirmasi_hapus_buku == 1:
                        hapus_buku(input_kode_buku_hapus)
                    if konfirmasi_hapus_buku == 2:
                        break

            else:
                print('data tidak ada')
                    
        if opsi_menu_4 ==2:
            menu_utama()

menu_utama()