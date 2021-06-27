from kivymd.app import MDApp
from kivy.lang import Builder

# from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, TwoLineIconListItem, IconLeftWidget
# from kivy.uix.scrollview import ScrollView

list_helper = """
Screen:
	ScrollView:
		MDList:
			id: container
"""

class ListApp(MDApp):
	def build(self):

		screen = Builder.load_string(list_helper)

# ---- not using builder method ---- #
		# screen = Screen()

		# scroll = ScrollView()
		# list_view = MDList()

		#add list view to scroll
		# scroll.add_widget(list_view)

		# #create a list of items
		# for i in range(20):
		# 	# items = OneLineListItem(text="Item " + str(i))
		# 	# items = TwoLineListItem(text="Item " + str(i), secondary_text='2nd line text')
		# 	# items = ThreeLineListItem(text="Item " + str(i), secondary_text='2nd line text',
		# 	# 							tertiary_text='third row seating')

		# 	#to add icon to 3 list item
		# 	icon = IconLeftWidget(icon="headphones")
		# 	items = TwoLineIconListItem(text="Item " + str(i), secondary_text='2nd line text')
			
		# 	#add icon to list items
		# 	items.add_widget(icon)

		# 	#add list items to list view
		# 	list_view.add_widget(items)

		# #add scroll(scroll has list_view, list_view has list items) to screen
		# screen.add_widget(scroll)

		return screen

	def on_start(self):
		for i in range(20):
			items = TwoLineListItem(text='Item: ' + str(i), secondary_text='2nd line text')
			#this grabs the value of container from id from root
			self.root.ids.container.add_widget(items)


ListApp().run()









