# input1 input2
def function (inputs):
    input1 = [inputs[0]]
    input2 = [inputs[1]]
    import gates.NandGate
    nand1 = gates.NandGate.function(input1 + input2)
    import gates.NandGate
    nand2 = gates.NandGate.function(input1 + nand1)
    import gates.NandGate
    nand3 = gates.NandGate.function(input2 + nand1)
    import gates.NandGate
    nand4 = gates.NandGate.function(nand2 + nand3)
    return nand4