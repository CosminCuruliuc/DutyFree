import tkinter
from datetime import *
from tkinter import *
from tkinter import ttk, messagebox
import queue
from tkinter.ttk import Combobox

import oracledb

import backend

main_menu = None
back = None
Adrese = None
Clienti = None
Comenzi = None
Furnizori = None
DetaliiComenzi = None
Produse = None
Angajati = None
all_tabels = None
count = None
my_tree = None
savepoints = queue.Queue(maxsize=5)


def exit_button():
    backend.close_connection()
    exit(0)


def back_selection(menu):
    menu.pack_forget()
    show_tabels(menu)


def back_menu(menu):
    menu.pack_forget()
    menuinfo()


def menuinfo():
    global main_menu, back, Adrese, Clienti, Comenzi, Furnizori, DetaliiComenzi, Produse, Angajati, all_tabels

    main_menu = Frame(root, bg="#829079", width=900, height=600)

    main_menu.pack_forget()
    main_menu.pack(fill="both", expand=True)

    menu_Label = Label(main_menu, text='Gestiunea activitatii unui magazin de tipul duty free', font=("Arial", 25),
                       bg="#829079", fg="#EDE6B9")
    menu_Label.pack(pady=235)

    print_tabels = Button(main_menu, text="Afiseaza tabelele", font=("Arial", 15), bg="#829079", fg="#EDE6B9", width=20,
                          height=2, command=lambda: show_tabels(main_menu))
    print_tabels.place(x=330, y=300)

    exitButton = Button(main_menu, text="Iesire", font=("Arial", 15), bg="#829079", fg="#EDE6B9", width=20, height=2,
                        command=exit_button)
    exitButton.place(x=330, y=375)


def show_tabels(menu):
    global main_menu, back, Adrese, Clienti, Comenzi, Furnizori, DetaliiComenzi, Produse, Angajati, all_tabels

    all_tabels = Frame(root, bg="#829079", width=900, height=600)
    Adrese = Frame(root, bg="#829079", width=900, height=600)
    Angajati = Frame(root, bg="#829079", width=900, height=600)
    Clienti = Frame(root, bg="#829079", width=900, height=600)
    Comenzi = Frame(root, bg="#829079", width=900, height=600)
    DetaliiComenzi = Frame(root, bg="#829079", width=900, height=600)
    Furnizori = Frame(root, bg="#829079", width=900, height=600)
    Produse = Frame(root, bg="#829079", width=900, height=600)
    menu.pack_forget()
    all_tabels.pack(fill="both", expand=True)

    back = Button(all_tabels, text="Inapoi", font=("Arial", 15), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_menu(all_tabels))
    adrese = Button(all_tabels, text="Adrese", font=("Arial", 25), bg="#829079", fg="#EDE6B9", command=adrese_info)
    angajati = Button(all_tabels, text="Angajati", font=("Arial", 25), bg="#829079", fg="#EDE6B9",
                      command=angajati_info)
    clienti = Button(all_tabels, text="Clienti", font=("Arial", 25), bg="#829079", fg="#EDE6B9", command=clienti_info)
    comenzi = Button(all_tabels, text="Comenzi", font=("Arial", 25), bg="#829079", fg="#EDE6B9", command=comenzi_info)
    furnizori = Button(all_tabels, text="Furnizori", font=("Arial", 25), bg="#829079", fg="#EDE6B9",
                       command=furnizori_info)
    detaliicomenzi = Button(all_tabels, text="DetaliiComenzi", font=("Arial", 25), bg="#829079", fg="#EDE6B9",
                            command=detalii_comenzi_info)
    produse = Button(all_tabels, text="Produse", font=("Arial", 25), bg="#829079", fg="#EDE6B9", command=produse_info)

    back.place(x=825, y=535)
    adrese.place(x=90, y=150, width=225, height=50)
    angajati.place(x=340, y=150, width=225, height=50)
    clienti.place(x=590, y=150, width=225, height=50)
    comenzi.place(x=90, y=250, width=225, height=50)
    furnizori.place(x=340, y=250, width=225, height=50)
    detaliicomenzi.place(x=590, y=250, width=225, height=50)
    produse.place(x=340, y=350, width=225, height=50)


def insert_into_adrese(window, tree, b, d, f, table, list):
    error = ''
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    error = backend.insert_into_table_adrese(table, list)
    if error == 'WRONG':
        adrese_info()
    else:
        clienti_info()


