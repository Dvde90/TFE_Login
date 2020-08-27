from tkinter import *
import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.messagebox import *
from hashlib import sha1
import DB_Log as db

conn = db.connect("db.sqlite")

def init(root):
	root = root
	root.title(" TFE-2020 ~ Van den Eede Derya ")
	root.geometry("1500x750+0+0")
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
			if username == '' or password == '' or password2 == '' or mail == '':
					showinfo("INFORMATION", "Please include all fields")
					Reg_Username.set("")
					Reg_Password.set("")
					Reg_Password2.set("")
					Reg_Mail.set("")
					txtRegUsername.focus()
			else:
				nw = db_reglog[1]
				if nw == username:
						showinfo("INFORMATION ", f"{username} is taken, please try again ! ")
						Reg_Username.set("")
						txtRegPassword.focus()
						txtRegPassword2.focus()
						txtRegUsermail.focus()
						return
				else:
						if password != password2:
								showinfo("Please try again !", "Your password is not matching... ")
								Reg_Password.set("")
								Reg_Password2.set("")
								txtRegUsername.focus()
								txtRegUsermail.focus()
						else:
								db.log_reg(conn, username, password, mail)
								showinfo("INFORMATION ", f"{username} have been registred ! ")
								return True

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

		lblRegTitle = Label(MRegLoginFrame, text='\t LOGIN REGISTRATION SYSTEM \t', font="Arial 30 bold",
		                    fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
		lblRegTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

		RegLoginFrame1 = LabelFrame(MRegLoginFrame, font="Arial 20 bold", relief='ridge', bd=10)
		RegLoginFrame1.pack(side=LEFT, fill=Y, expand="yes", padx=20, pady=40)

		RegLoginFrame2 = LabelFrame(MRegLoginFrame, font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
		RegLoginFrame2.pack(side=RIGHT, fill=Y, expand="yes", padx=20, pady=10)

		# ==================================================== ~ LOGIN REG ~ LABEL & ENTRY ~  ==================================================#

		lblRegUsername = Label(RegLoginFrame1, text=' USER NAME :', font="Arial 20 bold", bd=22)
		lblRegUsername.grid(row=0, column=0)
		txtRegUsername = Entry(RegLoginFrame1, textvariable=Reg_Username, font="Arial 20 bold", bd=10, width=33)
		txtRegUsername.grid(row=0, column=1, padx=120)

		lblRegPassword = Label(RegLoginFrame1, text=' PASSWORD :', font="Arial 20 bold", bd=22)
		lblRegPassword.grid(row=1, column=0)
		txtRegPassword = Entry(RegLoginFrame1, textvariable=Reg_Password, font="Arial 20 bold", bd=10, show='*', width=33)
		txtRegPassword.grid(row=1, column=1, columnspan=2, pady=30)

		lblRegPassword2 = Label(RegLoginFrame1, text=' PASSWORD :', font="Arial 20 bold", bd=22)
		lblRegPassword2.grid(row=2, column=0)
		txtRegPassword2 = Entry(RegLoginFrame1, textvariable=Reg_Password2, font="Arial 20 bold", bd=10, show='*', width=33)
		txtRegPassword2.grid(row=2, column=1, columnspan=2, pady=30)

		lblRegUsermail = Label(RegLoginFrame1, text=' USER E-MAIL :', font="Arial 20 bold", bd=22)
		lblRegUsermail.grid(row=3, column=0)
		txtRegUsermail = Entry(RegLoginFrame1, textvariable=Reg_Mail, font="Arial 20 bold", bd=10,  width=33)
		txtRegUsermail.grid(row=3, column=1, padx=120)

		# ==================================================== ~ LOGIN REG ~ BUTTONS ~  ========================================================#

		BtAdd = Button(RegLoginFrame2, text="ADD", font="Arial 20 bold", width=15, fg='Cadet Blue', bd=20, command=Regadd)
		BtAdd.grid(row=0, column=0, pady=20, padx=10)
		BtReset = Button(RegLoginFrame2, text="RESET", font="Arial 20 bold", width=15,fg='Cadet Blue', bd=20, command=RegReset)
		BtReset.grid(row=1, column=0, pady=20, padx=10)
		BtExit = Button(RegLoginFrame2, text="EXIT", font="Arial 20 bold", width=15, fg='Cadet Blue', bd=20, command=MReg.destroy)
		BtExit.grid(row=2, column=0, pady=20, padx=10)

	# ==================================================== ~ LOGIN TAB ~ FONCTIONS ~ ========================================================#

	def Login_System():
		username = (Username.get())
		password = (Password.get())
		db_pwd = db.log_in(conn, username)
		encoded_pwd = sha1(password.encode()).hexdigest()

		if db_pwd is None:
			msg = askyesno("Login System", "Invalid username Please try again! ")
			if msg == 0:
				root.destroy()
			else:
				Username.set("")
				Password.set("")
				txtUsername.focus()

		else:
			if db_pwd[0] != encoded_pwd:
				msg = askyesno("Login System", "Invalid password Please try again! ")
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
			iExit = askyesno("Login System", "Confirm if you want to Exit")
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

	lblTitle = Label(TabConrolLoginFrame, text='\t LOGIN SYSTEM \t', font="Arial 30 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	lblTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

	LoginFrame1 = LabelFrame(TabConrolLoginFrame, font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	LoginFrame1.pack(fill=X, expand="yes", padx=20, pady=20)

	LoginFrame2 = LabelFrame(TabConrolLoginFrame, font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	LoginFrame2.pack(fill=X, expand="yes", padx=20, pady=20)

	# ==================================================== ~ LOGIN TAB ~ LABEL & ENTRY ~  ==================================================#

	lblUsername = Label(LoginFrame1, text=' USER NAME :', font="Arial 25 bold", fg='Ghost White', bg='Cadet Blue', bd=22)
	lblUsername.grid(row=0, column=0)
	txtUsername = Entry(LoginFrame1, textvariable=Username, font="Arial 20 bold", bd=12,  width=30)
	txtUsername.grid(row=0, column=1, padx=50)

	lblPassword = Label(LoginFrame1, text=' PASSWORD :', font="Arial 25 bold", fg='Ghost White', bg='Cadet Blue', bd=22)
	lblPassword.grid(row=1, column=0)
	txtPassword = Entry(LoginFrame1, textvariable=Password, font="Arial 20 bold", bd=12, show='*', width=30)
	txtPassword.grid(row=1, column=1,  columnspan=2, pady=30)

	# ==================================================== ~ LOGIN TAB ~ BUTTONS ~  ========================================================#

	btnReg = Button(LoginFrame2, text='REGISTER', width=15, font="Arial 20 bold", fg='Cadet Blue', bd=12, command=Reg_System)
	btnReg.grid(row=3, column=0, pady=20, padx=10)

	btnReset = Button(LoginFrame2, text='RESET', width=15, font="Arial 20 bold", fg='Cadet Blue', bd=12, command=Reset)
	btnReset.grid(row=3, column=1, pady=20, padx=10)

	btnLogin = Button(LoginFrame2, text='LOGIN', width=15, font="Arial 20 bold", fg='Cadet Blue', bd=12, command=Login_System)
	btnLogin.grid(row=3, column=2,  pady=20, padx=10)

	btnExit = Button(LoginFrame2, text='EXIT', width=15, font="Arial 20 bold", fg='Cadet Blue', bd=12, command=iExit)
	btnExit.grid(row=4, column=1, pady=20, padx=10)

	# ==================================================== ~ CLIENT TAB ~ FONCTIONS ~ ========================================================#

	def res_client():
		cid.set("")
		c_ref.set("")
		c_nom.set("")
		c_prenom.set("")
		c_adresse.set("")
		c_ville.set("")
		c_tel.set("")
		c_email.set("")
		c_tva.set("")

	def getrow_client(event):
		rowidC = trv_cli.identify_row(event.y)
		item_cli = trv_cli.item(trv_cli.focus())
		cid.set(item_cli['values'][0])
		c_ref.set(item_cli['values'][1])
		c_nom.set(item_cli['values'][2])
		c_prenom.set(item_cli['values'][3])
		c_adresse.set(item_cli['values'][4])
		c_ville.set(item_cli['values'][5])
		c_tel.set(item_cli['values'][6])
		c_email.set(item_cli['values'][7])
		c_tva.set(item_cli['values'][8])

	def update_cli(conn):
		trv_cli.delete(*trv_cli.get_children())
		for row in db.client_read(conn):
			trv_cli.insert('', 'end', values=row)

	def clear_client():
		db.client_read(conn)
		update_cli(conn)
		res_client()

	def add_client():
		ref = c_ref.get()
		nom = c_nom.get()
		prenom = c_prenom.get()
		adresse = c_adresse.get()
		ville = c_ville.get()
		tel = c_tel.get()
		email = c_email.get()
		tva = c_tva.get()

		if ref == '' and nom == '' and prenom == '' and adresse == '' and ville == '' and tel == '' and email == '' and tva == '':
			showerror('Required Fields', 'Please include all fields')
		else:
			db.client_add(conn, ref, nom, prenom, adresse, ville, tel, email, tva)
			res_client()
			update_cli(conn)
			showinfo("Confirmation !", "The client added !")

	def del_client():
		c_id = cid.get()
		msg = askyesno("Confirm Delete Please !", "Are you sure you want to delete this client? ")
		if msg == 0:
			res_client()
		else:
			db.client_del(conn, c_id)
			res_client()
			update_cli(conn)
			showinfo("Confirmation !", "The client been deleted !")

	def update_client():
		c_id = cid.get()
		ref = c_ref.get()
		nom = c_nom.get()
		prenom = c_prenom.get()
		adresse = c_adresse.get()
		ville = c_ville.get()
		tel = c_tel.get()
		email = c_email.get()
		tva = c_tva.get()

		msg = askyesno("Confirm Update Please !", "Are you sure you want to update this client? ")
		if msg == 0:
			res_client()
		else:
			db.client_up(conn, ref, nom, prenom, adresse, ville, tel, email, tva, c_id)
			res_client()
			update_cli(conn)
			showinfo("Confirmation !", "The client updated !")

	def log_out_client():
		logout_msg = askyesno("Client System", "Confirm if you want to Exit")
		if logout_msg > 0:
			notebook.select(Tab0)
			notebook.hide(Tab1)
			notebook.hide(Tab2)
			notebook.hide(Tab3)
		else:
			command = Tab1
			return

	# ====================================== ~ CLIENT TAB ~ FRAME ~  ============================================#

	TabClientFrame = Frame(Tab1, relief=RIDGE)
	TabClientFrame.pack(fill=X, expand="yes")

	x_cli = tk.StringVar()
	cid = tk.IntVar()
	c_ref = tk.StringVar()
	c_nom = tk.StringVar()
	c_prenom = tk.StringVar()
	c_adresse = tk.StringVar()
	c_ville = tk.StringVar()
	c_tel = tk.IntVar()
	c_email = tk.StringVar()
	c_tva = tk.StringVar()

	lblPTitle = Label(TabClientFrame, text='CLIENT \t', font="Arial 30 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	lblPTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=20)

	wrapper1 = LabelFrame(TabClientFrame, text=" CLIENT DATA : ", font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper1.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper2 = LabelFrame(TabClientFrame, font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper2.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper3 = LabelFrame(TabClientFrame, text=" CLIENT LIST : ", font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper3.pack(fill=X, expand="yes", padx=20, pady=20)

	# ================================ ~ CLIENT TAB ~ TREEVIEW & SCROLLBAR ~ ====================================#

	mycanvas = Canvas(wrapper3)
	mycanvas.pack(fill="both", expand="yes", side=LEFT)

	trv_cli = ttk.Treeview(mycanvas, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9), show="headings", height=6)
	trv_cli.pack(fill="both", expand="yes", side=LEFT)

	ascenseurY = ttk.Scrollbar(wrapper3, orient=VERTICAL, command=trv_cli.yview)
	ascenseurY.pack(side=RIGHT, fill=Y)

	trv_cli.column(1, width=10, anchor='c')
	trv_cli.column(2, width=30, anchor='c')
	trv_cli.column(3, width=40, anchor='c')
	trv_cli.column(4, width=40, anchor='c')
	trv_cli.column(5, width=40, anchor='c')
	trv_cli.column(6, width=30, anchor='c')
	trv_cli.column(7, width=40, anchor='c')
	trv_cli.column(8, width=50, anchor='c')
	trv_cli.column(9, width=45, anchor='c')
	trv_cli.heading(1, text="ID :\t")
	trv_cli.heading(2, text="REF :\t")
	trv_cli.heading(3, text="NOM :\t")
	trv_cli.heading(4, text="PRENOM :\t")
	trv_cli.heading(5, text="ADDRESSE :\t")
	trv_cli.heading(6, text="VILLE :\t")
	trv_cli.heading(7, text="TELEPHONE :\t")
	trv_cli.heading(8, text="E-MAIL :\t")
	trv_cli.heading(9, text="TVA :\t")

	trv_cli.bind('<Double 1>', getrow_client)
	update_cli(conn)

	lblcID = Label(wrapper1, text="\t CLIENT ID : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcID.grid(row=0, column=0, padx=5, pady=3, sticky=E)
	txtcID = Entry(wrapper1, textvariable=cid, font="Arial 12 bold", bd=6, width=10, state='readonly')
	txtcID.grid(row=0, column=1, padx=5, pady=3, sticky=W)

	lblcREF = Label(wrapper1, text="\t REF : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcREF.grid(row=0, column=2, padx=5, pady=3, sticky=E)
	txtcREF = Entry(wrapper1, textvariable=c_ref, font="Arial 12 bold", bd=6, width=15)
	txtcREF.grid(row=0, column=3, padx=5, pady=3, sticky=W)

	lblcNom = Label(wrapper1, text=" NOM : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcNom.grid(row=1, column=0, padx=5, pady=3, sticky=E)
	txtcNom = Entry(wrapper1, textvariable=c_nom, font="Arial 12 bold", bd=6, width=30)
	txtcNom.grid(row=1, column=1, padx=5, pady=3, sticky=W)

	lblcProm = Label(wrapper1, text="\t PRENOM : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcProm.grid(row=2, column=0, padx=5, pady=3, sticky=E)
	txtcPnom = Entry(wrapper1, textvariable=c_prenom, font="Arial 12 bold", bd=6, width=30)
	txtcPnom.grid(row=2, column=1, padx=5, pady=3, sticky=W)

	lblcAdr = Label(wrapper1, text=" ADDRESSE : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcAdr.grid(row=3, column=0, padx=5, pady=3, sticky=E)
	txtcAdr = Entry(wrapper1, textvariable=c_adresse, font="Arial 12 bold", bd=6, width=30)
	txtcAdr.grid(row=3, column=1, padx=5, pady=3, sticky=W)

	lblcVille = Label(wrapper1, text=" VILLE : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcVille.grid(row=4, column=0, padx=5, pady=3, sticky=E)
	txtcVille = Entry(wrapper1, textvariable=c_ville,  font="Arial 12 bold", bd=6, width=30)
	txtcVille.grid(row=4, column=1, padx=5, pady=3, sticky=W)

	lblcTel = Label(wrapper1, text=" GSM : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcTel.grid(row=1, column=2, padx=5, pady=3, sticky=E)
	txtcTel = Entry(wrapper1, textvariable=c_tel,  font="Arial 12 bold", bd=6, width=30)
	txtcTel.grid(row=1, column=3, padx=5, pady=3, sticky=W)

	lblcMail = Label(wrapper1, text=" E-MAIL : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcMail.grid(row=2, column=2, padx=5, pady=3, sticky=E)
	txtcMail = Entry(wrapper1, textvariable=c_email, font="Arial 12 bold", bd=6, width=30)
	txtcMail.grid(row=2, column=3, padx=5, pady=3, sticky=W)

	lblcTva = Label(wrapper1, text=" TVA : ", font="Arial 12 bold", fg="Ghost White", bg='Cadet Blue', bd=6)
	lblcTva.grid(row=3, column=2, padx=5, pady=3, sticky=E)
	txtcTva = Entry(wrapper1, textvariable=c_tva, font="Arial 12 bold", bd=6, width=30)
	txtcTva.grid(row=3, column=3, padx=5, pady=3, sticky=W)

	# ==================================================== ~ CLIENT TAB ~ BUTTONS ~  ========================================================#
	add_btn = Button(wrapper2, text="ADD", font="Arial 10 bold", width=15, fg='Cadet Blue', bd=6, command=add_client)
	up_btn = Button(wrapper2, text="UPDATE", font="Arial 10 bold", width=15, fg='Cadet Blue', bd=6,command=update_client)
	del_btn = Button(wrapper2, text="DELETE", font="Arial 10 bold", width=15, fg='Cadet Blue', bd=6,command=del_client)
	res_btn = Button(wrapper2, text="CLEAR", font="Arial 10 bold", width=15, fg='Cadet Blue', bd=6,command=clear_client)
	s_btn = Button(wrapper2, text="SEARCH", font="Arial 10 bold", width=15, fg='Cadet Blue', bd=6)#, command=search_pro)
	lout_btn = Button(wrapper2, text="LOG OUT", font="Arial 10 bold", width=15, fg='Cadet Blue', bd=6, command=log_out_client)

	add_btn.pack(side=tk.LEFT, padx=10, pady=3)
	up_btn.pack(side=tk.LEFT, padx=10, pady=3)
	del_btn.pack(side=tk.LEFT, padx=10, pady=3)
	res_btn.pack(side=tk.LEFT, padx=10, pady=3)
	s_btn.pack(side=tk.LEFT, padx=10, pady=3)
	lout_btn.pack(side=tk.LEFT, padx=10, pady=3)

	# ==================================================== ~ PRODUIT TAB ~ FONCTIONS ~ ========================================================#

	def res_produit():
		tid_produit.set("")
		tnom_produit.set("")
		tlt_prix.set("")
		tlt_m2.set("")
		tlibelle_produit.set("")

	def getrow_produit(event):
		rowid = trv_pro.identify_row(event.y)
		item_pro = trv_pro.item(trv_pro.focus())
		tid_produit.set(item_pro['values'][0])
		tnom_produit.set(item_pro['values'][1])
		tlt_prix.set(item_pro['values'][2])
		tlt_m2.set(item_pro['values'][3])
		tlibelle_produit.set(item_pro['values'][4])

	def update_pro(conn):
		trv_pro.delete(*trv_pro.get_children())
		for row in db.produit_read(conn):
			trv_pro.insert('', 'end', values=row)

	def add_produit():
		nom_produit = tnom_produit.get()
		lt_prix = tlt_prix.get()
		lt_m2 = tlt_m2.get()
		libelle_produit = tlibelle_produit.get()
		if nom_produit == '' and lt_prix == '' and lt_m2 == '' and libelle_produit == '':
			showerror('Required Fields', 'Please include all fields')
		else:
			db.produit_add(conn, nom_produit, lt_prix, lt_m2, libelle_produit)
			res_produit()
			update_pro(conn)
			showinfo("Confirmation !", "Product been added !")

	def del_produit():
		id_produit = tid_produit.get()
		msg = askyesno("Confirm Delete Please !", "Are you sure you want to delete this product? ")
		if msg == 0:
			res_produit()
		else:
			db.produit_del(conn, id_produit)
			res_produit()
			update_pro(conn)
			showinfo("Confirmation !", "Product been deleted !")

	def update_produit():
		id_produit = tid_produit.get()
		nom_produit = tnom_produit.get()
		lt_prix = tlt_prix.get()
		lt_m2 = tlt_m2.get()
		libelle_produit = tlibelle_produit.get()

		msg = askyesno("Confirm Update Please !", "Are you sure you want to update_pro this product? ")
		if msg == 0:
			res_produit()
		else:
			db.produit_up(conn, nom_produit, lt_prix, lt_m2, libelle_produit, id_produit)
			res_produit()
			update_pro(conn)
			showinfo("Confirmation !", "Product been updated !")

	def clear_produit():
		db.produit_read(conn)
		update_pro(conn)
		res_produit()

	def search_pro():
		x2 = x_pro.get()
		if x2 == "":
			showerror("Invalid Product", " Please try again! ")
		else:
			trv_pro.delete(*trv_pro.get_children())
			for row in db.produit_search(conn, x2):
				trv_pro.insert('', 'end', values=row)
			x_pro.set("")

	def log_out():
		logout_msg = askyesno("Produit System", "Confirm if you want to Exit")
		if logout_msg > 0:
			notebook.select(Tab0)
			notebook.hide(Tab1)
			notebook.hide(Tab2)
			notebook.hide(Tab3)
		else:
			command = Tab3
			return

	# ====================================== ~ PRODUIT TAB ~ FRAME ~  ============================================#

	TabConrolProduitFrame = Frame(Tab3, relief=RIDGE)
	TabConrolProduitFrame.pack(fill=X, expand="yes")

	x_pro = tk.StringVar()
	tid_produit = tk.StringVar()
	tnom_produit = tk.StringVar()
	tlt_prix = tk.DoubleVar()
	tlt_m2 = tk.IntVar()
	tlibelle_produit = tk.StringVar()

	lblPTitle = Label(TabConrolProduitFrame, text='\t PRODUIT \t',
	                  font="Arial 30 bold", fg='Ghost White', bg='Cadet Blue',  relief='ridge', bd=10)
	lblPTitle.pack(side=TOP, fill=X, expand="yes", padx=20, pady=10)

	wrapper1 = LabelFrame(TabConrolProduitFrame, text=" PRODUCT LIST : ",
	                      font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper1.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper2 = LabelFrame(TabConrolProduitFrame, text=" SEARCH : ",
	                      font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper2.pack(fill=X, expand="yes", padx=20, pady=20)
	wrapper3 = LabelFrame(TabConrolProduitFrame, text=" PRODUCT DATA : ",
	                      font="Arial 20 bold", fg='Ghost White', bg='Cadet Blue', relief='ridge', bd=10)
	wrapper3.pack(fill=X, expand="yes", padx=20, pady=20)

	# ================================ ~ PRODUIT TAB ~ TREEVIEW & SCROLLBAR ~ ====================================#

	mycanvas = Canvas(wrapper1)
	mycanvas.pack(fill="both", expand="yes", side=LEFT)

	trv_pro = ttk.Treeview(mycanvas, columns=(1, 2, 3, 4, 5), show="headings", height=6)
	trv_pro.pack(fill="both", expand="yes", side=LEFT)

	ascenseurY = ttk.Scrollbar(wrapper1, orient=VERTICAL, command=trv_pro.yview)
	ascenseurY.pack(side=RIGHT, fill=Y)

	trv_pro.column(1, width=6, anchor='c')
	trv_pro.column(2, anchor='c')
	trv_pro.column(3, width=15, anchor='c')
	trv_pro.column(4, width=15, anchor='c')
	trv_pro.column(5, anchor='c')
	trv_pro.heading(1, text="PRODUIT-ID :\t")
	trv_pro.heading(2, text="NOM :\t")
	trv_pro.heading(3, text="PRIX LT :\t")
	trv_pro.heading(4, text="LT / M2 :\t")
	trv_pro.heading(5, text="LIBELLE :\t")

	trv_pro.bind('<Double 1>', getrow_produit)
	update_pro(conn)

	# ===================================== ~ PRODUIT TAB ~ LABEL & ENTRY ~  ====================================#

	# Search Section
	lbl = Label(wrapper2, text="\t SEARCH : ", font="Arial 12 bold", fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl.pack(side=tk.LEFT, padx=5, pady=3)
	ent = Entry(wrapper2, textvariable=x_pro, font="Arial 12 bold", bd=6, width=25)
	ent.pack(side=tk.LEFT, padx=10, pady=3)
	btn = Button(wrapper2, text="SEARCH", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=search_pro)
	btn.pack(side=tk.LEFT, padx=10, pady=3)
	cbtn = Button(wrapper2, text="RESET", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=clear_produit)
	cbtn.pack(side=tk.LEFT, padx=10, pady=3)

	# Produit Data Section
	lbl1 = Label(wrapper3, text="\t ID : ", font="Arial 12 bold", fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl1.grid(row=0, column=0, padx=5, pady=3, sticky=E)
	ent1 = Entry(wrapper3, textvariable=tid_produit, font="Arial 12 bold", bd=6, width=25, state='readonly')
	ent1.grid(row=0, column=1, padx=10, pady=3, sticky=E)

	lbl2 = Label(wrapper3, text="\t NOM : ", font="Arial 12 bold", fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl2.grid(row=1, column=0, padx=5, pady=3, sticky=E)
	ent2 = Entry(wrapper3, textvariable=tnom_produit, font="Arial 12 bold", bd=6, width=25)
	ent2.grid(row=1, column=1, padx=10, pady=3)

	lbl3 = Label(wrapper3, text="\t PRIX LT : ", font="Arial 12 bold", fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl3.grid(row=2, column=0, padx=5, pady=3, sticky=E)
	ent3 = Entry(wrapper3, textvariable=tlt_prix, font="Arial 12 bold", bd=6, width=25)
	ent3.grid(row=2, column=1, padx=10, pady=3)

	lbl4 = Label(wrapper3, text="\t LT / M2 : ", font="Arial 12 bold", fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl4.grid(row=3, column=0, padx=5, pady=3, sticky=E)
	ent4 = Entry(wrapper3, textvariable=tlt_m2, font="Arial 12 bold", bd=6, width=25)
	ent4.grid(row=3, column=1, padx=10, pady=3)

	lbl5 = Label(wrapper3, text="\t LIBELLE : ", font="Arial 12 bold", fg='Ghost White', bg='Cadet Blue', bd=6)
	lbl5.grid(row=4, column=0, padx=5, pady=3, sticky=E)
	ent5 = Entry(wrapper3, textvariable=tlibelle_produit, font="Arial 12 bold", bd=6, width=25)
	ent5.grid(row=4, column=1, padx=10, pady=3)

	# ==================================================== ~ PRODUIT TAB ~ BUTTONS ~  ========================================================#
	add_btn = Button(wrapper3, text="ADD", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=add_produit)
	up_btn = Button(wrapper3, text="UPDATE", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=update_produit)
	del_btn = Button(wrapper3, text="DELETE", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=del_produit)
	res_btn = Button(wrapper3, text="CLEAR", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=clear_produit)
	lout_btn= Button(wrapper3, text="LOG OUT", width=15, font="Arial 10 bold", fg='Cadet Blue', bd=6, command=log_out)

	add_btn.grid(row=1, column=2, padx=10, pady=3)
	up_btn.grid(row=2, column=2, padx=10, pady=3)
	del_btn.grid(row=3, column=2, padx=10, pady=3)
	res_btn.grid(row=2, column=3, padx=10, pady=3)
	lout_btn.grid(row=4, column=4, padx=10, pady=3)


if __name__ == '__main__':
	root = Tk()
	application = init(root)
	root.mainloop()




