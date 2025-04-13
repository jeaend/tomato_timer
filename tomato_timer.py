import rumps

class TomatoTimer(rumps.App):
    def __init__(self):
        super().__init__("🍅")
        self.menu = [
            "Start Tomato",
            "Start Break",
            "Pause / Resume",
            None        
            ]
    
        self.timer = rumps.Timer(self.on_tick, 1)
        self.remaining = 0
        self.running = False
        self.tomato_active = False
        self.break_active = False

    def on_tick(self, _):
        if self.remaining > 0:
            self.remaining -= 1
            mins = self.remaining // 60
            secs = self.remaining % 60
            print(f"{mins:02}:{secs:02}")
        else:
            self.timer.stop()
            self.running = False
            self.tomato_active = False
            self.break_active = False
            print("Timer done")

    # 25 minutes
    @rumps.clicked("Start Tomato")
    def start_tomato(self, _):
        if not self.tomato_active:
            print("Start Tomato")
            self.remaining = 25 * 60  
            self.tomato_active = True
            self.break_active = False
        else:  
            print("Resume Tomato")

        self.running = True    
        self.timer.start()

    # 5 minutes
    @rumps.clicked("Start Break")
    def start_break(self, _):
        if not self.break_active:
            print("Starting break")
            self.remaining = 5 * 60
            self.break_active = True
            self.tomato_active = False
        else:
            print("Resuming break")

    @rumps.clicked("Pause / Resume")
    def pause(self, _):
        if self.running:
            print("Pause") 
            self.timer.stop()
            self.running = False
        else:
            if self.tomato_active or self.break_active:       
                print("Resumed")
                self.timer.start()
                self.running = True
            else:
                print("Nothing to resume")

if __name__ == "__main__":
    TomatoTimer().run()