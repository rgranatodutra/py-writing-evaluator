from menu import select_menu
from extract import read_writing
from transform import calculate_writing_grade
from load import save_result

def execute():
    writing_content = None

    while not writing_content:
        filename = select_menu()
        file_path = "./extract/" + filename
        writing_content = read_writing(file_path)
        
    writing_theme = input("Digite o titulo do tema da redação: ")
    writing_grade = calculate_writing_grade(writing_content, writing_theme)
    result_path = save_result(filename, writing_grade)

    print(f"A avaliação foi salva em: {result_path}")

execute()