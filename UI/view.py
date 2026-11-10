import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None



    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        self._dd_biblioteche = ft.Dropdown(
            label="Biblioteca",
            hint_text="Seleziona una biblioteca",
            width=400,
            on_select=self.controller.read_biblioteca)

        self._dd_generi = ft.Dropdown(
            label="Genere",
            hint_text="Seleziona un genere",
            width=400,
            on_select=self.controller.read_genere)

        self._btnCerca = ft.Button(
            content=ft.Text("Cerca Libri"),
            on_click=self.controller.handle_mostra_libri,
            width=200)

        # Sezione 3: Libri
        self._lstResult = ft.ListView(expand=1, spacing=5, padding=10, auto_scroll=False)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        layout_principale = ft.Column(
            [
                self.toggle_cambia_tema,
                self.txt_titolo,
                ft.Divider(),
                ft.Row([self._dd_biblioteche, self._dd_generi], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([self._btnCerca], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(),
                self._lstResult
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        self.page.add(layout_principale)
        self.page.scroll = "adaptive"
        self.page.update()

        # --- Layout della pagina ---
        self.page.add()
        self.toggle_cambia_tema

        # Sezione 1
        self.txt_titolo,
        ft.Divider(),

        # Sezione 2: Filtraggio
        ft.Row(
            [self._dd_biblioteche, self._dd_generi],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [self._btnCerca],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Divider(),

        # Sezione 3: Libri
        self._lstResult

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
