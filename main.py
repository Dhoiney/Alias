from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput


# Win params
height = 700
width = 380
Config.set('graphics', 'resizable', 1)
Config.set('graphics', 'width', width)
Config.set('graphics', 'height', height)

text_size = 20


class StartScreen(Screen):
    def __init__(self, **kw):
        super(StartScreen, self).__init__(**kw)
        float1 = FloatLayout()
        stng_btn = Button(text='Settings',
                          font_size=text_size,
                          size_hint=(0.175, 0.06),
                          pos_hint={'center_x': 0.88, 'center_y': 0.92},
                          on_release=self.stng_press)
        game_name = Label(text='Alias The Game',
                          font_size=40,
                          size_hint=(0.4, 0.4),
                          pos_hint={'center_x': 0.5, 'center_y': 0.7})
        start_btn = Button(text='Play',
                           font_size=text_size,
                           size_hint=(0.3, 0.06),
                           pos_hint={'center_x': 0.7, 'center_y': 0.2},
                           on_release=self.play_press)
        help_btn = Button(text='Help',
                          font_size=text_size,
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
        label = Label(font_size=text_size,
                      text='Settings',
                      pos_hint={'center_x': 0.5,
                                'center_y': 0.95},
                      )
        float1.add_widget(label)

        back_btn = Button(text='Back',
                          font_size=text_size,
                          size_hint=(0.2, 0.1),
                          pos_hint={'center_x': 0.5, 'center_y': 0.2},
                          on_release=self.go_back)
        float1.add_widget(back_btn)
        slider_sound = Switch(active=False,
                              active_norm_pos=0,
                              pos_hint={'center_x': 0.7, 'center_y': 0.5},
                              size_hint_x=0.55,
                              size_hint_y=0.02)
        music_label = Label(text='Music:',
                            pos_hint={'center_x': 0.3, 'center_y': 0.5},
                            font_size=32)
        slider_audio = Switch(active=False,
                              active_norm_pos=0,
                              pos_hint={'center_x': 0.7, 'center_y': 0.7},
                              size_hint_x=0.55,
                              size_hint_y=0.02)
        sound_label = Label(text='Sound:',
                            pos_hint={'center_x': 0.3, 'center_y': 0.7},
                            font_size=32)
        font_size_spin = Spinner(text='Font Size',
                                 values=('Small', 'Medium', 'Big'),
                                 size_hint=(0.1, 0.1),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.35},)

        float1.add_widget(font_size_spin)
        float1.add_widget(music_label)
        float1.add_widget(sound_label)
        float1.add_widget(slider_sound)
        float1.add_widget(slider_audio)
        self.add_widget(float1)

    def go_back(self, instance):
        sm.current = 'start screen'


class HelpScreen(Screen):
    def __init__(self, **kw):
        super(HelpScreen, self).__init__(**kw)
        float1 = FloatLayout()
        help_btn = Button(text='Back',
                          font_size=text_size,
                          size_hint=(0.3, 0.06),
                          pos_hint={'center_x': 0.5, 'center_y': 0.2},
                          on_release=self.go_back)
        rules = Label(text='????\n????????????\n????????????????\n??????\n??????????????\n????????!!!', font_size=64)
        float1.add_widget(rules)
        float1.add_widget(help_btn)
        self.add_widget(float1)

    def go_back(self, instance):
        sm.current = 'start screen'


class TeamsScreen(Screen):
    def __init__(self, **kw):
        super(TeamsScreen, self).__init__(**kw)
        float1 = FloatLayout()
        label = Label(text='Teams',
                      pos_hint={'center_x': 0.5,
                                'center_y': 0.95},
                      font_size=text_size)
        t1 = Label(text='Team 1:',
                   pos_hint={'center_x': 0.15,
                             'center_y': 0.8},
                   font_size=text_size)
        team1 = TextInput(text='text',
                          size_hint=(0.7, 0.06),
                          pos_hint={'center_x': 0.6,
                                    'center_y': 0.8},
                          multiline=False,
                          font_size=text_size)
        t2 = Label(text='Team 2:',
                   pos_hint={'center_x': 0.15,
                             'center_y': 0.7},
                   font_size=text_size)
        team2 = TextInput(text='text',
                          size_hint=(0.7, 0.06),
                          pos_hint={'center_x': 0.6,
                                    'center_y': 0.7},
                          multiline=False,
                          font_size=text_size)
        add_team = Button(text='+',
                          font_size=40,
                          size_hint=(0.9, 0.05),
                          pos_hint={'center_x': 0.5,
                                    'center_y': 0.6},
                          on_releace=self.create_team)
        float1.add_widget(add_team)
        float1.add_widget(t1)
        float1.add_widget(t2)
        float1.add_widget(team1)
        float1.add_widget(team2)
        float1.add_widget(label)
        self.add_widget(float1)

    def create_team(self, instance):
        print('TbIK')


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
