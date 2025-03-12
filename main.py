import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button





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

            self.entry = TextInput(
                multiline=False,
                font_size=dp(16),
                size_hint_x=0.15,
                hint_text='Введите перевод: ',
                padding=[dp(5), dp(10)]
            )

            self.btn = Button(
                text="GO",
                font_size=dp(12),
                size_hint_x=0.05,
                background_normal='',
                background_color=(0.2, 0.6, 0.9, 1)
            )
            self.btn.bind(on_press=lambda instance, e=self.entry, a=answers: self.check(instance, e, a))

            row.add_widget(label)
            row.add_widget(self.entry)
            row.add_widget(self.btn)
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

    def calculate_height(self):
        return len(x) * dp(50) + dp(10)

    def check(self, instance, entry, answers):
        answer = entry.text.strip().lower()
        instance.background_color = (0.2, 0.8, 0.3, 1) if answer in [a.lower() for a in answers] else (0.9, 0.2, 0.2, 1)
        instance.text = "Ja!" if answer in [a.lower() for a in answers] else "Nein"

    def show_answers(self, instance):
        answers = '\n\n'.join([f"[b]{word}:[/b] {', '.join(answers)}" for word, answers in x])
        self.answers_panel.text = answers
        self.answers_panel.markup = True


class MemoryApp(App):
    def build(self):
        self.title = "Language Memory Game"
        return MemoryGame()


if __name__ == '__main__':
    MemoryApp().run()
