class CPU:
    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def __repr__(self):
        return f'CPU({self.name}, {self.brand}'


class Memory:
    def __init__(self, memory_type, capacity):
        self.type = memory_type
        self.capacity = capacity

    def __repr__(self):
        return f'Memory of type:{self.type} and capacity: {self.capacity}'


class Monitor:
    def __init__(self, size, resolution, color_accuracy):
        self.size = size
        self.resolution = resolution
        self.color_accuracy = color_accuracy

    def __repr__(self):
        return f'Monitor with size:{self.size}, resolution:{self.resolution}, color accuracy:{self.color_accuracy}'


class Battery:
    def __init__(self, battery_type, capacity, cell_voltage):
        self.type = battery_type
        self.capacity = capacity
        self.cell_voltage = cell_voltage

    def __repr__(self):
        return f"The type of battery is {self.type}, capacity is {self.capacity} and cell_voltage is {self.cell_voltage}"


class Camera:
    def __init__(self, camera_pixels, pixel_size, iso, hdr, motion):
        self.pixels = camera_pixels
        self.pixel_size = pixel_size
        self.ISO = iso
        self.HDR = hdr
        self.motion = motion

    def __repr__(self):
        return (f"This camera has {self.pixels} pixels with size {self.pixel_size}, it "
                f"{"has" if self.ISO else "has not"} ISO, and {"has" if self.HDR else "has not"} HDR, and"
                f" {"has slow-motion and high-speed" if self.motion else "has not slow-motion and high-speed"}")


class SmartPhone:
    def __init__(self, cpu, memory, monitor, battery, camera, agi_hardware, water_resistance, starlink_connection, vr):
        self.cpu = cpu
        self.memory = memory
        self.monitor = monitor
        self.battery = battery
        self.camera = camera
        self.agi_hardware = agi_hardware
        self.water_resistance = water_resistance
        self.starlink_connection = starlink_connection
        self.vr = vr

    def __repr__(self):
        return (f"This smart phone uses {self.cpu} cpu, {self.memory} memory size, with {self.monitor} monitor,"
                f"{self.battery} battery, and {self.camera} for front camera and {self.camera} for back camera,"
                f"this phone {"supports" if self.agi_hardware else "does not supports"} agi hardware, "
                f"{"is" if self.water_resistance else "is not"} water resistance, "
                f"{"supports" if self.starlink_connection else "does not supports"} starlink connection, "
                f"and {"supports too" if self.vr else "does not supports"} virtual reality.")


