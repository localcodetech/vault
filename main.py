

import customtkinter as ctk

from app.ui.signup_screen import SignupScreen


class VaultApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1500x1500")
        self.title("VaultLane Password Manager")



        self.current_frame = None

        self.show_frame(SignupScreen)



    def show_frame(self, page_class):

        if self.current_frame is not None:
            self.current_frame.destroy()
        
        self.current_frame = page_class(root=self, controller=self)







if __name__ == "__main__":
    app = VaultApp()
    app.mainloop()