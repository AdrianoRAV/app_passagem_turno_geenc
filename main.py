import flet as ft
import webbrowser  # Para abrir URLs diretamente
from datetime import datetime


class PassagemTurnoApp:
    def __init__(self, page: ft.Page):
        self.embarques = [] # para envio de whatsapp
        self.desembarques = [] # para envio de whatsapp


        def check_item_clicked(e):
            e.control.checked = not e.control.checked
            page.update()

        page.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Text(value="PASSAGEM DE TURNO", size=24, weight=ft.FontWeight.BOLD, color="black"),
            center_title=False,
            bgcolor=ft.colors.BLUE,
            actions=[
                ft.PopupMenuButton(
                    items=[
                        ft.PopupMenuItem(text="Item 1"),
                        ft.PopupMenuItem(),  # divider
                        ft.PopupMenuItem(
                            text="Checked item", checked=False, on_click=check_item_clicked
                        ),
                    ]
                ),
            ],
        )

        self.page = page
        self.page.title = "Passagem de Turno"
        self.page.vertical_alignment = ft.MainAxisAlignment.START
        self.page.window_width = 600
        self.page.window_height = 800
        self.color = {
            "primary": "#005ca9",  # Azul Correios
            "secondary": "#ffcc00",  # Amarelo Correios
            "white": "#ffffff"
        }

        self.main()

    def main(self):
        # Títulos das abas
        tab_embarque = ft.Tab(
            text="Embarque",
            content=self.criar_conteudo_embarque()
        )
        tab_desembarque = ft.Tab(
            text="Desembarque",
            content=self.criar_conteudo_desembarque()
        )
        tab_unitilizador = ft.Tab(
            text="Unitilizador",
            content=self.criar_conteudo_unitilizador()
        )
        tab_autcomplete = ft.Tab(
            text="Auto Complete",
            content=ft.Column(controls=self.card_list(),scroll=ft.ScrollMode.AUTO),
        )

        # Criando as abas
        tabs = ft.Tabs(
            tabs=[tab_embarque, tab_desembarque, tab_unitilizador, tab_autcomplete],
            selected_index=0,  # Define a aba inicial como embarque
            expand=1
        )

        # Botão para enviar via WhatsApp
        enviar_button = ft.ElevatedButton(
            text="Enviar via WhatsApp", on_click=self.enviar_whatsapp, bgcolor="#4CAF50", color="#FFFFFF"
        )

        self.page.add(tabs, enviar_button)

    def criar_conteudo_embarque(self):
        subtitulo_embarque = ft.Text(
            value="EMBARQUE", size=20, weight=ft.FontWeight.BOLD, color="black"
        )

        tabela_embarque = ft.Column(
            scroll=ft.ScrollMode.AUTO,
        )

        def adicionar_linha_embarque(e):
            linha = {
                "linha": ft.TextField(label="Nº DA LINHA", width=100),
                "turno": ft.Dropdown(
                    label="TURNO",
                    options=[
                        ft.dropdown.Option("TURNO 01"),
                        ft.dropdown.Option("TURNO 02"),
                        ft.dropdown.Option("TURNO 03"),
                    ],
                    width=100,
                ),
                "situacao": ft.Dropdown(
                    label="SITUAÇÃO",
                    options=[
                        ft.dropdown.Option("DOCA"),
                        ft.dropdown.Option("CARREGADO"),
                        ft.dropdown.Option("DESCARREGADO"),
                        ft.dropdown.Option("NÃO CHEGOU!"),
                    ],
                    width=150,
                )
            }
            tabela_embarque.controls.append(
                ft.Row(
                    controls=[linha["linha"], linha["turno"], linha["situacao"]]
                )
            )
            self.embarques.append(linha)  # Adiciona à lista de embarques
            tabela_embarque.update()

        botao_add_embarque = ft.ElevatedButton(
            text="Adicionar Linha Embarque", on_click=adicionar_linha_embarque, bgcolor="#ffcc00", color="#005ca9"
        )

        return ft.Column(
            controls=[
                subtitulo_embarque,
                botao_add_embarque,
                tabela_embarque,
            ],
            scroll=ft.ScrollMode.AUTO,  # Adiciona rolagem à coluna principal de embarque
            expand=True  # Expande para ocupar o espaço disponível
        )

    def criar_conteudo_desembarque(self):
        subtitulo_desembarque = ft.Text(
            value="DESEMBARQUE", size=20, weight=ft.FontWeight.BOLD, color="black"
        )

        tabela_desembarque = ft.Column(
            scroll=ft.ScrollMode.AUTO,
        )

        def adicionar_linha_desembarque(e):
            linha = {
                "linha": ft.TextField(label="Nº DA LINHA", width=100),
                "turno": ft.Dropdown(
                    label="TURNO",
                    options=[
                        ft.dropdown.Option("TURNO 01"),
                        ft.dropdown.Option("TURNO 02"),
                        ft.dropdown.Option("TURNO 03"),
                    ],
                    width=100,
                ),
                "situacao": ft.Dropdown(
                    label="SITUAÇÃO",
                    options=[
                        ft.dropdown.Option("DOCA"),
                        ft.dropdown.Option("CARREGADO"),
                        ft.dropdown.Option("DESCARREGADO"),
                        ft.dropdown.Option("NÃO CHEGOU!"),
                    ],
                    width=150,
                )
            }
            tabela_desembarque.controls.append(
                ft.Row(
                    controls=[linha["linha"], linha["turno"], linha["situacao"]]
                )
            )
            self.desembarques.append(linha)  # Adiciona à lista de desembarques
            tabela_desembarque.update()

        botao_add_desembarque = ft.ElevatedButton(
            text="Adicionar Linha Desembarque", on_click=adicionar_linha_desembarque, bgcolor="#ffcc00", color="#005ca9"
        )

        return ft.Column(
            controls=[
                subtitulo_desembarque,
                botao_add_desembarque,
                tabela_desembarque,

            ],
            scroll=ft.ScrollMode.AUTO,  # Adiciona rolagem à coluna principal de desembarque
            expand=True  # Expande para ocupar o espaço disponível
        )

    def criar_conteudo_unitilizador(self):


        tabela = ft.Column(
            scroll=ft.ScrollMode.AUTO,
        )

        def button_clicked(e):
            t.value = (
                f"Checkboxes values are:  {c1.value}, {c2.value}, {c3.value}, {c4.value}, {c5.value}."
            )
            #self.page.update()

        t = ft.Text()
        c1 = ft.Checkbox(label="Unchecked by default checkbox", value=False)
        c2 = ft.Checkbox(label="Undefined by default tristate checkbox", tristate=True)
        c3 = ft.Checkbox(label="Checked by default checkbox", value=True)
        c4 = ft.Checkbox(label="Disabled checkbox", disabled=True)
        c5 = ft.Checkbox(
            label="Checkbox with rendered label_position='left'", label_position=ft.LabelPosition.LEFT
        )
        b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
        #self.page.add(c1, c2, c3, c4, c5, b, t)
        return ft.Column(
            controls=[

                t,
                c1,
                c2,
                c3,
                c4,
                c5,
                b,
                tabela

            ],
            scroll=ft.ScrollMode.AUTO,  # Adiciona rolagem à coluna principal de desembarque
            expand=True  # Expande para ocupar o espaço disponível
        )

    def card_list(self):
        # Lista de títulos ou qualquer outro conteúdo variável
        items = [
            "TAMPAS COLOCADAS NO LOCAL CORRETO E ORGANIZADO",
            "LIXO SEPARADO ADEQUADAMENTE",
            "MATERIAIS RECICLADOS IDENTIFICADOS",
            "FERRAMENTAS ORGANIZADAS NO LOCAL CERTO",
            "FERRAMENTAS ORGANIZADAS NO LOCAL CERTO",
            "FERRAMENTAS ORGANIZADAS NO LOCAL CERTO",
            "FERRAMENTAS ORGANIZADAS NO LOCAL CERTO",
            "FERRAMENTAS ORGANIZADAS NO LOCAL CERTO"
        ]


        # Lista que armazenará os cartões
        cards = []

        # Loop para criar um cartão para cada item na lista
        def on_button_click(e, button_sim, button_nao):
            # Desmarcar ambos os botões antes de aplicar a seleção
            button_sim.bgcolor = None
            button_nao.bgcolor = None

            # Se o botão clicado for "SIM", marque-o
            if e.control == button_sim:
                button_sim.bgcolor = "green"
            else:
                button_nao.bgcolor = "green"

            # Atualize os botões
            button_sim.update()
            button_nao.update()

            # Loop para criar um cartão para cada item na lista

        for item in items:
            # Definindo os botões "SIM" e "NÃO"
            button_sim = ft.TextButton("SIM")
            button_nao = ft.TextButton("NÃO")

            # Definindo o comportamento dos botões ao serem clicados
            button_sim.on_click = lambda e, s=button_sim, n=button_nao: on_button_click(e, s, n)
            button_nao.on_click = lambda e, s=button_sim, n=button_nao: on_button_click(e, s, n)

            # Criando o cartão
            card = ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Icon(ft.icons.ALBUM),
                                title=ft.Text(item),
                            ),
                            ft.Row(
                                [button_sim, button_nao],
                                alignment=ft.MainAxisAlignment.END,
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                ),
            )

            # Adiciona o cartão à lista
            cards.append(card)

            # Certifique-se de que a função retorne a lista de cartões
        return cards
    def criar_auto_complete(self):


        tabela = ft.Column(
            scroll=ft.ScrollMode.AUTO,
        )

        def button_clickede(e):
             self.page.add(
                  ft.AutoComplete(
                    suggestions=[
                        ft.AutoCompleteSuggestion(key="one 1", value="One"),
                        ft.AutoCompleteSuggestion(key="two 2", value="Two"),
                        ft.AutoCompleteSuggestion(key="three 3", value="Three"),
                    ],
                    on_select=lambda e: print(e.control.selected_index, e.selection),
                )
            )


        #self.page.add(c1, c2, c3, c4, c5, b, t)
        return ft.Column(
            controls=[



            ],
            scroll=ft.ScrollMode.AUTO,  # Adiciona rolagem à coluna principal de desembarque
            expand=True  # Expande para ocupar o espaço disponível
        )


    def enviar_whatsapp(self, e):
        # Formatar embarques e desembarques
        mensagem = "Passagem de Turno:\n\n"
        mensagem += "Embarques:\n"
        for embarque in self.embarques:
            mensagem += f"Linha: {embarque['linha'].value}, Turno: {embarque['turno'].value}, Situação: {embarque['situacao'].value}\n"

        mensagem += "\nDesembarques:\n"
        for desembarque in self.desembarques:
            mensagem += f"Linha: {desembarque['linha'].value}, Turno: {desembarque['turno'].value}, Situação: {desembarque['situacao'].value}\n"

        # Usar URL wa.me para enviar a mensagem via WhatsApp
        numero_telefone = "+5531988342368"  # Substitua pelo número de telefone desejado
        mensagem_url = mensagem.replace("\n", "%0A")  # Substituir quebras de linha pela codificação da URL
        whatsapp_url = f"https://wa.me/{numero_telefone}?text={mensagem_url}"
        webbrowser.open(whatsapp_url)


# Iniciar o app
if __name__ == "__main__":
    ft.app(target=PassagemTurnoApp)


