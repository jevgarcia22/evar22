from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from screen_manager_helper import screen_helper

Window.size = (300, 500)

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

screen_manager = ScreenManager()
screen_manager.add_widget(MenuScreen(name='menu'))
screen_manager.add_widget(ProfileScreen(name='profile'))
screen_manager.add_widget(ProfileScreen(name='upload'))

class changeScreens(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

changeScreens().run()