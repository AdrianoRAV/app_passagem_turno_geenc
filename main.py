import flet as ft


class PassagemTurnoApp:
    def __init__(self, page: ft.Page):
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

        # Criando as abas
        tabs = ft.Tabs(
            tabs=[tab_embarque, tab_desembarque],
            selected_index=0,  # Define a aba inicial como embarque
        )

        self.page.add(tabs)

    def criar_conteudo_embarque(self):
        subtitulo_embarque = ft.Text(
            value="EMBARQUE", size=20, weight=ft.FontWeight.BOLD, color="black"
        )

        tabela_embarque = ft.Column(
            scroll=ft.ScrollMode.AUTO,
        )

        def adicionar_linha_embarque(e):
            tabela_embarque.controls.append(
                ft.Row(
                    controls=[
                        ft.TextField(label="Nº DA LINHA", width=100),
                        ft.Dropdown(
                            label="TURNO",
                            options=[
                                ft.dropdown.Option("TURNO 01"),
                                ft.dropdown.Option("TURNO 02"),
                                ft.dropdown.Option("TURNO 03"),
                            ],
                            width=100,
                        ),
                        ft.Dropdown(
                            label="SITUAÇÃO",
                            options=[
                                ft.dropdown.Option("DOCA"),
                                ft.dropdown.Option("CARREGADO"),
                                ft.dropdown.Option("DESCARREGADO"),
                                ft.dropdown.Option("NÃO CHEGOU!"),
                            ],
                            width=150,
                        ),
                    ]
                )
            )
            tabela_embarque.update()

        botao_add_embarque = ft.ElevatedButton(
            text="Adicionar Linha Embarque", on_click=adicionar_linha_embarque, bgcolor="#ffcc00", color="#005ca9"
        )

        return ft.Column(
            controls=[
                subtitulo_embarque,
                botao_add_embarque,
                tabela_embarque,
            ]
        )

    def criar_conteudo_desembarque(self):
        subtitulo_desembarque = ft.Text(
            value="DESEMBARQUE", size=20, weight=ft.FontWeight.BOLD, color="black"
        )

        tabela_desembarque = ft.Column(
            scroll=ft.ScrollMode.AUTO,
        )

        def adicionar_linha_desembarque(e):
            tabela_desembarque.controls.append(
                ft.Row(
                    controls=[
                        ft.TextField(label="Nº DA LINHA", width=100),
                        ft.Dropdown(
                            label="TURNO",
                            options=[
                                ft.dropdown.Option("TURNO 01"),
                                ft.dropdown.Option("TURNO 02"),
                                ft.dropdown.Option("TURNO 03"),
                            ],
                            width=100,
                        ),
                        ft.Dropdown(
                            label="SITUAÇÃO",
                            options=[
                                ft.dropdown.Option("DOCA"),
                                ft.dropdown.Option("CARREGADO"),
                                ft.dropdown.Option("DESCARREGADO"),
                                ft.dropdown.Option("NÃO CHEGOU!"),
                            ],
                            width=150,
                        ),
                    ]
                )
            )
            tabela_desembarque.update()

        botao_add_desembarque = ft.ElevatedButton(
            text="Adicionar Linha Desembarque", on_click=adicionar_linha_desembarque, bgcolor="#ffcc00", color="#005ca9"
        )

        return ft.Column(
            controls=[
                subtitulo_desembarque,
                botao_add_desembarque,
                tabela_desembarque,
            ]
        )


# Iniciar o app
if __name__ == "__main__":
    ft.app(target=PassagemTurnoApp)
