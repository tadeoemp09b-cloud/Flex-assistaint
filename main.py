from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import urllib.request
import json

GEMINI_API_KEY = "AQ.Ab8RN6Kx0GeBarQNqZwAsc12DAfVr5aWS7k3clzmrmDlsV0-Lw"

class FlexApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.label = Label(text="Hola, soy Flex. ¿Qué deseas?", font_size=20)
        self.layout.add_widget(self.label)
        
        self.input = TextInput(hint_text="Escribe tu orden aquí...", size_hint_y=None, height=50)
        self.layout.add_widget(self.input)
        
        self.btn = Button(text="Preguntar a Flex", size_hint_y=None, height=60)
        self.btn.bind(on_press=self.consultar_ia)
        self.layout.add_widget(self.btn)
        
        return self.layout

    def consultar_ia(self, instance):
        texto = self.input.text
        if not texto:
            return
        self.label.text = "Pensando..."
        
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        datos = json.dumps({"contents": [{"parts": [{"text": texto}]}]}).encode("utf-8")
        req = urllib.request.Request(url, data=datos, headers={"Content-Type": "application/json"})
        
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                res = json.loads(resp.read().decode())
                respuesta = res["candidates"][0]["content"]["parts"][0]["text"]
                self.label.text = respuesta
        except Exception as e:
            self.label.text = "Error al conectar con Gemini."

if __name__ == '__main__':
    FlexApp().run()
