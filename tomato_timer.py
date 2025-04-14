import rumps
import subprocess

def play_sound(path):
    subprocess.run(["afplay", path])

class Tomato_Timer(rumps.App):
    def __init__(self):
        super().__init__("🍅")
        self.pause_resume_item = rumps.MenuItem("Pause", callback=self.pause)

        self.menu = [
            "Start Tomato",
            "Start Break",
            self.pause_resume_item,
            None
        ]
    
        self.timer = rumps.Timer(self.on_second, 1)
        self.remaining = 0
        self.running = False
        self.tomato_active = False
        self.break_active = False

    def on_second(self, _):
        if self.remaining > 0:
            self.remaining -= 1
            self.update_title()
        else:
            self.timer.stop()
            self.running = False

            if self.tomato_active:
                play_sound("/System/Library/Sounds/Hero.aiff")
                self.title = "🍅 Done! 🍅"
            elif self.break_active:
                play_sound("/System/Library/Sounds/Purr.aiff")
                self.title = "☕ Done! ☕"

            self.tomato_active = False
            self.break_active = False
            self.pause_resume_item.title = "Pause"

    def update_title(self):
        mins, secs = divmod(self.remaining, 60)
        label = "🍅" if self.tomato_active else "☕"
        self.title = f"{label} {mins:02}:{secs:02} {label}"

    @rumps.clicked("Start Tomato")
    def start_tomato(self, _):
        if not self.tomato_active:
            print("Start Tomato")
            self.remaining = 25 * 60
            self.tomato_active = True
            self.break_active = False
            self.pause_resume_item.title = "Pause"
        
        self.update_title()
        self.running = True
        self.pause_resume_item.set_callback(self.pause)
        self.timer.start()

    @rumps.clicked("Start Break")
    def start_break(self, _):
        if not self.break_active:
            print("Starting break")
            self.remaining = 5 * 60
            self.break_active = True
            self.tomato_active = False
            self.pause_resume_item.title = "Pause"
        
        self.update_title()
        self.running = True
        self.pause_resume_item.set_callback(self.pause)
        self.timer.start()

    def pause(self, _):
        if self.running:
            print("Pause")
            self.timer.stop()
            self.running = False
            self.pause_resume_item.title = "Resume"
        else:
            if self.tomato_active or self.break_active:
                print("Resumed")
                self.timer.start()
                self.running = True
                self.pause_resume_item.title = "Pause"
            else:
                print("Nothing to resume")

if __name__ == "__main__":
    Tomato_Timer().run()
