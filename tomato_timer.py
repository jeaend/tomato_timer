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

    def on_tick(self, _):
        print("tick")

    @rumps.clicked("Start Tomato")
    def start_tomato(self, _):
        print("Start Tomato")
        self.timer.start()


    @rumps.clicked("Start Break")
    def start_break(self, _):
        print("Pause clicked")
        
    @rumps.clicked("Pause")
    def pause(self, _):
        print("Pause")    

if __name__ == "__main__":
    TomatoTimer().run()