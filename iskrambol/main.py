import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.config import Config

from kivy.uix.boxlayout import BoxLayout

# screen size are based on Galaxy S20 (most common screen size for mobile)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 800)


class MainPage(BoxLayout):
    pass


class Iskrambol(App):
    
    def build(self):
        root = MainPage()
        return root


if __name__ == '__main__':
    Iskrambol().run()
