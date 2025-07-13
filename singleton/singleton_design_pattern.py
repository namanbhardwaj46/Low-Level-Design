import threading

class dbconn:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            with cls.__lock:
                if cls.__instance is None:
                    cls.__instance = super(dbconn, cls).__new__(cls)

        return cls.__instance


dbcon1 = dbconn()
dbcon2 = dbconn()

print(dbcon1)
print(dbcon2)

# TODO: Create objects of dbconn in multiple threads and verify that they are the same instance.