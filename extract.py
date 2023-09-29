import break_text as bt

def read_writing(path: str):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        break_content = bt.break_text(content)
        content_lines = len(break_content.split("\n"))

        if content_lines in range(7, 31):
            return break_content
        else:
            print("A redação deve ter entre 7 e 30 linhas.")
            return None
