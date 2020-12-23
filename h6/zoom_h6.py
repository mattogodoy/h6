import serial
from time import sleep


class ZoomH6:
    is_initialized = False
    is_handshake_complete = False
    s = None
    commands = {
        'stop':             bytearray([0b10010000, 0b00000000]),
        'forward':          bytearray([0b10001000, 0b00000000]),
        'reverse':          bytearray([0b10000100, 0b00000000]),
        'play_pause':       bytearray([0b10000010, 0b00000000]),
        'record':           bytearray([0b10000001, 0b00000000]),
        'vol_up':           bytearray([0b10000000, 0b10000000]),
        'vol_down':         bytearray([0b10000000, 0b01000000]),
        'ch4':              bytearray([0b10000000, 0b00100000]),
        'ch3':              bytearray([0b10000000, 0b00010000]),
        'ch2':              bytearray([0b10000000, 0b00001000]),
        'ch1':              bytearray([0b10000000, 0b00000100]),
        'right':            bytearray([0b10000000, 0b00000010]),
        'left':             bytearray([0b10000000, 0b00000001]),
        'release_button':   bytearray([0b10000000, 0b00000000])
    }

    def __init__(self, serial_port):
        # Initialize serial port
        try:
            self.s = serial.Serial(serial_port)
            self.s.baudrate = 2400
            self.s.timeout = 0.032
            self.is_initialized = True
        except serial.serialutil.SerialException:
            print(f'[ERROR] Serial port "{serial_port}" not found')

    def initialize(self) -> None:
        if self.is_initialized and not self.is_handshake_complete:
            while not self.is_handshake_complete:
                self.s.write(b'\00')

                if self.s.read(1) == b'\x82':
                    self.s.write(b'\xC2')

                    if self.s.read(1) == b'\x83':
                        self.s.write(b'\xE1\x31\x2E\x30\x30')

                        if self.s.read(1) == b'\x80':
                            self.s.write(b'\xA1')

                            if self.s.read(1) == b'\x81':
                                self.s.write(b'\x80\x80')
                                self.is_handshake_complete = True

            sleep(0.1)
            return True
        else:
            print('[ERROR] Recorder not is_initialized')
            return False

    def is_valid_command(self, command: str) -> bool:
        valid_commands = self.commands.keys()
        return command in valid_commands

    def send(self, command: str) -> None:
        if not self.is_valid_command(command):
            print('[ERROR] Invalid command')
            return False

        if self.is_handshake_complete:
            self.s.write(self.commands[command])
            self.s.write(self.commands['release_button'])
            return True
        else:
            print('[ERROR] Recorder not is_initialized')
            return False

    def rec(self) -> None:
        self.send('record')

    def stop(self) -> None:
        self.send('record')
