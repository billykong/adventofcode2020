from itertools import product

from input import test_input_2, real_input
from q1 import Q1


class Q2(Q1):
    @staticmethod
    def apply_mask(mask, value):
        """
        Parameters:
            mask bit:   0 -> unchanged
                        1 -> 1
                        X -> floating

        Returns:
            a set consisting of all the permutations of the masked decimal_value
        """
        addresses = set()
        bin_string = str(bin(value))[2::][::-1]
        masked_bin = [None] * len(mask)
        float_count = 0
        for i, bit in enumerate(mask[::-1]):
            if bit == "0":
                masked_bin[i] = bin_string[i] if i < len(bin_string) else "0"
            elif bit == "1":
                masked_bin[i] = "1"
            elif bit == "X":
                masked_bin[i] = "X"
                float_count += 1
        
        # e.g. float_count = 3
        # [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
        replacements = product(range(2), repeat=float_count)
        addresses_bin = []

        for replacement in replacements:
            tmp_masked_bin = masked_bin
            for bit in replacement:
                tmp_masked_bin = "".join(tmp_masked_bin).replace("X", str(bit), 1)
            addresses_bin.append(tmp_masked_bin[::-1])

        return { int(masked_bin, 2) for masked_bin in addresses_bin }

    @classmethod
    def solution(cls, input):
        memory = {}
        mask = None
        for line in input.split("\n"):
            if line.startswith("mask"):
                mask = cls.get_mask_from_line(line)
            elif line.startswith("mem"):
                address, decimal_value = cls.get_mem_address_and_value_from_line(line)
                addresses = cls.apply_mask(mask, address)
                for address in addresses:
                    memory[address] = decimal_value

        return sum(memory.values())


if __name__ == "__main__":
    assert(Q2.solution(test_input_2) == 208)
    print(Q2.solution(real_input))

