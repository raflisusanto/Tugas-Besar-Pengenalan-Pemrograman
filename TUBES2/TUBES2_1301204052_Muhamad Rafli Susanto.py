import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.scrolledtext import ScrolledText
from time import strftime

todos = {}

# key disini itu maksudnya tanggal
def addTodo(win, key, jam, menit, judul, keterangan):
    newTodo = {
        'waktu':'{}:{}'.format(jam.get(), menit.get()),
        'judul': judul.get(),
        'keterangan': keterangan.get('1.0', tk.END)
    }
    # ngecek apakah tanggal udh punya list atau belum
    if key in todos:
        todos[key].append(newTodo)
    else:
        todos[key] = [newTodo]
    win.destroy()
    ListTodo()

def ListTodo(cb=None):
    for i in treev.get_children():
        treev.delete(i)
    tanggal = str(cal.selection_get())
    if tanggal in todos:
        # kenapa pake len, dia ngecek di todos itu mungkin sudah ada multiple kegiatan, jadi otomatis ngeprint semua
        for i in range(len(todos[tanggal])):  # menampilkan kegiatan yang sudah ditambahkan, ke dalam treeview
            treev.insert("", "end", text=i, values=(todos[tanggal][i]['waktu'], todos[tanggal][i]['judul']))

def delTodos():
    tanggal = str(cal.selection_get())
    selectedItem = treev.focus()  # Meng-assign treeview yang di klik
    todos[tanggal].pop(treev.item(selectedItem)['text'])  # text disini isinya index listnya yg kita buat di ListTodo()
    ListTodo()

def SaveTodos():
    f = open('mytodo.dat', 'w')
    f.write(str(todos))
    f.close()

def LoadTodos():
    global todos
    f = open('mytodo.dat', 'r')
    data = f.read()
    f.close()
    todos = eval(data)  # data bisa langsung di konversi ke dict
    ListTodo()

def detailTodos(cb=None):
    win = tk.Toplevel()
    win.wm_title("Detail Kegiatan")
    win.configure(bg='orange')
    tanggal = str(cal.selection_get())
    # Atur biar value nya sesuai yg di klik
    selectedItem = treev.focus()
    selectedIndex = treev.item(selectedItem)['text']  # Index disini tuh index list yang ada dalam dictionary
    selectedTodo = todos[tanggal][selectedIndex]  # Ngeassign list yang dipilih
    # Bikin Widget nya
    judul = tk.StringVar(value=selectedTodo['judul'])
    tk.Label(win, text='Tanggal          :', font="Poppins 12 bold", background='orange', foreground='white').grid(row=0, column=0, sticky='W')
    tk.Label(win, font="Poppins 12", background='orange', foreground='white', text='{} | {}'.format(tanggal, selectedTodo['waktu'])).grid(row=0, column=1, sticky='W')
    tk.Label(win, text="Judul                 :", font="Poppins 12 bold", background='orange', foreground='white').grid(row=1, column=0, sticky='W')
    # Maksud disabled disini jadi buat field tk.Entry menjadi read only
    tk.Entry(win, state="disabled", textvariable=judul).grid(row=1, column=1, sticky='W')
    tk.Label(win, text="Keterangan:", font="Poppins 12 bold", background='orange', foreground='white').grid(row=2, column=0, sticky='W')
    keterangan = ScrolledText(win, width=12, height=5)  # Bikin scroll
    keterangan.grid(row=2, column=1, sticky='W')
    keterangan.insert(tk.INSERT, selectedTodo['keterangan'])  # Ambil value keterangan dari dict
    keterangan.configure(state='disabled')  # Buat field jadi read only


