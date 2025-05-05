import tkinter as tk
from typing import Optional

KEY_YES = "Y"
KEY_NO = "N"
KEY_RESTART = "R"

cenas = [
    {
        "imagem": "🌲🌫️🌲\n🌫️🙎‍♂️🌫️\n🌲🌫️🌲",
        "texto": "Você desperta em meio a uma floresta coberta por névoa.\nHá um som de água corrente à distância.\nVocê decide seguir em direção ao som? (Y/N)",
        "yes": 1,
        "no": 2
    },
    {
        "imagem": "🌊🛶🌉",
        "texto": "Você segue até um rio. Há uma ponte quebrada e uma canoa velha.\nVocê tenta usar a canoa para atravessar? (Y/N)",
        "yes": 3,
        "no": 4
    },
    {
        "imagem": "🌲🌲🏚️🌲🌲",
        "texto": "Você decide ignorar o som de água e segue pela trilha de terra.\nLogo encontra uma cabana abandonada.\nVocê entra? (Y/N)",
        "yes": 5,
        "no": 6
    },
    {
        "imagem": "🌊😱🌊",
        "texto": "A canoa afunda no meio do rio. Você luta para nadar de volta, mas algo te puxa para o fundo.\nFIM.",
        "yes": None,
        "no": None
    },
    {
        "imagem": "🌉🕴️🌉",
        "texto": "Você contorna o rio e encontra uma ponte mais adiante.\nAo atravessar, uma figura encapuzada te observa... FIM.",
        "yes": None,
        "no": None
    },
    {
        "imagem": "📜🗺️📖",
        "texto": "Dentro da cabana, você encontra um mapa antigo com símbolos estranhos.\nTalvez seja o começo de uma jornada... FIM.",
        "yes": None,
        "no": None
    },
    {
        "imagem": "🏃‍♂️👣🌫️",
        "texto": "Você se afasta da cabana, mas escuta passos atrás de você.\nQuando se vira, não há ninguém. Você corre... e nunca mais é visto.\nFIM.",
        "yes": None,
        "no": None
    }
]

class JogoRPG:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Mini RPG")
        self.root.configure(bg="black")
        self.root.geometry("600x300")

        self.label = tk.Label(
            root, text="", fg="white", bg="black", justify="left", anchor="nw"
        )
        self.label.pack(padx=20, pady=20, fill="both", expand=True)

        self.cena_atual = 0
        self.char_index = 0

        self.atualizar_fonte()
        self.exibir_texto()

        self.root.bind("<Configure>", self.redimensionar_fonte)
        self.root.bind("<Key>", self.tecla_pressionada)

    def exibir_texto(self):
        cena = cenas[self.cena_atual]
        completo = f"{cena['imagem']}\n\n{cena['texto']}"
        if self.char_index <= len(completo):
            self.label.config(text=completo[:self.char_index])
            self.char_index += 1
            self.root.after(25, self.exibir_texto)

    def tecla_pressionada(self, event: tk.Event):
        key = event.keysym.upper()

        if key == KEY_RESTART:
            self.ir_para_cena(0)
            return

        if cenas[self.cena_atual]["yes"] is None:
            return

        if key == KEY_YES:
            self.ir_para_cena(cenas[self.cena_atual]["yes"])
        elif key == KEY_NO:
            self.ir_para_cena(cenas[self.cena_atual]["no"])

    def ir_para_cena(self, index: Optional[int]):
        """Atualiza a cena atual."""
        if index is not None:
            self.cena_atual = index
            self.char_index = 0
            self.exibir_texto()

    def atualizar_fonte(self):
        largura = self.root.winfo_width()
        altura = self.root.winfo_height()
        tamanho = max(10, min(largura // 40, altura // 15))
        self.label.config(font=("Courier", tamanho), wraplength=largura - 50)

    def redimensionar_fonte(self, event: tk.Event):
        self.atualizar_fonte()

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoRPG(root)
    root.mainloop()
