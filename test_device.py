import unittest

def identify_device(device):
    device_types = ['Router', 'PC', 'Switch', 'Server']

    if device in device_types:
        return device
    else:
        return f'Unknown Device!: {device}'

class TestDeviceType(unittest.TestCase):
    def test_router(self):
        self.assertEqual(identify_device('Router'), 'Router')
    def test_PC(self):
        self.assertEqual(identify_device('PC'), 'PC')
    def test_switch(self):
        self.assertEqual(identify_device('Switch'), 'Switch')
    def test_server(self):
        self.assertEqual(identify_device('Server'), 'Server')
    def test_unknown_device(self):
        self.assertEqual(identify_device('Printer'), 'Unknown Device!: Printer')

if __name__ == '__main__':
    unittest.main()
