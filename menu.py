import os

files = os.listdir("./extract")
writings = [w for w in files if w.endswith(".txt")]

def select_menu():
    options = ["Saír"] + writings
    is_running = True
    print(f'Selecione a redação que você deseja calcular a nota:')

    for number, option in enumerate(options):
        print(f'{number} - {option}')

    while is_running:
        selected_value = input()
        invalid_option_text = "Opção inválida, selecione um dos números listados..."
    
        if not selected_value.isnumeric():
            print(invalid_option_text)
            continue
        elif not(int(selected_value) >= 0 and int(selected_value) < len(options)):
            print(invalid_option_text)
            continue
        else:
            is_running = False
            return options[int(selected_value)]