from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from hashlib import sha1
import DB_Log as db

conn = db.connect("db.sqlite")
cur = conn.cursor()


def init(root):
	root = root
	root.title(" TFE-2020 ~ Van den Eede Derya ")
	root.geometry("1700x750+0+0")
	root.configure()
	initTabs(root)

def initTabs(root):
	notebook = ttk.Notebook(root)
	Tab0 = ttk.Frame(notebook)
	Tab1 = ttk.Frame(notebook)
	Tab2 = ttk.Frame(notebook)
	Tab3 = ttk.Frame(notebook)
	notebook.add(Tab0, text="\t LOGIN")
	notebook.add(Tab1, text="\t CLIENTS",  state="hidden")
	notebook.add(Tab2, text="\t VENDEURS", state="hidden")
	notebook.add(Tab3, text="\t PRODUITS", state="hidden")
	notebook.grid()

	# ======================================= ~ LOGIN REG ~ FONCTIONS ~ =========================================#

	def Reg_System():
		MReg = Toplevel(Tab0)
		MReg.title("REGISTER USER")
		MReg.geometry("1500x750+0+0")
		MReg.configure()

		def Regadd():
			username = (Reg_Username.get())
			password = (Reg_Password.get())
			password2 = (Reg_Password2.get())
			mail = (Reg_Mail.get())
			txtRegUsername.focus()
			db_reglog = db.log_read(conn)
			if username == '' or password == '' or password == '' or mail == '':
				showinfo("INFORMATION", "Please include all fields")
				Reg_Username.set("")
				Reg_Password.set("")
				Reg_Password2.set("")
				Reg_Mail.set("")
				txtRegUsername.focus()
			else:
				if db_reglog[1] != username:
					if password != password2:
						messagebox.showinfo("Please try again !", "Your password is not matching... ")
						Reg_Password.set("")
						Reg_Password2.set("")
						txtRegUsername.focus()
						txtRegUsermail.focus()
					else:
						db.log_reg(conn, username, password, mail)
						messagebox.showinfo("INFORMATION ", "Your have been registred ! ")
				else:
						messagebox.showinfo("INFORMATION ", "Username is taken, please try again ! ")
						Reg_Username.set("")
						txtRegPassword.focus()
						txtRegPassword2.focus()
						txtRegUsermail.focus()

		def RegReset():
			Reg_Username.set("")
			Reg_Password.set("")
			Reg_Password2.set("")
			Reg_Mail.set("")
			txtRegUsername.focus()

		# ==================================================== ~ LOGIN REG ~ FRAME ~ ========================================================#
		MRegLoginFrame = Frame(MReg, relief=RIDGE)
		MRegLoginFrame.pack(fill=X, expand="yes")

		Reg_Username = StringVar()
		Reg_Password = StringVar()
		Reg_Password2 = StringVar()
		Reg_Mail = StringVar()

		lblRegTitle = Label(MRegLoginFrame, text='\t LOGIN REGISTRATION SYSTEM \t', font=('arial', 30, 'bold'),
		                    fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
		lblRegTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

		RegLoginFrame1 = LabelFrame(MRegLoginFrame, font=('arial', 20, 'bold'), relief='ridge', bd=10)
		RegLoginFrame1.pack(side=LEFT, fill=Y, expand="yes", padx=20, pady=40)

		RegLoginFrame2 = LabelFrame(MRegLoginFrame, font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
		RegLoginFrame2.pack(side=RIGHT, fill=Y, expand="yes", padx=20, pady=10)

		# ==================================================== ~ LOGIN REG ~ LABEL & ENTRY ~  ==================================================#

		lblRegUsername = Label(RegLoginFrame1, text=' USER NAME :', font=('arial', 20, 'bold'), bd=22)
		lblRegUsername.grid(row=0, column=0)
		txtRegUsername = Entry(RegLoginFrame1, font=('arial', 20, 'bold'), bd=10, textvariable=Reg_Username, width=33)
		txtRegUsername.grid(row=0, column=1, padx=120)

		lblRegPassword = Label(RegLoginFrame1, text=' PASSWORD :', font=('arial', 20, 'bold'), bd=22)
		lblRegPassword.grid(row=1, column=0)
		txtRegPassword = Entry(RegLoginFrame1, font=('arial', 20, 'bold'), bd=10, textvariable=Reg_Password, show='*', width=33)
		txtRegPassword.grid(row=1, column=1, columnspan=2, pady=30)

		lblRegPassword2 = Label(RegLoginFrame1, text=' PASSWORD :', font=('arial', 20, 'bold'), bd=22)
		lblRegPassword2.grid(row=2, column=0)
		txtRegPassword2 = Entry(RegLoginFrame1, font=('arial', 20, 'bold'), bd=10, textvariable=Reg_Password2, show='*', width=33)
		txtRegPassword2.grid(row=2, column=1, columnspan=2, pady=30)

		lblRegUsermail = Label(RegLoginFrame1, text=' USER E-MAIL :', font=('arial', 20, 'bold'), bd=22)
		lblRegUsermail.grid(row=3, column=0)
		txtRegUsermail = Entry(RegLoginFrame1, font=('arial', 20, 'bold'), bd=10, textvariable=Reg_Mail, width=33)
		txtRegUsermail.grid(row=3, column=1, padx=120)

		# ==================================================== ~ LOGIN REG ~ BUTTONS ~  ========================================================#

		BtAdd = Button(RegLoginFrame2, text="ADD", font=('arial', 20, 'bold'), width=15, fg='Cadet Blue', bd=20, command=Regadd)
		BtAdd.grid(row=0, column=0, pady=20, padx=10)
		BtReset = Button(RegLoginFrame2, text="RESET", font=('arial', 20, 'bold'), width=15,fg='Cadet Blue', bd=20, command=RegReset)
		BtReset.grid(row=1, column=0, pady=20, padx=10)
		BtExit = Button(RegLoginFrame2, text="EXIT", font=('arial', 20, 'bold'), width=15, fg='Cadet Blue', bd=20, command=MReg.destroy)
		BtExit.grid(row=2, column=0, pady=20, padx=10)

	# ==================================================== ~ LOGIN TAB ~ FONCTIONS ~ ========================================================#

	def Login_System():
		username = (Username.get())
		password = (Password.get())
		db_pwd = db.log_in(conn, username)
		encoded_pwd = sha1(password.encode()).hexdigest()

		if db_pwd is None:
			msg = tk.messagebox.askyesno("Login System", "Invalid username Please try again! ")
			if msg == 0:
				root.destroy()
			else:
				Username.set("")
				Password.set("")
				txtUsername.focus()

		else:
			if db_pwd[0] != encoded_pwd:
				msg = tk.messagebox.askyesno("Login System", "Invalid password Please try again! ")
				if msg == 0:
					root.destroy()
				else:
					txtUsername.focus()
					Password.set("")

			elif username == "admin":
				Username.set("")
				Password.set("")
				txtUsername.focus()
				notebook.tab(0, state="hidden")
				notebook.tab(1, state="normal")
				notebook.tab(2, state="normal")
				notebook.tab(3, state="normal")
				notebook.select(1)
				return True
			else:
				Username.set("")
				Password.set("")
				txtUsername.focus()
				notebook.tab(0, state="hidden")
				notebook.tab(1, state="normal")
				notebook.tab(2, state="hidden")
				notebook.tab(3, state="hidden")
				notebook.select(1)
				return True

	def Reset():
		Username.set("")
		Password.set("")
		txtUsername.focus()

	def iExit():
			iExit = tk.messagebox.askyesno("Login System", "Confirm if you want to Exit")
			if iExit > 0:
				root.destroy()
			else:
				command = root
				return

	# ==================================================== ~ LOGIN TAB ~ FRAME ~  ========================================================#

	TabConrolLoginFrame = Frame(Tab0, relief=RIDGE)
	TabConrolLoginFrame.pack(fill=X, expand="yes")

	Username = StringVar()
	Password = StringVar()

	lblTitle = Label(TabConrolLoginFrame, text='\t LOGIN SYSTEM \t', font=('arial', 30, 'bold'),
	                 fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	lblTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

	LoginFrame1 = LabelFrame(TabConrolLoginFrame, font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	LoginFrame1.pack(fill=X, expand="yes", padx=20, pady=20)

	LoginFrame2 = LabelFrame(TabConrolLoginFrame, font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	LoginFrame2.pack(fill=X, expand="yes", padx=20, pady=20)

	# ==================================================== ~ LOGIN TAB ~ LABEL & ENTRY ~  ==================================================#

	lblUsername = Label(LoginFrame1, text=' USER NAME :', font=('arial', 25, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=22)
	lblUsername.grid(row=0, column=0)
	txtUsername = Entry(LoginFrame1, font=('arial', 20, 'bold'), bd=12, textvariable=Username, width=30)
	txtUsername.grid(row=0, column=1, padx=50)

	lblPassword = Label(LoginFrame1, text=' PASSWORD :', font=('arial', 25, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=22)
	lblPassword.grid(row=1, column=0)
	txtPassword = Entry(LoginFrame1, font=('arial', 20, 'bold'), bd=12, textvariable=Password, show='*', width=30)
	txtPassword.grid(row=1, column=1,  columnspan=2, pady=30)

	# ==================================================== ~ LOGIN TAB ~ BUTTONS ~  ========================================================#

	btnReg = Button(LoginFrame2, text='REGISTER', width=15, font=('arial', 20, 'bold'), fg='Cadet Blue', bd=12, command=Reg_System)
	btnReg.grid(row=3, column=0, pady=20, padx=10)

	btnReset = Button(LoginFrame2, text='RESET', width=15, font=('arial', 20, 'bold'), fg='Cadet Blue', bd=12, command=Reset)
	btnReset.grid(row=3, column=1, pady=20, padx=10)

	btnLogin = Button(LoginFrame2, text='LOGIN', width=15, font=('arial', 20, 'bold'), fg='Cadet Blue', bd=12, command=Login_System)
	btnLogin.grid(row=3, column=2,  pady=20, padx=10)

	btnExit = Button(LoginFrame2, text='EXIT', width=15, font=('arial', 20, 'bold'), fg='Cadet Blue', bd=12, command=iExit)
	btnExit.grid(row=4, column=1, pady=20, padx=10)

	# ==================================================== ~ PRODUIT TAB ~ FONCTIONS ~ ========================================================#


	# ====================================== ~ CLIENT TAB ~ FRAME ~  ============================================#

	TabClientFrame = Frame(Tab1, relief=RIDGE)
	TabClientFrame.pack(fill=X, expand="yes")

	x = tk.StringVar()
	id = IntVar()
	ref = StringVar()
	nom = StringVar()
	prenom = StringVar()
	adresse = StringVar()
	ville = StringVar()
	tel = IntVar()
	email = StringVar()
	tva = StringVar()

	lblPTitle = Label(TabClientFrame, text='\t CLIENT \t',
	                  font=('arial', 30, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	lblPTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

	wrapper1 = LabelFrame(TabClientFrame, text=" CLIENT DATA : ",
	                      font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper1.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper2 = LabelFrame(TabClientFrame, text=" SEARCH : ",
	                      font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper2.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper3 = LabelFrame(TabClientFrame, text=" CLIENT LIST : ",
	                      font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper3.pack(fill=X, expand="yes", padx=20, pady=20)

	# ================================ ~ CLIENT TAB ~ TREEVIEW & SCROLLBAR ~ ====================================#

	mycanvas = Canvas(wrapper3)
	mycanvas.pack(fill="both", expand="yes", side=LEFT)

	trv = ttk.Treeview(mycanvas, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height=10)
	trv.pack(fill="both", expand="yes", side=LEFT)

	ascenseurY = ttk.Scrollbar(wrapper3, orient=VERTICAL, command=trv.yview)
	ascenseurY.pack(side=RIGHT, fill=Y)

	trv.column(1, width=10, anchor='c')
	trv.column(2, width=30, anchor='c')
	trv.column(3, width=40, anchor='c')
	trv.column(4, width=40, anchor='c')
	trv.column(5, width=40, anchor='c')
	trv.column(6, width=30, anchor='c')
	trv.column(7, width=40, anchor='c')
	trv.column(8, width=50, anchor='c')
	trv.column(9, width=45, anchor='c')
	trv.heading(1, text="ID :\t")
	trv.heading(2, text="REF :\t")
	trv.heading(3, text="NOM :\t")
	trv.heading(4, text="PRENOM :\t")
	trv.heading(5, text="ADDRESSE :\t")
	trv.heading(6, text="VILLE :\t")
	trv.heading(7, text="TELEPHONE :\t")
	trv.heading(8, text="E-MAIL :\t")
	trv.heading(9, text="TVA :\t")

	trv.bind('<Double 1>')

	# ==================================================== ~ PRODUIT TAB ~ FONCTIONS ~ ========================================================#

	def res_produit():
		tid_produit.set("")
		tnom_produit.set("")
		tlt_prix.set("")
		tlt_m2.set("")
		tlibelle_produit.set("")

	def getrow(event):
		rowid = trv.identify_row(event.y)
		item = trv.item(trv.focus())
		tid_produit.set(item['values'][0])
		tnom_produit.set(item['values'][1])
		tlt_prix.set(item['values'][2])
		tlt_m2.set(item['values'][3])
		tlibelle_produit.set(item['values'][4])

	def update(conn):
		trv.delete(*trv.get_children())
		for row in db.produit_read(conn):
			trv.insert('', 'end', values=row)

	def add_produit():
		nom_produit = tnom_produit.get()
		lt_prix = tlt_prix.get()
		lt_m2 = tlt_m2.get()
		libelle_produit = tlibelle_produit.get()
		if nom_produit == '' and lt_prix == '' and lt_m2 == '' and libelle_produit == '':
			messagebox.showerror('Required Fields', 'Please include all fields')
		else:
			db.produit_add(conn, nom_produit, lt_prix, lt_m2, libelle_produit)
			res_produit()
			update(conn)
			tk.messagebox.showinfo("Confirmation !", "Product been added !")

	def del_produit():
		id_produit = tid_produit.get()
		msg = messagebox.askyesno("Confirm Delete Please !", "Are you sure you want to delete this product? ")
		if msg == 0:
			res_produit()
		else:
			db.produit_del(conn, id_produit)
			res_produit()
			update(conn)
			tk.messagebox.showinfo("Confirmation !", "Product been deleted !")

	def update_produit():
		id_produit = tid_produit.get()
		nom_produit = tnom_produit.get()
		lt_prix = tlt_prix.get()
		lt_m2 = tlt_m2.get()
		libelle_produit = tlibelle_produit.get()

		msg = messagebox.askyesno("Confirm Update Please !", "Are you sure you want to update this product? ")
		if msg == 0:
			res_produit()
		else:
			db.produit_up(conn, nom_produit, lt_prix, lt_m2, libelle_produit, id_produit)
			res_produit()
			update(conn)
			tk.messagebox.showinfo("Confirmation !", "Product been updated !")

	def clear_produit():
		db.produit_read(conn)
		update(conn)
		res_produit()

	def search():
		x2 = x.get()
		if x2 == "":
			tk.messagebox.showerror("Invalid Product", " Please try again! ")
		else:
			trv.delete(*trv.get_children())
			for row in db.produit_search(conn, x2):
				trv.insert('', 'end', values=row)
			x.set("")

	# ====================================== ~ PRODUIT TAB ~ FRAME ~  ============================================#

	TabConrolProduitFrame = Frame(Tab3, relief=RIDGE)
	TabConrolProduitFrame.pack(fill=X, expand="yes")

	x = tk.StringVar()
	tid_produit = tk.StringVar()
	tnom_produit = tk.StringVar()
	tlt_prix = tk.DoubleVar()
	tlt_m2 = tk.IntVar()
	tlibelle_produit = tk.StringVar()

	lblPTitle = Label(TabConrolProduitFrame, text='\t PRODUIT \t',
	                  font=('arial', 30, 'bold'), fg='Ghost White', bg='Cadet Blue',  relief='ridge', bd=10)
	lblPTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

	wrapper1 = LabelFrame(TabConrolProduitFrame, text=" PRODUCT LIST : ",
	                      font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper1.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper2 = LabelFrame(TabConrolProduitFrame, text=" SEARCH : ",
	                      font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper2.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper3 = LabelFrame(TabConrolProduitFrame, text=" PRODUCT DATA : ",
	                      font=('arial', 20, 'bold'), fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper3.pack(fill=X, expand="yes", padx=20, pady=20)

	# ================================ ~ PRODUIT TAB ~ TREEVIEW & SCROLLBAR ~ ====================================#

	mycanvas = Canvas(wrapper1)
	mycanvas.pack(fill="both", expand="yes", side=LEFT)

	trv = ttk.Treeview(mycanvas, columns=(1, 2, 3, 4, 5), show="headings", height=6)
	trv.pack(fill="both", expand="yes", side=LEFT)

	ascenseurY = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=trv.yview)
	ascenseurY.pack(side=RIGHT, fill=Y)

	trv.column(1, width=6, anchor='c')
	trv.column(2, anchor='c')
	trv.column(3, width=15, anchor='c')
	trv.column(4, width=15, anchor='c')
	trv.column(5, anchor='c')
	trv.heading(1, text="PRODUIT-ID :\t")
	trv.heading(2, text="NOM :\t")
	trv.heading(3, text="PRIX LT :\t")
	trv.heading(4, text="LT / M2 :\t")
	trv.heading(5, text="LIBELLE :\t")

	trv.bind('<Double 1>', getrow)
	update(conn)

	# ===================================== ~ PRODUIT TAB ~ LABEL & ENTRY ~  ====================================#

	# Search Section
	lbl = Label(wrapper2, text="\t SEARCH : ", font=('arial', 12, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl.pack(side=tk.LEFT, padx=5, pady=3)
	ent = Entry(wrapper2, textvariable=x, font=('arial', 12, 'bold'), bd=6, width=25)
	ent.pack(side=tk.LEFT, padx=10, pady=3)
	btn = Button(wrapper2, text="SEARCH", width=15, font=('arial', 10, 'bold'), fg='Cadet Blue', bd=6, command=search)
	btn.pack(side=tk.LEFT, padx=10, pady=3)
	cbtn = Button(wrapper2, text="RESET", width=15, font=('arial', 10, 'bold'), fg='Cadet Blue', bd=6, command=clear_produit)
	cbtn.pack(side=tk.LEFT, padx=10, pady=3)

	# Produit Data Section
	lbl1 = Label(wrapper3, text="\t ID : ", font=('arial', 12, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl1.grid(row=0, column=0, padx=5, pady=3, sticky=E)
	ent1 = Entry(wrapper3, textvariable=tid_produit, font=('arial', 12, 'bold'), bd=6, width=25, state='readonly')
	ent1.grid(row=0, column=1, padx=10, pady=3, sticky=E)

	lbl2 = Label(wrapper3, text="\t NOM : ", font=('arial', 12, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=E)
	ent2 = Entry(wrapper3, textvariable=tnom_produit, font=('arial', 12, 'bold'), bd=6, width=25)
	ent2.grid(row=1, column=1, padx=10, pady=3)

	lbl3 = Label(wrapper3, text="\t PRIX LT : ", font=('arial', 12, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=E)
	ent3 = Entry(wrapper3, textvariable=tlt_prix, font=('arial', 12, 'bold'), bd=6, width=25)
	ent3.grid(row=2, column=1, padx=10, pady=3)

	lbl4 = Label(wrapper3, text="\t LT / M2 : ", font=('arial', 12, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=E)
	ent4 = Entry(wrapper3, textvariable=tlt_m2, font=('arial', 12, 'bold'), bd=6, width=25)
	ent4.grid(row=3, column=1, padx=10, pady=3)

	lbl5 = Label(wrapper3, text="\t LIBELLE : ", font=('arial', 12, 'bold'), fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl5.grid(row=4, column=0, padx=5, pady=3, sticky=E)
	ent5 = Entry(wrapper3, textvariable=tlibelle_produit, font=('arial', 12, 'bold'), bd=6, width=25)
	ent5.grid(row=4, column=1, padx=10, pady=3)

	# ==================================================== ~ PRODUIT TAB ~ BUTTONS ~  ========================================================#
	add_btn = Button(wrapper3, text="ADD", width=15, font=('arial', 10, 'bold'), fg='Cadet Blue', bd=6, command=add_produit)
	up_btn = Button(wrapper3, text="UPDATE", width=15, font=('arial', 10, 'bold'), fg='Cadet Blue', bd=6, command=update_produit)
	del_btn = Button(wrapper3, text="DELETE", width=15, font=('arial', 10, 'bold'), fg='Cadet Blue', bd=6, command=del_produit)
	res_btn = Button(wrapper3, text="CLEAR", width=15, font=('arial', 10, 'bold'), fg='Cadet Blue', bd=6, command=clear_produit)

	add_btn.grid(row=2, column=2, padx=10, pady=3)
	up_btn.grid(row=2, column=3, padx=10, pady=3)
	del_btn.grid(row=2, column=4, padx=10, pady=3)
	res_btn.grid(row=4, column=3, padx=10, pady=3)


if __name__ == '__main__':
	root = Tk()
	application = init(root)
	root.mainloop()




