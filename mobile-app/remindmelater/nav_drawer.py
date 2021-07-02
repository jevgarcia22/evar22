from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.navigationdrawer import MDNavigationLayout

Window.size = (300, 500)

navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                Image:
                    source: 'evil_homer.png'
                MDLabel:
                    text: '   Remind Me Later!'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: '   Help'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Help?'
                            IconLeftWidget:
                                icon: 'dog'
                        OneLineIconListItem:
                            text: 'Logout'
                            IconLeftWidget:
                                icon: 'logout'
"""


class navDrawerApp(MDApp):

    def build(self):
        screen = Builder.load_string(navigation_helper)
        return screen


navDrawerApp().run()