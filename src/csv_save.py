import os

class CsvSave:
    def __init__(self):
        self.saves = []
        self.directory = './csv_files'
        os.makedirs(self.directory, exist_ok=True)  

    def add_save(self, data_frame, name):
        self.saves.append((data_frame, name))

    def save(self):
        for data_frame, name in self.saves:
            filename = os.path.join(self.directory, f'output_{name}.csv')
            data_frame.to_csv(filename, index=False)