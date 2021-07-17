import re

from input import test_input, real_input

class Q1():
    @staticmethod
    def get_mask_from_line(line):
        return line.partition("mask = ")[2]

    @staticmethod
    def get_mem_address_and_value_from_line(line):
        address = re.search(r"\[(\d+)\]", line).group(1)
        decimal_value = int(re.search(r"= (\d+)$", line).group(1))
        return address, decimal_value

    @staticmethod
    def apply_mask(mask, decimal_value):
        bin_string = str(bin(decimal_value))[2::][::-1]
        sum = 0
        for i, bit in enumerate(mask[::-1]):
            place = pow(2, i)
            if bit == "0":
                continue
            elif bit == "1":
                sum += place
            elif bit == "X":
                if i < len(bin_string) and bin_string[i] == "1":
                    sum += place

        return sum

    @classmethod
    def solution(cls, input):
        memory = {}
        mask = None
        for line in input.split("\n"):
            if line.startswith("mask"):
                mask = cls.get_mask_from_line(line)
            elif line.startswith("mem"):
                address, decimal_value = cls.get_mem_address_and_value_from_line(line)
                memory[address] = cls.apply_mask(mask, decimal_value)

        return sum(memory.values())



if __name__ == "__main__":
    assert(Q1.solution(test_input) == 165)
    print(Q1.solution(real_input))

