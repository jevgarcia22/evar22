#these helpers use the Builder method
#MDTextField is auto imported, no need to import in the app code
#all the same attributes are given the same as if defining in the app code
txt_input_helper= """
MDTextField:
	hint_text: "What do you want to remember?"
	helper_text: "Enter some words"
	helper_text_mode: "on_focus"
	icon_right: "head-question"
	icon_right_color: app.theme_cls.primary_color
	pos_hint:{'center_x':0.5, 'center_y':0.5}
	size_hint_x:None
	width:550
"""