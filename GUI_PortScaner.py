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

        List_settings = tk.Listbox(self)
        List_settings.insert(1,"List all current settings")
        List_settings.insert(2,"List all current settings")
        List_settings.place(relx=0, rely=.15, relwidth=.3, relheight=0.4)

        Scrollbar_for_Output_Feild = tk.Scrollbar(self)
        Scrollbar_for_Output_Feild.place(relx=.45, rely=.15, relwidth=.02, relheight=0.4)
        Output_Feild = tk.Listbox(self, yscrollcommand=Scrollbar_for_Output_Feild.set)
        Scrollbar_for_Output_Feild.config(command=Output_Feild.yview)
        x = 1
        while x <= 50:
            Output_Feild.insert(x,"Hello world {}".format(x))
            x=x+1
        Output_Feild.place(relx=.5, rely=.15, relwidth=.50, relheight=0.4)
   

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
