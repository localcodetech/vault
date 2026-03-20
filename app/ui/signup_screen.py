

import customtkinter as ctk

from CTkMessagebox import CTkMessagebox

from ..utils.apptheme import ThemeWidget



class SignupScreen(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color=ThemeWidget.default)
        self.controller = controller
        self.pack(fill="both", expand=1)

        self.columnconfigure(0, weight=1)


        self.signup_label = ctk.CTkLabel(master=self,
                                         text="Sign up",
                                         font=ThemeWidget.signupfont)
        self.signup_label.grid(row=0, column=0, sticky="news", pady=(120,20))

        self.firstname_label = ctk.CTkLabel(master=self, 
                                            text="First Name",
                                            font=ThemeWidget.signuplabeltexts)
        self.firstname_label.grid(row=1, column=0, pady=(20,5))

        self.firstname_entry = ctk.CTkEntry(master=self,
                                            width=300, 
                                            height=40,
                                            fg_color="#ffffff",
                                            placeholder_text="first name")
        self.firstname_entry.grid(row=2, column=0, pady=(5,30))



        self.lastname_label = ctk.CTkLabel(master=self, 
                                            text="Last Name",
                                            font=ThemeWidget.signuplabeltexts)
        self.lastname_label.grid(row=3, column=0, pady=(20,5))

        self.lastname_entry = ctk.CTkEntry(master=self,
                                            width=300, 
                                            height=40,
                                            fg_color="#ffffff",
                                            placeholder_text="last name")
        self.lastname_entry.grid(row=4, column=0, pady=(5,30))



        self.username_label = ctk.CTkLabel(master=self, 
                                            text="username",
                                            font=ThemeWidget.signuplabeltexts)
        self.username_label.grid(row=5, column=0, pady=(20,5))

        self.username_entry = ctk.CTkEntry(master=self,
                                            width=300, 
                                            height=40,
                                            fg_color="#ffffff",
                                            placeholder_text="username")
        self.username_entry.grid(row=6, column=0, pady=(5,30))
        
        
