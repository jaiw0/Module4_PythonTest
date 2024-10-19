import unittest
from subnet_validator import prefix_to_subnet_mask, is_valid_subnet_mask

class TestSubnetValidator(unittest.TestCase):

    def test_prefix_to_subnet_mask(self):
        # Test prefix lengths with expected subnet masks
        test_cases = {
            24: "255.255.255.0",
            16: "255.255.0.0",
            8:  "255.0.0.0",
            0:  "0.0.0.0",
        }

        for prefix, expected_mask in test_cases.items():
            self.assertEqual(prefix_to_subnet_mask(prefix), expected_mask)

    def test_is_valid_subnet_mask(self):
        valid_masks = [
            "255.255.255.0",
            "255.255.0.0",
            "255.0.0.0",
            "0.0.0.0",
        ]
        
        for mask in valid_masks:
            self.assertTrue(is_valid_subnet_mask(mask))

if __name__ == '__main__':
    unittest.main()