def AddForm():
    win = tk.Toplevel()
    win.wm_title("Tambah Kegiatan")
    win.configure(bg='orange')
    # Default Value dari jam, menit, dan judul
    jam = tk.IntVar(value=10)
    menit = tk.IntVar(value=30)
    judul = tk.StringVar(value="")
    # Buat label/teks untuk waktu terus dibuat spinbox nya
    tk.Label(win, text='Waktu              :', font="Poppins 12 bold", background='orange', foreground='white').grid(row=0, column=0, sticky='W')
    tk.Spinbox(win, from_=0, to=23, textvariable=jam, width=3).grid(row=0, column=1, sticky="W")
    tk.Spinbox(win, from_=0, to=59, textvariable=menit, width=3).grid(row=0, column=2, sticky="W")
    # Buat label/teks untuk judul dan dibuat box entry nya
    tk.Label(win, text="Judul                 :", font="Poppins 12 bold",background='orange', foreground='white').grid(row=1, column=0, sticky='W')
    tk.Entry(win, textvariable=judul).grid(row=1, column=1, columnspan=3)
    # Buat label/teks untuk keterangan
    tk.Label(win, text="Keterangan:", font="Poppins 12 bold",background='orange', foreground='white').grid(row=2, column=0, sticky='W')
    # Buat Scroll button untuk keterangan
    keterangan = ScrolledText(win, width=12, height=5)
    keterangan.grid(row=2, column=1, columnspan=2, rowspan=4)
    tanggal = str(cal.selection_get())
    # Buat button tambah dan manggil fungsi addTodo (command)
    tk.Button(win, text="Tambah", font="Poppins 9 bold", bg="green", fg='white', command=lambda: addTodo(win, tanggal, jam, menit, judul, keterangan)).grid(row=8, column=1, sticky='WS')

def title():
    waktu = strftime('%H:%M')
    tanggal = str(cal.selection_get())
    root.title(tanggal + " | " + waktu + " | Calendar")
    root.after(1000, title)

root = tk.Tk()
s = ttk.Style()
s.theme_use("clam")
s.configure('Treeview', rowheight=16, font='Poppins 9')
s.configure('Treeview.Heading', font="Poppins 8")
root.title("Calendar")

cal = Calendar(root, font="Poppins 14 bold", selectmode="day", locale="id_ID", cursor="hand1", background="orange", disabledbackground="black", bordercolor="white",
               headersbackground="white", normalbackground="orange", foreground='white',
               normalforeground='white', headersforeground='black', weekendbackground='red', weekendforeground='white', firstweekdaybackground='red')
cal.grid(row=0, column=0, sticky="N", rowspan=14, columnspan=2)
cal.bind("<<CalendarSelected>>", ListTodo)  # Binding ListTodo ke Tanggal yg di select
tanggal = str(cal.selection_get())  # Untuk masukkin tanggal yg di select ke variabel

treev = ttk.Treeview(root)
treev.grid(row=15, column=0, sticky="WNES", rowspan=5, columnspan=2)

scrollBar = tk.Scrollbar(root, orient="vertical", command=treev.yview)
scrollBar.grid(row=15, column=2, sticky="ENS", rowspan=5)

treev.configure(yscrollcommand=scrollBar.set)
treev.bind("<Double-1>", detailTodos)  # Nge bind double click mouse1 utk ngejalanin fungsi detailTodos()
treev['columns'] = ("1", "2")
treev['show'] = 'headings'
treev.column("1", width=20)
treev.heading("1", text="Jam")
treev.heading("2", text="Judul")

btnAdd = tk.Button(root, text="Tambah", width=20, command=AddForm, font="Poppins 10 bold", bg='green', fg='white')
btnAdd.grid(row=20, column=0, sticky='WNES')

btnDel = tk.Button(root, text="Hapus", width=20, command=delTodos, font="Poppins 10 bold", bg='red', fg='white')
btnDel.grid(row=21, column=0, sticky='WNES')

btnLoad = tk.Button(root, text="Load", width=20, command=LoadTodos, font="Poppins 10")
btnLoad.grid(row=21, column=1, sticky='WNES')

btnSave = tk.Button(root, text="Save", width=20, command=SaveTodos, font="Poppins 10")
btnSave.grid(row=20, column=1, sticky='WNES')
title()

root.mainloop()