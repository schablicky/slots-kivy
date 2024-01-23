# slotmachine.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import random
from symbol import Symbol

class SlotMachine:
    def __init__(self, symbols):
        self.symbols = symbols
        self.result_label = Label(text="Výsledek: ")
        self.spin_button = Button(text="Zatočit", on_press=self.spin)
        self.rows = 3
        self.cols = 3
        self.wheels = [[Image(source=self.symbols[0].image_path) for _ in range(self.rows)] for _ in range(self.cols)]
        pass

    def spin(self, instance):
        # Zastavení symbolů náhodně
        results = [[random.choice(self.symbols) for _ in range(self.cols)] for _ in range(self.rows)]

        # Aktualizace obrazů na válích
        for i in range(self.rows):
            for j in range(self.cols):
                self.wheels[i][j].source = results[i][j].image_path

        # Vyhodnocení výsledku
        self.evaluate_results(results)

    def evaluate_results(self, results):


        for row in results:
            if row[0].name == row[1].name == row[2].name:
                print("Výhra")

            pass
        #     for j in range(len(results[0]) - 2):
        #         if results[i][j] == results[i][j + 1] and results[i][j] == results[i][j + 2]:
        #             self.result_label.text = "Výhra, linie 1!"
        #             return
        #         if results[i + 1][j] == results[i + 1][j + 1] and results[i + 1][j] == results[i + 1][j + 2]:
        #             self.result_label.text = "Výhra, linie 2!"
        #             return
        #         if results[i + 2][j] == results[i + 2][j + 1] and results[i + 2][j] == results[i + 2][j + 2]:
        #             self.result_label.text = "Výhra, linie 3!"
        #             return
        #         if results[i][j] == results[i + 1][j + 1] and results[i][j] == results[i + 2][j + 2]:
        #             self.result_label.text = "Výhra, diagonala 1!"
        #             return
        #         if results[i + 2][j] == results[i + 1][j + 1] and results[i + 2][j] == results[i][j + 2]:
        #             self.result_label.text = "Výhra, diagonala 2!"
        #             return

        self.result_label.text = "Žádná výhra"

        """
        # Vyhodnocení výsledku podle výherních linií
        for i in range(len(results) - 2):
            for j in range(len(results[0]) - 2):
                symbol = results[i][j]
                pass
                # Kontrola shod ve sloupci
                if all(results[i + k][j] == symbol for k in range(3)):
                    self.result_label.text = f"Výhra! Trojité shodné symboly ve vedlejším sloupci, sloupec {j + 1}!"
                    return

                # Kontrola shod v řádku
                if all(results[i][j + k] == symbol for k in range(3)):
                    self.result_label.text = f"Výhra! Trojité shodné symboly vedle sebe, řádek {i + 1}!"
                    return

                # Kontrola shod na diagonále (zleva do prava)
                if all(results[i + k][j + k] == symbol for k in range(3)):
                    self.result_label.text = f"Výhra! Trojité shodné symboly diagonálně (zleva do prava), začíná na sloupci {j + 1} a řádku {i + 1}!"
                    return

        self.result_label.text = "Zkus to znovu. Žádná výhra tentokrát."
"""

class SlotMachineLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(SlotMachineLayout, self).__init__(**kwargs)
        symbols = [
            Symbol("cherry", "symbol_cherry.png"),
            Symbol("lemon", "symbol_lemon.png"),
            Symbol("orange", "symbol_orange.png"),
            Symbol("plum", "symbol_plum.png"),
            Symbol("bell", "symbol_bell.png"),
            Symbol("bar", "symbol_bar.png"),
            Symbol("seven", "symbol_seven.png")
        ]
        self.slot_machine = SlotMachine(symbols)
        self.add_widget(self.slot_machine.result_label)
        for j in range(self.slot_machine.cols):
            row_layout = BoxLayout(orientation='vertical')
            for i in range(self.slot_machine.rows):
                row_layout.add_widget(self.slot_machine.wheels[i][j])
            self.add_widget(row_layout)
        self.add_widget(self.slot_machine.spin_button)
