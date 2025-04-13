import rumps

class TomatoTimer(rumps.App):
    def __init__(self):
        super().__init__("🍅")
        self.menu = [
            "Start Tomato",
            "Start Break",
            "Pause",
            None        
            ]
    
        self.timer = rumps.Timer(self.on_tick, 1)
        self.remaining = 0

    def on_tick(self, _):
        if self.remaining > 0:
            self.remaining -= 1
            mins = self.remaining // 60
            secs = self.remaining % 60
            print(f"{mins:02}:{secs:02}")
        else:
            self.timer.stop()
            print("Timer done")

    # 25 minutes
    @rumps.clicked("Start Tomato")
    def start_tomato(self, _):
        print("Start Tomato")
        self.remaining = 25 * 60  
        self.timer.start()

    # 5 minutes
    @rumps.clicked("Start Break")
    def start_break(self, _):
        print("Pause clicked")
        self.remaining = 5 * 60  
        self.timer.start()

    @rumps.clicked("Pause")
    def pause(self, _):
        print("Pause")                   
        self.timer.pause()

if __name__ == "__main__":
    TomatoTimer().run()