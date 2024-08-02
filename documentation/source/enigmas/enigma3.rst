=======================================
Enigma 003 : The Four-Square Chessboard
=======================================

Alice and Bob continue their journey in space. They are challenged by Aïka, who's hidden a key under one of the four chessboard squares. A coin is then randomly placed on each of the four squares. How will Alice communicate to Bob the exact position of the key by flipping only one coin? You will apply a new concept, the control by the 0-state.

**Make sure to watch the following video before getting started with this problem set:**

.. raw:: html

    <iframe class="embed-responsive-item" width="560" height="315" src="https://www.youtube.com/embed/UuVbtFXOEKQ?rel=0" allowfullscreen="">
    </iframe>

|

.. dropdown:: :material-regular:`error;1.2em;sd-text-warning` Important
    :animate: fade-in
    :color: warning
    
    On this website, you will be able to write your own Python code as well as run it. To do so, you will need to click on the "Activate" button to enable all the code editors and establish a connection to a Kernel. Once clicked, you will see that the Status widget will start to show the connection progress, and in the line below, the connection information will be shown. You are ready to write and run your code once you see :code:`Status:Kernel Connected` and :code:`kernel thebe.ipynb status changed to ready[idle]` in the line below. If you run into any issues, please try to reconnect by clicking on the "Activate" button again or reloading the page.

.. raw:: html

    <!-- Configure and load Thebe !-->
    <script type="text/x-thebe-config">
        {
            requestKernel: true,
            kernelOptions: {
                name: "python3",
            },
            binderOptions: {
                repo: "algolab-quantique/quantum-enigmas",
            },
            mountActivateWidget: true,
            mountStatusWidget: true
        }
    </script>
    <div class="thebe-activate"></div>
    <div class="thebe-status"></div>
    <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>

.. dropdown:: :material-regular:`info;1.2em;sd-text-info` Note
    :animate: fade-in
    :color: info
    
    When running your code, you'll know that the code is running if you see :code:`kernel thebe.ipynb status changed to ready[busy]`. If it seems to stay on :code:`ready[idle]` when running your code and/or you're not getting an output when you're supposed to, it most likely means that there's an error in your code. Since the code editor seems to be struggling with outputting error messages, there is no output.

|

Run the cell below to install the necessary packages.

.. raw:: html

    <pre data-executable="true" data-language="python">
    import sys
    !{sys.executable} -m pip install qiskit==1.1.1
    !{sys.executable} -m pip install qiskit_aer==0.14.2
    !{sys.executable} -m pip install pylatexenc==2.10
    </pre>

Now, run the cell below to import the necessary packages.

.. raw:: html

    <pre data-executable="true" data-language="python">
    import numpy as np
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
    from qiskit.circuit.library import MCXGate
    from qiskit.visualization import plot_histogram
    from qiskit_aer import Aer, AerSimulator
    </pre>

..
    .. raw:: html

        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        #myDIV {
        width: 100%;
        padding: 50px 0;
        text-align: center;
        background-color: lightblue;
        margin-top: 20px;
        display: none;
        }
        </style>
        </head>
        <body>

        <p>Click the "Try it" button to toggle between hiding and showing the DIV element:</p>

        <button onclick="myFunction()">Click to reveal the answer</button>

        <div id="myDIV">
        This is my DIV element.
        </div>

        <p><b>Note:</b> The element will not take up any space when the display property 
        is set to "none".</p>

        <script>
        function myFunction() {
            var x = document.getElementById("myDIV");
            if (x.style.display === "block") {
            x.style.display = "none";
            } else {
            x.style.display = "block";
            }
        }
        </script>

        </body>

|

The enigma uses a modulo two addition like this one:

.. raw:: html

    <style>
        .center {
            margin-left: 45px
        }
        .equation.stacked {
            display: inline-block;
        }
        .equation.stacked .number {
            display: block;
            margin-left: 1em;
            text-align: right;
        }
        .equation.stacked .operator {
            float: left;
        }
        .equation.stacked .equals {
            display: block;
            height: 0;
            border-bottom: solid 1px black;
            overflow: hidden;
        }
        div {
            margin-bottom: 1em;
        }
    </style>
    <div class="center">
        <div>
            <span class="equation stacked">
                <span class="number">1 0</span>
                <span class="operator">+</span>
                <span class="number">0 1</span>
                <span class="equals">=</span>
                <span class="number">1 1</span>
            </span>
        </div>
    </div>

Such addition has the interesting characteristic that the numbers can be interchanged in any order like this

.. raw:: html

    <div class="center">
        <div>
            <span class="equation stacked">
                <span class="number">1 1</span>
                <span class="operator">+</span>
                <span class="number">0 1</span>
                <span class="equals">=</span>
                <span class="number">1 0</span>
            </span>
        </div>
    </div>

Or

.. raw:: html

    <div class="center">
        <div>
            <span class="equation stacked">
                <span class="number">1 1</span>
                <span class="operator">+</span>
                <span class="number">1 0</span>
                <span class="equals">=</span>
                <span class="number">0 1</span>
            </span>
        </div>
    </div>

Meaning that adding any two of them gives the third one as an answer (this is true for any numbers). Playing with modulo two additions also has other interesting characteristics. In the enigma, adding the first number to the second is done by applying a CNOT between *q*\ :sub:`4`\  and *q*\ :sub:`6`\  (and *q*\ :sub:`5`\  and *q*\ :sub:`7`\). Here is the code of the algorithm in the enigma. 

.. code:: python

    #qubits 0 to 3 are the 4 squares
    #qubits 4 and 5 is where the key is hidden
    #qubits 6 and 7 is where the focus first lands
    #qubits 8 and 9 is where the focus lands at the end which is the key location
    problem_qc = QuantumCircuit(10)

    #coin distribution on each square
    for i in range(4):
        problem_qc.h(i)

    problem_qc.barrier()

    #hiding the key under one of the 4 squares
    problem_qc.h(4)
    problem_qc.h(5)

    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q5
    problem_qc.cx(1, 6)
    problem_qc.cx(3, 6)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q6
    problem_qc.cx(2, 7)
    problem_qc.cx(3, 7)
    problem_qc.barrier()

    #adding modulo 2 the position of the key and the position of the focus
    problem_qc.cx(4, 6)
    problem_qc.cx(5, 7)
    problem_qc.barrier()

    #turning the right coin
    problem_qc.ccx(7,6,3)
    problem_qc.barrier()
    problem_qc.x(6)
    problem_qc.ccx(7,6,2)
    problem_qc.x(6)
    problem_qc.barrier()
    problem_qc.x(7)
    problem_qc.ccx(7,6,1)
    problem_qc.x(7)
    problem_qc.barrier()
    problem_qc.x(6)
    problem_qc.x(7)
    problem_qc.ccx(7,6,0)
    problem_qc.x(7)
    problem_qc.x(6)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q8
    problem_qc.cx(1, 8)
    problem_qc.cx(3, 8)
    problem_qc.barrier()

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q9
    problem_qc.cx(2, 9)
    problem_qc.cx(3, 9)
    problem_qc.barrier()

    problem_qc.draw(output='mpl')

.. image:: ..

What is the value on q6 after such an operation?

    |  Q6 now has the answer to the modulo two addition between q4 and q6.
    |
    |  An extra qubit would be needed to have the answer to the modulo two addition
    |            between q4 and q6.
    |  No addition has been performed between q4 and q6.
    |
    |  The CNOT does not permit to perform modulo two additions.

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

