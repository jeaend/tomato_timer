import rumps

class TomatoTimer(rumps.App):
    def __init__(self):
        super().__init__("🍅")
        self.menu = ["Start"]

    @rumps.clicked("Start")
    def start_timer(self, _):
        print("Start clicked")

if __name__ == "__main__":
    TomatoTimer().run()