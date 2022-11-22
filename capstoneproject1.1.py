# Project Nilai Siswa :

# 1.	Tampilkan nilai
# 2.	Tambahkan nilai siswa
# 3.	Update nilai
# 4.	Hapus nilai
# 5.	Selesai/keluar

#membuat dictionary untuk Daftar Nama Siswa
DNS = {
    'IM' : {'Nama Lengkap' : 'Irin Marsita', 'Jenis Kelamin' : 'Perempuan', 'Tanggal Lahir' : '15 Agustus 1996' , 'Nilai Akhir' : '94' , 'Status Kelulusan' : 'Lulus'},
    'DP': {'Nama Lengkap' : 'Dian Puspita' , 'Jenis Kelamin' : 'Perempuan', 'Tanggal Lahir' : '15 April 1996' , 'Nilai Akhir' : '88' , 'Status Kelulusan' : 'Lulus'},
    'GC' : {'Nama Lengkap' : 'Guritno Can', 'Jenis Kelamin' : 'Laki-laki' , 'Tanggal Lahir' : '28 Oktober 1996' , 'Nilai Akhir' : '55' , 'Status Kelulusan' : 'Tidak Lulus'},
    'EP': {'Nama Lengkap' : 'Eka Pratama' , 'Jenis Kelamin' : 'Laki-laki', 'Tanggal Lahir' : '31 Desember 1996' , 'Nilai Akhir' : 'N/A' , 'Status Kelulusan' : 'Incomplete'},
    'EN' : {'Nama Lengkap' : 'Evan Nababan', 'Jenis Kelamin' : 'Laki-laki' , 'Tanggal Lahir' : '1 oktober 1996' , 'Nilai Akhir' : '80' , 'Status Kelulusan' : 'Lulus'},
    'DN': {'Nama Lengkap' : 'Denisa Nur', 'Jenis Kelamin' : 'Perempuan' , 'Tanggal Lahir' : '1 Desember 1996' , 'Nilai Akhir' : '45' , 'Status Kelulusan' : 'Tidak Lulus'}
} 

def Nama_Siswa ():
    if len (DNS) == 0 :
        print ('Nama tidak ditemukan')
    else : 
        print ('Nama Lengkap \t | Jenis Kelamin \t| Tanggal Lahir \t| Nilai Akhir \t| Status Kelulusan')
        for key in DNS.keys():
            print ('{} \t {} \t\t {} \t\t {} \t {} \t'.format(DNS[key]['Nama Lengkap'],DNS[key]['Jenis Kelamin'], DNS[key]['Tanggal Lahir'], DNS[key]['Nilai Akhir'], DNS[key]['Status Kelulusan'] ) )
            
