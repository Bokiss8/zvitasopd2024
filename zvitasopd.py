import os
import shutil
import re


def process_files(source_dir, dest_dir, target_month):
    # Создаем каталог назначения, если его нет
    dest_base_dir = os.path.join(dest_dir, f"month_{target_month}")
    os.makedirs(dest_base_dir, exist_ok=True)

    # Регулярное выражение для проверки правильности имени файла
    filename_pattern = re.compile(r'^(\d{4})(\d{2})(\d{4})(\d{2})\.CSV$')

    files_found = False  # Флаг для проверки наличия файлов

    for target_code in [f"{i:02d}" for i in range(1, 18)]:
        dest_subdir = os.path.join(dest_base_dir, target_code)
        os.makedirs(dest_subdir, exist_ok=True)

        # Получаем список файлов в исходном каталоге
        files = os.listdir(source_dir)

        for filename in files:
            match = filename_pattern.match(filename)
            if match:
                district_code, file_month, file_year, file_code = match.groups()

                # Проверяем совпадение месяца и кода помощи
                if int(file_month) == target_month and file_code == target_code:
                    source_path = os.path.join(source_dir, filename)
                    dest_path = os.path.join(dest_subdir, filename)

                    # Перемещаем файл в каталог назначения
                    shutil.move(source_path, dest_path)
                    print(f"Файл {filename} перемещен в {dest_subdir}")

                    files_found = True

    if not files_found:
        print(f"Не найдено файлов для месяца {target_month}")


if __name__ == "__main__":
    source_directory = r"D:\time_export"
    destination_directory = r"D:\time_export"

    # Запрос у пользователя ввода месяца
    target_month = int(input("Введите месяц (в формате от 1 до 12): "))

    process_files(source_directory, destination_directory, target_month)
