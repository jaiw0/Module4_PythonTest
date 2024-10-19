import unittest

def router(loc_R1, ipAdd, subnetMask):
    if loc_R1 == 'TIP_Manila':
        return True
    else:
        return False
    if ipAdd == '192.168.45.25':
        return True
    else:
        return False
    if subnetMask == '255.255.255.0':
        return True
    else:
        return False

class MyTest(unittest.TestCase):
    def test(self):
        self.assertTrue(router('TIP_Manila', '192.168.45.25', '255.255.255.0'))

if __name__ == '__main__':
    unittest.main()