
class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.aiProcessor = None


    def set_gpu(self, gpu):
        self.gpu = gpu

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_storage(self, storage):
        self.storage = storage

    def set_aiProcessor(self, aiProcessor):
        self.aiProcessor = aiProcessor