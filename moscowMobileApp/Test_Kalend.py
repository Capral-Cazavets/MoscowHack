from typing import Text
from kivy.lang.builder import Instruction
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivymd.uix.picker import MDDatePicker, MDThemePicker, get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase

Window.size = (400, 650)

class Kalendar(ScreenManager):
    pass



class Main(MDApp):
    def build(self):
        Builder.load_file("kalendar.kv")
        return Kalendar()

    def on_save(self, instance, value, date_range):

        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker(primary_color=get_color_from_hex("#cf2317"),
        selector_color=get_color_from_hex("#e93f39"),
        text_toolbar_color=get_color_from_hex("#cccccc"),
        
        input_field_text_color=(.81,.14,.09,1),
        text_current_color=get_color_from_hex("#e93f39"), 
        text_button_color=(1,0,0,1))
        
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    
    


Main().run()