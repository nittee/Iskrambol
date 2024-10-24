import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from playscreen import PlayScreen

# screen size are based on Galaxy S20 (most common screen size for mobile)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 800)


def load_kv_files():
    Builder.load_file('iskrambol.kv')
    Builder.load_file('playscreen.kv')
    Builder.load_file('modesscreen.kv')
    Builder.load_file('aboutscreen.kv')


class WindowManager(ScreenManager):
    """Required class for window navigation."""
    pass


# screens:
class MainScreen(Screen):
    """Main menu screen."""
    pass


PlayScreen()


class ModesScreen(Screen):
    pass


class AboutScreen(Screen):
    pass


class IskrambolApp(App):
    """
    App object.
    """


    def build(self):

        screen_manager = WindowManager()
        screens = [
            MainScreen(name='main_screen'),
            PlayScreen(name='play_screen'),
            ModesScreen(name='modes_screen'),
            AboutScreen(name='about_screen')
        ]

        for screen in screens:
            screen_manager.add_widget(screen)

        screen_manager.current = 'main_screen'

        return screen_manager


if __name__ == '__main__':
    load_kv_files()
    IskrambolApp().run()
