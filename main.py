from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class Manager(ScreenManager):
    pass


class LoginScreen(Screen):
    pass


class Entrada(Screen):
    pass


class Saida(Screen):
    pass


class PontoDigitalApp(MDApp):
    def build(self):
        gerenciador = Manager()
        gerenciador.add_widget(LoginScreen(name='loginscreen'))
        gerenciador.add_widget(LoginScreen(name='entrada'))
        gerenciador.add_widget(LoginScreen(name='saida'))
        return gerenciador

if __name__ == '__main__':
    aplicativo = PontoDigitalApp()
    aplicativo.run()