# membuat program kasir 
def Ulang_kasir():
    Ulang_kasir = input('hitung lagi: (y/n)')
    if Ulang_kasir == 'y':
        
        kasir()
    
    elif Ulang_kasir == 'n':
        print('ingin hitung lagi?')
        tanya()
    
    else:
        print('input program salah harap ulangi')

def kasir():
 
    nama_barang = input('masukan pesanan anda \t: ')
    harga = int(input('masukan harga barang \t: '))
    jumlah_beli = int(input('masukan jumlah barang yang anda beli: '))

    
    total = harga * jumlah_beli
    
   
    print(f'harga total: {nama_barang}, = {total}')

   
    bayar = int(input('masukan pembayaran \t: '))

    
    kurang = total - bayar
    kembalian = bayar - total

    if bayar > total:
        print(f'jumlah kembalian anda adalah {kembalian}')
        tanya()
    
    elif bayar == total:
        print('uang anda pas, terimakasih telah berbelanja ')

    else:
        print(f'maaf uang anda tidak cukup, uang anda kurang {kurang}')
        Ulang_kasir()


def main_menu():
  
    print('=' * 12, 'MAIN MENU APLIKASI KASIR', '=' * 12)
    print('selamat datang di aplikasi kasir')
    print('=' * 20, 'masukan input aplikasi', '=' * 20)
    print('1. Program kasir')
    print('2. program kalkulator')
    print('3. exit program')

   
    pilihan = input('pilih menu: ')

    if pilihan == '1':
        kasir()
    elif pilihan == '2':
        kalkulator()
    else:
        print('Exit')
        exit()



def get_login():
    print('=' * 20)
    print('halaman login kasir')
    username = input('masukan username kasir anda \t: ')
    password = input('masukan password \t\t: ')

    if username == 'admin' and password == 'adminpass':
        print('login berhasil\n\n')
        main_menu()
    else:
        print('login gagal coba lagi')
        get_login()

def tanya():
    tanya = input('kembali ke menu? (y/n)')
    if tanya == 'y':
        main_menu()
    elif tanya == 'n':
        exit()
    else:
        print('input salah')
        print('masukan dengan benar')


def kalkulator():
    print('=' * 12)
    print('Program Kalukator')

    print()
    print('Operator')
    print('=' * 12)
    print('1. tambah')
    print('2. kurang ')
    print('3. bagi')
    print('4. kali')
    print('5. sisa bagi')

    a = int(input('masukan angka pertama \t: '))
    b = int(input('masukan angka kedua \t: '))

    operator = input('masukan operator \t: ')

    if operator == '1':
        print('hasil dari {} + {} = {}'.format(a, b, a + b))
    elif operator == '2':
        print('hasil dari {} - {} = {}'.format(a, b, a - b))
    elif operator == '3':
        print('hasil dari {} / {} = {}'.format(a, b, a / b))
    elif operator == '4':
        print('hasil dari {} * {} = {}'.format(a, b, a * b))
    elif operator == '5':
        print('hasil dari {} % {} = {}'.format(a, b, a % b))
    else:
        print('masukan input yang benar')


if __name__=='__main__':
    get_login()