# Script para automação de transferência de dados

## Objetivo
O script Python realiza captura de dados em uma aplicação, tratamento e e armazenazenamento em arquivo CSV.
Seu funcionamento baseia-se na simulação de clicks do usuário para copiar os dados do software e transferí-los de maneira ordenada para uma planilha.



## Requisitos

### Dependências:
1. **Python 3.8 ou superior**: Certifique-se de que o Python está instalado no seu computador.
2. **Bibliotecas Python**: Instale as seguintes bibliotecas antes de usar o script:
    - `pyautogui`
    - `pyperclip`
    - `pandas`
    - `re`

### Instalação de Bibliotecas:
Abra o terminal ou prompt de comando e digite:

```bash
pip install pyautogui pyperclip pandas
```


## Instruções para Utilizar o Script

### Passo 1: Navegar até o Diretório do Script
1. Localize a pasta onde o script Python foi salvo (Exemplo: D:\analise_dados\analise_biopac).
2. Abra o terminal ou prompt de comando.
3. Use o comando `cd` para navegar até a pasta do script.

#### Exemplo:
Se o script está em `C:\Usuarios\SeuNome\Projetos`, execute:
```bash
cd C:\Usuarios\SeuNome\Projetos
```

### Passo 2: Executar o Script
Para executar o script, dentro da pasta específica, digite no terminal:
```bash
python automatic_transfer.py
```



## Determinação dos Pontos de Clique do Mouse
Ao iniciar o script, ele perguntará onde clicar para capturar os dados da aplicação. Este processo é essencial para garantir que o script funcione corretamente.

### Etapas:
1. Abra o software do qual os dados serão copiados em janela grande e o termial em janela pequena.
2. Quando solicitado, posicione o mouse sobre o **botão ou área** onde o clique deve ser feito.
3. Pressione **ENTER** no teclado para capturar as coordenadas do mouse.
4. Repita o processo, posicionanando o mouse no local onde aparece a opção "Copy to Clipboard" 

O local capturado será salvo e usado automaticamente durante toda a execução do script.

Obs: Essa etapa pode ser evitada caso o local de click seja pré-definido. Para utilizar essa opção altere a *linha 10* do script para `flag_escolha_local = True` e defina os valores fixos nas *linhas 15 e 16*

```bash
 8 ############################################################################################
 9 
10 flag_escolha_local = True                   # True ou False
11
12 ############################################################################################
```

## Operação

### Criar Novo Arquivo ou Continuar Com Existente
Quando o script for iniciado, ele perguntará o nome do arquivo CSV.

   - Se o arquivo **não existir**, um novo arquivo será criado com o nome informado.
   - Se o arquivo **já existir**, o script carregará o arquivo existente e continuará adicionando colunasd de dados a ele.



### Captura e Armazenamento de Dados
1. Inicie o script e caso necessário, aponte os locais a serem clicados.
2. Escolha `c` quando solicitado para capturar novos dados.
3. Informe o **nome da nova coluna** onde os valores serão armazenados.
4. O script realizará os cliques necessários e copiará os dados.
5. Os dados serão processados e salvos no arquivo CSV.

### Encerramento
- Para encerrar o script, digite `s` quando solicitado.
- O arquivo CSV atualizado será salvo automaticamente antes do fechamento do programa.



## Estrutura do Arquivo CSV
O arquivo gerado terá a seguinte estrutura:

| Variáveis    | Nome_Coluna_1 | Nome_Coluna_2 |
|---------------|---------------|---------------|
| Variável_1   | Valor_1       | Valor_2       |
| Variável_2   | Valor_3       | Valor_4       |

- A coluna `Variáveis` contém os nomes das variáveis capturadas.
- Cada nova captura adiciona uma **nova coluna de valores** ao arquivo existente.



## Dicas e Solução de Problemas
1. **Erros ao Capturar Coordenadas:** Certifique-se de pressionar ENTER quando o mouse estiver posicionado corretamente.
2. **Excel Não Reconhece Colunas:** Verifique o delimitador utilizado no arquivo CSV. Use `,` ou `;` conforme as configurações regionais do seu sistema.
3. **Reiniciar o Processo:** Se algo der errado, pressione `Ctrl + C` no terminal para parar o script e recomeçar.
4. **Espaço para click:** Lembre-se o script está simulando clicks na tela do computador, ele não está atrelado ao programa que contém os dados, portanto é importante que não existam janelas sobrepondo **o lugar que receberá o click**, podem existir janelas em outros lugares.



## Suporte
Em caso de bugs ou alterações necessárias contate: [gmcamargo@gmail.com](mailto:gmcamargo@gmail.com)
