# input1 input2
def function (inputs):
    input1 = inputs[0]
    input2 = inputs[1]
    import gates.NotGate
    not1 = gates.NotGate.function([input1])
    import gates.NotGate
    not2 = gates.NotGate.function([input2])
    import gates.NandGate
    nand1 = gates.NandGate.function([not1, not2])
    return nand1