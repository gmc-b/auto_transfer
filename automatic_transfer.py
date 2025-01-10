import pyautogui
import pyperclip
import pandas as pd
import time
import os
import re

############################################################################################

flag_escolha_local = False # True ou False

############################################################################################


COORD_CAIXA = (220, 158)
COORD_COPY = (272, 192)


def obter_local_clique():
    # Pergunta ao usuário o local de clique e retorna as coordenadas.
    print("Posicione o mouse primeiro retângulo branco com o valor desejado.")
    input("Pressione ENTER quando estiver pronto...")
    x_esq, y_esq = pyautogui.position()
    print(f"Local de clique capturado: ({x_esq}, {y_esq})\n")
    
    print("Clique com o botão direito e posicione o mouse sobre 'copy to clipboard'.")
    input("Pressione ENTER quando estiver pronto...")
    x_dir, y_dir = pyautogui.position()
    print(f"Local de clique capturado: ({x_dir}, {y_dir})\n")

    return (x_esq, y_esq), (x_dir, y_dir)


def processar_dados(nome_coluna, clique_caixa, clique_copy, df):
    
    # Processa os dados copiados e adiciona ao DataFrame.
    # ->param nome_coluna: Nome da nova coluna de valores.
    # ->param local_clique: Tupla com as coordenadas (x, y) para o clique.
    # ->param df: DataFrame existente.
    # ->return: DataFrame atualizado.
    
    # Realiza o clique com o botão esquerdo para trocar de janela
    pyautogui.click(clique_caixa, button="left")
    time.sleep(0.2)  # Aguardar a troca de janela

    # Realiza o clique com o botão direito para liberar a opção "Copy to Clipboard"
    pyautogui.click(clique_caixa, button="right")
    time.sleep(1)  # Aguardar a interface carregar

    # Realiza o clique com o botão esquerdo para clical em "Copy to Clipboard"
    pyautogui.click(clique_copy, button="left")
    time.sleep(0.5)  # Aguardar a interface carregar

    # Copia os dados para o clipboard

    #pyautogui.hotkey("ctrl", "c")
    #time.sleep(1)  # Aguardar a cópia ser realizada

    # Obtém os dados copiados
    dados_copiados = pyperclip.paste().strip('"')

    regex_horario_ano = r".*?\d{2}:\d{2}:\d{2} 20\d{2}"

    # Substituir tudo antes do horário e ano por vazio
    dados_processados = re.sub(regex_horario_ano, "", dados_copiados)

    print("Dados copiados do clipboard com sucesso.\n")

    # Processa os dados
    linhas = dados_processados.split("\n")
    novos_dados = {}
    for item in linhas:
        if "=" in item:
            variavel, valor = item.split("=")
            variavel = variavel.strip()
            valor = valor.strip()
            novos_dados[variavel] = valor

    # Garante que todas as variáveis estejam no DataFrame
    for chave in novos_dados.keys():
        if chave not in df["Variáveis"].values:
            df = pd.concat([df, pd.DataFrame([[chave]], columns=["Variáveis"])], ignore_index=True)

    # Adicionar a nova coluna de valores
    df[nome_coluna] = df["Variáveis"].map(novos_dados)
    return df


def main():
    # Pergunta o nome do arquivo CSV
    nome_arquivo = input("Digite o nome do arquivo CSV a ser criado (sem extensão): ") + ".csv"

    # Carrega ou criar o DataFrame
    if os.path.exists(nome_arquivo):
        df = pd.read_csv(nome_arquivo)
        print(f"Arquivo {nome_arquivo} carregado com sucesso.\n")
    else:
        df = pd.DataFrame(columns=["Variáveis"])
        print(f"Novo arquivo {nome_arquivo} será criado.\n")

    # Captura o local de clique
    if flag_escolha_local:
        clique_caixa, clique_copy = obter_local_clique()
    else:
        clique_caixa, clique_copy = COORD_CAIXA ,COORD_COPY 

    # Loop principal para coletar dados
    while True:
        comando = input("Digite 'c' para capturar dados ou 's' para sair: ").lower()

        if comando == "c":
            nome_coluna = input("Digite o nome da nova coluna de valores: ")
            if nome_coluna in df.columns:
                print(f"A coluna '{nome_coluna}' já existe. Escolha outro nome.")
                continue
            print("Clique em 1 segundos...\n")
            time.sleep(1)

            df = processar_dados(nome_coluna, clique_caixa, clique_copy, df)
            # Salvar o DataFrame no arquivo
            df.to_csv(nome_arquivo, index=False)
            print(f"Dados salvos no arquivo: {nome_arquivo}")
        elif comando == "s":
            print("Finalizando o programa.")
            break
        else:
            print("Comando inválido. Tente novamente.")


if __name__ == "__main__":
    main()
