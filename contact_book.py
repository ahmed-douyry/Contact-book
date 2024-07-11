from tkinter import *
from tkinter import ttk  # Importation de ttk pour pines widgets améliorés
from sqlite3 import *  # Importation de SQLite pour la gestion de la base de données
from tkinter import messagebox  # Importation de messagebox pour afficher des messages à l'utilisateur
import re

class Contact:
    def __init__(self, root):
        # Initialisation de la fenêtre principale
        self.root = root

        # Variables pour la recherche
        self.search_by = StringVar()
        self.search_txt = StringVar()
        self.Email = StringVar()
        self.City = StringVar()
        self.job = StringVar()
        self.gender = StringVar()

        # Dimension de la fenêtre
        root.geometry("1400x750+10+10")

        # Titre de l'application
        root.title('Contact_Book')
        title = Label(root, text="The Contacts Book", bd=6, font=("arial", 30, "bold"), bg='#063241', fg="white")
        title.place(x=500 , y=20)

        # Initialisation des variables pour les entrées de texte
        self.name_var = StringVar()
        self.Number = StringVar()
        self.ID = StringVar()
        self.Email = StringVar()
        self.City = StringVar()
        self.job = StringVar()
        self.gender = StringVar()

        # Cadre de gestion pour les boutons d'ajout, mise à jour, suppression et effacement
        Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="#063241")
        Manage_Frame.place(x=5, y=100, width=500, height=560)
        m_title = Label(Manage_Frame, text="Welcome to our Contact Book", fg="white", bg="#063241", font=("arial", 22, "bold"))
        m_title.place(x=35,y=30)
        
        # Labels et champs de saisie pour le nom et le numéro ,email ,ville ,job ,gender
        lbl_name = Label(Manage_Frame, text="Name    ", fg="white", bg="#063241", font=("arial", 15, "bold"))
        lbl_name.place(x=100,y=90)
        txt_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=3, relief=GROOVE)
        txt_name.place(x=180,y=90)
        
        lbl_Number = Label(Manage_Frame, text="Number  ", fg="white", bg="#063241", font=("times new roman", 15, "bold"))
        lbl_Number.place(x=100,y=150)
        txt_Number = Entry(Manage_Frame, textvariable=self.Number,width=22,font=("times new roman", 14, "bold"), bd=3, relief=GROOVE)
        txt_Number.place(x=180,y=150)

        lbl_Email = Label(Manage_Frame, text="Email", fg="white", bg="#063241", font=("times new roman", 15, "bold"))
        lbl_Email.place(x=100,y=210)
        txt_Email = Entry(Manage_Frame, textvariable=self.Email,width=22, font=("times new roman", 14, "bold"), bd=3, relief=GROOVE)
        txt_Email.place(x=180,y=210)
        
        lbl_Ville = Label(Manage_Frame, text="City", fg="white", bg="#063241", font=("times new roman", 15, "bold"))
        lbl_Ville.place(x=100,y=270)
        txt_Ville = Entry(Manage_Frame, textvariable=self.City,width=22, font=("times new roman", 14, "bold"), bd=3, relief=GROOVE)
        txt_Ville.place(x=180,y=270)

        lbl_job = Label(Manage_Frame, text="Job", fg="white", bg="#063241", font=("times new roman", 15, "bold"))
        lbl_job.place(x=100,y=330)
        txt_job = Entry(Manage_Frame, textvariable=self.job,width=22, font=("times new roman", 14, "bold"), bd=3, relief=GROOVE)
        txt_job.place(x=180,y=330)

        lbl_gender = Label(Manage_Frame, text="Gender", fg="white", bg="#063241", font=("times new roman", 15, "bold"))
        lbl_gender.place(x=100, y=390)
        male_radio = ttk.Radiobutton(Manage_Frame, text="Male", value='Male', variable=self.gender, style='TButton')
        male_radio.place(x=180, y=390)
        female_radio = ttk.Radiobutton(Manage_Frame, text="Female", value='Female', variable=self.gender, style='TButton')
        female_radio.place(x=290, y=390)
        ttk.Style().configure('TButton', font=("times new roman", 14, "bold"),bg="#063241")

        # Cadre pour les boutons d'action
        Btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="mint cream")
        Btn_Frame.place(x=5, y=450, width=480)
        addbtn = Button(Btn_Frame, text="Add", font=("times new roman", 12, "bold"), width=10, bg="#063241", fg="white", command=self.add_contacts)
        addbtn.grid(row=0, column=0, padx=5, pady=5)
        updatebtn = Button(Btn_Frame, text="Update", font=("times new roman", 12, "bold"), bg="#063241", fg="white", width=10,command=self.update_data)
        updatebtn.grid(row=0, column=1, padx=5, pady=5)
        deletebtn = Button(Btn_Frame, text="Delete", font=("times new roman", 12, "bold"), bg="#063241", fg="white", width=10,command=self.delete_data)
        deletebtn.grid(row=0, column=2, padx=5, pady=5)
        clearbtn = Button(Btn_Frame, text="Clear", font=("times new roman", 12, "bold"), bg="#063241", fg="white", width=10, command=self.clear)
        clearbtn.grid(row=0, column=3, padx=5, pady=5)
        lbl_msg = Label(Manage_Frame, text="Means Required fields", bg="#063241" , fg="black", font=("times new roman", 15, "bold"))
        lbl_msg.place(x=140,y=520)

        # Cadre de détails
        Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#063241")
        Details_Frame.place(x=510, y=100, width=850, height=560)
        # Cadre pour les boutons d'action
        rec_Details_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="mint cream")
        rec_Details_Frame.place(x=533, y=108, width=800, height=60)
        lbl_search = Label(rec_Details_Frame, text="Search", fg="#063241",bg="White", font=("times new roman", 20, "bold")).place(x=25,y=12)
        combo_search = ttk.Combobox(rec_Details_Frame, width=13,textvariable=self.search_by, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Name", "Number", "Email", "City", "Job", "Gender")
        combo_search.place(x=190,y=20)
        combo_search.bind("<<ComboboxSelected>>", self.update_search_field)  # Bind event to combobox selection
        self.search_field = Entry(rec_Details_Frame, textvariable=self.search_txt, width=20, font=("times new roman", 10, "bold"), bd=5, relief=GROOVE)
        self.search_field.place(x=350,y=18)
        self.gender_search_combo = ttk.Combobox(rec_Details_Frame, width=16, font=("times new roman", 12, "bold"), state="readonly")
        self.gender_search_combo['values'] = ("Male", "Female")
        searchbtn = Button(rec_Details_Frame, text="Search", bg="#063241", fg="white", font=("times new roman", 12, "bold"), command=self.search_data,width=10, pady=2).place(x=530,y=18)
        showallbtn = Button(rec_Details_Frame, text="Show_all", bg="#063241", fg="white", font=("times new roman", 12, "bold"), command=self.fetch_data,width=10, pady=2).place(x=660,y=18)
        
        # Cadre de affichage
        Table_Frame = Frame(Details_Frame, bd=4, relief=RIDGE, bg="mint cream")
        Table_Frame.place(x=20, y=70, width=800, height=460)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.contacts_table = ttk.Treeview(Table_Frame, columns=("ID", "Name", "Number", "Email", "City", "Job", "Gender"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.contacts_table.xview)
        scroll_y.config(command=self.contacts_table.yview)
        self.contacts_table.heading("ID", text="ID")
        self.contacts_table.heading("Name", text="Name")
        self.contacts_table.heading("Number", text="Number")
        self.contacts_table.heading("Email", text="Email")
        self.contacts_table.heading("City", text="City")
        self.contacts_table.heading("Job", text="Job")
        self.contacts_table.heading("Gender", text="Gender")
        self.contacts_table['show'] = "headings"
        self.contacts_table.column("ID", width=50)
        self.contacts_table.column("Name", width=100)
        self.contacts_table.column("Number", width=100)
        self.contacts_table.column("Email", width=150)
        self.contacts_table.column("City", width=150)
        self.contacts_table.column("Job", width=70)
        self.contacts_table.column("Gender", width=50)
        self.contacts_table.pack(fill=BOTH, expand=1)
        self.contacts_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # Fonction pour ajouter un contact
    def add_contacts(self):
        numbre = self.checkvalidNumber(self.Number.get())
        email = self.check_valid_email(self.Email.get())
        if not numbre:
            messagebox.showerror("Error", "Invalid phone number")
        elif not email:
            messagebox.showerror("Error", "Invalid Email")
        elif self.name_var.get() == "" or self.Number.get() == "" or self.Email.get() == "" or self.City.get() == "" or self.job.get() == "" or self.gender.get() == "":
            messagebox.showerror("Error", "Required fields are not filled")
        else:
            conn = connect("contacts.db")
            cur = conn.cursor()
            cur.execute("insert into contacts values(Null,?,?,?,?,?,?)", (self.name_var.get(), self.Number.get(), self.Email.get(), self.City.get(), self.job.get(), self.gender.get()))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success", "Successfully added")
            
    # Fonction pour mettre à jour les données du contact
    def update_data(self):
        if self.name_var.get() == "" or self.Number.get() == "" or self.Email.get() == "" or self.City.get() == "" or self.job.get() == "" or self.gender.get() == "":
                messagebox.showerror("Error", "Required fields are not filled")
        else:
            if not self.checkvalidNumber(self.Number.get()):
                return  # Stop execution if the number is invalid
            if not self.check_valid_email(self.Email.get()):
                messagebox.showerror("Error", "Invalid Email")
                return  # Stop execution if the email is invalid
            conn = connect("contacts.db")
            cur = conn.cursor()
            cur.execute("UPDATE contacts SET Name=?, Number=?, Email=?, City=?, Job=?, Gender=? WHERE ID=?", (self.name_var.get(), self.Number.get(), self.Email.get(), self.City.get(), self.job.get(), self.gender.get(), self.ID.get()))
            conn.commit()
            conn.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Successfully updated")

    # Fonction pour vérifier la validité du numéro de téléphone
    def checkvalidNumber(self, phone_number):
        if len(phone_number) < 10 or len(phone_number) > 13:
                messagebox.showerror("Error", "Phone number Invalid")
                return False
        if phone_number[0] != '+' and not phone_number[1:].isdigit():
                messagebox.showerror("Error", "Phone number must start with '+' or there's Character ")
                return False
        return True

    # Function to check the validity of the email address
    def check_valid_email(self, email):
        pattern = r'^[\w\.-]+@[a-z]+\.[a-z]+$'
        return re.match(pattern, email) is not None

    # Fonction pour effacer les champs de saisie
    def clear(self):
        self.name_var.set("")
        self.Number.set("")
        self.Email.set("")
        self.City.set("")
        self.job.set("")
        self.gender.set("")

    # Fonction pour récupérer le curseur
    def get_cursor(self, ev):
        cursor_row = self.contacts_table.focus()
        content = self.contacts_table.item(cursor_row)
        row = content['values']
        self.ID.set(row[0])
        self.name_var.set(row[1])
        self.Number.set('0'+str(row[2]))
        self.Email.set(row[3])
        self.City.set(row[4])
        self.job.set(row[5])
        self.gender.set(row[6])


    # Fonction pour supprimer les données du contact
    def delete_data(self):
        if self.ID.get() == "":
                messagebox.showerror("Error", "No contact selected")
        else:
            conn = connect("contacts.db")
            cur = conn.cursor()
            sql_query = f"DELETE FROM contacts WHERE ID={self.ID.get()}"
            cur.execute(sql_query)
            conn.commit()
            conn.close()
            self.clear()
            self.fetch_data()  # Refresh the display after deletion
            messagebox.showinfo("Success", "Successfully Deleted")

    # Fonction pour récupérer les données depuis la base de données
    def fetch_data(self):
        conn = connect("contacts.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM contacts")
        rows = cur.fetchall()
        self.contacts_table.delete(*self.contacts_table.get_children())  # Clear the table
        if len(rows) != 0:
            for row in rows:
                self.contacts_table.insert('', END, values=row)  # Repopulate the table
            conn.commit()
        conn.close()

    # Function to update search field based on search criterion
    def update_search_field(self, event):
        if self.search_by.get() == "Gender":
            self.search_field.place_forget()
            self.gender_search_combo.place(x=350, y=18)
        else:
            self.gender_search_combo.place_forget()
            self.search_field.place(x=350, y=18)

    # Fonction pour rechercher des données dans la base de données
    def search_data(self):
        conn = connect("contacts.db")
        cur = conn.cursor()
        if self.search_by.get() == "Gender":
            sql_query = "SELECT * FROM contacts WHERE Gender = ?"
            cur.execute(sql_query, (self.gender_search_combo.get(),))
            self.fetch_data()
        else:
            sql_query = f"SELECT * FROM contacts WHERE {self.search_by.get()} LIKE ?"
            cur.execute(sql_query, (f'%{self.search_txt.get()}%',))
        rows = cur.fetchall()
        if len(rows) != 0:
                self.contacts_table.delete(*self.contacts_table.get_children())
                for row in rows:
                    self.contacts_table.insert('', END, values=row)
                conn.commit()
        else:
             messagebox.showerror("Error", "No Data available")
        conn.close()


root = Tk()                     
root.title("Contact Book")
root.config(background="#063241")
con = connect('contacts.db')   
cur = con.cursor()               
cur.execute("CREATE TABLE IF NOT EXISTS contacts( ID integer PRIMARY KEY AUTOINCREMENT, Name text NOT NULL, Number text NOT NULL UNIQUE,Email text NOT NULL UNIQUE,City TEXT NOT NULL ,Job TEXT ,Gender TEXT NOT NULL); ")   
con.commit()                    
con.close()                      
ob = Contact(root)              
root.mainloop()
