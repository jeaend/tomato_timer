import rumps 


class TomatoApp(object):
    def __init__(self):
        self.app = rumps.App("Tomato_Timer", "🍅")
 
    def run(self):
        self.app.run()
 
if __name__ == '__main__':
    app = TomatoApp()
    app.run()