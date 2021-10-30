
**10/30/2021, 1:23:00 PM**: I'd like to reinvent this project as an interpreted language that parses a csv file.
I think with one special gate that implements basically a goto feature I could simulate anything i wanted to in binary.

**10/23/2021, 10:34:06 PM**: The program is complete as far as I am aware. The next step is to spilt it into a
compiler and an interpreter, then start with some fancy features.


**12/2/2020, 1:51:19 PM**: Another possible solution involves using a separate function for each output:

![](/home/sam/Workspaces/Python/Gates/.journal.assets/.journal-.journal-fb3289f2.jpg)

**12/2/2020, 12:49:26 PM**: I need a viable way to represent two bits out of a gate. i.e:
```drawdown.flow.gates
    - input.
    - gate.
        - output1.
    - output2.
```
One possible method is a list, where `returned[i]` represents 1 or 0 times 10^i.


**11/28/2020, 3:58:15 PM**:
Simple Concept for a gate sketcher: This will not be terribly easy to implement and so is probably a little way off.
```
NandGate:
input1---+---------+    +---------+
         | AndGate +----+ NotGate +---output1
input2---+---------+    +---------+
```
