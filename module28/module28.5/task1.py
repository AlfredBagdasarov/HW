class File:
    def __init__(self, file_name, mode):
        print('Начинаю работу!')
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True


with File('example.txt', 'w') as file:
    file.write('Всем привет!')