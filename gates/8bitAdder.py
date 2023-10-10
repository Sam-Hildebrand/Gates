# bit1_0 bit1_1 bit1_2 bit1_3 bit1_4 bit1_5 bit1_6 bit1_7 bit2_0 bit2_1 bit2_2 bit2_3 bit2_4 bit2_5 bit2_6 bit2_7
def function (inputs):
    bit1_0 = [inputs[0]]
    bit1_1 = [inputs[1]]
    bit1_2 = [inputs[2]]
    bit1_3 = [inputs[3]]
    bit1_4 = [inputs[4]]
    bit1_5 = [inputs[5]]
    bit1_6 = [inputs[6]]
    bit1_7 = [inputs[7]]
    bit2_0 = [inputs[8]]
    bit2_1 = [inputs[9]]
    bit2_2 = [inputs[10]]
    bit2_3 = [inputs[11]]
    bit2_4 = [inputs[12]]
    bit2_5 = [inputs[13]]
    bit2_6 = [inputs[14]]
    bit2_7 = [inputs[15]]
    import gates.FullAdder
    Bit0 = gates.FullAdder.function(bit2_0 + bit1_0 + [0])
    import gates.FullAdder
    Bit1 = gates.FullAdder.function(bit2_1 + bit1_1 + Bit0[0])
    import gates.FullAdder
    Bit2 = gates.FullAdder.function(bit2_2 + bit1_2 + Bit1[0])
    import gates.FullAdder
    Bit3 = gates.FullAdder.function(bit2_3 + bit1_3 + Bit2[0])
    import gates.FullAdder
    Bit4 = gates.FullAdder.function(bit2_4 + bit1_4 + Bit3[0])
    import gates.FullAdder
    Bit5 = gates.FullAdder.function(bit2_5 + bit1_5 + Bit4[0])
    import gates.FullAdder
    Bit6 = gates.FullAdder.function(bit2_6 + bit1_6 + Bit5[0])
    import gates.FullAdder
    Bit7 = gates.FullAdder.function(bit2_7 + bit1_7 + Bit6[0])
    return Bit0[1], Bit1[1], Bit2[1], Bit3[1], Bit4[1], Bit5[1], Bit6[1], Bit7[1]