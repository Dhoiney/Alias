from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


# Win params
height = 700
width = 380
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)


class StartScreen(Screen):
    def __init__(self, **kw):
        super(StartScreen, self).__init__(**kw)
        float1 = FloatLayout()
        stng_btn = Button(text='Settings',
                          font_size=12,
                          size_hint=(0.175, 0.06),
                          pos_hint={'center_x': 0.88, 'center_y': 0.92},
                          on_release=self.stng_press)
        game_name = Label(text='Alias The Game',
                          font_size=30,
                          size_hint=(0.4, 0.4),
                          pos_hint={'center_x': 0.5, 'center_y': 0.7})
        start_btn = Button(text='Play',
                           font_size=18,
                           size_hint=(0.3, 0.06),
                           pos_hint={'center_x': 0.7, 'center_y': 0.2},
                           on_release=self.play_press)
        help_btn = Button(text='Help',
                          font_size=18,
                          size_hint=(0.3, 0.06),
                          pos_hint={'center_x': 0.30, 'center_y': 0.2},
                          on_release=self.help_press)
        float1.add_widget(help_btn)
        float1.add_widget(start_btn)
        float1.add_widget(game_name)
        float1.add_widget(stng_btn)
        self.add_widget(float1)

    def stng_press(self, instance):
        sm.current = 'settings'

    def play_press(self, instance):
        sm.current = 'teams'

    def help_press(self, instance):
        sm.current = 'help_screen'


class SettingsScreen(Screen):
    def __init__(self, **kw):
        super(SettingsScreen, self).__init__(**kw)
        float1 = FloatLayout()
        label = Label(text='Settings', pos_hint={'center_x': 0.5, 'center_y': 0.9})
        float1.add_widget(label)
        back_btn = Button(text='Back',
                          font_size=18,
                          size_hint=(0.2, 0.1),
                          pos_hint={'center_x': 0.5, 'center_y': 0.2},
                          on_release=self.go_back)
        float1.add_widget(back_btn)
        self.add_widget(float1)

    def go_back(self, instance):
        sm.current = 'start screen'


class HelpScreen(Screen):
    def __init__(self, **kw):
        super(HelpScreen, self).__init__(**kw)
        pass


class TeamsScreen(Screen):
    def __init__(self, **kw):
        super(TeamsScreen, self).__init__(**kw)
        pass


class WordsScreen(Screen):
    def __init__(self, **kw):
        super(WordsScreen, self).__init__(**kw)
        pass


class GameScreen(Screen):
    def __init__(self, **kw):
        super(GameScreen, self).__init__(**kw)
        pass


class ResultScreen(Screen):
    def __init__(self, **kw):
        super(ResultScreen, self).__init__(**kw)
        pass


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(StartScreen(name='start screen'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(TeamsScreen(name='teams'))
sm.add_widget(WordsScreen(name='words'))
sm.add_widget(ResultScreen(name='results'))
sm.add_widget(GameScreen(name='game_screen'))
sm.add_widget(HelpScreen(name='help_screen'))


class AliasApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    AliasApp().run()
