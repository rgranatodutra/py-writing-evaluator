# Pipeline ETL para Avaliação de Redações

Este projeto consiste em um Pipeline ETL (Extração, Transformação e Carregamento) em Python, projetado para extrair redações de um arquivo TXT e gerar avaliações com a ajuda do ChatGPT.

## Instruções de Uso

Siga estas etapas para utilizar a aplicação:

1. **Inserção de Redação**:
   - Coloque a redação que você deseja avaliar em um arquivo de texto (.txt).
   - Certifique-se de que cada parágrafo esteja separado por uma linha vazia. Veja um exemplo:

     ```
     Parágrafo 1 ...

     Parágrafo 2 ...

     Parágrafo 3 ...
     ```

2. **Execução do Programa**:
   - Abra o terminal.
   - Navegue até o diretório raiz do projeto.
   - Execute o seguinte comando para iniciar o processo de avaliação:

     ```
     python main.py
     ```

   - O programa solicitará que você selecione o arquivo de redação que deseja avaliar.

3. **Resultado**:
   - O resultado da avaliação será gerado e salvo na pasta `/results`.

Agora você pode utilizar esta aplicação para avaliar redações de forma eficiente.

## Instalando as Dependências

Siga estas etapas para configurar o ambiente e instalar as dependências necessárias:

1. Crie um ambiente virtual (venv) executando o seguinte comando:

   ```
   python -m venv venv
   ```
2. Ative o ambiente virtual:

- No Windows:

  ```
  venv\Scripts\activate
  ```

- No macOS e Linux:

  ```
  source venv/bin/activate
  ```

3. Instale as dependências do projeto executando o seguinte comando:

   ```
   pip install -r requirements.txt
   ```
   
Agora você tem o ambiente configurado e todas as dependências instaladas para executar o projeto.

Aproveite!