def tampilkan_nilai ():
    while len (DNS) ==0:
        print  ('nilai tidak ditemukan')
        break
    else :
        while True:
            pilih_menu = int(input('==Menu Nilai Akademik==\n1. Lihat Status Kelulusan\n 2. Lihat Seluruh Data Siswa \n 3. Pencarian Nama \n 4. kembali ke menu \n Pilih menu : ')) 
            if pilih_menu == 1:
                pilih_status = int(input('==Status Kelulusan==\n1. Lulus \n 2. Tidak Lulus \n 3. Incomplete \n 4. kembali ke menu \n Pilih Status : '))
                if pilih_status == 1:
                    print ('Nama Lengkap \t |Jenis Kelamin \t| Tanggal lahir \t| Nilai Akhir \t|Status Kelulusan')
                    for key in DNS.keys():
                        if DNS[key]['Status Kelulusan'] == 'Lulus':
                            print ('{} \t {} \t\t {} \t {} \t {} \t'.format(DNS[key]['Nama Lengkap'],DNS[key]['Jenis Kelamin'], DNS[key]['Tanggal Lahir'], DNS[key]['Nilai Akhir'], DNS[key]['Status Kelulusan'] ) ) 
                        else :
                             continue
                elif pilih_status == 2:
                    print ('Nama Lengkap \t |Jenis Kelamin \t| Tanggal lahir \t| Nilai Akhir \t|Status Kelulusan')
                    for key in DNS.keys():
                        if DNS[key]['Status Kelulusan'] == 'Tidak Lulus':
                            print ('{} \t {} \t\t {} \t {} \t {} \t'.format(DNS[key]['Nama Lengkap'],DNS[key]['Jenis Kelamin'], DNS[key]['Tanggal Lahir'], DNS[key]['Nilai Akhir'], DNS[key]['Status Kelulusan'] ) )
                        else :
                            continue
                elif pilih_status == 3:
                    print ('Nama Lengkap \t |Jenis Kelamin \t| Tanggal lahir \t| Nilai Akhir \t|Status Kelulusan')
                    for key in DNS.keys():
                        if DNS[key]['Status Kelulusan'] == 'Incomplete':
                            print ('{} \t {} \t\t {} \t {} \t {} \t'.format(DNS[key]['Nama Lengkap'],DNS[key]['Jenis Kelamin'], DNS[key]['Tanggal Lahir'], DNS[key]['Nilai Akhir'], DNS[key]['Status Kelulusan'] ) )
                        else :
                             continue
                elif pilih_status == 4:
                    break
                else :
                    print ('Status yang dicari tidak tersedia')
            elif pilih_menu == 2:
                Nama_Siswa()
            elif pilih_menu == 3:
                cari = input ("Nama Siswa yang dicari : ")
                print ('Nama Lengkap \t |Jenis Kelamin \t| Tanggal Lahir \t| Nilai Akhir \t|Status Kelulusan')
                for key in DNS.keys():
                    if cari.lower() in DNS[key]['Nama Lengkap'].lower() :
                        print ('{} \t {} \t\t {} \t {} \t {} \t'.format(DNS[key]['Nama Lengkap'],DNS[key]['Jenis Kelamin'], DNS[key]['Tanggal Lahir'], DNS[key]['Nilai Akhir'], DNS[key]['Status Kelulusan'] ) )
                    else :
                        continue
            elif pilih_menu == 4:
                break
            else :
                print ('menu tidak ditemukan')

def tambah_data():
    while True:
        Nama_Siswa()
        input_nama = input ('Masukkan Nama :')
        nama_baru = input_nama.replace (' ','')
        if nama_baru.lower() not in DNS.keys ():
            print ('isi data siswa baru')
            nl_baru = input ('Masukkan Nama  :')
            jk_baru = input ('Masukkan Jenis Kelamin :')
            tl_baru =input ('Masukkan Tanggal Lahir :')
            nilai_baru = input ( 'Masukkan Nilai :')
            status_baru = input ('Masukkan Status :')
            cek = input (f'apakah informasi ini akan ditambahkan = {nl_baru},{jk_baru},{tl_baru},{nilai_baru},{status_baru} Y/N :')
            if cek != 'Y' :
                print ('dibatalkan')
                break
            else :
                DNS[nama_baru.lower()]={'Nama Lengkap' : nl_baru, 'Jenis Kelamin' : jk_baru, 'Tanggal Lahir' : tl_baru, 'Nilai Akhir' : nilai_baru, 'Status Kelulusan' : status_baru }
                Nama_Siswa()
                print ("data siswa berhasil ditambahkan")
                break
        else :
            print ('siswa tersebut sudah terdaftar')
            break

