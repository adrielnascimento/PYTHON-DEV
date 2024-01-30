# chat
    # usuario entrou no chat
    # Mensagens do usuário

import flet as ft

def main(pagina): 
    #titulo
    texto = ft.Text('ProZap')
    nome_usuario = ft.TextField(label='Escreva seu nome')
    def enviar_msg(evento):
        texto_mensagen = enviar_mensagem.value
        chat.controls.append(ft.Text(f'{nome_usuario.value}: {texto_mensagen}'))
        pagina.update()
        
    enviar_mensagem = ft.TextField(label='Escreva sua mensagem aqui',
                                   on_submit=enviar_msg)

    botao_enviar = ft.ElevatedButton('enviar', on_click=enviar_msg)

    chat = ft.Column()

    def entrar_chat(evento): 
        popup.open = False
        pagina.add(chat)
        linha_mensagem = ft.Row([enviar_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        pagina.remove(botao_iniciar)
        popup.update()

    #criar popup
    popup = ft.AlertDialog(open=False,
                            modal=True,
                            title=ft.Text("Bem vindo ao ProZAp"),
                            content=nome_usuario,
                            actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)])
    

    #funçao do botao para entrar no popup
    def iniciar_chat(evento): #por padrão a funçao que esta no on_click do botão recebe como parametro um evento
        pagina.dialog = popup
        popup.open = True
        pagina.update()# para atualizar a pagina


    #criar botao
    botao_iniciar = ft.ElevatedButton("iniciar chat", on_click= iniciar_chat)
    
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(main)
#ft.app(main, view=ft.WEB_BROWSER)