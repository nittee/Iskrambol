import kivy
kivy.require('2.3.0')

from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.core.window import Window

from functions.playscreen import PlayScreen

# screen size are based on Galaxy S20 (most common screen size for mobile)
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', 360)
Config.set('graphics', 'height', 800)


def load_kv_files():
    kv_path = "./ui/"
    kv_files = [
        'iskrambol.kv',
        'playscreen.kv', 
        'modesscreen.kv', 
        'aboutscreen.kv', 
        'settingscreen.kv', 
        'accountscreen.kv',
    ]
    
    for file in kv_files:
        Builder.load_file(kv_path + file)


class WindowManager(ScreenManager):
    """Required class for window navigation."""
    pass


# screens:
class MainScreen(Screen):
    """Main menu screen."""
    def show_exit_popup(self):
        show = ExitWindow()
        global exitPopup
        exitPopup = Popup(title="Exit", content=show, size_hint=(0.8,0.6))
        exitPopup.open()


class ModesScreen(Screen):
    pass

class AboutScreen(Screen):
    pass


class ExitWindow(Screen):
    def close_exit_popup(self):
        exitPopup.dismiss()


class SettingScreen(Screen):
    pass

class AccountScreen(Screen):
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
            AboutScreen(name='about_screen'),
            SettingScreen(name='setting_screen'),
            AccountScreen(name='account_screen')
        ]

        for screen in screens:
            screen_manager.add_widget(screen)

        screen_manager.current = 'main_screen'

        return screen_manager
    

    def close_application(self):
        App.get_running_app().stop()
        Window.close()


if __name__ == '__main__':
    load_kv_files()
    IskrambolApp().run()
