import random
import json
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# Загрузка данных из файла
with open('GOGO.json', 'r', encoding='utf-8') as f:
    wort = json.load(f)

NUM_WORDS = 10
x = random.sample(list(wort.items()), NUM_WORDS)


class MemoryGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = dp(10)
        self.padding = [dp(10), dp(10), dp(10), dp(10)]

        # Main scroll container
        scroll = ScrollView(size_hint_y=0.8)
        self.input_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=self.calculate_height()
        )

        # Dynamic content
        self.entries = []
        self.buttons = []
        for i, (word, answers) in enumerate(x):
            row = BoxLayout(
                size_hint_y=None,
                height=dp(50),
                spacing=dp(5)
            )

            label = Label(
                text=word,
                font_size=dp(18),
                bold=True,
                size_hint_x=0.35,
                halign='left',
                valign='middle',
                text_size=(dp(150), None)
            )

            entry = TextInput(
                multiline=False,
                font_size=dp(16),
                size_hint_x=0.15,
                hint_text='Введите перевод: ',
                padding=[dp(5), dp(10)]
            )
            self.entries.append(entry)

            btn = Button(
                text="GO",
                font_size=dp(12),
                size_hint_x=0.05,
                background_normal='',
                background_color=(0.2, 0.6, 0.9, 1)
            )
            btn.bind(on_press=lambda instance, e=entry, a=answers: self.check(instance, e, a))
            self.buttons.append(btn)

            row.add_widget(label)
            row.add_widget(entry)
            row.add_widget(btn)
            self.input_layout.add_widget(row)

        scroll.add_widget(self.input_layout)
        self.add_widget(scroll)

        # Answers section
        self.answers_panel = Label(
            text='',
            size_hint_y=None,
            height=dp(150),
            font_size=dp(16),
            color=(0.3, 0.3, 0.3, 1),
            padding=[dp(10), dp(10)]
        )
        self.add_widget(self.answers_panel)

        # Show answers button
        self.show_btn = Button(
            text="Die Antworten",
            size_hint_y=None,
            height=dp(40),
            font_size=dp(18),
            background_color=(0.4, 0.8, 0.4, 1)
        )
        self.show_btn.bind(on_press=self.show_answers)
        self.add_widget(self.show_btn)

        # Restart button
        self.restart_btn = Button(
            text="Начать заново",
            size_hint_y=None,
            height=dp(40),
            font_size=dp(18),
            background_color=(0.9, 0.5, 0.2, 1)
        )
        self.restart_btn.bind(on_press=self.restart)
        self.add_widget(self.restart_btn)

    def calculate_height(self):
        return len(x) * dp(50) + dp(10)

    def check(self, instance, entry, answers):
        answer = entry.text.strip().lower()
        instance.background_color = (0.2, 0.8, 0.3, 1) if answer in [a.lower() for a in answers] else (0.9, 0.2, 0.2, 1)
        instance.text = "Ja!" if answer in [a.lower() for a in answers] else "Nein"

    def show_answers(self, instance):
        answers_text = '\n\n'.join([f"[b]{word}:[/b] {', '.join(answers)}" for word, answers in x])

        # Создание нового окна для отображения ответов
        popup_layout = BoxLayout(orientation='vertical')
        popup_label = Label(
            text=answers_text,
            markup=True,
            size_hint_y=None,
            height=dp(300),
            font_size=dp(16),
            padding=[dp(10), dp(10)]
        )
        popup_layout.add_widget(popup_label)

        popup = Popup(
            title='Ответы',
            content=popup_layout,
            size_hint=(None, None),
            size=(dp(400), dp(350))
        )
        popup.open()

    def restart(self, instance):
        global x
        x = random.sample(list(wort.items()), NUM_WORDS)
        self.clear_widgets()
        self.__init__()


class MemoryApp(App):
    def build(self):
        self.title = "Language Memory Game"
        return MemoryGame()


if __name__ == '__main__':
    MemoryApp().run()