def update_data ():
    perbaru_data = int(input('==Update Data==\n1. Ubah Data\n 2.  kembali ke menu \n Pilih menu : '))
    if perbaru_data == 1:
         Nama_Siswa()
         perbaru_data = input('masukkan data yang mau di update :')
         hasil_update = perbaru_data.replace (' ','')
         while hasil_update.lower() in DNS.keys():
            menu_update = int(input('==UPDATE DATA SISWA==\n DATA YANG HENDAK DIUPDATE \n 1.Nama Lengkap \n 2.Jenis Kelamin \n 3.Tanggal lahir \n 4. Nilai Akhir \n5.Status Kelulusan \n 6. kembali ke menu \n Pilih menu : '))
            if menu_update ==1 :
                update_nama = input('masukkan nama')
                update_nama_baru = update_nama.replace (' ','')
                while update_nama_baru.lower() in DNS.keys():
                    print ('nama tersebut telah ada')
                    update_nama = input('masukkan nama baru')
                    update_nama_baru = update_nama.replace (' ','')
                ceklagi1= input ('apakah informasi yakin mau di update? Y/N :')
                if ceklagi1 != 'Y' :
                    print ('dibatalkan')
                    break
                else :
                     DNS[update_nama_baru] = DNS[hasil_update.lower()]
                     del DNS[hasil_update.lower()]
                     DNS[update_nama_baru] ['Nama Lengkap'] = update_nama
                     Nama_Siswa ()
                     print ('Nama Terupdate')
                     break
            elif menu_update==2:
                update_jk = input('masukkan update jenis kelamin : ')
                ceklagi2= input ('apakah informasi ini akan diupdate? Y/N :')
                if ceklagi2 != 'Y' :
                    break
                else :
                    DNS[hasil_update.lower ()]['Jenis Kelamin'] = update_jk 
                    Nama_Siswa ()
                    print ('update jenis kelamin')
                    break
            elif menu_update==3:
                update_tl = input('masukkan update tanggal lahir: ')
                ceklagi3= input ('apakah informasi ini akan diupdate ? Y/N :')
                if ceklagi3 != 'Y' :
                    break
                else :
                    DNS[hasil_update.lower()]['Tanggal Lahir'] = update_tl
                    Nama_Siswa ()
                    print ('tanggal lahir diubah')
                    break
            elif menu_update==4:
                update_nilai = input('masukkan update nilai: ')
                ceklagi4= input (f'apakah informasi ini akan diupdate = {update_nilai} Y/N :')
                if ceklagi4 != 'Y' :
                    print ('dibatalkan')
                    break
                else :
                    DNS[hasil_update.lower ()]['Nilai akhir'] = update_nilai
                    Nama_Siswa ()
                    print ('update nilai')
                    break
            elif menu_update==5:
                update_status = input('masukkan update status: ')
                ceklagi5= input (f'apakah informasi ini akan diupdate = {update_status} Y/N :')
                if ceklagi4 != 'Y' :
                    print ('dibatalkan')
                    break
                else :
                    DNS[hasil_update.lower ()]['Status Kelulusan'] = update_status
                    Nama_Siswa ()
                    print ('tidak ada update nilai')
                    break
            else :
                break
         else :
             print ('tidak tersedia')

def hapus_data ():
    Nama_Siswa ()
    hapus_data = input('masukkan data yang ingin dihapus :')
    data_terhapus = hapus_data.replace (' ','')
    while data_terhapus.lower() not in DNS.keys():
        print ('data tidak ditemukan')
        break
    else : 
        cekhapus11 = input (f'apakah informasi akan dihapus {data_terhapus}  ?  Y/N :')
        while cekhapus11 != "Y" :
            print ('data tidak dihapus')
            break
        else :
            del DNS.keys[data_terhapus.lower()]
            Nama_Siswa ()
            print('data terhapus')


while True :
    pilih_menu = int (input ('''
    
    Menu Utama :     
1.	Tampilkan Data Siswa
2.	Tambahkan Data Siswa
3.	Update nilai
4.	Hapus nilai
5.	Selesai/keluar 
    
    
Masukkan Pilihan Menu :  '''))

    if pilih_menu ==1:
        tampilkan_nilai()
    elif pilih_menu ==2:
        tambah_data()
    elif pilih_menu ==3:
        update_data()   
    elif pilih_menu ==4:
        hapus_data()
    elif pilih_menu ==5:
        quit()
    else :
        print ('Tidak Ditemukan')        


    











                    



# xxxx



# (main menu nya tinggal panggil funsi)
# while True :
# aksi = int(input(‘’’
# Main Menu : 
# 1.	Tampilkan nilai
# 2.	Tambahkan nilai siswa
# 3.	Update nilai
# 4.	Hapus nilai
# 5.	Selesai/keluar
# Masukkan nomor pilihan aksi : ‘’’))

# If aksi ==1 :
# 	Xxxx
# elif aksi ==2 :
# 	Xxxx 
# elif aksi ==3 :
# 	Xxxx 
# elif aksi ==4:
# 	Xxxx 
# elif aksi ==0 :
# 	quit ()
# else :
# print (‘aksi tidak ditemukan’)




