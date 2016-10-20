from kivy.app import App
from kivy.uix.widget import Widget


class TictactoeGame(Widget):
    pass


class TictactoeApp(App):
    def build(self):
        return TictactoeGame()


if __name__ == '__main__':
    TictactoeApp().run()