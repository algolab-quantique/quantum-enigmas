==================================
Enigma 002 : The Four Hair Colours
==================================

.. raw:: html

    <!-- Configure and load Thebe !-->
    <script type="text/x-thebe-config">
        {
            requestKernel: true,
            binderOptions: {
            repo: "algolab-quantique/quantum-enigmas",
            },
            codeMirrorConfig: {
                theme: 'abcdef'
            },
        }
    </script>
    <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>

    <pre data-executable="true" data-language="python">
    %matplotlib inline
    import numpy as np
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.scatter(*np.random.rand(2, 100), c=np.random.rand(100))
    ax.set(title="Wow it works!")
    </pre>

.. raw:: html

    <button id="activateButton" style="width: 120px; height: 40px; font-size: 1.5em;">Activate</button>
    <script>
    var bootstrapThebe = function() {
        thebelab.bootstrap();
    }

    document.querySelector("#activateButton").addEventListener('click', bootstrapThebe)
    </script>

.. code:: python

    from qiskkit import QuantumCircuit, ClassicalRegister, QuantumRegister
    import matplotlib

.. ---------------------------------
.. :math:`\phantom{0}`
.. ---------------------------------

|

.. raw:: html

    <span style="font-size:20px;font-weight:bold">Code for 4 people circuit</span>

.. ^^^^^^^^^^^^^^^^^^^^^^^^^
.. Code for 4 people circuit
.. ^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    problem_qc = QuantumCircuit(8)

    problem_qc.h(0)
    problem_qc.h(1)
    problem_qc.h(2)
    problem_qc.h(3)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7)
        
    # You check if the number of indigo hair color in front of you is even or odd
    problem_qc.cx(1,4)
    problem_qc.cx(2,4)
    problem_qc.cx(3,4)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7)

    # Everyone takes note of the answer
    problem_qc.cx(4,5)
    problem_qc.cx(4,6)
    problem_qc.cx(4,7)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7)

    # Bob checks the parity of the hair color in front of him
    problem_qc.cx(2,5)
    problem_qc.cx(3,5)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7)

    # Charlie and Dahlia take note of the answer
    problem_qc.cx(5,6)
    problem_qc.cx(5,7)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7)

    # Charkie checks the parity of Dahlia's hair color
    problem_qc.cx(3,6)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7)

    # Dahlia takes note of Charlie's hair color
    problem_qc.cx(6,7)

|

.. code:: python

    problem_qc.draw(output='mpl')

|

**Question 1** : Can you adapt the circuit for 6 people?

.. code:: python

    problem_qc = QuantumCircuit(12)
   
    problem_qc.h(0)
    problem_qc.h(1)
    problem_qc.h(2)
    problem_qc.h(3)
    problem_qc.h(4)
    problem_qc.h(5)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    
    # You check if the number of indigo hair color in front of you is even or not
    problem_qc.cx(1,6)
    problem_qc.cx(2,6)
    problem_qc.cx(3,6)
    problem_qc.cx(4,6)
    problem_qc.cx(5,6)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Everyone takes note of the answer
    problem_qc.cx(6,7)
    problem_qc.cx(6,8)
    problem_qc.cx(6,9)
    problem_qc.cx(6,10)
    problem_qc.cx(6,11)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Bob checks the parity of the hair color in front of him
    problem_qc.cx(2,7)
    problem_qc.cx(3,7)
    problem_qc.cx(4,7)
    problem_qc.cx(5,7)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Everyone takes note of the answer
    problem_qc.cx(7,8)
    problem_qc.cx(7,9)
    problem_qc.cx(7,10)
    problem_qc.cx(7,11)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Charlie checks the parity of the hair color in front of him
    problem_qc.cx(3,8)
    problem_qc.cx(4,8)
    problem_qc.cx(5,8)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Everyone takes note of the answer
    problem_qc.cx(8,9)
    problem_qc.cx(8,10)
    problem_qc.cx(8,11)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Dahlia checks the parity of the hair color in front of her
    problem_qc.cx(4,9)
    problem_qc.cx(5,9)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Everyone takes note of the answer
    problem_qc.cx(9,10)
    problem_qc.cx(9,11)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # Player E checks the parity of Player F hair's color
    problem_qc.cx(5,10)
    problem_qc.barrier(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

    # The last player finds his/her hair color depending on all the other players
    problem_qc.cx(10,11)

|

.. code:: python

    problem_qc.draw(output='mpl')

|

| **Question 2 : Simplify the code with a for loop**
| Can you write a circuit for any number of people using a for loop?

.. code:: python

    nb_players = 6

    nb_qubits = nb_players*2

    problem_qc = QuantumCircuit(nb_qubits)

    for i in range(nb_players):
        problem_qc.h(i)

    start_qubit = 1

    for j in range(nb_players, nb_qubits-start_qubit):
        problem_qc.barrier()
        for i in range(start_qubit, nb_players):
            problem_qc.cx(i, j)
        problem_qc.barrier()
        for k in range(j+1, nb_qubits):
            problem_qc.cx(j, k)
        start_qubit = start_qubit+1

|

.. code:: python

    problem_qc.draw(output='mpl')

|

.. |check| raw:: html

    <input checked=""  type="checkbox">

.. |check_| raw:: html

    <input checked=""  disabled="" type="checkbox">

.. |uncheck| raw:: html

    <input type="checkbox">

.. |uncheck_| raw:: html

    <input disabled="" type="checkbox">

**Question 3 : What is the condition to get 100% of right answers?**

    | |uncheck| By chance, the first answer must be the same color as the key to the enigma is.
    | |uncheck| The answers never are all right for all situations.
    | |uncheck| The last person must get a right answer.
    | |uncheck| It depends on the number of people in the line.

|

**Question 4 : Only one qubit is not entangled in the system, which one is it?**

    | |uncheck| The first qubit
    | |uncheck| The second qubit
    | |uncheck| The third qubit
    | |uncheck| The last qubit

|

**Question 5 : Run the circuit on a simulator. Can you explain the significance of each qubit in any given measured state?**

The first 4 qubits each represent the hair color of each player.
    
    For example, if qubit 0 is measured at 0, then the first player, Alice, has orange hair.

The last 4 qubits each represent the hair color each player is giving as his answer.

    For example, if qubit 4 is measured at 0, then the first player, Alice, has predicted to be having orange hair.
