import customtkinter
import os
from  PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Milembri")
janela.geometry("800x850")
pasta = os.path.dirname(os.path.abspath(__file__))
janela.iconbitmap(os.path.join(pasta, "azul.ico"))

Logodabunda = customtkinter.CTkImage(light_image=Image.open(os.path.join(pasta,"Logotipolaranja.png")), dark_image=Image.open(os.path.join(pasta,"Logotipoazul.png")), size= (300,75))

labeldalogo = customtkinter.CTkLabel(janela, text="", image=Logodabunda)
labeldalogo.pack(anchor="w",padx=20,pady=(15, 5))

tamanho_letra = 26
limite = 6
textos_dos_lembretes = []

def atualizar_icone():
    tema_atual = customtkinter.get_appearance_mode()

    if tema_atual == "Dark":
        arquivo = "azul.ico"
    else:
        arquivo = "laranja.ico"

    caminho = os.path.join(pasta, arquivo)
    janela.iconbitmap(caminho)

def atualizar_contador():
    quantidade = len(textos_dos_lembretes)

    if quantidade == 0:
        contador.configure(
            text="Nenhum lembrete. Aproveita o descanso!"
        )
    elif quantidade == 1:
        contador.configure(text="Você tem 1 lembrete")
    else:
        contador.configure(
            text="Você tem " + str(quantidade) + " lembretes"
        )

def adicionar():
    texto = entrada.get().strip()
    contexto = entrada_contexto.get().strip()
    passo = entrada_passo.get().strip()

    if texto == "":
        contador.configure(
            text="Escreve um lembrete primeiro!"
        )
        return

    if len(textos_dos_lembretes) >= limite:
        contador.configure(
            text="Lista cheia! Conclui um lembrete antes."
        )
        return

    caixinha = customtkinter.CTkFrame(
        master=frame_lista
    )
    caixinha.pack(
        padx=10, pady=6, fill="x"
    )

    texto_lembrete = customtkinter.CTkLabel(
        master=caixinha,
        text=texto,
        font=("Comic Sans MS", tamanho_letra),
        text_color=("#000000", "#FFFFFF"),
        wraplength=650,
        anchor="w",
        justify="left"
    )
    texto_lembrete.pack(
        padx=12, pady=(10, 4), anchor="w"
    )

    if contexto != "":
        label_contexto = customtkinter.CTkLabel(
            master=caixinha,
            text="Para lembrar: " + contexto,
            text_color=("#000000", "#FFFFFF"),
            font=("Comic Sans MS", 16),
            wraplength=650,
            anchor="w",
            justify="left"
        )
        label_contexto.pack(
            padx=12, pady=3, anchor="w"
        )

    if passo != "":
        label_passo = customtkinter.CTkLabel(
            master=caixinha,
            text="Primeiro passo: " + passo,
            text_color=("#000000", "#FFFFFF"),
            font=("Comic Sans MS", 16),
            wraplength=650,
            anchor="w",
            justify="left"
        )
        label_passo.pack(
            padx=12, pady=3, anchor="w"
        )

    textos_dos_lembretes.append(texto_lembrete)

    def concluir():
        textos_dos_lembretes.remove(texto_lembrete)
        caixinha.destroy()
        atualizar_contador()

    btn_feito = customtkinter.CTkButton(
        master=caixinha,
        text="Feito ✓",
        text_color=("#000000", "#FFFFFF"),
        width=110,
        height=40,
        font=("Comic Sans MS", 18),
        fg_color=("#FFAE52", "#3061A4"),
        hover_color=("#D6841F", "#163D89" ),
        command=concluir)
    btn_feito.pack(padx=10, pady=8, anchor="e")

    entrada.delete(0, "end")
    entrada_contexto.delete(0, "end")
    entrada_passo.delete(0, "end")

    atualizar_contador()

def aumentar():
    global tamanho_letra

    if tamanho_letra < 60:
        tamanho_letra += 4

        for texto_lembrete in textos_dos_lembretes:
            texto_lembrete.configure(
                font=("Comic Sans MS", tamanho_letra)
            )

        info_tamanho.configure(
            text="Letra: " + str(tamanho_letra)
        )

def diminuir():
    global tamanho_letra

    if tamanho_letra > 16:
        tamanho_letra -= 4

        for texto_lembrete in textos_dos_lembretes:
            texto_lembrete.configure(
                font=("Comic Sans MS", tamanho_letra)
            )

        info_tamanho.configure(
            text="Letra: " + str(tamanho_letra)
        )

