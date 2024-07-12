=======================================
Enigma 003 : The Four-Square Chessboard
=======================================

.. |uncheck| raw:: html

    <input type="checkbox">
    
.. code:: python

    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
    import matplotlib
    from qiskit.circuit.library import MCXGate

The enigma uses an addition modulo two like this one

::

    10
  + 01
    __
    11

Such addition has the interesting characteristic that the numbers can be interchanged to any order like this
::

    11
  + 01
    __
    10

Or

:: 

    11
  + 10
    __
    01

Meaning that adding any two of them gives the third one as an answer (this is true for any numbers). Playing with modulo two additions also have other interesting characteristics. In the enigma, adding the first number to the second is done by applying a CNOT between q4 and q6 (and q5 and q7). What is the value on q6 after such an operation?

    |  |uncheck| Q6 now has the answer to the modulo two addition between q4 and q6.
    |
    |  |uncheck| An extra qubit would be needed to have the answer to the modulo two addition
    |            between q4 and q6.
    |  |uncheck| No addition has been performed between q4 and q6.
    |
    |  |uncheck| The CNOT does not permit to perform modulo two additions.

|

**Question 2 : Write the circuit for a 4 by 4 square chess**

Can you write the circuit for a 4 by 4 square chess set until you calculate the position of the piece to turn?

*HINT 1*

Start by drawing a 4 by 4 chess board and number each square from 0 to 15 in decimal and binary numbers starting with the top row.

*HINT 2*

The trick is now to add (modulo 2) all the squares that end with a 1 and to proceed the same way with all squares that have a 1 on their second bit counting from right to left and so on using four extra squares.

*HINT 3*

Provide the drawing of Hint 2 with the arrows for the counting

.. code:: python

    nb_coins = 16

    #qubits 0 to 15 are the 16 squares
    #qubits 16 to 19 is where the key is hidden
    #qubits 20 to 23 is where the focus first lands
    #qubits 24 to 27 is where the focus lands at the end which is the key location
    problem_qc = QuantumCircuit(nb_coins+12)

    #coin distribution on each square
    for i in range(16):
        problem_qc.h(i)

    problem_qc.barrier()

    #hiding the key under one of the 16 squares
    for i in range(16, 20):
        problem_qc.h(i)

    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q20
    problem_qc.cx(1, 20)
    problem_qc.cx(3, 20)
    problem_qc.cx(5, 20)
    problem_qc.cx(7, 20)
    problem_qc.cx(9, 20)
    problem_qc.cx(11, 20)
    problem_qc.cx(13, 20)
    problem_qc.cx(15, 20)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q21
    problem_qc.cx(2, 21)
    problem_qc.cx(3, 21)
    problem_qc.cx(6, 21)
    problem_qc.cx(7, 21)
    problem_qc.cx(10, 21)
    problem_qc.cx(11, 21)
    problem_qc.cx(14, 21)
    problem_qc.cx(15, 21)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as their 3rd digit from the right and putting the answer on q22
    problem_qc.cx(4, 22)
    problem_qc.cx(5, 22)
    problem_qc.cx(6, 22)
    problem_qc.cx(7, 22)
    problem_qc.cx(12, 22)
    problem_qc.cx(13, 22)
    problem_qc.cx(14, 22)
    problem_qc.cx(15, 22)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as their 4th digit from the right and putting the answer on q23
    problem_qc.cx(8, 23)
    problem_qc.cx(9, 23)
    problem_qc.cx(10, 23)
    problem_qc.cx(11, 23)
    problem_qc.cx(12, 23)
    problem_qc.cx(13, 23)
    problem_qc.cx(14, 23)
    problem_qc.cx(15, 23)
    problem_qc.barrier()

    #adding modulo 2 the position of the key and the position of the focus
    problem_qc.cx(16, 20)
    problem_qc.cx(17, 21)
    problem_qc.cx(18, 22)
    problem_qc.cx(19, 23)

|

.. code:: python

    problem_qc.draw(output='mpl')

|

**Question 3 :**

Complete the circuit to allow Alice to turn the right coin

.. code:: python

    #allowing for multi-controlled x gates
    gate = MCXGate(4)

    #turning the right coin on the bottom row
    problem_qc.append(gate, [20, 21, 22, 23, 15])

    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 14])
    problem_qc.x(23)

    problem_qc.x(22)
    problem_qc.append(gate, [20, 21, 22, 23, 13])
    problem_qc.x(22)

    problem_qc.x(22)
    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 12])
    problem_qc.x(22)
    problem_qc.x(23)

    #turning the right coin on the 3rd row
    problem_qc.x(21)

    problem_qc.append(gate, [20, 21, 22, 23, 11])

    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 10])
    problem_qc.x(23)

    problem_qc.x(22)
    problem_qc.append(gate, [20, 21, 22, 23, 9])
    problem_qc.x(22)

    problem_qc.x(22)
    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 8])
    problem_qc.x(22)
    problem_qc.x(23)


    #turning the right coin on the 2nd row
    problem_qc.x(21)
    problem_qc.x(20)

    problem_qc.append(gate, [20, 21, 22, 23, 7])

    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 6])
    problem_qc.x(23)

    problem_qc.x(22)
    problem_qc.append(gate, [20, 21, 22, 23, 5])
    problem_qc.x(22)

    problem_qc.x(22)
    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 4])
    problem_qc.x(22)
    problem_qc.x(23)

    #turning the right coin on the 2nd row
    problem_qc.x(21)

    problem_qc.append(gate, [20, 21, 22, 23, 3])

    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 2])
    problem_qc.x(23)

    problem_qc.x(22)
    problem_qc.append(gate, [20, 21, 22, 23, 1])
    problem_qc.x(22)

    problem_qc.x(22)
    problem_qc.x(23)
    problem_qc.append(gate, [20, 21, 22, 23, 0])
    problem_qc.x(22)
    problem_qc.x(23)

    #now that the right coin has been turned, it is time to put the focus on the square where the key is located
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q24
    problem_qc.cx(1, 24)
    problem_qc.cx(3, 24)
    problem_qc.cx(5, 24)
    problem_qc.cx(7, 24)
    problem_qc.cx(9, 24)
    problem_qc.cx(11, 24)
    problem_qc.cx(13, 24)
    problem_qc.cx(15, 24)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q25
    problem_qc.cx(2, 25)
    problem_qc.cx(3, 25)
    problem_qc.cx(6, 25)
    problem_qc.cx(7, 25)
    problem_qc.cx(10, 25)
    problem_qc.cx(11, 25)
    problem_qc.cx(14, 25)
    problem_qc.cx(15, 25)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as their 3rd digit from the right and putting the answer on q26
    problem_qc.cx(4, 26)
    problem_qc.cx(5, 26)
    problem_qc.cx(6, 26)
    problem_qc.cx(7, 26)
    problem_qc.cx(12, 26)
    problem_qc.cx(13, 26)
    problem_qc.cx(14, 26)
    problem_qc.cx(15, 26)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as their 4th digit from the right and putting the answer on q27
    problem_qc.cx(8, 27)
    problem_qc.cx(9, 27)
    problem_qc.cx(10, 27)
    problem_qc.cx(11, 27)
    problem_qc.cx(12, 27)
    problem_qc.cx(13, 27)
    problem_qc.cx(14, 27)
    problem_qc.cx(15, 27)

|

.. code:: python

    problem_qc.draw(output='mpl')

