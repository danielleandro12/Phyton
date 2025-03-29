import flet as ft
import requests
import os
import time

# Configuração da API Groq - REMOVA SUA CHAVE ANTES DE COMPARTILHAR O CÓDIGO
GROQ_API_KEY = os.getenv("GROQ_API_KEY") or "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def ler_arquivo_texto(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Erro ao ler arquivo: {str(e)}"

def resposta_chatbot(mensagem, contexto_arquivo=None, model="llama3-70b-8192", temperature=0.7):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    # Construir o payload corretamente
    messages = [{
        "role": "system",
        "content": "Você é um assistente útil que pode analisar textos e arquivos. "
                   "Se fornecido com um arquivo, você pode resumir ou responder perguntas sobre ele."
    }]
    
    # Adicionar contexto do arquivo como mensagem do usuário se existir
    if contexto_arquivo and ("arquivo" in mensagem.lower() or 
                            "resum" in mensagem.lower() or 
                            "analis" in mensagem.lower()):
        messages.append({
            "role": "user",
            "content": f"Por favor, analise este texto:\n\n{contexto_arquivo}\n\nPergunta: {mensagem}"
        })
    else:
        messages.append({
            "role": "user",
            "content": mensagem
        })
    
    payload = {
        "messages": messages,
        "model": model,
        "temperature": temperature,
        "max_tokens": 4096
    }
    
    try:
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)
        
        # Verificar erros na resposta
        if response.status_code != 200:
            error_detail = response.json().get("error", {}).get("message", "Erro desconhecido")
            return f"Erro na API (HTTP {response.status_code}): {error_detail}"
        
        resposta_api = response.json()
        return resposta_api["choices"][0]["message"]["content"]
    
    except requests.exceptions.RequestException as e:
        return f"Erro de conexão: {str(e)}"
    except Exception as e:
        return f"Erro ao processar resposta: {str(e)}"

def main(page: ft.Page):
    page.title = "ChatBot Groq com Upload de Arquivos"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    
    # Variáveis de estado
    conteudo_arquivo = None
    nome_arquivo = None
    
    # Elementos da interface
    chat_box = ft.ListView(expand=True, spacing=10, auto_scroll=True)
    
    text_input = ft.TextField(
        label="Digite sua mensagem ou comando",
        multiline=True,
        min_lines=1,
        max_lines=5,
        expand=True,
    )
    
    # Upload de arquivo
    def pick_files_result(e: ft.FilePickerResultEvent):
        nonlocal conteudo_arquivo, nome_arquivo
        if e.files:
            try:
                file_path = e.files[0].path
                nome_arquivo = e.files[0].name
                conteudo_arquivo = ler_arquivo_texto(file_path)
                
                if len(conteudo_arquivo) > 100000:  # Limite de ~100k caracteres
                    chat_box.controls.append(
                        ft.Container(
                            ft.Text("Arquivo muito grande (limite: 100k caracteres)", color=ft.colors.RED),
                            padding=10
                        )
                    )
                    conteudo_arquivo = None
                else:
                    chat_box.controls.append(
                        ft.Container(
                            ft.Text(f"✅ Arquivo carregado: {nome_arquivo} ({len(conteudo_arquivo)} caracteres)", 
                                   color=ft.colors.BLUE_800),
                            bgcolor=ft.colors.BLUE_50,
                            padding=10,
                            border_radius=10,
                        )
                    )
                page.update()
            except Exception as e:
                chat_box.controls.append(
                    ft.Container(
                        ft.Text(f"Erro ao carregar arquivo: {str(e)}", color=ft.colors.RED),
                        padding=10
                    )
                )
                page.update()
    
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    
    upload_button = ft.ElevatedButton(
        "📁 Upload Arquivo",
        on_click=lambda _: pick_files_dialog.pick_files(
            allowed_extensions=["txt", "md", "csv", "json", "log"],
            allow_multiple=False
        ),
    )
    
    # Envio de mensagem
    def enviar_mensagem(e):
        nonlocal conteudo_arquivo, nome_arquivo
        
        if not text_input.value.strip():
            return
            
        user_message = text_input.value
        text_input.value = ""
        
        # Adicionar mensagem do usuário
        chat_box.controls.append(
            ft.Container(
                ft.Text(f"Você: {user_message}", color=ft.colors.BLUE_800),
                bgcolor=ft.colors.BLUE_100,
                padding=10,
                border_radius=10,
            )
        )
        page.update()
        
        # Indicador de processamento
        typing_indicator = ft.Container(
            ft.Row([
                ft.ProgressRing(width=16, height=16, stroke_width=2),
                ft.Text("Processando...", italic=True, color=ft.colors.GREY)
            ], spacing=5),
            padding=10
        )
        chat_box.controls.append(typing_indicator)
        page.update()
        
        # Obter resposta
        start_time = time.time()
        bot_response = resposta_chatbot(user_message, conteudo_arquivo)
        elapsed_time = time.time() - start_time
        
        # Remover indicador e mostrar resposta
        chat_box.controls.remove(typing_indicator)
        
        chat_box.controls.append(
            ft.Column([
                ft.Container(
                    ft.Text(f"🤖 Bot: {bot_response}", color=ft.colors.GREEN_800),
                    bgcolor=ft.colors.GREEN_100,
                    padding=10,
                    border_radius=10,
                ),
                ft.Text(f"⏱️ {elapsed_time:.2f} segundos", size=10, color=ft.colors.GREY)
            ], spacing=5)
        )
        page.update()
    
    send_button = ft.ElevatedButton(
        "📤 Enviar",
        icon=ft.icons.SEND,
        on_click=enviar_mensagem,
    )
    
    # Limpar chat
    def limpar_chat(e):
        nonlocal conteudo_arquivo, nome_arquivo
        chat_box.controls.clear()
        conteudo_arquivo = None
        nome_arquivo = None
        page.update()
    
    clear_button = ft.ElevatedButton(
        "🧹 Limpar",
        on_click=limpar_chat,
    )
    
    # Layout
    page.add(
        ft.Column([
            ft.Text("ChatBot Groq - Análise de Texto", 
                   size=24, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_800),
            
            ft.Container(
                chat_box,
                expand=True,
                padding=10,
                border=ft.border.all(1, ft.colors.GREY_300),
                border_radius=10,
                margin=ft.margin.only(bottom=10)
            ),
            
            ft.Row([upload_button, clear_button], spacing=10),
            
            ft.Row([
                text_input,
                ft.IconButton(icon=ft.icons.SEND, on_click=enviar_mensagem)
            ], spacing=5)
        ], expand=True)
    )

if __name__ == "__main__":
    ft.app(target=main)
