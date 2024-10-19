import unittest
import re 

def is_valid_ip(ip):
    ip_pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(' \
                 r'25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(' \
                 r'25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(' \
                 r'25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(ip_pattern, ip) is not None

def is_valid_mac(mac):
    mac_pattern = r'^([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})$'
    return re.match(mac_pattern, mac) is not None

class TestValidators(unittest.TestCase):

    def test_valid_ip(self):
        valid_ips = [
            "192.168.1", #Invalid ip format
            "255.255.255.255",
            "0.0.0.0",
            "10.0.0.1"
        ]
        for ip in valid_ips:
            self.assertTrue(is_valid_ip(ip))

    def test_valid_mac(self):
        valid_macs = [
            "00:14:22:01:23:45",
            "00-14-22-01-23-45",
            "FF:FF:FF:FF:FF:FF",
            "aa:bb:cc:dd:ee:ff"
        ]
        for mac in valid_macs:
            self.assertTrue(is_valid_mac(mac))

if __name__ == '__main__':
    unittest.main()