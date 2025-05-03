import customtkinter as ctk
import random
import time
import threading

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class ReactionTestApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Тест на реакцію")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Натисни 'Почати' і чекай...", font=ctk.CTkFont(size=18))
        self.label.pack(pady=20)

        self.start_button = ctk.CTkButton(self, text="Почати", command=self.start_test)
        self.start_button.pack(pady=10)

        self.react_button = ctk.CTkButton(self, text="НАТИСКАЙ!", command=self.reacted, state="disabled")
        self.react_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=16))
        self.result_label.pack(pady=20)

        self.start_time = None

    def start_test(self):
        self.result_label.configure(text="")
        self.react_button.configure(state="disabled")
        self.label.configure(text="Чекай сигналу...")
        self.after(100, lambda: threading.Thread(target=self.wait_and_show).start())

    def wait_and_show(self):
        time.sleep(random.uniform(2, 5))
        self.start_time = time.time()
        self.label.configure(text="НАТИСКАЙ!")
        self.react_button.configure(state="normal")

    def reacted(self):
        if self.start_time:
            reaction_time = round((time.time() - self.start_time) * 1000, 2)
            self.result_label.configure(text=f"Твоя реакція: {reaction_time} мс")
            self.label.configure(text="Натисни 'Почати', щоб спробувати знову")
            self.react_button.configure(state="disabled")
            self.start_time = None

if __name__ == "__main__":
    app = ReactionTestApp()
    app.mainloop()