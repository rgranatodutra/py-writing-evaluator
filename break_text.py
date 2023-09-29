from dotenv import load_dotenv
import os

load_dotenv()
line_len = int(os.getenv("MAXIMUM_LINE_LENGTH"))

def break_text(txt: str):

    paragraphs = []

    for paragraph in txt.split("\n\n"):
        words = paragraph.split(" ")
        lines = []
        current_line = []

        for word in words:
            if sum(len(w) for w in current_line) + len(word) + len(current_line) <= line_len:
                current_line.append(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]

        if current_line:
            lines.append(" ".join(current_line))

        paragraphs.append("\n".join(lines))

    return "\n".join(paragraphs)