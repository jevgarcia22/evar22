screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    MDLabel: 
        text: 'hello world'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    MDLabel: 
        text: 'hello upload world'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'
"""