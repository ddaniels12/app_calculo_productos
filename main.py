from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.metrics import dp


class MyApp(App):
    def build(self):
        self.productos = {
            "Producto 1": 590,
            "Producto 2": 800,
            "Producto 3": 1200,
            "Producto 4": 950,
            "Producto 5": 700,
            "Producto 6": 1500,
            "Producto 7": 800,
            "Producto 8": 1200,
            "Producto 9": 950,
            "Producto 10": 700,
            "Producto 11": 1500
        }
        self.seleccionados = {}

        layout = GridLayout(cols=2, spacing=dp(10), padding=dp(20))

        for producto, precio in self.productos.items():
            btn = Button(text=producto, size_hint=(None, None), size=(dp(150), dp(40)),
                         background_normal='', background_color=(0.2, 0.6, 0.9, 1))
            btn.bind(on_release=self.actualizar_seleccion)
            layout.add_widget(btn)

        self.costo_total_label = Button(text="Costo Total: $0", size_hint=(None, None), size=(dp(150), dp(40)),
                                        background_normal='', background_color=(0.8, 0.2, 0.2, 1))
        layout.add_widget(self.costo_total_label)

        reiniciar_btn = Button(text="Reiniciar", size_hint=(None, None), size=(dp(150), dp(40)),
                               background_normal='', background_color=(0.9, 0.2, 0.2, 1))
        reiniciar_btn.bind(on_release=self.reiniciar)
        layout.add_widget(reiniciar_btn)

        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        return layout

    def actualizar_seleccion(self, btn):
        producto = btn.text
        if producto in self.seleccionados:
            self.seleccionados[producto] += 1
        else:
            self.seleccionados[producto] = 1

        costo_total = sum(self.productos[prod] * cant for prod, cant in self.seleccionados.items())
        self.costo_total_label.text = f"Costo Total: ${costo_total}"

    def reiniciar(self, btn):
        self.seleccionados = {}
        self.costo_total_label.text = "Costo Total: $0"


if __name__ == '__main__':
    MyApp().run()
