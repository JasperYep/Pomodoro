import rumps
import time

class PomodoroApp(rumps.App):
    def __init__(self):
        super().__init__("🍅")
        self.timer = rumps.Timer(self.on_tick, 1)
        self.time_left = 25 * 60  # 25 分钟
        self.running = False
        self.button = rumps.MenuItem("Start", callback=self.start_stop)
        self.menu = [self.button]

    def on_tick(self, sender):
        self.time_left -= 1
        mins, secs = divmod(self.time_left, 60)
        self.title = f"{mins:02d}:{secs:02d}"
        if self.time_left <= 0:
            self.timer.stop()
            self.running = False
            self.button.title = "Start"
            rumps.notification("Pomodoro", "Time's Up!", "Have a rest 🧘")
            self.time_left = 25 * 60
            self.title = "🍅"

    def start_stop(self, sender):
        if self.running:
            self.timer.stop()
            self.button.title = "Start"
        else:
            self.timer.start()
            self.button.title = "Pause"
        self.running = not self.running

if __name__ == "__main__":
    PomodoroApp().run()