def trocar_tema():
    tema_atual = customtkinter.get_appearance_mode()

    if tema_atual == "Dark":
        customtkinter.set_appearance_mode("light")
        btn_tema.configure(text="Modo escuro")
    else:
        customtkinter.set_appearance_mode("dark")
        btn_tema.configure(text="Modo claro")
    atualizar_icone()

frame_barra = customtkinter.CTkFrame(
    master=janela
)
frame_barra.pack(
    padx=10, pady=10, fill="x"
)

btn_diminuir = customtkinter.CTkButton(
    master=frame_barra,
    text="A-",
    text_color=("#000000","#FFFCFC"),
    fg_color=("#FFAE52", "#3061A4"),
    hover_color=("#D6841F", "#163D89" ),
    width=60,
    height=45,
    font=("Comic Sans MS", 22),
    command=diminuir
)
btn_diminuir.pack(
    side="left", padx=5, pady=10
)

btn_aumentar = customtkinter.CTkButton(
    master=frame_barra,
    text="A+",
    width=60,
    height=45,
    text_color=("#000000","#FFFCFC"),
    fg_color=("#FFAE52", "#3061A4"),
    hover_color=("#D6841F", "#163D89" ),
    font=("Comic Sans MS", 22),
    command=aumentar
)
btn_aumentar.pack(
    side="left", padx=5, pady=10
)

info_tamanho = customtkinter.CTkLabel(
    master=frame_barra,
    text="Letra: 26",
    font=("Comic Sans MS", 20)
)
info_tamanho.pack(
    side="left", padx=15
)

btn_tema = customtkinter.CTkButton(
    master=frame_barra,
    text="Modo claro",
    text_color=("#000000","#FFFCFC"),
    fg_color=("#FFAE52", "#3061A4"),
    hover_color=("#D6841F", "#163D89" ),
    height=45,
    font=("Comic Sans MS", 18),
    command=trocar_tema
)
btn_tema.pack(
    side="right", padx=10, pady=10
)

frame_entrada = customtkinter.CTkFrame(
    master=janela
)
frame_entrada.pack(
    padx=10, pady=10, fill="x"
)

entrada = customtkinter.CTkEntry(
    master=frame_entrada,
    height=45,
    font=("Comic Sans MS", 20),
    text_color=("#000000","#FFFCFC"),
    placeholder_text="O que você precisa lembrar?"
)
entrada.pack(
    padx=10, pady=5, fill="x"
)

entrada_contexto = customtkinter.CTkEntry(
    master=frame_entrada,
    height=40,
    font=("Comic Sans MS", 17),
    text_color=("#000000","#FFFCFC"),
    placeholder_text="Contexto (opcional): onde deixei?"
)
entrada_contexto.pack(
    padx=10, pady=5, fill="x"
)

entrada_passo = customtkinter.CTkEntry(
    master=frame_entrada,
    height=40,
    font=("Comic Sans MS", 17),
    text_color=("#000000","#FFFCFC"),
    placeholder_text="Próximo passo (opcional)"
)
entrada_passo.pack(
    padx=10, pady=5, fill="x"
)

btn_adicionar = customtkinter.CTkButton(
    master=frame_entrada,
    text="Adicionar lembrete +",
    text_color=("#000000","#FFFCFC"),
    fg_color=("#FFAE52", "#3061A4"),
    hover_color=("#D6841F", "#163D89" ),
    height=45,
    font=("Comic Sans MS", 20),
    command=adicionar
)
btn_adicionar.pack(
    padx=10, pady=8, fill="x"
)

frame_lista = customtkinter.CTkScrollableFrame(
    master=janela,
    fg_color=("gray90", "gray10")
)
frame_lista.pack(
    padx=10, pady=10, fill="both", expand=True
)

frame_rodape = customtkinter.CTkFrame(
    master=janela,
    fg_color="transparent"
)
frame_rodape.pack(
    padx=10, pady=10, fill="x"
)

contador = customtkinter.CTkLabel(
    master=frame_rodape,
    text_color=("#000000","#FFFCFC"),
    text="Nenhum lembrete. Aproveita o descanso!",
    font=("Comic Sans MS", 20)
)
contador.pack(pady=5)

janela.mainloop()