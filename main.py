from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.config import Config

# Win params
height = 480
width = 640

Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)


# Game name Alias
class AliasApp(App):
    def build(self):    # standard class
        anchlayout = AnchorLayout(anchor_x='center',
                                  anchor_y='bottom',
                                  size_hint=(1, 0.2),
                                  padding=[40, 0, 50, 50],)

        box = BoxLayout(spacing=10)
        startbtn = Button(text='Начать игру!', on_press=self.categories())
        helpbtn = Button(text='Правила Игры',)   # on_press=self.help_menu()
        box.add_widget(startbtn, helpbtn)
        anchlayout.add_widget(box)

        return anchlayout   # return 1-st  layout

    def categories(self):
        anchlayout = AnchorLayout(anchor_x='center',
                                  anchor_y='top',
                                  size_hint=(1, 0.1), )
        box = BoxLayout(orientation='vertical', spacing=5)
        anchlayout.add_widget(box)
        first_cat = Button(text='1 cat',)    # on press=self.first_cat()
        second_cat = Button(text='2 cat', )  # on press=self.second_cat()
        third_cat = Button(text='3 cat', )  # on press=self.third_cat()
        four_cat = Button(text='4 cat', )  # on press=self.four_cat()
        box.add_widget(first_cat)
        box.add_widget(second_cat)
        box.add_widget(third_cat)
        box.add_widget(four_cat)

        return anchlayout



if __name__ == "__main__":
    AliasApp().run()
