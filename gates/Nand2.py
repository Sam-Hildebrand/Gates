# input1 input2
def function (inputs):
    input1 = inputs[0]
    input2 = inputs[1]
    import gates.NandGate
    nand1 = gates.NandGate.function([input1, input2])
    return nand1
