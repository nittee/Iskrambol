from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup


class PlayScreen(Screen):
    def show_pause_popup(self):
        global pausePopup
        pausePopup = Popup(title="Pause", content=PauseWindow(), size_hint=(0.8,0.6))
        pausePopup.open()


class PauseWindow(Screen):
    def close_pause_popup(self):
        pausePopup.dismiss()
