from abc import ABC


class Transportation(ABC):
    def deliver(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class Packaging(ABC):
    def pack(self):
        raise NotImplementedError("This method should be overridden by subclasses")


 # concreate objects..
class Truck(Transportation):
    def deliver(self):
        return "Delivering by land in a box"

class Ship(Transportation):
    def deliver(self):
        return "Delivering by sea in a container"

class Airplane(Transportation):
    def deliver(self):
        return "Delivering by air in a package"


class Auto(Transportation):
    def deliver(self):
        return "Delivering by road in a vehicle"


class Box(Packaging):
    def pack(self):
        return "Packing in a box"

class Container(Packaging):
    def pack(self):
        return "Packing in a container"


class LogisticFactoryAbc(ABC):
    @staticmethod
    def create_transportation(type):
        raise NotImplementedError("This method should be overridden by subclasses")

    @staticmethod
    def create_packaging():
        raise NotImplementedError("This method should be overridden by subclasses")


class RoadFactory(LogisticFactoryAbc):
    @staticmethod
    def create_transportation(type):
        if type == "truck":
            return Truck()
        elif type == "auto":
            return Auto()
        else:
            return None

    @staticmethod
    def create_packaging():
            return Box()

class SeaFactory(LogisticFactoryAbc):
    @staticmethod
    def create_transportation(type):
        if type == "ship":
            return Ship()
        else:
            return None

    @staticmethod
    def create_packaging():
            return Container()


class LogisticProvider:
    @staticmethod
    def getFactory(type):
        if type == "road":
            return RoadFactory()
        elif type == "sea":
            return SeaFactory()
        else:
            raise ValueError("Unknown logistics type")


if __name__ == "__main__":
    transport_way = "sea"
    factory = LogisticProvider.getFactory(transport_way)
    packaging = factory.create_packaging()
    transport = factory.create_transportation("ship")

    print(packaging.pack())
    print(transport.deliver())


#  TODO: Create a button class that implements like a flutter code...
#   1. create a Flutterfactory
#   2. return a android and ios factory
#   3. create a button in android and ios factory
#   4. return a button in android and ios factory