def adrese_info():
    global my_tree
    all_tabels.forget()
    Adrese.pack(fill="both", expand=True)
    back = Button(Adrese, text="Inapoi", font=("Arial", 15), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(Adrese))
    back.place(x=825, y=535)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Adrese)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[0])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0], columns[5][0])

    # print(my_tree)

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ADRESAID", anchor=W, width=85, stretch=NO)
    my_tree.column("STRADA", anchor=CENTER, width=225, stretch=NO)
    my_tree.column("ORAS", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("STAT", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("TARA", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("CODPOSTAL", anchor=CENTER, width=150, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ADRESAID", text="ADRESAID", anchor=W)
    my_tree.heading("STRADA", text="STRADA", anchor=CENTER)
    my_tree.heading("ORAS", text="ORAS", anchor=CENTER)
    my_tree.heading("STAT", text="STAT", anchor=CENTER)
    my_tree.heading("TARA", text="TARA", anchor=CENTER)
    my_tree.heading("CODPOSTAL", text="COD_POSTAL", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[0])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Adrese, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    strada = Label(data_frame, text="Strada", background="#829079", foreground="#E4D4C8")
    strada.grid(row=0, column=0, padx=10, pady=10)
    strada_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="strada")
    strada_entry.grid(row=0, column=1, padx=40, pady=10)

    oras = Label(data_frame, text="Oras", background="#829079", foreground="#E4D4C8")
    oras.grid(row=0, column=2, padx=10, pady=10)
    oras_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="oras")
    oras_entry.grid(row=0, column=3, padx=65, pady=10)

    stat = Label(data_frame, text="Stat", background="#829079", foreground="#E4D4C8")
    stat.grid(row=0, column=4, padx=10, pady=10)
    stat_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="stat")
    stat_entry.grid(row=0, column=5, padx=10, pady=10)

    tara = Label(data_frame, text="Tara", background="#829079", foreground="#E4D4C8")
    tara.grid(row=1, column=0, padx=10, pady=10)
    tara_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="tara")
    tara_entry.grid(row=1, column=1, padx=10, pady=10)

    cd = Label(data_frame, text="Cod_postal", background="#829079", foreground="#E4D4C8")
    cd.grid(row=1, column=2, padx=10, pady=10)
    cd_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="cd")
    cd_entry.grid(row=1, column=3, padx=10, pady=10)

    button_frame = LabelFrame(Adrese, text="Comenzi", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_adrese(Adrese, my_tree, data_frame, button_frame, tree_frame,
                                                           backend.Table_names[0],
                                                           [None, strada_entry.get(), oras_entry.get(),
                                                            stat_entry.get(), tara_entry.get(),
                                                            cd_entry.get()]
                                                           ))

    add_button.grid(row=0, column=1, padx=10, pady=10)
    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_adrese(my_tree, strada_entry, oras_entry, stat_entry,
                                                                tara_entry, cd_entry, id_entry)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_adrese(my_tree, id_entry, Adrese, data_frame, button_frame,
                                                                tree_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_adrese(Adrese, my_tree, data_frame, button_frame, tree_frame,
                                                                strada_entry,
                                                                oras_entry, stat_entry,
                                                                tara_entry, cd_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_adrese(e, data_frame))


def remove_record_adrese(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM Adrese
                WHERE ADRESAID = :id""",
                                      {
                                          'id': id.get(),
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    adrese_info()


def cancel_update_adrese(window, tree, b, d, f, strada_entry,
                         oras_entry, stat_entry,
                         tara_entry, cd_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    strada_entry.delete(0, END)
    oras_entry.delete(0, END)
    stat_entry.delete(0, END)
    tara_entry.delete(0, END)
    cd_entry.delete(0, END)

    adrese_info()


def select_record_adrese(event, parent):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("strada").insert(0, record[1])
    parent.children.get("oras").insert(0, record[2])
    parent.children.get("stat").insert(0, record[3])
    parent.children.get("tara").insert(0, record[4])
    parent.children.get("cd").insert(0, record[5])


def update_record_adrese(my_tree, strada, oras, stat, tara, cd, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            strada.get(), oras.get(), stat.get(), tara.get(), cd.get()))

    try:
        backend.conn.cursor().execute("""UPDATE Adrese SET
            STRADA = :strada,
            ORAS = :oras,
            STAT = :stat,
            TARA = :tara,
            CODPOSTAL = :cd 

            WHERE ADRESAID = :id""",
                                      {
                                          'strada': strada.get(),
                                          'oras': oras.get(),
                                          'stat': stat.get(),
                                          'tara': tara.get(),
                                          'cd': cd.get(),
                                          'id': id.get(),
                                      })
    except oracledb.DatabaseError as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_angajati(window, tree, b, d, f, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    error = backend.insert_into_table(table, list)
    if error == 'WRONG':
        menuinfo()
    else:
        angajati_info()


def angajati_info():
    global my_tree
    all_tabels.forget()
    Angajati.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Angajati)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[1])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0],
                          columns[3][0], columns[4][0], columns[5][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ANGAJATID", anchor=W, width=95, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=200, stretch=NO)
    my_tree.column("PRENUME", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("POZITIE", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("DATAANGAJARII", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("EMAIL", anchor=CENTER, width=175, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ANGAJATID", text="ANGAJATID", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("PRENUME", text="PRENUME", anchor=CENTER)
    my_tree.heading("POZITIE", text="POZITIE", anchor=CENTER)
    my_tree.heading("DATAANGAJARII", text="DATAANGAJARII", anchor=CENTER)
    my_tree.heading("EMAIL", text="EMAIL", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[1])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4].date(), record[5]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4].date(), record[5]),
                           tags=('oddrow',))
        count += 1

    data_frame = LabelFrame(Angajati, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#829079", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    prenume = Label(data_frame, text="Prenume", background="#829079", foreground="#E4D4C8")
    prenume.grid(row=0, column=2, padx=10, pady=10)
    prenume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="prenume")
    prenume_entry.grid(row=0, column=3, padx=65, pady=10)

    pozitie = Label(data_frame, text="Pozitie", background="#829079", foreground="#E4D4C8")
    pozitie.grid(row=0, column=4, padx=10, pady=10)
    optiuni = ["Junior", "Mediu", "Senior", "Expert"]
    selected_option = StringVar()
    pozitie_entry = Combobox(data_frame, values=optiuni, textvariable=selected_option, background="#829079",
                             foreground="#E4D4C8")
    pozitie_entry.grid(row=0, column=5, padx=65, pady=10)
    pozitie_entry.current(0)

    data_angajare = Label(data_frame, text="Data_angajare", background="#829079", foreground="#E4D4C8")
    data_angajare.grid(row=1, column=0, padx=10, pady=10)
    data_angajare_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8",
                                textvariable=StringVar(Angajati, value=str(date.today())), name="data_angajare")
    data_angajare_entry.grid(row=1, column=1, padx=10, pady=10)

    email = Label(data_frame, text="Email", background="#829079", foreground="#E4D4C8")
    email.grid(row=1, column=2, padx=10, pady=10)
    email_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="email")
    email_entry.grid(row=1, column=3, padx=10, pady=10)

    button_frame = LabelFrame(Angajati, text="Comenzi", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    back = Button(Angajati, text="Inapoi", font=("Arial", 13), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(Angajati))
    back.place(x=835, y=530)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_angajati(Angajati, my_tree, data_frame, button_frame, tree_frame,
                                                             backend.Table_names[1],
                                                             [None, nume_entry.get(), prenume_entry.get(),
                                                              pozitie_entry.get(),
                                                              datetime.strptime(data_angajare_entry.get(), '%Y-%m-%d'),
                                                              email_entry.get()])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_record_angajati(my_tree, nume_entry, prenume_entry,
                                                                  pozitie_entry, data_angajare_entry,
                                                                  email_entry, id_entry)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_angajati(my_tree, id_entry, Angajati, data_frame,
                                                                  button_frame, tree_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_angajati(Angajati, my_tree, data_frame, button_frame,
                                                                  tree_frame,
                                                                  nume_entry, prenume_entry, pozitie_entry,
                                                                  data_angajare_entry, email_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_angajati(e, data_frame, selected_option))


def remove_record_angajati(my_tree, id, window, b, d, f):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM Angajati
                WHERE ANGAJATID = :id""",
                                      {
                                          'id': id.get(),
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()

    angajati_info()


def cancel_update_angajati(window, tree, b, d, f, nume_entry, prenume_entry, pozitie_entry,
                           data_angajare_entry, email_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()

    nume_entry.delete(0, END)
    prenume_entry.delete(0, END)
    pozitie_entry.delete(0, END)
    data_angajare_entry.delete(0, END)
    email_entry.delete(0, END)

    angajati_info()


def select_record_angajati(event, parent, selected_option):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("prenume").insert(0, record[2])
    selected_option.set(record[3])
    parent.children.get("data_angajare").insert(0, record[4])
    parent.children.get("email").insert(0, record[5])


def update_record_angajati(my_tree, nume, prenume, pozitie, data_angajare, email,
                           id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            nume.get(), prenume.get(),
                                            pozitie.get(),
                                            datetime.strptime(data_angajare.get(), '%Y-%m-%d').date(),
                                            email.get()
                                            )
                 )

    try:
        backend.conn.cursor().execute("""UPDATE Angajati SET
            NUME = :nume,
            PRENUME = :prenume,
            POZITIE = :pozitie,
            DATAANGAJARII = :data_angajare,
            EMAIL = :email

            WHERE ANGAJATID = :id""",
                                      {
                                          'nume': nume.get(),
                                          'prenume': prenume.get(),
                                          'pozitie': pozitie.get(),
                                          'data_angajare': datetime.strptime(data_angajare.get(), '%Y-%m-%d').date(),
                                          'email': email.get(),
                                          'id': id.get()
                                      })

    except oracledb.DatabaseError as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_clienti(window, tree, b, d, f, s, table, list):
    error = ''
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    error = backend.insert_into_table_clienti(table, list)
    if error == 'WRONG':
        adrese_info()
    elif (error is None and
          len(backend.select_from_table(backend.Table_names[2])) == len(backend.select_from_table(table))):
        clienti_info()
    elif len(backend.select_from_table(backend.Table_names[2])) < len(backend.select_from_table(table)):
        adrese_info()


def update_clienti(my_tree, nume_entry, prenume_entry, email_entry, numar_telefon_entry,
                   clicked_adresa,
                   id_entry, window, b, d, f, s):
    update_record_clienti(my_tree, nume_entry, prenume_entry, email_entry, numar_telefon_entry, clicked_adresa,
                          id_entry)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    clienti_info()


def clienti_info():
    global my_tree
    all_tabels.forget()
    Clienti.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Clienti)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[2])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0],
                          columns[4][0], columns[5][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("CLIENTID", anchor=W, width=100, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("PRENUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("EMAIL", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("NUMARTELEFON", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("ADRESAID", anchor=CENTER, width=250, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("CLIENTID", text="CLIENTID", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("PRENUME", text="PRENUME", anchor=CENTER)
    my_tree.heading("EMAIL", text="EMAIL", anchor=CENTER)
    my_tree.heading("NUMARTELEFON", text="NUMARTELEFON", anchor=CENTER)
    my_tree.heading("ADRESAID", text="ADRESAID", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[2])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                           tags=('oddrow',))
        count += 1

    data_frame = LabelFrame(Clienti, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#829079", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=40, pady=10)

    prenume = Label(data_frame, text="Prenume", background="#829079", foreground="#E4D4C8")
    prenume.grid(row=0, column=2, padx=10, pady=10)
    prenume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="prenume")
    prenume_entry.grid(row=0, column=3, padx=65, pady=10)

    email = Label(data_frame, text="Email", background="#829079", foreground="#E4D4C8")
    email.grid(row=1, column=0, padx=10, pady=10)
    email_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="email")
    email_entry.grid(row=1, column=1, padx=10, pady=10)

    numar_telefon = Label(data_frame, text="Numar Telefon", background="#829079", foreground="#E4D4C8")
    numar_telefon.grid(row=1, column=2, padx=10, pady=10)
    numar_telefon_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="numar_telefon")
    numar_telefon_entry.grid(row=1, column=3, padx=10, pady=10)

    select_frame = LabelFrame(Clienti, text="Alegeti datele:", background="#829079", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_adrese = backend.select_from_table(backend.Table_names[0])

    clicked_adrese = StringVar(Clienti)
    clicked_adrese.set(tabela_adrese[0])
    alege_adresa = Label(select_frame, text="Alegeti adresa", background="#829079", foreground="#E4D4C8")
    alege_adresa.grid(row=0, column=0)
    drop_adrese = OptionMenu(select_frame, clicked_adrese, *tabela_adrese)
    drop_adrese.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                          activeforeground="#E4D4C8", highlightthickness=0)
    drop_adrese.grid(row=0, column=1, padx=0, pady=1)

    button_frame = LabelFrame(Clienti, text="Comenzi", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_clienti(Clienti, my_tree, data_frame, button_frame, tree_frame,
                                                            select_frame,
                                                            backend.Table_names[2],
                                                            [None, nume_entry.get(), prenume_entry.get(),
                                                             email_entry.get(), numar_telefon_entry.get(),
                                                             int(clicked_adrese.get().replace(',', '     ')[1:4])])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_clienti(my_tree, nume_entry, prenume_entry, email_entry,
                                                          numar_telefon_entry, clicked_adrese, id_entry,
                                                          Clienti, data_frame, button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_clienti(my_tree, id_entry, Clienti, data_frame,
                                                                 button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_clienti(Clienti, my_tree, data_frame, button_frame, tree_frame,
                                                                 select_frame,
                                                                 nume_entry, prenume_entry, email_entry,
                                                                 numar_telefon_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    back = Button(Clienti, text="Inapoi", font=("Arial", 13), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(Clienti))
    back.place(x=825, y=530)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_clienti(e, data_frame, clicked_adrese, tabela_adrese))


def remove_record_clienti(my_tree, id, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM Clienti
                WHERE CLIENTID = :id""",
                                      {
                                          'id': id.get(),
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    clienti_info()


def cancel_update_clienti(window, tree, b, d, f, s, nume_entry, prenume_entry, email_entry, numar_telefon_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    nume_entry.delete(0, END)
    prenume_entry.delete(0, END)
    email_entry.delete(0, END)
    numar_telefon_entry.delete(0, END)

    clienti_info()


def select_record_clienti(event, parent, adrese, ta):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("prenume").insert(0, record[2])
    parent.children.get("email").insert(0, record[3])
    parent.children.get("numar_telefon").insert(0, record[4])
    adrese.set(ta[record[5] - 13])


def update_record_clienti(my_tree, nume, prenume, email, numar_telefon, clicked_adrese, id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            nume.get(), prenume.get(), email.get()))

    try:
        backend.conn.cursor().execute("""UPDATE Clienti SET
            NUME = :nume,
            PRENUME = :prenume,
            EMAIL = :email,
            NUMARTELEFON = :numar_telefon,
            ADRESAID = :adrc
            
            WHERE CLIENTID = :id""",
                                      {
                                          'nume': nume.get(),
                                          'prenume': prenume.get(),
                                          'email': email.get(),
                                          'numar_telefon': numar_telefon.get(),
                                          'adrc': int(clicked_adrese.get().replace(',', '     ')[1:4]),
                                          'id': id.get()
                                      })
    except oracledb.DatabaseError as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_furnizori(window, tree, b, d, f, s, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    backend.insert_into_table(table, list)
    furnizori_info()


def update_furnizori(my_tree, nume_companie_entry, contact_nume_entry, contact_prenume_entry, contact_telefon_entry,
                     contact_email_entry, clicked_adresa,
                     id_entry, window, b, d, f, s):
    update_record_furnizori(my_tree, nume_companie_entry, contact_nume_entry, contact_prenume_entry,
                            contact_telefon_entry,
                            contact_email_entry, clicked_adresa,
                            id_entry)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    furnizori_info()


def furnizori_info():
    global my_tree
    all_tabels.forget()
    Furnizori.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Furnizori)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[5])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0], columns[5][0],
                          columns[6][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("FURNIZORID", anchor=W, width=100, stretch=NO)
    my_tree.column("NUMECOMPANIE", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("CONTACTNUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("CONTACTPRENUME", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("CONTACTTELEFON", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("CONTACTEMAIL", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("ADRESAID", anchor=CENTER, width=250, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("FURNIZORID", text="FURNIZORID", anchor=W)
    my_tree.heading("NUMECOMPANIE", text="NUMECOMPANIE", anchor=CENTER)
    my_tree.heading("CONTACTNUME", text="CONTACTNUME", anchor=CENTER)
    my_tree.heading("CONTACTPRENUME", text="CONTACTPRENUME", anchor=CENTER)
    my_tree.heading("CONTACTTELEFON", text="CONTACTTELEFON", anchor=CENTER)
    my_tree.heading("CONTACTEMAIL", text="CONTACTEMAIL", anchor=CENTER)
    my_tree.heading("ADRESAID", text="ADRESAID", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[5])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                           tags=('oddrow',))
        count += 1

    data_frame = LabelFrame(Furnizori, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume_companie = Label(data_frame, text="Nume_Companie", background="#829079", foreground="#E4D4C8")
    nume_companie.grid(row=0, column=0, padx=10, pady=10)
    nume_companie_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="nume_companie")
    nume_companie_entry.grid(row=0, column=1, padx=10, pady=10)

    contact_nume = Label(data_frame, text="Contact_Nume", background="#829079", foreground="#E4D4C8")
    contact_nume.grid(row=0, column=2, padx=10, pady=10)
    contact_nume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="contact_nume")
    contact_nume_entry.grid(row=0, column=3, padx=10, pady=10)

    contact_prenume = Label(data_frame, text="Contact_Prenume", background="#829079", foreground="#E4D4C8")
    contact_prenume.grid(row=1, column=4, padx=10, pady=10)
    contact_prenume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="contact_prenume")
    contact_prenume_entry.grid(row=1, column=5, padx=10, pady=10)

    numar_telefon = Label(data_frame, text="Numar_Telefon", background="#829079", foreground="#E4D4C8")
    numar_telefon.grid(row=1, column=0, padx=10, pady=10)
    numar_telefon_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="numar_telefon")
    numar_telefon_entry.grid(row=1, column=1, padx=10, pady=10)

    email = Label(data_frame, text="Email", background="#829079", foreground="#E4D4C8")
    email.grid(row=1, column=2, padx=10, pady=10)
    email_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="email")
    email_entry.grid(row=1, column=3, padx=10, pady=10)

    select_frame = LabelFrame(Furnizori, text="Alegeti datele:", background="#829079", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_adrese = backend.select_from_table(backend.Table_names[0])

    clicked_adrese = StringVar(Furnizori)
    clicked_adrese.set(tabela_adrese[0])
    alege_adresa = Label(select_frame, text="Alegeti adresa", background="#829079", foreground="#E4D4C8")
    alege_adresa.grid(row=0, column=0)
    drop_adrese = OptionMenu(select_frame, clicked_adrese, *tabela_adrese)
    drop_adrese.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                          activeforeground="#E4D4C8", highlightthickness=0)
    drop_adrese.grid(row=0, column=1, padx=0, pady=1)

    button_frame = LabelFrame(Furnizori, text="Furnizori", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_furnizori(Furnizori, my_tree, data_frame, button_frame, tree_frame,
                                                              select_frame,
                                                              backend.Table_names[5],
                                                              [None, nume_companie_entry.get(),
                                                               contact_nume_entry.get(),
                                                               contact_prenume_entry.get(), numar_telefon_entry.get(),
                                                               email_entry.get(),
                                                               int(clicked_adrese.get().replace(',', '     ')[1:4])])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_furnizori(my_tree, nume_companie_entry, contact_nume_entry,
                                                            contact_prenume_entry, numar_telefon_entry, email_entry,
                                                            clicked_adrese, id_entry, Furnizori, data_frame,
                                                            button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_furnizori(my_tree, id_entry, Furnizori, data_frame,
                                                                   button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_furnizori(Furnizori, my_tree, data_frame, button_frame,
                                                                   tree_frame,
                                                                   select_frame,
                                                                   nume_companie_entry, contact_nume_entry,
                                                                   contact_prenume_entry,
                                                                   numar_telefon_entry, email_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    back = Button(Furnizori, text="Inapoi", font=("Arial", 13), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(Furnizori))
    back.place(x=825, y=525)

    my_tree.bind('<<TreeviewSelect>>', lambda e: select_record_furnizori(e, data_frame, clicked_adrese, tabela_adrese))


def remove_record_furnizori(my_tree, id, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM Furnizori
                WHERE FURNIZORID = :id""",
                                      {
                                          'id': id.get(),
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    furnizori_info()


def cancel_update_furnizori(window, tree, b, d, f, s, nume_companie_entry, contact_nume_entry, contact_prenume_entry,
                            numar_telefon_entry, email_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    nume_companie_entry.delete(0, END)
    contact_nume_entry.delete(0, END)
    contact_prenume_entry.delete(0, END)
    numar_telefon_entry.delete(0, END)
    email_entry.delete(0, END)

    furnizori_info()


def select_record_furnizori(event, parent, adrese, ta):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume_companie").insert(0, record[1])
    parent.children.get("contact_nume").insert(0, record[2])
    parent.children.get("contact_prenume").insert(0, record[3])
    parent.children.get("numar_telefon").insert(0, record[4])
    parent.children.get("email").insert(0, record[5])
    adrese.set(ta[record[6] - 19])


def update_record_furnizori(my_tree, nume_companie, contact_nume, contact_prenume, numar_telefon, email, clicked_adrese,
                            id):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get(),
                                            nume_companie.get(), contact_nume.get(), contact_prenume.get(),
                                            numar_telefon.get(), email.get()))

    try:
        backend.conn.cursor().execute("""UPDATE Furnizori SET
            NUMECOMPANIE = :nume_companie,
            CONTACTNUME = :contact_nume,
            CONTACTPRENUME = :contact_prenume,
            CONTACTTELEFON = :numar_telefon,
            CONTACTEMAIL = :email,
            ADRESAID = :adrc
            
            WHERE FURNIZORID = :id""",
                                      {
                                          'nume_companie': nume_companie.get(),
                                          'contact_nume': contact_nume.get(),
                                          'contact_prenume': contact_prenume.get(),
                                          'numar_telefon': numar_telefon.get(),
                                          'email': email.get(),
                                          'adrc': int(clicked_adrese.get().replace(',', '     ')[1:4]),
                                          'id': id.get()
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_comanda(window, tree, b, d, f, s, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    backend.insert_into_table(table, list)
    comenzi_info()


def update_comanda(my_tree, data_cumpararii_entry, status_entry, clicked_clienti, clicked_angajati,
                   id_entry, window, b, d, f, s):
    update_record_comenzi(my_tree, data_cumpararii_entry, status_entry, clicked_clienti, clicked_angajati,
                          id_entry)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    comenzi_info()


def comenzi_info():
    global my_tree

    all_tabels.forget()
    Comenzi.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Comenzi)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[3])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("COMANDAID", anchor=W, width=105, stretch=NO)
    my_tree.column("DATACOMANDA", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("STATUS", anchor=CENTER, width=145, stretch=NO)
    my_tree.column("CLIENTID", anchor=CENTER, width=145, stretch=NO)
    my_tree.column("ANGAJATID", anchor=CENTER, width=145, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("COMANDAID", text="COMANDAID", anchor=W)
    my_tree.heading("DATACOMANDA", text="DATACOMANDA", anchor=CENTER)
    my_tree.heading("STATUS", text="STATUS", anchor=CENTER)
    my_tree.heading("CLIENTID", text="CLIENTID", anchor=CENTER)
    my_tree.heading("ANGAJATID", text="ANGAJATID", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[3])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1].date(), record[2], record[3], record[4]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1].date(), record[2], record[3], record[4]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Comenzi, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    data_cumpararii = Label(data_frame, text="Data_cumpararii", background="#829079", foreground="#E4D4C8")
    data_cumpararii.grid(row=0, column=0, padx=10, pady=10)
    data_cumpararii_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8",
                                  textvariable=StringVar(Comenzi, value=str(date.today())), name="data_cumpararii")
    data_cumpararii_entry.grid(row=0, column=1, padx=40, pady=10)

    status = Label(data_frame, text="Status", background="#829079", foreground="#E4D4C8")
    status.grid(row=0, column=2, padx=10, pady=10)
    optiuni_status = ["In procesare", "In asteptare", "Finalizata", "In livrare", "Preluata"]
    selected_status = StringVar()
    status_entry = Combobox(data_frame, values=optiuni_status, textvariable=selected_status, background="#829079",
                            foreground="#E4D4C8")
    status_entry.grid(row=0, column=3, padx=65, pady=10)
    status_entry.current(0)

    select_frame = LabelFrame(Comenzi, text="Alegeti datele:", background="#829079", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_clienti = backend.select_from_table(backend.Table_names[2])
    tabela_angajati = backend.select_from_table(backend.Table_names[1])

    clicked_clienti = StringVar(Comenzi)
    clicked_clienti.set(tabela_clienti[0])
    alege_client = Label(select_frame, text="Alegeti clientul", background="#829079", foreground="#E4D4C8")
    alege_client.grid(row=0, column=0)
    drop_clienti = OptionMenu(select_frame, clicked_clienti, *tabela_clienti)
    drop_clienti.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_clienti.grid(row=0, column=1, padx=0, pady=1)

    clicked_angajati = StringVar(Comenzi)
    clicked_angajati.set(tabela_angajati[0])
    alege_angajat = Label(select_frame, text="Alegeti angajatul", background="#829079", foreground="#E4D4C8")
    alege_angajat.grid(row=1, column=0)
    drop_angajati = OptionMenu(select_frame, clicked_angajati, *tabela_angajati)
    drop_angajati.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                            activeforeground="#E4D4C8", highlightthickness=0)
    drop_angajati.grid(row=1, column=1, padx=50, pady=0)

    button_frame = LabelFrame(Comenzi, text="Comenzi", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_comanda(Comenzi, my_tree, data_frame, button_frame, tree_frame,
                                                            select_frame,
                                                            backend.Table_names[3],
                                                            [None,
                                                             datetime.strptime(data_cumpararii_entry.get(), '%Y-%m-%d'),
                                                             status_entry.get(),
                                                             int(clicked_clienti.get().replace(',', '     ')[1:4]),
                                                             int(clicked_angajati.get().replace(',', '     ')[1:4])])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    back = Button(Comenzi, text="Inapoi", font=("Arial", 13), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(Comenzi))
    back.place(x=825, y=520)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_comanda(my_tree, data_cumpararii_entry, status_entry,
                                                          clicked_clienti, clicked_angajati, id_entry,
                                                          Comenzi, data_frame, button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_comenzi(my_tree, id_entry, Comenzi, data_frame,
                                                                 button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_comenzi(Comenzi, my_tree, data_frame, button_frame, tree_frame,
                                                                 select_frame,
                                                                 data_cumpararii_entry, status_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>',
                 lambda e: select_record_comenzi(e, data_frame, clicked_clienti, clicked_angajati,
                                                 tabela_clienti, tabela_angajati, selected_status))


def remove_record_comenzi(my_tree, id, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM Comenzi
                WHERE COMANDAID = :id""",
                                      {
                                          'id': id.get(),
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    comenzi_info()


def cancel_update_comenzi(window, tree, b, d, f, s, data_cumpararii_entry, status_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    data_cumpararii_entry.delete(0, END)
    status_entry.delete(0, END)

    comenzi_info()


def select_record_comenzi(event, parent, clienti, angajati, tc, ta, selected_status):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("data_cumpararii").insert(0, record[1])
    selected_status.set(record[2])
    clienti.set(tc[record[3] - 6])
    angajati.set(ta[record[4] - 25])


def update_record_comenzi(my_tree, data_cumpararii_entry, status_entry, clicked_clienti, clicked_angajati,
                          id_entry):
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    try:
        backend.conn.cursor().execute("""UPDATE COMENZI SET
            DATACOMANDA = :data_cumpararii,
            STATUS = :status,
            CLIENTID = :ccc,
            ANGAJATID = :aca

            WHERE COMANDAID = :id""",
                                      {
                                          'data_cumpararii': datetime.strptime(data_cumpararii_entry.get(),
                                                                               '%Y-%m-%d').date(),
                                          'status': status_entry.get(),
                                          'ccc': int(clicked_clienti.get().replace(',', '     ')[1:4]),
                                          'aca': int(clicked_angajati.get().replace(',', '     ')[1:4]),
                                          'id': id_entry.get()
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_produse(window, tree, b, d, f, s, table, list):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    backend.insert_into_table(table, list)
    produse_info()


def update_produse(my_tree, nume_entry, pret_entry, stoc_entry, clicked_furnizor, id_entry, window, b, d, f, s):
    update_record_produse(my_tree, nume_entry, pret_entry, stoc_entry, clicked_furnizor, id_entry)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    produse_info()


def produse_info():
    global my_tree
    all_tabels.forget()
    Produse.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(Produse)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)
    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_down,
                           selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[6])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0], columns[3][0], columns[4][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("PRODUSID", anchor=W, width=100, stretch=NO)
    my_tree.column("NUME", anchor=CENTER, width=150, stretch=NO)
    my_tree.column("PRET", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("STOC", anchor=CENTER, width=175, stretch=NO)
    my_tree.column("FURNIZORID", anchor=CENTER, width=225, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("PRODUSID", text="PRODUSID", anchor=W)
    my_tree.heading("NUME", text="NUME", anchor=CENTER)
    my_tree.heading("PRET", text="PRET", anchor=CENTER)
    my_tree.heading("STOC", text="STOC", anchor=CENTER)
    my_tree.heading("FURNIZORID", text="FURNIZORID", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[6])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(
                               record[0], record[1], record[2], record[3], record[4]),
                           tags=('oddrow',))
        # increment counter
        count += 1

    data_frame = LabelFrame(Produse, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    id_entry = Entry(name="id_entry", master=data_frame)

    nume = Label(data_frame, text="Nume", background="#829079", foreground="#E4D4C8")
    nume.grid(row=0, column=0, padx=10, pady=10)
    nume_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="nume")
    nume_entry.grid(row=0, column=1, padx=65, pady=10)

    pret = Label(data_frame, text="Pret", background="#829079", foreground="#E4D4C8")
    pret.grid(row=0, column=2, padx=10, pady=10)
    pret_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="pret")
    pret_entry.grid(row=0, column=3, padx=65, pady=10)

    stoc = Label(data_frame, text="Stoc", background="#829079", foreground="#E4D4C8")
    stoc.grid(row=1, column=0, padx=10, pady=10)
    stoc_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="stoc")
    stoc_entry.grid(row=1, column=1, padx=65, pady=10)

    select_frame = LabelFrame(Produse, text="Alegeti datele:", background="#829079", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_furnizori = backend.select_from_table(backend.Table_names[5])

    clicked_furnizori = StringVar(Produse)
    clicked_furnizori.set(tabela_furnizori[0])
    alege_furnizor = Label(select_frame, text="Alegeti furnizor", background="#829079", foreground="#E4D4C8")
    alege_furnizor.grid(row=0, column=0)
    drop_furnizori = OptionMenu(select_frame, clicked_furnizori, *tabela_furnizori)
    drop_furnizori.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                             activeforeground="#E4D4C8", highlightthickness=0)
    drop_furnizori.grid(row=0, column=1, padx=0, pady=1)

    button_frame = LabelFrame(Produse, text="Comenzi", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=1)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_produse(Produse, my_tree, data_frame, button_frame, tree_frame,
                                                            select_frame,
                                                            backend.Table_names[6],
                                                            [None,
                                                             nume_entry.get(),
                                                             pret_entry.get(),
                                                             stoc_entry.get(),
                                                             int(clicked_furnizori.get().replace(',', '     ')[1:4])]
                                                            )
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    back = Button(Produse, text="Inapoi", font=("Arial", 12), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(Produse))
    back.place(x=840, y=515)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_produse(my_tree, nume_entry, pret_entry, stoc_entry,
                                                          clicked_furnizori, id_entry,
                                                          Produse, data_frame, button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    my_tree.bind('<<TreeviewSelect>>',
                 lambda e: select_record_produse(e, data_frame, clicked_furnizori,
                                                 tabela_furnizori))

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_produse(Produse, my_tree, data_frame, button_frame, tree_frame,
                                                                 select_frame,
                                                                 nume_entry, pret_entry, stoc_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_produse(my_tree, id_entry, Produse, data_frame,
                                                                 button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)


def remove_record_produse(my_tree, id, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(id.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM Produse
                WHERE PRODUSID = :id""",
                                      {
                                          'id': id.get(),
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    produse_info()


def cancel_update_produse(window, tree, b, d, f, s, nume_entry, pret_entry, stoc_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    nume_entry.delete(0, END)
    pret_entry.delete(0, END)
    stoc_entry.delete(0, END)

    produse_info()


def select_record_produse(event, parent, furnizor, tf):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("id_entry").insert(0, record[0])
    parent.children.get("nume").insert(0, record[1])
    parent.children.get("pret").insert(0, record[2])
    parent.children.get("stoc").insert(0, record[3])
    furnizor.set(tf[record[4] - 6])


def update_record_produse(my_tree, nume_entry, pret_entry, stoc_entry,
                          clicked_furnizori, id_entry):
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    try:
        backend.conn.cursor().execute("""UPDATE Produse SET
            NUME = :nume,
            PRET = :pret,
            STOC = :stoc,
            FURNIZORID = :fc

            WHERE PRODUSID = :id""",
                                      {
                                          'nume': nume_entry.get(),
                                          'pret': pret_entry.get(),
                                          'stoc': stoc_entry.get(),
                                          'fc': int(clicked_furnizori.get().replace(',', '     ')[1:4]),
                                          'id': id_entry.get()
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def insert_into_detalii_comenzi(window, tree, b, d, f, s, table, list):
    global DetealiiComenzi
    error = ''
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    error = backend.insert_into_table(table, list)
    if error == 'WRONG':
        back_selection(DetealiiComenzi)
    elif error is None:
        detalii_comenzi_info()


def update_detalii_comenzi(my_tree, cantitate_entry, clicked_comanda, clicked_produs, window, b, d, f, s):
    update_record_detalii_comenzi(my_tree, cantitate_entry, clicked_comanda, clicked_produs)
    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    detalii_comenzi_info()


def detalii_comenzi_info():
    global my_tree, DetaliiComenzi
    all_tabels.forget()
    DetaliiComenzi.pack(fill="both", expand=True)

    style = ttk.Style()
    style.theme_use('clam')

    style.configure("Treeview",
                    background="gray",
                    foreground="black",
                    rowheight=30,
                    fieldbackground="#829079",
                    font=("Arial", 10))

    style.map('Treeview',
              background=[('selected', '#523A28')])

    tree_frame = Frame(DetaliiComenzi)
    tree_frame.pack(pady=5)

    tree_scroll = Scrollbar(tree_frame)
    tree_scroll_down = Scrollbar(tree_frame, orient=HORIZONTAL)

    tree_scroll.pack(side=RIGHT, fill=Y)
    tree_scroll_down.pack(side=BOTTOM, fill=X)

    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse")
    my_tree.pack(fill="both", expand=True)

    tree_scroll.config(command=my_tree.yview)
    tree_scroll_down.config(command=my_tree.xview)

    columns = backend.get_Column_names(backend.Table_names[4])
    my_tree['columns'] = (columns[0][0], columns[1][0], columns[2][0])

    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("CANTITATE", anchor=CENTER, width=100, stretch=NO)
    my_tree.column("COMANDAID", anchor=CENTER, width=250, stretch=NO)
    my_tree.column("PRODUSID", anchor=CENTER, width=250, stretch=NO)

    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("CANTITATE", text="CANTITATE", anchor=W)
    my_tree.heading("COMANDAID", text="COMANDAID", anchor=CENTER)
    my_tree.heading("PRODUSID", text="PRODUSID", anchor=CENTER)

    data = backend.select_from_table(backend.Table_names[4])

    my_tree.tag_configure('oddrow', background="#B9925E")
    my_tree.tag_configure('evenrow', background="#EDE6B9")

    global count
    count = 0

    for record in data:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2]),
                           tags=('evenrow',))
        else:
            my_tree.insert(parent='', index='end', iid=count, text='',
                           values=(record[0], record[1], record[2]),
                           tags=('oddrow',))
        count += 1

    data_frame = LabelFrame(DetaliiComenzi, text="Introduceti datele:", background="#829079", foreground="#E4D4C8")
    data_frame.pack(pady=0, padx=0, fill='x')

    cantiate = Label(data_frame, text="Cantitate", background="#829079", foreground="#E4D4C8")
    cantiate.grid(row=0, column=0, padx=10, pady=10)
    cantitate_entry = Entry(data_frame, background="#829079", foreground="#E4D4C8", name="cantitate")
    cantitate_entry.grid(row=0, column=1, padx=40, pady=10)

    select_frame = LabelFrame(DetaliiComenzi, text="Alegeti datele:", background="#829079", foreground="#E4D4C8")
    select_frame.pack(pady=0, padx=0, fill='x')

    tabela_comenzi = backend.select_from_table(backend.Table_names[3])
    tabela_produse = backend.select_from_table(backend.Table_names[6])

    clicked_comenzi = StringVar(DetaliiComenzi)
    clicked_comenzi.set(tabela_comenzi[0])
    alege_comanda = Label(select_frame, text="Alegeti comanda", background="#829079", foreground="#E4D4C8")
    alege_comanda.grid(row=0, column=0)
    drop_comanda = OptionMenu(select_frame, clicked_comenzi, *tabela_comenzi)
    drop_comanda.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                           activeforeground="#E4D4C8", highlightthickness=0)
    drop_comanda.grid(row=0, column=1, padx=0, pady=1)

    clicked_produse = StringVar(DetaliiComenzi)
    clicked_produse.set(tabela_produse[0])
    alege_produs = Label(select_frame, text="Alegeti produs", background="#829079", foreground="#E4D4C8")
    alege_produs.grid(row=1, column=0)
    drop_produs = OptionMenu(select_frame, clicked_produse, *tabela_produse)
    drop_produs.configure(background="#829079", foreground="#E4D4C8", activebackground="#829079",
                          activeforeground="#E4D4C8", highlightthickness=0)
    drop_produs.grid(row=1, column=1, padx=0, pady=1)

    button_frame = LabelFrame(DetaliiComenzi, text="Comenzi", background="#829079", foreground="#E4D4C8")
    button_frame.pack(fill="x", padx=0, pady=0)

    add_button = Button(button_frame, text="Adaugare inregistrare",
                        font=("Arial", 10), bg="#829079", fg="#EDE6B9",
                        command=lambda: insert_into_detalii_comenzi(DetaliiComenzi, my_tree, data_frame, button_frame,
                                                                    tree_frame, select_frame, backend.Table_names[4],
                                                                    [cantitate_entry.get(),
                                                                     int(clicked_comenzi.get().replace(',', '     ')[
                                                                         1:4]),
                                                                     int(clicked_produse.get().replace(',', '     ')[
                                                                         1:4])])
                        )

    add_button.grid(row=0, column=1, padx=10, pady=10)

    update_button = Button(button_frame, text="Update inregistrare",
                           command=lambda: update_detalii_comenzi(my_tree, cantitate_entry, clicked_comenzi,
                                                                  clicked_produse, DetaliiComenzi, data_frame,
                                                                  button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    update_button.grid(row=0, column=2, padx=10, pady=10)

    remove_button = Button(button_frame, text="Stergere inregistrare",
                           command=lambda: remove_record_detalii_comenzi(my_tree, cantitate_entry, DetaliiComenzi,
                                                                         data_frame,
                                                                         button_frame, tree_frame, select_frame)
                           , bg="#829079", fg="#EDE6B9")
    remove_button.grid(row=0, column=4, padx=10, pady=10)

    cancel_button = Button(button_frame, text="Anuleaza",
                           command=lambda: cancel_update_detalii_comenzi(DetaliiComenzi, my_tree, data_frame,
                                                                         button_frame, tree_frame, select_frame,
                                                                         cantitate_entry),
                           background="#829079", foreground="#EDE6B9")
    cancel_button.grid(row=0, column=3, padx=10, pady=10)

    back = Button(DetaliiComenzi, text="Inapoi", font=("Arial", 13), bg="#829079", fg="#EDE6B9",
                  command=lambda: back_selection(DetaliiComenzi))
    back.place(x=825, y=520)

    my_tree.bind('<<TreeviewSelect>>',
                 lambda e: select_record_detalii_comenzi(e, data_frame, clicked_comenzi, tabela_comenzi,
                                                         clicked_produse, tabela_produse))


def remove_record_detalii_comenzi(my_tree, cantitate, window, b, d, f, s):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(cantitate.get()))

    try:
        backend.conn.cursor().execute("""DELETE FROM DetaliiComenzi
                WHERE CANTITATE = :cantitate""",
                                      {
                                          'cantitate': cantitate.get()
                                      })
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    window.pack_forget()
    my_tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()

    detalii_comenzi_info()


def cancel_update_detalii_comenzi(window, tree, b, d, f, s, cantitate_entry):
    window.pack_forget()
    tree.forget()
    b.forget()
    d.forget()
    f.forget()
    s.forget()
    cantitate_entry.delete(0, END)

    detalii_comenzi_info()


def select_record_detalii_comenzi(event, parent, comenzi, tc, produse, tp):
    global my_tree
    for selected_item in my_tree.selection():
        item = my_tree.item(selected_item)
        record = item['values']

    for child in parent.winfo_children():
        if child.winfo_class() == "Entry":
            child.delete(0, END)

    parent.children.get("cantitate").insert(0, record[0])
    comenzi.set(tc[record[1] - 6])
    produse.set(tp[record[2] - 11])


def update_record_detalii_comenzi(my_tree, cantitate, clicked_comenzi, clicked_produse):
    selected = my_tree.focus()

    my_tree.item(selected, text="", values=(cantitate.get()))

    try:
        backend.conn.cursor().execute("""UPDATE DetaliiComenzi SET
            CANTITATE = :cantitate
            WHERE COMANDAID = :adrc AND PRODUSID = :adrp """,

                                      {
                                          'cantitate': cantitate.get(),
                                          'adrc': int(clicked_comenzi.get().replace(',', '     ')[1:4]),
                                          'adrp': int(clicked_produse.get().replace(',', '     ')[1:4]),
                                      })
    except oracledb.DatabaseError as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def add_savepoint(savePointName, popup):
    global savepoints
    # print("SAVEPOINT " + str(savePointName))
    try:
        backend.conn.cursor().execute("SAVEPOINT " + str(savePointName))
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)

    if savepoints.qsize() == 5:
        savepoints.get()
        savepoints.put(savePointName)
    else:
        savepoints.put(savePointName)

    popup.destroy()


def savepoint():
    savePoint_name = StringVar()
    popup = tkinter.Toplevel()
    popup.title('Savepoints')
    # popup.geometry('100x100')
    popup.configure(background="#829079")
    label = tkinter.Label(popup, text="Savepoint", font=("Arial", 10), background="#829079",
                          foreground="#EDE6B9")
    label.pack()
    Entry(popup, textvariable=savePoint_name, width=30).pack()

    ok_button = Button(popup, text="OK", command=lambda: add_savepoint(savePoint_name.get(), popup),
                       background="#829079", foreground="#EDE6B9")
    ok_button.pack()


def rollback_to_savepoint(name, popup):
    global savepoints

    try:
        backend.conn.cursor().execute("ROLLBACK TO " + str(name))
        savepoints.queue.remove(name)
    except Exception as err:
        message = "Error while using rollback: " + str(err)
        messagebox.showerror(title='Error', message=message)

    popup.destroy()
    rollback()


def commit():
    try:
        backend.conn.cursor().execute("COMMIT")
    except Exception as err:
        message = "Error while creating the connection: " + str(err)
        messagebox.showerror(title='Error', message=message)


def rollback():
    global savepoints
    popup = tkinter.Toplevel()
    popup.title('Rollbacks')
    # popup.geometry('400x200')
    popup.configure(background="#829079")
    label = tkinter.Label(popup, text="Rollback la savepoint", font=("Arial", 10), background="#829079",
                          foreground="#EDE6B9")
    label.pack()
    # for element in savepoints.queue:
    #    print(element)
    # facem un suster
    # butonul asta inapoi, unde e functia lui?
    # putem sa apelam de aici comanda butonului back? Nu sunt sigur, adica daca il apelam cu global la inceput nu ar merge?
    for i in range(savepoints.qsize()):
        button = tkinter.Button(popup, text=savepoints.queue[i],
                                command=lambda: rollback_to_savepoint(savepoints.queue[i], popup), background="#829079",
                                foreground="#EDE6B9")
        button.pack()


if __name__ == "__main__":
    backend.Table_names = backend.connection('bd005', 'aaa', '81.180.214.85', 1539,
                                             'orcl')
    root = Tk()
    root.title("DB Manager")
    root.geometry("900x600")
    root.resizable(False, False)
    root.configure(background="#14110F")
    root.iconbitmap("Airport-icon_30354.ico")
    my_menu = Menu(root)
    root.config(menu=my_menu)

    my_menu.add_command(label="Commit", command=commit)
    my_menu.add_command(label="Rollback", command=rollback)
    my_menu.add_command(label="Savepoint", command=savepoint)

    menuinfo()

    root.mainloop()
    backend.close_connection()
