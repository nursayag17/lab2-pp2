import os
import nbformat as nbf

# Папка, где лежат файлы .py
source_folder = "."
# Папка для сохранения файлов .ipynb
output_folder = "notebooks"

# Создаём папку для .ipynb, если её ещё нет
os.makedirs(output_folder, exist_ok=True)

# Получаем список всех файлов в папке
files = os.listdir(source_folder)
print("Файлы в папке:", files)  # Проверка списка файлов

# Проходим по всем .py файлам в папке
for filename in files:
    if filename.endswith(".py") and filename != "convert_to_ipynb.py":  # Исключаем сам скрипт
        input_path = os.path.join(source_folder, filename)
        output_path = os.path.join(output_folder, filename.replace(".py", ".ipynb"))

        # Читаем содержимое файла .py
        with open(input_path, "r") as f:
            code = f.read()

        # Создаём Jupyter Notebook
        notebook = nbf.v4.new_notebook()
        notebook.cells = [nbf.v4.new_code_cell(code)]

        # Сохраняем как .ipynb
        with open(output_path, "w") as f:
            nbf.write(notebook, f)

        print(f"{filename} -> {output_path}")

print("Конвертация завершена! Все файлы сохранены в папке:", output_folder)
