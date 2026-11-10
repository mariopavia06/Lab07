import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

        #self.fill_dd_biblioteche()
        #self.fill_dd_generi()

        # --- POPOLA DROPDOWN ---

    def fill_dd_biblioteche(self):
        """Popola il menu a tendina delle biblioteche recuperandole dal modello."""
        biblioteche = self._model.get_biblioteche()
        for biblio in biblioteche:
            self._view._dd_biblioteche.options.append(
                ft.dropdown.Option(key=biblio.id, text=biblio.nome)
            )
        self._view.update()

    def fill_dd_generi(self):
        """Popola il menu a tendina dei generi letterari recuperandoli dal modello."""
        generi = self._model.get_generi()
        for genere in generi:
            self._view._dd_generi.options.append(
                ft.dropdown.Option(text=genere)
            )
        self._view.update()

        # --- CALLBACKS DROPDOWN ---

    def read_biblioteca(self, e):
        """Cattura la biblioteca scelta dall'utente nel menu a tendina."""
        if e.control.value is None:
            self.biblioteca_selezionata = None
        else:
            self.biblioteca_selezionata = e.control.value

    def read_genere(self, e):
        """Cattura il genere scelto dall'utente nel menu a tendina."""
        if e.control.value is None:
            self.genere_selezionato = None
        else:
            self.genere_selezionato = e.control.value

        # --- AZIONE: MOSTRA LIBRI ---

    def handle_mostra_libri(self, e):
        """Gestisce il click sul pulsante per visualizzare i libri filtrati."""
        # Pulisce la lista dei risultati precedenti nell'interfaccia
        self._view._lstResult.controls.clear()

        # Interroga il modello passando i filtri correnti (biblioteca e genere)
        libri = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        if not libri:
            self._view._lstResult.controls.append(
                ft.Text("Nessun libro trovato con i filtri selezionati.")
            )
        else:
            for libro in libri:
                self._view._lstResult.controls.append(
                    ft.Text(str(libro))
                )

        # Aggiorna la vista per mostrare i risultati a schermo
        self.update_view()

    def update_view(self):
        """Metodo di comodo per aggiornare la pagina Flet."""
        self._view.update()