####
#### Port Scanner With GUI
#### Author: Roberto Rodriguez
#### Co Author: Bianca Rodriguez (Helped With Research and Programming first Starting GUI)
#### 


from tkinter import *
import tkinter as tk

Color_of_choice="#b6c4bf"
button_color="#dedede"

class Top(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "Port Scanner")
        self.geometry("480x500")

        Container = tk.Frame(self)
        Container.pack(side="top", fill="both", expand=True)
        Container.grid_rowconfigure(0, weight=1)
        Container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Main_page, Protocol, Ip_Address, Ports, Web_Server, Timeout, Helper):

            frame = F(Container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main_page)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        
        Go_To_Main = tk.Button(self, text="Main",bg=Color_of_choice , command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Protocol = tk.Button(self, text="Protocol", command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)
        
        Help = tk.Button(self, text="Help", command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)


        Start = tk.Button(self, text="Start", bg=button_color)
        Start.place(relx=0, rely=.90, relwidth=.30, relheight=0.1)

        Stop = tk.Button(self, text="Stop", bg=button_color)
        Stop.place(relx=.70, rely=.90, relwidth=.30, relheight=0.1)

        Scrollbar_for_List_Settings = tk.Scrollbar(self)
        Scrollbar_for_List_Settings.place(relx=.0, rely=.15, relwidth=.02, relheight=0.4)
        List_settings = tk.Listbox(self, yscrollcommand=Scrollbar_for_List_Settings.set)
        List_settings.insert(1,"List all current settings")
        List_settings.insert(2,"List all current settings")
        List_settings.place(relx=.03, rely=.15, relwidth=.3, relheight=0.4)
        Scrollbar_for_List_Settings.config(command=List_settings.yview)

        Scrollbar_for_Output_Feild = tk.Scrollbar(self)
        Scrollbar_for_Output_Feild.place(relx=.40, rely=.15, relwidth=.02, relheight=0.4)
        Output_Feild = tk.Listbox(self, yscrollcommand=Scrollbar_for_Output_Feild.set)
        Output_Feild.insert(1,"Display All ports for different ips")
        Output_Feild.insert(2,"Display All ports for different ips")
        Output_Feild.place(relx=.43, rely=.15, relwidth=.55, relheight=0.4)
        Scrollbar_for_Output_Feild.config(command=Output_Feild.yview)
   

class Protocol(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Go_To_Main = tk.Button(self, text="Main", command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)

        Go_To_Protocol = tk.Button(self, text="Protocol", bg=Color_of_choice, command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)
        
        Help = tk.Button(self, text="Help", command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)

        CheckVar1=IntVar()
        CheckVar2=IntVar()

        TCP = Checkbutton(self, text="TCP", variable=CheckVar1, onvalue=1, offvalue=0)
        TCP.place(relx=0, rely=.40, relwidth=.10, relheight=.10)
        UDP = Checkbutton(self, text="UDP", variable=CheckVar2, onvalue=1, offvalue=0)
        UDP.place(relx=0, rely=.60, relwidth=.10, relheight=.10)

class Ip_Address(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Go_To_Main = tk.Button(self, text="Main", command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)

        Go_To_Protocol = tk.Button(self, text="Protocol", command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", bg=Color_of_choice, command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)
        
        Help = tk.Button(self, text="help", command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)

        Ip_Entry = Text(self)
        Ip_Entry.place(relx=.10, rely=.10, relwidth=.80, relheight=.60)

        File_Ipaddress = tk.Button(self, text="File")
        File_Ipaddress.place(relx=.10, rely=.70, relwidth=.15, relheight=.05)

class Ports(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Go_To_Main = tk.Button(self, text="Main", command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Protocol = tk.Button(self, text="Protocol", command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", bg=Color_of_choice, command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)
        
        Help = tk.Button(self, text="Help", command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)

        Port_Entry = Text(self)
        Port_Entry.place(relx=.10, rely=.10, relwidth=.80, relheight=.60)

        File_Ports = tk.Button(self, text="File")
        File_Ports.place(relx=.10, rely=.70, relwidth=.15, relheight=.05)

class Web_Server(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Go_To_Main = tk.Button(self, text="Main", command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Protocol = tk.Button(self, text="Protocol", command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", bg=Color_of_choice, command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)
        
        Help = tk.Button(self, text="Help", command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)

        CheckVar3=IntVar()
        CheckVar4=IntVar()
        CheckVar5=IntVar()
        CheckVar6=IntVar()
        CheckVar7=IntVar()
        
        Finger_print = Checkbutton(self, text="Finger Print     ", variable=CheckVar3, onvalue=1, offvalue=0)
        Finger_print.place(relx=0, rely=.10,)
        
        Status_code = Checkbutton(self, text="Status Code      ", variable=CheckVar4, onvalue=1, offvalue=0)
        Status_code.place(relx=0, rely=.20,)
        
        Title_page = Checkbutton(self, text="Title Page       ", variable=CheckVar5, onvalue=1, offvalue=0)
        Title_page.place(relx=0, rely=.30,)
        
        Type_Of_Page = Checkbutton(self, text="Type Of Page     ", variable=CheckVar6, onvalue=1, offvalue=0)
        Type_Of_Page.place(relx=0, rely=.40,)
        
        Version_Of_Server = Checkbutton(self, text="Version Of Server", variable=CheckVar7, onvalue=1, offvalue=0)
        Version_Of_Server.place(relx=0, rely=.50,)

class Timeout(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Go_To_Main = tk.Button(self, text="Main", command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Protocol = tk.Button(self, text="Protocol", command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", bg=Color_of_choice, command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)
        
        Help = tk.Button(self, text="Help", command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)

        CheckVar8=IntVar()

        Choose_your_own = Radiobutton(self, text="Choose_your_own", variable=CheckVar8, value=1)
        Choose_your_own.place(relx=.0, rely=.10)

        Slow = Radiobutton(self, text="Slow", variable=CheckVar8, value=2)
        Slow.place(relx=.0, rely=.20)

        Medium = Radiobutton(self, text="Medium", variable=CheckVar8, value=3)
        Medium.place(relx=.0, rely=.30)

        Fast = Radiobutton(self, text="Fast", variable=CheckVar8, value=5)
        Fast.place(relx=.0, rely=.40)

        Want_to_get_caught = Radiobutton(self, text="Want_to_get_caught", variable=CheckVar8, value=6)
        Want_to_get_caught.place(relx=.0, rely=.50)

        User_choice = Spinbox(self, from_=0, to=10000, textvariable="Number in millisec")
        User_choice.place(relx=.30, rely=.10, relwidth=.20, relheight=.05)

class Helper(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Go_To_Main = tk.Button(self, text="Main", command=lambda: controller.show_frame(Main_page))
        Go_To_Main.place(relx=0, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Protocol = tk.Button(self, text="Protocol", command=lambda: controller.show_frame(Protocol))
        Go_To_Protocol.place(relx=.15, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ip_Address = tk.Button(self, text="Ip_Address", command=lambda: controller.show_frame(Ip_Address))
        Go_To_Ip_Address.place(relx=.30, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Ports = tk.Button(self, text="Ports", command=lambda: controller.show_frame(Ports))
        Go_To_Ports.place(relx=.45, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Web_Server = tk.Button(self, text="Web_Server", command=lambda: controller.show_frame(Web_Server))
        Go_To_Web_Server.place(relx=.60, rely=0, relwidth=.15, relheight=.05)
        
        Go_To_Timeout = tk.Button(self, text="Timeout", command=lambda: controller.show_frame(Timeout))
        Go_To_Timeout.place(relx=.75, rely=0, relwidth=.15, relheight=.05)

        Help = tk.Button(self, text="Help", bg=Color_of_choice, command=lambda: controller.show_frame(Helper))
        Help.place(relx=.90, rely=0, relwidth=.10, relheight=.05)

applacation = Top()
applacation.mainloop()
