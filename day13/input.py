from dataclasses import dataclass

@dataclass
class Input:
    timestamp: int
    routes: str

test_input = Input(939, "7,13,x,x,59,x,31,19")
input = Input(1001287, "13,x,x,x,x,x,x,37,x,x,x,x,x,461,x,x,x,x,x,x,x,x,x,x,x,x,x,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,739,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,x,x,x,23")

