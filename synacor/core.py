# core vm components

class StopVirtualMachine(Exception):
    '''thrown to signal program termination'''

class ROM():
    def __init__(self, data, size = None):
        self.memory = data
        byte_count = size if size is not None else len(data)
        if byte_count % 2 > 0:
            raise ValueError('byte count must be a multiple of 2')
        self.size = byte_count // 2
        self.offset = 0

    def read(self, address):
        if address >= self.size:
            raise IndexError()
        offset = address * 2
        value = self.memory[offset:offset + 2]
        return value

    def read_int(self, address):
        raw = self.read(address)
        decoded = int.from_bytes(raw, byteorder = 'little')
        if decoded > 32775:
            msg = 'value {} out of valid range (0..32775)'.format(decoded)
            raise ValueError(msg)
        return decoded

    def read_hex(self, address):
        return self.read(address).hex()

    def __len__(self):
        return self.size
