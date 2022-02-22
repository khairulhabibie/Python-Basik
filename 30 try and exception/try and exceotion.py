while True:
    try:
        pembilang = int(input('masukkan angka pembilang: '))

        penyebut = int(input('masukkan angka penyebut: '))
        hasil = pembilang/penyebut
        break
    except ValueError:
        print('yang anda masukkan bukan angka')
    except ZeroDivisionError:
        print('angka penyebut yang anda masukkan adalah nol, input angka yang bukan nol ya!')

print('berhasil anda memasukkan angka: ', hasil)