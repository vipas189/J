from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageGrab
import pyautogui as pt
from Baigiamasis_Back import *
import sqlite3
from tkinter.colorchooser import askcolor


class coordinates_colors_window:
    def __init__(self, tkinter):
        self.tkinter = tkinter
        self.tab = ttk.Notebook(self.tkinter)
        self.tkinter.resizable(False, False)
        tkinter_geometry_center(self.tkinter, 650, 320)
        self.tkinter.protocol("WM_DELETE_WINDOW", on_closing)
        self.tkinter.title('Colorite')
        self.tkinter.iconbitmap(r'f.ico')

        self.frame_tab_coordinates_colors = Frame(self.tab)
        self.frame_tab_color = Frame(self.tab)
        self.frame_tab_login = Frame(self.tab)
        self.frame_login = Frame(self.frame_tab_login)
        self.frame_login_2 = Frame(self.frame_tab_login)

        self.org_aprasymas = Label(self.frame_tab_coordinates_colors, text='\nCoordinates and colors:\n', font=25,
                                   height=1)
        self.org_koordinates = Label(self.frame_tab_coordinates_colors, text='', font=("Fixedsys", 15))
        self.org_spalvos_kodas = Label(self.frame_tab_coordinates_colors, text='', font=("Fixedsys", 15))
        self.org_spalvos_laukelis = Label(self.frame_tab_coordinates_colors, bg='#ffffff', height=4, width=13)
        self.login_username = Label(self.frame_login_2, text='Username')
        self.login_password = Label(self.frame_login_2, text='Password')
        self.login_empty_2 = Label(self.frame_login_2, width=23)
        self.login_empty = Label(self.frame_login, width=28, height=2)
        self.login_ar_prisijungta = Label(self.frame_login_2, text='Neprisijungta', fg='RED',
                                          font=("Times New", 7))
        self.frame_login_login_label = Label(self.frame_login, text='Login', font=("Fixedsys", 13))
        self.login_registracija = Label(self.frame_login_2, text='Register', font=("Times New", 7), fg='#2E2E2E')
        self.login_registracija_here = Label(self.frame_login_2, text='here', cursor="hand2", fg='RED',
                                             font=("Times New", 7))

        self.org_spalvu_listbox_scroll = Scrollbar(self.frame_tab_coordinates_colors)

        self.org_spalvu_listbox = Listbox(self.frame_tab_coordinates_colors,
                                          yscrollcommand=self.org_spalvu_listbox_scroll.set, width=13,
                                          height=5)

        self.org_remove_button = Button(self.frame_tab_coordinates_colors, text='X', height=1, width=1,
                                        command=self.delete)
        self.org_copy_button = Button(self.frame_tab_coordinates_colors, text='Copy', width=4)
        self.org_close_button = Button(self.frame_tab_coordinates_colors, text='Close', font=("Fixedsys", 16),
                                       bg='#676F73', height=2,
                                       width=43,
                                       command=self.tkinter.destroy)
        self.color_close_button = Button(self.frame_tab_color, text='Close', font=("Fixedsys", 16),
                                         bg='#676F33', height=2,
                                         width=40,
                                         command=self.tkinter.destroy)
        self.login_login_button = Button(self.frame_login_2, text='Login', height=1, command=self.login)

        self.color_button = Button(self.frame_tab_coordinates_colors, text='Color', command=askcolor)

        self.user_input = StringVar()
        self.pass_input = StringVar()
        self.login_username_entry = Entry(self.frame_login_2, width=22, textvariable=self.user_input)
        self.login_password_entry = Entry(self.frame_login_2, show="*", width=22, textvariable=self.pass_input)

        self.login_checkbutton_remember = Checkbutton(self.frame_login_2, text='Remember credentials',
                                                      font=("Times New", 6), fg='#4C4C4C')
        self.showpassword = IntVar()
        self.login_checkbutton_showpassword = Checkbutton(self.frame_login_2, text='Show password',
                                                          font=("Times New", 6), variable=self.showpassword, onvalue=1,
                                                          offvalue=0, command=self.show_password, fg='#4C4C4C')

    def frames(self):
        self.tab.add(self.frame_tab_login, text='Login')
        self.tab.grid()
        self.frame_login.grid(row=0)
        self.frame_login_2.grid(row=1)

    def labels(self):
        self.org_aprasymas.grid(row=0, column=1)
        self.org_spalvos_laukelis.grid(row=2, column=3, sticky='E')
        self.org_koordinates.grid(row=1, column=1)
        self.org_spalvos_kodas.grid(row=2, column=1)
        self.login_empty_2.grid(row=2, column=0)
        self.login_empty.grid(row=0, column=0)
        self.login_username.grid(row=2, column=1)
        self.login_password.grid(row=3, column=1)
        self.login_ar_prisijungta.grid(row=6, column=2, sticky='NE')
        self.frame_login_login_label.grid(row=1, column=1)
        self.login_registracija.grid(row=7, column=2, sticky='W')
        self.login_registracija_here.grid(row=7, column=2, sticky='W', padx=45)

    def scrollbars(self):
        self.org_spalvu_listbox_scroll.config(command=self.org_spalvu_listbox.yview())
        self.org_spalvu_listbox_scroll.grid(row=1, column=4)

    def listboxes(self):
        self.org_spalvu_listbox.grid(row=1, column=3, sticky='E')

    def buttons(self):
        self.org_remove_button.grid(row=1, column=3, sticky='W', ipadx=15)
        self.org_close_button.grid(row=3, columnspan=5, sticky='S')
        # self.org_copy_button.grid(row=1, column=2, sticky=E)

        self.color_close_button.grid()
        self.login_login_button.grid(row=6, column=2, sticky='W')
        self.color_button.grid(row=2, column=3, sticky='W')

    def entry(self):
        self.login_username_entry.grid(row=2, column=2)
        self.login_password_entry.grid(row=3, column=2)

    def checkbutton(self):
        # self.login_checkbutton_remember.grid(row=5, column=2, sticky='W')
        self.login_checkbutton_showpassword.grid(row=4, column=2, sticky='W')

    def keys(self):
        self.tkinter.bind('<Shift_L>',
                          lambda a: self.org_spalvu_listbox.insert(END, self.org_spalvos_kodas.cget('text')))
        self.login_registracija_here.bind('<Button-1>', lambda a: self.naujas_langas())

    # Atnaujina informacija

    def atnaujinimas(self):
        x_asis = [x for x in str(pt.position()).split()[0] if x.isnumeric()]
        y_asis = [x for x in str(pt.position()).split()[1] if x.isnumeric()]
        x = int("".join(x_asis))
        y = int("".join(y_asis))
        color = ImageGrab.grab().getpixel((x, y))
        self.org_koordinates.configure(text=f'x = {x}    y = {y}')
        self.org_spalvos_kodas.configure(text=f'#{rgb_to_hex((color[0], color[1], color[2]))}\n')
        self.org_spalvos_laukelis.configure(bg=f'#{rgb_to_hex((color[0], color[1], color[2]))}')
        self.tkinter.after(1, self.atnaujinimas)

    # Papildomi metodai
    def delete(self):
        self.org_spalvu_listbox.delete(ACTIVE)

    def show_password(self):
        if self.showpassword.get() == 1:
            self.login_password_entry.configure(show='')
        else:
            self.login_password_entry.configure(show='*')

    def naujas_langas(self):
        registracija = registration_window(Toplevel(self.tkinter))
        return registracija

    def login(self):
        db = sqlite3.connect('Baigiamasis.db')
        with db:
            cursor = db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Login(Username TEXT, Password TEXT)')
        cursor.execute('SELECT * FROM login where Username=? AND Password=?',
                       (self.login_username_entry.get(), self.login_password_entry.get()))
        row = cursor.fetchone()
        if row:
            self.login_ar_prisijungta.configure(text='Sekmingai prisijungta', fg='GREEN')
            self.tab.add(self.frame_tab_coordinates_colors, text='Coordinates and Colors')
            self.tab.grid()
            # self.tab.add(self.frame_tab_color, text='Color Palette')
            self.tab.grid()

        else:
            self.login_ar_prisijungta.configure(text='Neteisingi duomenys', fg='RED')


