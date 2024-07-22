==================================
Enigma 002 : The Four Hair Colours
==================================

Make sure to watch the following video before getting started with this problem set:

.. raw:: html

    <iframe class="embed-responsive-item" width="560" height="315" src="https://www.youtube.com/embed/enXT5xTaPb8?rel=0" allowfullscreen="">
    </iframe>

|

.. dropdown:: :material-regular:`error;1.2em;sd-text-warning` Important
    :animate: fade-in
    :color: warning
    :open:
    
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
    :open:
    
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
    from qiskit.visualization import plot_histogram
    from qiskit_aer import Aer, AerSimulator
    </pre>

|

.. raw:: html

    <span style="font-size:30px;font-weight:bold">Problem 1</span>

The enigma video presented a quantum circuit to solve the hair color problem with 4 people. Here's an example of the code associated with the circuit:

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

Can you adapt the circuit for 6 people?

.. raw:: html

    <pre data-executable="true" data-language="python">
    problem_qc = QuantumCircuit(12)

    ### Start writing your code here. ###
    

    # Visualize the circuit
    problem_qc.draw('mpl')
    </pre>

|

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

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

        # Visualize the circuit
        problem_qc.draw('mpl')
    
    .. image:: ../answers_png/E2_P1.png
        :width: 100%

|

.. raw:: html

    <span style="font-size:30px;font-weight:bold">Problem 2</span>

Simplify the code with a :code:`for` loop. Can you write a circuit for any number of people using a for loop?

.. raw:: html

    <pre data-executable="true" data-language="python" data-readonly>
    nb_players = 5

    nb_qubits = nb_players*2

    problem_qc = QuantumCircuit(nb_qubits)

    for i in range(nb_players):
        problem_qc.h(i)

    start_qubit = 1

    ### Add the rest of the code here. ###


    # Visualize the circuit
    problem_qc.draw('mpl')
    </pre>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python

        nb_players = 5
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
        
        # Visualize the circuit
        problem_qc.draw('mpl')

    .. image:: ../answers_png/E2_P2.png
        :width: 100%

|

.. .. raw:: html
..
    <pre data-executable="true" data-language="python">
    problem_qc.draw(output='mpl')
    </pre>

|

**Question 3 : What is the condition to get 100% of right answers?**

 .. raw:: html

    <form id="question3-form">
        <div id="answers-container-q3"></div>
        <button type="submit">Submit Answer</button>
    </form>
    <pre id="log3"></pre>

.. raw:: html

    <script>
        // List of answers
        const answersQ3 = [
            { id: 'q3a', value: 'a', text: 'By chance, the first answer must be the same color as the key to the enigma is.' },
            { id: 'q3b', value: 'b', text: 'The answers never are all right for all situations.' },
            { id: 'q3c', value: 'c', text: 'The last person must get a right answer.' },
            { id: 'q3d', value: 'd', text: 'It depends on the number of people in the line.' }
        ];

        // Function to shuffle the answers
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        // Shuffle the answers
        shuffle(answersQ3);

        // Insert shuffled answers into the form
        const containerQ3 = document.getElementById('answers-container-q3');
        answersQ3.forEach(answer => {
            const input = document.createElement('input');
            input.type = 'radio';
            input.id = answer.id;
            input.name = 'q3';
            input.value = answer.value;

            const label = document.createElement('label');
            label.htmlFor = answer.id;
            label.textContent = answer.text;

            containerQ3.appendChild(input);
            containerQ3.appendChild(label);
            containerQ3.appendChild(document.createElement('br'));
        });

        // Handle form submission
        document.querySelector('#question3-form').onsubmit = function(e) {
            e.preventDefault();
            const log = document.getElementById('log3');
            const selectedAnswer = document.querySelector('input[name="q3"]:checked');
            if (selectedAnswer) {
                if (selectedAnswer.value === 'a') {
                    log.textContent = 'Correct! The first person must get a right answer.';
                } else {
                    log.textContent = 'Incorrect! Try again.';
                }
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

|

**Question 4 : Only one qubit is not entangled in the system, which one is it?**

 .. raw:: html

    <form id="question4-form">
        <div id="answers-container-q4"></div>
        <button type="submit">Submit Answer</button>
    </form>
    <pre id="log4"></pre>

.. raw:: html

    <script>
        // List of answers
        const answersQ4 = [
            { id: 'q4a', value: 'a', text: 'The first qubit' },
            { id: 'q4b', value: 'b', text: 'The second qubit' },
            { id: 'q4c', value: 'c', text: 'The third qubit' },
            { id: 'q4d', value: 'd', text: 'The last qubit' }
        ];

        // Function to shuffle the answers
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        // Shuffle the answers
        shuffle(answersQ4);

        // Insert shuffled answers into the form
        const containerQ4 = document.getElementById('answers-container-q4');
        answersQ4.forEach(answer => {
            const input = document.createElement('input');
            input.type = 'radio';
            input.id = answer.id;
            input.name = 'q4';
            input.value = answer.value;

            const label = document.createElement('label');
            label.htmlFor = answer.id;
            label.textContent = answer.text;

            containerQ4.appendChild(input);
            containerQ4.appendChild(label);
            containerQ4.appendChild(document.createElement('br'));
        });

        // Handle form submission
        document.querySelector('#question4-form').onsubmit = function(e) {
            e.preventDefault();
            const log = document.getElementById('log4');
            const selectedAnswer = document.querySelector('input[name="q4"]:checked');
            if (selectedAnswer) {
                if (selectedAnswer.value === 'a') {
                    log.textContent = 'Correct! The first qubit is not entangled in the system.';
                } else {
                    log.textContent = 'Incorrect! Try again.';
                } 
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

|

**Question 5 : Run the circuit on a simulator. Can you explain the significance of each qubit in any given measured state?**

The first 4 qubits each represent the hair color of each player.
    
    For example, if qubit 0 is measured at 0, then the first player, Alice, has orange hair.

The last 4 qubits each represent the hair color each player is giving as his answer.

    For example, if qubit 4 is measured at 0, then the first player, Alice, has predicted to be having orange hair.