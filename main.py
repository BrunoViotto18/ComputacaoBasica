from logic_gates import AndGate, OrGate, NandGate, NorGate, XorGate
from basics import Bit


def main():
    gates = {'and': AndGate(), 'or': OrGate(), 'nand': NandGate(), 'nor': NorGate(), 'xor': XorGate()}
    b1 = [False, True, False, True]
    b2 = [False, False, True, True]

    a = AndGate(Bit(True), Bit(True))
    print(a.value)

    for gate_name, gate in gates.items():
        for a, b in zip(b1, b2):
            gate.a = a
            gate.b = b
            print(f'{gate.a}\t{gate_name}\t{gate.b}\t=\t{gate.value}')
        print()


if __name__ == '__main__':
    main()
