import kivy
from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class main_screen(App):
    def build(self):
        lbl = Label(text="TrackurBrain", pos_hint={'center_x': 0.5,
                                                   'center_y': 0.96})

        btn = Button(text="Push Me !",
                     font_size="20sp",
                     background_color=(1, 1, 1, 1),
                     color=(1, 1, 1, 1),
                     size=(32, 32),
                     size_hint=(.2, .2),
                     pos=(300, 250))

        return lbl

label = main_screen()
label.run()
button = main_screen()
button.run()