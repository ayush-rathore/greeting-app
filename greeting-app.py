from kivymd.app import MDApp                 # Importing all the necessary libraries
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

kv = """                                   # KV string for GUI
Screen:
    in_class: text
    MDLabel:
        text: 'Greeting App'
        font_style: "H3"
        pos_hint: {'center_x': 0.83, 'center_y': 0.8}

    MDLabel:
        text: "(Don't judge me on my appearance, I'm trying to get better everyday.)"
        pos_hint: {'center_x': 0.7, 'center_y': 0.725}

    MDTextField:
        id: text
        hint_text: 'Enter your name'
        helper_text_mode: "on_focus"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        size_hint_x: None
        width: 300
        required: True
        icon_right : "human-greeting"

    MDRectangleFlatButton:
        text: 'Submit'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            app.greet()

    MDLabel:
        text: ''
        id: show
        pos_hint: {'center_x': 0.95, 'center_y': 0.2}


"""
class MainApp(MDApp):             #Creating a class for the app
    in_class = ObjectProperty(None)

    def build(self):
        return Builder.load_string(kv)     #Loading the KV String

    def greet(self):
        self.dialog = MDDialog(title='Greeting you', text="Hello %s!" %(self.root.in_class.text), size_hint=(0.8,1), buttons=[MDFlatButton(text='Thank You', on_release=self.close_dialog)])
        self.dialog.open()             # Greeting Dialog-Box

    def close_dialog(self,obj):
        self.dialog.dismiss()         

MainApp().run()                    #Running the app.

#Read more about KivyMD here ~ "https://kivymd.readthedocs.io/en/latest/"