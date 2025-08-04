import time
import tkinter as tk
import threading

class PomodoroApp:

    def __init__(self, root):
        self.root = root
        self.root.title("🍅 Pomodoro Timer")

        self.timer_label = tk.Label(root, text="25:00", font=("Helvetica", 48))
        self.timer_label.pack(pady=20)

        self.status_label = tk.Label(root,
                                     text="Siap untuk mulai",
                                     font=("Helvetica", 14))
        self.status_label.pack()

        self.start_button = tk.Button(root,
                                      text="Mulai",
                                      command=self.mulai_timer)
        self.start_button.pack(pady=10)

        self.reset_button = tk.Button(root,
                                      text="Reset",
                                      command=self.reset_timer)
        self.reset_button.pack(pady=5)

        self.siklus = 0
        self.timer_running = False

    def mulai_timer(self):
        if not self.timer_running:
            self.timer_running = True
            thread = threading.Thread(target=self.jalankan_siklus)
            thread.start()

    def reset_timer(self):
        self.timer_running = False
        self.siklus = 0
        self.timer_label.config(text="25:00")
        self.update_status("⏹️ Direset. Siap untuk mulai.")

    def jalankan_siklus(self):
        while self.siklus < 4 and self.timer_running:
            self.update_status(f"Fokus ke-{self.siklus + 1}")
            self.hitung_mundur(25 * 60)

            if not self.timer_running:
                break  # keluar kalau sudah di-reset

            if self.siklus < 3:
                self.update_status("Istirahat pendek (5 menit)")
                self.hitung_mundur(5 * 60)
            else:
                self.update_status("Istirahat panjang (15 menit)")
                self.hitung_mundur(15 * 60)

            self.siklus += 1

        if self.timer_running:
            self.update_status("🎉 Semua sesi selesai!")

        self.timer_running = False

    def hitung_mundur(self, detik):
        while detik >= 0 and self.timer_running:
            menit, sisa = divmod(detik, 60)
            self.timer_label.config(text=f"{menit:02}:{sisa:02}")
            time.sleep(1)
            detik -= 1
            self.root.update()

    def update_status(self, teks):
        self.status_label.config(text=teks)
        self.root.update()

# Jalankan GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()
