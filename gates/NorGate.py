# input1 input2
def function (inputs):
    input1 = [inputs[0]]
    input2 = [inputs[1]]
    import gates.OrGate
    orOut = gates.OrGate.function(input1 + input2)
    import gates.NotGate
    notOut = gates.NotGate.function(orOut)
    return notOut