# input1 input2
def function (inputs):
    input1 = inputs[0]
    input2 = inputs[1]
    import gates.AndGate
    and1 = gates.AndGate.function([input1, input2])
    import gates.NotGate
    not1 = gates.NotGate.function(and1)
    return not1
