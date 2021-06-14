from typing import Text
from kivy.lang.builder import Instruction
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.uix.swiper import MDSwiper,MDSwiperItem
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.list import MDList,TwoLineAvatarListItem
import requests

from kivymd.uix.picker import MDDatePicker, MDThemePicker, get_color_from_hex
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase
Window.size = (450, 700)

class MyItem(MDList):
    source = StringProperty()
    text = StringProperty()
    pass
class MySwip(MDSwiperItem):
    source = StringProperty()
    text = StringProperty()
    pass
class One_Screen(ScreenManager):
    def on_start(self, **kwargs):
        rows = [i for i in self.ids.swip.get_items()]
        for row1 in rows:
            if isinstance(row1, MySwip):
                self.ids.swip.remove_widget(row1)
        top = requests.get('http://178.170.242.221:8000',params={'near':"loc"})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,4):
            widget =  MySwip()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            self.ids.swip.add_widget(widget,0)
        top = requests.get('http://178.170.242.221:8000',params={'id':"1234"})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,4):
            widget =  MySwip()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            self.ids.list.add_widget(widget,0)
    def start(self,swip):
        rows = [i for i in swip.get_items()]
        for row1 in rows:
            if isinstance(row1, MySwip):
                swip.remove_widget(row1)
        top = requests.get('http://178.170.242.221:8000',params={'near':"loc"})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,4):
            widget =  MySwip()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            swip.add_widget(widget,0)
        top = requests.get('http://178.170.242.221:8000',params={'id':"polz"})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,4):
            widget =  MyItem()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            self.ids.list.add_widget(widget,0)
    def near(self,swip):
        ident = ""
        rows = [i for i in swip.get_items()]
        for row1 in rows:
            if isinstance(row1, MySwip):
                swip.remove_widget(row1)
        top = requests.get('http://178.170.242.221:8000',params={'near':"loc"})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,4):
            widget =  MySwip()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            swip.add_widget(widget,0)
    def pop(self,swip):
        rows = [i for i in swip.get_items()]
        for row1 in rows:
            if isinstance(row1, MySwip):
                swip.remove_widget(row1)
        top = requests.get('http://178.170.242.221:8000',params={'pop':"pop"})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,10):
            widget =  MySwip()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            swip.add_widget(widget,0)
    def on_search(self,text):
        txt=text.split('[size=0][color=#ffffff]')
        self.ids.poisk2.text=text
        top = requests.get('http://178.170.242.221:8000',params={'poisc':text})
        print(top.content.decode(encoding='utf-8').split('http'))
        toop = []
        toop = top.content.decode(encoding='utf-8').split('http')
        for i in range(1,4):
            widget =  MyItem()
            widget.source = "http"+toop[i]
            widget.text = "   Мероприятие"
            self.ids.list2.add_widget(widget,0)
    pass    
class ClickableText(MDScreen):
    text = StringProperty()
    hint_text = StringProperty()

class Main(MDApp):
    
    def build(self):
        app =  One_Screen()
        Builder.load_file("down.kv")
        self=One_Screen()
        return self
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
