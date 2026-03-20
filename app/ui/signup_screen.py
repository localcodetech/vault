

import customtkinter as ctk

from CTkMessagebox import CTkMessagebox

from ..utils.apptheme import ThemeWidget



class SignupScreen(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root, fg_color=ThemeWidget.default)
        self.controller = controller
        self.pack(fill="both", expand=1)


        

        