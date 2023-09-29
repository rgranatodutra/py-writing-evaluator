def read_writing(path: str) -> str | None:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        content_lines = len(content.split("\n"))

        if content_lines in range(7, 31):
            return content
        else:
            print("A redação deve ter entre 7 e 30 linhas.")
