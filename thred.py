import threading
from queue import Queue
import time


# Функція для пошуку ключових слів у файлі
def search_keywords(file_path, keywords, results):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


# Потокова обробка файлів
def thread_handler(files, keywords):
    results = {keyword: [] for keyword in keywords}
    threads = []
    for file_path in files:
        thread = threading.Thread(target=search_keywords, args=(file_path, keywords, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results


# Основна функція
def main_threading(files, keywords):
    start_time = time.time()
    results = thread_handler(files, keywords)
    print(f"Time taken: {time.time() - start_time} seconds")
    return results


# Приклад використання
files = ["file1.txt", "file2.txt", "file3.txt"]  # Список файлів
keywords = ["keyword1", "keyword2"]  # Список ключових слів
print(main_threading(files, keywords))
