# input1 input2
def function (inputs):
    input1 = [inputs[0]]
    input2 = [inputs[1]]
    import gates.AndGate
    andOut = gates.AndGate.function(input1 + input2)
    import gates.NotGate
    notOut = gates.NotGate.function(andOut)
    return notOut