class registration_window:
    def __init__(self, tkinter):
        self.tkinter = tkinter
        self.tkinter.title('Register')
        tkinter_geometry_center(self.tkinter, 300, 160)
        self.user_reg_input = StringVar()
        self.pass_reg_input = StringVar()
        self.reg_username_entry = Entry(self.tkinter, width=22, textvariable=self.user_reg_input)
        self.reg_password_entry = Entry(self.tkinter, show="*", width=22, textvariable=self.pass_reg_input)
        self.sshowpassword = IntVar()
        self.reg_checkbutton_showpassword = Checkbutton(self.tkinter, text='Show password',
                                                        font=("Times New", 6), variable=self.sshowpassword, onvalue=1,
                                                        offvalue=0, command=self.show_password, fg='#4C4C4C')
        self.reg_username = Label(self.tkinter, text='Username')
        self.reg_password = Label(self.tkinter, text='Password')
        self.reg_button = Button(self.tkinter, text='Register', height=1, command=self.login)
        self.reg_ar_prisijungta = Label(self.tkinter, text='', fg='RED',
                                        font=("Times New", 7))
        self.reg_empty = Label(self.tkinter, width=2, height=1)

        self.reg_empty.grid(row=0, column=0)
        self.reg_username_entry.grid(row=1, column=2)
        self.reg_password_entry.grid(row=2, column=2)
        self.reg_username.grid(row=1, column=1)
        self.reg_password.grid(row=2, column=1)
        self.reg_checkbutton_showpassword.grid(row=3, column=2, sticky='W')
        self.reg_button.grid(row=4, column=2, sticky='W')
        self.reg_ar_prisijungta.grid(row=4, column=2, sticky='E')

    def show_password(self):
        if self.sshowpassword.get() == 1:
            self.reg_password_entry.configure(show='')
        else:
            self.reg_password_entry.configure(show='*')

    def login(self):
        user = self.reg_username_entry.get()
        passw = self.reg_password_entry.get()
        if self.reg_username_entry.get() == '' or self.reg_password_entry.get() == '':
            self.reg_ar_prisijungta.configure(text='Negali buti tusti laukeliai', fg='RED')
        else:
            db2 = sqlite3.connect('Baigiamasis.db')
            with db2:
                cursor = db2.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS Login(Username TEXT, Password TEXT)')
            cursor.execute('INSERT INTO Login(Username, Password) VALUES(?, ?)',
                           (user, passw))
            db2.commit()
            self.reg_ar_prisijungta.configure(text='Sekmingai \nuzsiregistruota', fg='GREEN')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        gui.destroy()


gui = Tk()
coordinates_colors_window1 = coordinates_colors_window(gui)
coordinates_colors_window1.frames()
coordinates_colors_window1.labels()
coordinates_colors_window1.scrollbars()
coordinates_colors_window1.listboxes()
coordinates_colors_window1.buttons()
coordinates_colors_window1.entry()
coordinates_colors_window1.checkbutton()
coordinates_colors_window1.keys()
coordinates_colors_window1.atnaujinimas()
gui.mainloop()
