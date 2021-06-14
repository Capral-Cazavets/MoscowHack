import hashlib
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.button import MDRaisedButton #Прямоугольная Плоская кнопка MD
import requests
import string
import pandas as pd
from kivymd.icon_definitions import md_icons
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window #Для размера окна
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from kivymd.uix.list import OneLineListItem
from kivy.properties import StringProperty
Window.size = (450, 700)

class Home(ScreenManager):
    pass
class ClickableText(MDScreen):
    text = StringProperty()
    hint_text = StringProperty()

class Main(MDApp):
    def build(self):
        Builder.load_file("main.kv")
        return Home()

Main().run()