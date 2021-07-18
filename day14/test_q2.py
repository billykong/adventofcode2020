from q2 import Q2

class TestQ2():
    def test_apply_mask(self):
        mask = "000000000000000000000000000000X1001X"
        address = 42
        expected_addresses = "000000000000000000000000000000X1101X"
        assert expected_addresses == Q2.apply_mask(mask, address)

    def test_get_product_addresses(self):
        masked_address = "000000000000000000000000000000X1101X"
        expected_addresses = { 26, 27, 58, 59 }
        assert expected_addresses == Q2.get_product_addresses(masked_address)
