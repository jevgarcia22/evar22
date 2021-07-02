from kivymd.app import MDApp
from kivy.lang import Builder

#to manually set windowsize for mobile - never push this to prod!!
from kivy.core.window import Window
Window.size = (300,500)

toolbar_helper = """
Screen:
	BoxLayout:
		orientation: "vertical"
		MDToolbar:
			title: "toolbar"
			left_action_items: [["menu", lambda x: app.navigation_draw()]]
			right_action_items: [["clock", lambda x: app.navigation_draw()]]
			elevation: 10
		MDLabel:
			text: "this is a label"
			halign: "center"
		MDBottomAppBar:
			MDToolbar:
				left_action_items: [["coffee", lambda x: app.navigation_draw()]]
				mode: "end"
				icon: "language-python"
				on_action_button: app.navigation_draw()
"""

class toolbarApp(MDApp):

	def build(self):
		self.theme_cls.primary_palette = "Red"
		screen = Builder.load_string(toolbar_helper)

		return screen

	def navigation_draw(self):
		print('navigation')


toolbarApp().run()