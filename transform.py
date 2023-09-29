from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def calculate_writing_grade(content: str, theme: str) -> str:
    PROMPT_ROLE = """ Você é um corretor do ENEM e deve fazer a correção da prova de redação
do ENEM considerando cinco competências

1. Domínio da norma padrão da língua escrita

2. Compreensão da proposta de redação e aplicação de conceitos 
das várias áreas do conhecimento para o desenvolvimento do tema 
nos limites estruturais do texto dissertativo-argumentativo

3. Capacidade de selecionar, relacionar, organizar e interpretar 
informações, fatos, opiniões e argumentos em defesa de um ponto 
de vista

4. Conhecimento dos mecanismos linguísticos necessários à 
construção da argumentação

5. Elaboração de proposta de intervenção para o problema 
abordado, respeitados os direitos humanos.

A pontuação atribuída a cada competência pode variar até 200 pontos. 
A nota máxima da redação é de mil pontos. 
"""
    PROMPT_USER = f"Corrija minha redação, do tema: {theme}\n{content}"

    try:
        print("Gerando resposta...")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": PROMPT_ROLE
                }, 
                {
                    "role": "user",
                    "content": PROMPT_USER
                }
            ]
        )

        return completion.choices[0].message.content
    except Exception as e:
        input_key = input("Erro durante a requisição com o ChatGPT. Digite \"e\" para mostrar o erro ou qualquer tecla para sair.")
        if input_key == "e":
            print(e)
