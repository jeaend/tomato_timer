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

    @rumps.clicked("Start Tomato")
    def start_tomato(self, _):
        print("Start Tomato")

    @rumps.clicked("Start Break")
    def start_break(self, _):
        print("Pause clicked")
        
    @rumps.clicked("Pause")
    def pause(self, _):
        print("Pause")    

if __name__ == "__main__":
    TomatoTimer().run()