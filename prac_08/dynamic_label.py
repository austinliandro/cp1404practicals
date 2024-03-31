"""
Kivy example for CP140
Dynamically create buttons based on content of dictionary
Austin Liandro, first version: 10/09/2023
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Main program"""

    def __init__(self, **kwargs):
        """Construct  main App"""
        super().__init__(**kwargs)
        self.list_color = ["Timberwolf", "Misty rose", "Tea Rose (red)", "Orchid pink", "Violet", "Pine Green",
                           "Citrine", "Coquelicot", "Russian Violet", "Argentinian Blue"]

    def build(self):
        """Build the kivy GUI"""
        self.title = "Dynamic Label"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create Label from data and add them to the GUI"""
        for color in self.list_color:
            temp_label = Label(text=color)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelApp().run()