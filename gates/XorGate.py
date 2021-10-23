# input1 input2
def function (inputs):
    input1 = inputs[0]
    input2 = inputs[1]
    import gates.OrGate
    or1 = gates.OrGate.function([input1, input2])
    import gates.NandGate
    nand1 = gates.NandGate.function([input1, input2])
    import gates.AndGate
    and1 = gates.AndGate.function([or1, nand1])
    return and1