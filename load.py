from datetime import datetime

def save_result(filename: str, result: str):
    current_date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    result_filename = f"{current_date}_{filename}"
    result_path = f"./results/{result_filename}"

    with open(result_path, "w") as result_file:
        result_file.write(result)
        
        return result_path