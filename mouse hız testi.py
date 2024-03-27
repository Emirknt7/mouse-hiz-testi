import tkinter as tk
import random
import winsound # burada windows için yapılmış bir bir ses kütüphanesi

class PanelGame:
    def __init__(self, root):
        self.root = root
        self.root.title("mouse hız testi")

        self.score = 0

        self.score_label = tk.Label(self.root, text="Skor: 0")
    
        self.score_label.pack()

        self.panels_frame = tk.Frame(self.root)
        self.panels_frame.pack()

        self.panels = []
        for i in range(4):
            row = []
            for j in range(4):
                panel = tk.Label(self.panels_frame, width=15, height=7, bg="gray", relief="raised", cursor="hand2")
                panel.grid(row=i, column=j, padx=5, pady=5)
                panel.bind("<Button-1>", self.panel_clicked)
                row.append(panel)
            self.panels.append(row)

        self.reset_button = tk.Button(self.root, text="Yeniden Başla", command=self.reset_game)
        self.reset_button.pack()

        self.root.geometry("600x600")  # Pencere boyutunu ayarla

        self.change_random_panel_color()

    def change_random_panel_color(self):
        random_row = random.randint(0, 3)
        random_column = random.randint(0, 3)
        self.panels[random_row][random_column].configure(bg="green")


        """SND_FILENAME	:Ses parametresi bir WAV dosyasının adıdır.
           SND_LOOP	:Sesi tekrar tekrar çal
           SND_MEMORY	:PlaySound()'un ses parametresi, bayt benzeri bir nesne olarak WAV dosyasının hafıza görüntüsüdür.
           SND_ASYNC	:Seslerin eşzamansız olarak çalınmasına izin vererek hemen geri dönün.
           SND_NODEFAULT	:Belirtilen ses bulunamazsa sistemin varsayılan sesini çalmayın.
           SND_NOSTOP	:O anda çalmakta olan sesleri kesmeyin."""
        winsound.PlaySound("click.wav", winsound.SND_ASYNC)  # Tıklama sesini çal


        self.root.after(2000, lambda: self.panels[random_row][random_column].configure(bg="gray"))

    def panel_clicked(self, event):
        clicked_panel = event.widget
        for i in range(4):
            for j in range(4):
                if self.panels[i][j] == clicked_panel and clicked_panel.cget("bg") == "green":
                    self.score += 1
                    self.score_label.config(text="Skor: " + str(self.score))
                    self.change_random_panel_color()
                    return

    def reset_game(self):
        self.score = 0
        self.score_label.config(text="Skor: 0")
        self.change_random_panel_color()

if __name__ == "__main__":
    root = tk.Tk()
    game = PanelGame(root)
    root.mainloop()
