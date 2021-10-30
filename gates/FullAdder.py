# input1 input2 carryIn
def function (inputs):
    input1 = [inputs[0]]
    input2 = [inputs[1]]
    carryIn = [inputs[2]]
    import gates.XorGate
    xor1 = gates.XorGate.function(input1 + input2)
    import gates.AndGate
    and1 = gates.AndGate.function(input1 + input2)
    import gates.XorGate
    xor2 = gates.XorGate.function(xor1 + carryIn)
    import gates.AndGate
    and2 = gates.AndGate.function(xor1 + carryIn)
    import gates.OrGate
    or1 = gates.OrGate.function(and1 + and2)
    return or1, xor2
