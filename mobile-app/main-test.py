from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
# from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder #can use Builder instead of MDTextField
from helpers import txt_input_helper

from kivymd.uix.dialog import MDDialog #for dialog

class ReminderApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Indigo"
		self.theme_cls.primary_hue = "100"
		self.theme_cls.theme_style= "Dark"

		screen = Screen()

		label = MDLabel(text='title', 
						halign='center', 
						theme_text_color="Custom",
						text_color=(0,0,1,1),
						font_style="H2")

		icon_label = MDIcon(icon='language-python', halign='center')

		
		button1 = MDRectangleFlatButton(text='Save', 
								pos_hint={'center_x':0.5, 'center_y':0.4},
								on_release=self.show_data)

		icon_btn = MDIconButton(icon='android',
								pos_hint={'center_x':0.5, 'center_y':0.2})

		action_btn = MDFloatingActionButton(icon='language-python',
											pos_hint={'center_x':0.5, 'center_y':0.1})

# -- this uses MDTextField instead of Builder method -- #
		# txt_input = MDTextField(text='enter text',
		# 						pos_hint={'center_x':0.5, 'center_y':0.5},
		# 						size_hint_x=None, width=300)

# -- this uses the Builder method -- #
		self.txt_input = Builder.load_string(txt_input_helper)

		# screen.add_widget(label)
		# screen.add_widget(icon_label)
		screen.add_widget(button1)
		# screen.add_widget(icon_btn)
		screen.add_widget(action_btn)
		screen.add_widget(self.txt_input)

		return screen

	def show_data(self, obj):
		if self.txt_input.text is "":
			check_string = "No text found! Enter something to remember"
		else:
			check_string = 'data saved'
		close_btn = MDFlatButton(text='close', on_release=self.close_btn)
		more_btn = MDFlatButton(text='more')
		self.dialog = MDDialog(title="success!",text=check_string,
						size_hint=(0.7, 1),
						buttons=[close_btn, more_btn])
		self.dialog.open()

	def close_btn(self, obj):
		self.dialog.dismiss()


ReminderApp().run()









