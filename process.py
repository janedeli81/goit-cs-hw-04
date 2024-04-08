from multiprocessing import Process, Queue, Manager
import time


# Функція для пошуку ключових слів у файлі
def search_keywords(file_path, keywords, results):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    if keyword not in results:
                        results[keyword] = []
                    results[keyword].append(file_path)
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")


# Процесорна обробка файлів
def process_handler(files, keywords, results):
    processes = []
    for file_path in files:
        process = Process(target=search_keywords, args=(file_path, keywords, results))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


# Основна функція
def main_multiprocessing(files, keywords):
    with Manager() as manager:
        start_time = time.time()
        results = manager.dict()
        process_handler(files, keywords, results)
        print(f"Time taken: {time.time() - start_time} seconds")
        return dict(results)


# Приклад використання
files = ["file1.txt", "file2.txt", "file3.txt"]  # Список файлів
keywords = ["keyword1", "keyword2"]  # Список ключових слів
print(main_multiprocessing(files, keywords))
