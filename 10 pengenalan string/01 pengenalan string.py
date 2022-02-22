# pengenalan string
'''
1. dengan menggunakan single qout '...'
2. dengan menggunakan double qout "..."
'''
# cara penulisan string:
    # single qouts
data = 'halo, apa kabar?'
print(data)
print(type(data))
    # double qouts
data = "halo, apa kabar?"
print(data)
print(type(data))

# karakter tanda backslash \
print('karakter tanda'.center(30,'-'))
    # membuat tanda ' menjadi string
print('mari sholat jum\'at')
print('g\'day, isn\'t it?')
    # backlslash
print("c:\\user\\Habibie")
    # tab
print("khairul\thabibie, jauhan")
    # backspace
print("khairul \bhabibie, deketan")
    # newline
print("baris pertama.\nbaris kedua.")   #LF -> line feed -> unix, linux, macos
print("baris pertama.\rbaris kedua.")   #CR -> carriage return -> commmodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") #CRLF -> line feed carriage return -> dipakai oleh window

# string literal atau raw
print('='*10+'string literal atau raw')
print('C:\new folder')      # salah penulisan
print(r'C:\new folder')     # salah penulisan
    # multiline literal string
print("""
nama : khairul
kelas : ipa 2
""")

# multiline literal string dan RAW
print('='*10+'multinline literal atau raw')
print(r"""
nama : khairul
kelas : ipa 2
website : www.khairul.com\newID
""")
