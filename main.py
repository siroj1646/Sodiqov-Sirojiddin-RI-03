import tkinter as tk
from tkinter import *
from tkinter import *



class SampleAPP(tk.Tk):


    def __init__(self, *arg, **kwargs ):
        tk.Tk.__init__(self,*arg,**kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)




        self.frames = {}
        for F in(StartPage, MenuPage,FunPage):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name]=frame


            frame.grid(row = 0, column = 0, sticky="nsew")

            self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()







class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        """app.geometry("400x400")
        bg = PhotoImage(file="wall2.png")
        canvas1 = Canvas(app, width=400, height=400)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")"""

        tk.Frame.__init__(self, parent, bg= "black")
        self.controller = controller
        self.controller.title("MY FIRST ATM")
        self.controller.state('zoomed')

        #self.controller.iconphoto(False, tk.PhotoImage(file = 'wall.png'))

        big_lable = tk.Label(self, text = "THIS IS ATM", font = ('Bernard MT Condensed',50,'bold'),fg= "pink", bg = "black")
        big_lable.pack(pady=30)

        login_lable= tk.Label(self, text = "ENTER YOUR LOGIN", font = ('Bernard MT Condensed',15,'bold'),fg= "pink", bg = "black")
        login_lable.pack(pady=30)


        my_login = tk.StringVar()
        login_entry = tk.Entry(self,textvariable = my_login,  font = ('Bernard MT Condensed',15,'bold'),fg= "pink", bg = "black")
        login_entry.pack(pady=30)

        password_lable = tk.Label(self, text = "ENTER YOUR PASSWORD", font = ('Bernard MT Condensed',15,'bold'),fg= "pink", bg = "black")
        password_lable.pack()



        my_password = tk.StringVar()
        password_entry = tk.Entry(self,textvariable = my_password,  font = ('Bernard MT Condensed',15,'bold'),fg= "pink", bg = "black")
        password_entry.pack(pady=30)

        def check_password():
            if my_password.get()=="1646" and my_login.get()=="sirojiddin":
                controller.show_frame('MenuPage')

                #right_lable = tk.Label(self, text= "right answer")
                #right_lable.pack()

            else:
                right_lable['text']= "Wrong Password or login"

        password_button = tk.Button(self, text="Check you password and login", command=check_password,
                                    font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        password_button.pack()
        right_lable = tk.Label(self,font = ('Bernard MT Condensed',15,'bold'),fg= "pink", bg = "black" )
        right_lable.pack(pady = 30)

        def next_page():
            controller.show_frame('FunPage')


        next_fun_button = tk.Button(self, text="move to next page", command=next_page,
                                    font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        next_fun_button.pack()



class MenuPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent,bg="black",)
        self.controlle = controller
        big_lable = tk.Label(self, text="WELCOME TO MY ATM", font=('Bernard MT Condensed', 50, 'bold'), fg="pink", bg="black")
        big_lable.pack(pady=30)

        def return_page():
            controller.show_frame('StartPage')
        return_button = tk.Button(self, text = "return to main page",command = return_page,font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black")
        return_button.pack(pady= 30)




        balance_lable = tk.Label(self, text="Enter your MONEY", font=('Bernard MT Condensed', 15, 'bold'),
                                 fg="pink", bg="black")
        balance_lable.pack()

        my_balance = tk.IntVar()
        balance_entry = tk.Entry(self, textvariable=my_balance, font=('Bernard MT Condensed', 15, 'bold'), fg="pink",
                                  bg="black")
        balance_entry.pack(pady=5)

        def get_balance():
            result_balance_lable['text'] = my_balance.get()

        result_balance_lable = tk.Label(self, font=('Bernard MT Condensed', 15, 'bold'),
                                        fg="pink", bg="black")
        result_balance_lable.pack(pady =5)

        balance_button = tk.Button(self, text="Check ur money", command=get_balance,
                                   font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        balance_button.pack(pady =5)

        cash_label = tk.Label(self, text="GET UR CASH", font=('Bernard MT Condensed', 15, 'bold'),
                              fg="pink", bg="black")
        cash_label.pack(pady =5)
        my_cash = tk.IntVar()
        cash_entry = tk.Entry(self, textvariable=my_cash, font=('Bernard MT Condensed', 15, 'bold'), fg="pink",
                              bg="black")
        cash_entry.pack(pady =5)
        money_charge = tk.IntVar()

        def get_cash():
            global new_cash
            global money_charge

            money_charge = int(my_cash.get()) * 0.05
            new_cash = int(my_balance.get()) - int(my_cash.get())- int(money_charge)
            cash_label['text'] = str(new_cash) + "Som"

            service_label_pr['text'] = ("Service charge 5%:") + str(money_charge)



        cash_label = tk.Label(self, font=('Bernard MT Condensed', 15, 'bold'),
                              fg="pink", bg="black")
        cash_label.pack(pady =5)



        service_label_pr = tk.Label(self, font=('Bernard MT Condensed', 10, 'bold'),
                                    fg="pink", bg="black")
        service_label_pr.pack(pady=5)

        cash_button = tk.Button(self, text="Check your balance", command=get_cash,
                                font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        cash_button.pack(pady =5)



        conversion_label = tk.Label(self, text="ONLINE CONVERSION = $", font=('Bernard MT Condensed', 15, 'bold'),
                                 fg="pink", bg="black")
        conversion_label.pack(pady=5)
        my_conversion = tk.IntVar()
        conversion_entry = tk.Entry(self, textvariable=my_conversion, font=('Bernard MT Condensed', 15, 'bold'), fg="pink",
                              bg="black")
        conversion_entry.pack(pady =5)

        def conversion():
            global som_usd
            som_usd = int(my_conversion.get())*11300
            conversion_label_2['text'] = som_usd

        conversion_label_2 = tk.Label(self, font=('Bernard MT Condensed', 15, 'bold'),
                                      fg="pink", bg="black")
        conversion_label_2.pack()


        conversion_button = tk.Button(self, text="Convert to SOM", command=conversion,
                                font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        conversion_button.pack(pady =5)



class FunPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent,bg="black",)
        self.controller = controller




        big_lable = tk.Label(self, text="WELCOME TO PAYMENT PAGE ", font=('Bernard MT Condensed', 50, 'bold'),
                             fg="pink", bg="black")
        big_lable.pack(pady=30)

        ucell_label = tk.Label(self, text="Pay for UCELL ", font=('Bernard MT Condensed', 15, 'bold'), fg="pink",
                               bg="black")
        big_lable.pack(pady=30)
        ucell_label.pack()
        ucell_pay = tk.IntVar()
        ucell_entry = tk.Entry(self, textvariable=ucell_pay, font=('Bernard MT Condensed', 15, 'bold'), fg="pink",
                               bg="black")
        ucell_entry.pack()
        def pay_ucell():
            global ucell_money
            ucell_money = my_new_balance - int(ucell_pay.get())
            ucell_pay_label['text'] = ucell_money

        ucell_pay_button = tk.Button(self, text="PAY", command=pay_ucell,
                                     font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        ucell_pay_button.pack()

        ucell_pay_label = tk.Label(self, font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black")
        big_lable.pack(pady=30)
        ucell_pay_label.pack()
        def next_page():
            controller.show_frame('MenuPage')

        next_fun_button = tk.Button(self, text="move to next page", command=next_page,
                                    font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        next_fun_button.pack()
        my_new_balance = 1000




        bonus_label = tk.Label(self, text = "bonus for u ", font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black")
        big_lable.pack(pady=30)
        bonus_label.pack()

        def get_bonus():
            global my_bonus
            ucell_money = int(my_new_balance.get()) + 3
            bonus_label_result['text'] = ucell_money

        bonus_label_result = tk.Label(self, font=('Bernard MT Condensed', 15, 'bold'),
                                          fg="pink", bg="black")
        bonus_label_result.pack()

        get_bonus_button = tk.Button(self, text="BONUS", command=get_bonus,
                                     font=('Bernard MT Condensed', 15, 'bold'), fg="pink", bg="black", width='25')
        get_bonus_button.pack()
























if __name__=="__main__":

    app = SampleAPP()

    app.mainloop()
















