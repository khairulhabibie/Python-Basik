import tkinter

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text='hore aku di tekan')
    label2.pack()

label = tkinter.Label(main_window, text='halo, saya dalah \n GUI sederhana yang \n menggunakan python')
tombol = tkinter.Button(main_window, text='tekan aku', command=event_tekan)

label.pack()
tombol.pack()
main_window.mainloop()