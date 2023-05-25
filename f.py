# не забудь імпортувати необхідні елементи!
from kivy.app import *
from kivy.uix.label import *
from kivy.uix.button import *
from kivy.uix.textinput import *
from kivy.uix.boxlayout import *
from kivy.uix.screenmanager import *
from kivy.uix.scrollview import *

class ScrButton(Button):
	def __init__(self, screen, direction = "right", goal="main", **kwargs):
		super().__init__(**kwargs)
		self.screen = screen
		self.direction = direction
		self.goal = goal
	def on_press(self):
		self.screen.manager.transition.direction = self.direction
		self.screen.manager.current = self.goal

class MainScr(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		vl = BoxLayout(orientation="vertical", padding = 8, spacing = 8)
		hl = BoxLayout()
		txt = Label(text="Вибери екран")
		vl.add_widget(ScrButton(self, direction="down", goal="first", text="1"))
		vl.add_widget(ScrButton(self, direction="left", goal="second", text="2"))
		vl.add_widget(ScrButton(self, direction="up", goal="third", text="3"))
		vl.add_widget(ScrButton(self, direction="right", goal="fourth", text="4"))
		hl.add_widget(txt)
		hl.add_widget(vl)
		self.add_widget(hl)

class FirstScr(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		vl = BoxLayout(orientation = "vertical", size_hint = (.5, .5), pos_hint = {"center_x":0.5, "center_y":0.5})
		btn = Button(text="Вибір: 1", size_hint = (.5, 1), pos_hint = {"left":0})
		btn_back = ScrButton(self, direction="up", goal="main", text="Назад", size_hint = (.5, 1), pos_hint = {"right":1})
		vl.add_widget(btn)
		vl.add_widget(btn_back)
		self.add_widget(vl)

class SecondScr(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		vl = BoxLayout(orientation = "vertical")
		self.txt = Label(text = "Вибір: 2")
		vl.add_widget(self.txt)

		hl_0 = BoxLayout(size_hint = (0.8, None), height = "30sp")
		lbl1 = Label(text = "Введіть пароль:", halign = "right")
		self.input = TextInput(multiline = False)
		hl_0.add_widget(lbl1)
		hl_0.add_widget(self.input)
		vl.add_widget(hl_0)

		hl = BoxLayout(size_hint = (0.5, 0.2), pos_hint = {"center_x":0.5})
		btn_false = Button(text = "OK!")
		btn_back = ScrButton(self, direction="right", goal="main", text="Назад")
		hl.add_widget(btn_false)
		hl.add_widget(btn_back)
		vl.add_widget(hl)
		self.add_widget(vl)
		btn_false.on_press = self.change_text
	def change_text(self):
		self.txt.text = self.input.text + "? Не спрацювало ..."

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.txt = Label(text = "Твій власний екран")
        layout.add_widget(self.txt)
        hl_0 = BoxLayout(size_hint = (0.8, None), height = "30sp")
        lbl1 = Label(text = "Ваша відповідь:", halign = "right")
        self.input = TextInput(multiline = False)
        hl_0.add_widget(lbl1)
        hl_0.add_widget(self.input)
        layout.add_widget(hl_0)
        hl = BoxLayout(size_hint = (0.5, 0.2), pos_hint = {"center_x":0.5})
        btn_false = Button(text = "OK!")
        btn_back = ScrButton(self, direction="right", goal="main", text="Назад")
        hl.add_widget(btn_false)
        hl.add_widget(btn_back)
        layout.add_widget(hl)
        self.add_widget(layout)
        btn_false.on_press = self.change_text
    def change_text(self):
        if self.input == 'добре':
            self.txt.text = "Оо я рада це чути!)"
        elif self.input == 'не дуже':
            self.txt.text = "Хмм...  Може теплий чай з солодким і фільм(тільки веселий) допоможуть підняти настрій?🤔"
        elif self.input == 'погано':
            self.txt.text = "Так собі новина. Може тоді піти з друзями до кафе чи влаштувати собі відпустку за кордоном?🙃"
        else:
            self.txt.text = "Не розумію. Спробуй використати 'добре'; 'не дуже'; 'погано'"

class FourthScr(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		vl = BoxLayout()
		btn_back = ScrButton(self, direction="left", goal="main", text="Назад")
		vl.add_widget(btn_back)
		self.add_widget(vl)

class MyApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MainScr(name="main"))
		sm.add_widget(FirstScr(name="first"))
		sm.add_widget(SecondScr(name="second"))
		sm.add_widget(ThirdScr(name="third"))
		sm.add_widget(FourthScr(name="fourth"))
		return sm

MyApp().run()
