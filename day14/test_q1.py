from q1 import Q1

class TestQ1():
    def test_get_mask_from_line(self):
        line = "mask = 0101110101111X0010100000X10X000X1X1X"
        mask = "0101110101111X0010100000X10X000X1X1X"
        assert mask == Q1.get_mask_from_line(line)

    def test_get_mem_address_and_value_from_line(self):
        line = "mem[52304] = 107295284"
        address = "52304"
        decimal_value = 107295284
        assert (address, decimal_value) == Q1.get_mem_address_and_value_from_line(line)

    def test_apply_mask(self):
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        decimal_value = 11
        assert 73 == Q1.apply_mask(mask, decimal_value)

