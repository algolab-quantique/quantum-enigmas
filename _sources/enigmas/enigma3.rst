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
    
    On this website, you will be able to write and run your own Python code. To do so, you will need to click on the "Activate" button to enable all the code editors and establish a connection to a Kernel. Once clicked, you will see that the Status widget will start to show the connection progress, as well as the connection information. You are ready to write and run your code once you see :code:`Status:Kernel Connected` and :code:`kernel thebe.ipynb status changed to ready[idle]` just below. **Please note that that refreshing the page in any way will cause you to lose all the code that you wrote**. If you run into any issues, please try to reconnect by clicking on the "Activate" button again or reloading the page.

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
    <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>

.. margin::

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

---------------------------
**Problem 1 - Quick quiz**
---------------------------

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
        .equation-container {
            margin-bottom: 1em;
        }
    </style>
    <div class="center">
        <div class="equation-container">
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
        <div class="equation-container">
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
        <div class="equation-container">
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

    problem_qc.barrier([4,5])

    #hiding the key under one of the 4 squares
    problem_qc.h(4)
    problem_qc.h(5)

    problem_qc.barrier([4,5,6,7])

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q5
    problem_qc.cx(1, 6)
    problem_qc.cx(3, 6)
    problem_qc.barrier([6,7])

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q6
    problem_qc.cx(2, 7)
    problem_qc.cx(3, 7)
    problem_qc.barrier([6,7])

    #adding modulo 2 the position of the key and the position of the focus
    problem_qc.cx(4, 6)
    problem_qc.cx(5, 7)
    problem_qc.barrier([6,7])

    #turning the right coin
    problem_qc.ccx(7,6,3)
    problem_qc.barrier([6,7])
    problem_qc.x(6)
    problem_qc.ccx(7,6,2)
    problem_qc.x(6)
    problem_qc.barrier([6,7])
    problem_qc.x(7)
    problem_qc.ccx(7,6,1)
    problem_qc.x(7)
    problem_qc.barrier([6,7])
    problem_qc.x(6)
    problem_qc.x(7)
    problem_qc.ccx(7,6,0)
    problem_qc.x(7)
    problem_qc.x(6)
    problem_qc.barrier([6,7,8,9])

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q8
    problem_qc.cx(1, 8)
    problem_qc.cx(3, 8)
    problem_qc.barrier([6,7,8,9])

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q9
    problem_qc.cx(2, 9)
    problem_qc.cx(3, 9)

    problem_qc.draw(output='mpl')

.. image:: ../images/E3_P1.png
    :width: 100%

|

.. raw:: html

    <style>

        .button-23 {
            background-color: #D7D7D7;
            border: 1px solid #222222;
            border-radius: 8px;
            box-sizing: border-box;
            color: #222222;
            cursor: pointer;
            display: inline-block;
            font-family: Circular,-apple-system,BlinkMacSystemFont,Roboto,"Helvetica Neue",sans-serif;
            font-size: 16px;
            font-weight: 600;
            line-height: 20px;
            margin: 0;
            outline: none;
            padding: 13px 23px;
            position: relative;
            text-align: center;
            text-decoration: none;
            touch-action: manipulation;
            transition: box-shadow .2s,-ms-transform .1s,-webkit-transform .1s,transform .1s;
            user-select: none;
            -webkit-user-select: none;
            width: auto;
        }

        .button-23:focus-visible {
        box-shadow: #222222 0 0 0 2px, rgba(255, 255, 255, 0.8) 0 0 0 4px;
        transition: box-shadow .2s;
        }

        .button-23:active {
        background-color: #F7F7F7;
        border-color: #000000;
        transform: scale(.96);
        }

        .button-23:disabled {
        border-color: #DDDDDD;
        color: #DDDDDD;
        cursor: not-allowed;
        opacity: 1;
        }
    </style>

.. raw:: html

    <p><strong>What is the value on <em>q</em><sub>6&nbsp;</sub>after such an operation?</strong></p>
    </p>

\

 .. raw:: html

    <style>
        #log1 {
            white-space: pre-wrap;
            word-wrap: break-word;
        }

        .correct-answer {
            background-color: #d4edda;
            border-color: #c3e6cb;
            color: #155724;
        }

        .incorrect-answer {
            background-color: #f8d7da;
            border-color: #f5c6cb;
            color: #721c24;
        }
    </style>

    <form id="question1-form">
        <div id="answers-container-q1"></div>
        <button type="submit" class="button-23">Submit Answer</button>
    </form>
    <pre id="log1"></pre>

.. raw:: html

    <script>
        // List of answers
        const answersQ1 = [
            { id: 'q1a', value: 'a', text: '<em>q</em><sub>6</sub> now has the answer to the modulo two addition between <em>q</em><sub>4</sub> and <em>q</em><sub>6</sub>.' },
            { id: 'q1b', value: 'b', text: 'An extra qubit would be needed to have the answer to the modulo two addition between <em>q</em><sub>4</sub> and <em>q</em><sub>6</sub>.' },
            { id: 'q1c', value: 'c', text: 'No addition has been performed between <em>q</em><sub>4</sub> and <em>q</em><sub>6</sub>.' },
            { id: 'q1d', value: 'd', text: 'The CNOT does not permit to perform modulo two additions.' }
        ];

        // Function to shuffle the answers
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        // Shuffle the answers
        shuffle(answersQ1);

        // Insert shuffled answers into the form
        const containerQ1 = document.getElementById('answers-container-q1');
        answersQ1.forEach(answer => {
            const input = document.createElement('input');
            input.type = 'radio';
            input.id = answer.id;
            input.name = 'q1';
            input.value = answer.value;

            const label = document.createElement('label');
            label.htmlFor = answer.id;
            label.innerHTML = answer.text;

            containerQ1.appendChild(input);
            containerQ1.appendChild(label);
            containerQ1.appendChild(document.createElement('br'));
        });

        // Handle form submission
        document.querySelector('#question1-form').onsubmit = function(e) {
            e.preventDefault();
            const log = document.getElementById('log1');
            const selectedAnswer = document.querySelector('input[name="q1"]:checked');
            if (selectedAnswer) {
                if (selectedAnswer.value === 'a') {
                    log.textContent = 'Correct!.';
                    log.classList.remove('incorrect-answer');
                    log.classList.add('correct-answer');
                } else if (selectedAnswer.value === 'b') {
                    log.textContent = 'Incorrect! b.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                } else if (selectedAnswer.value === 'c') {
                    log.textContent = 'Incorrect! c';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                } else if (selectedAnswer.value === 'd') {
                    log.textContent = 'Incorrect! d.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                }
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

.. image:: ../images/chessboard.png
    :width: 0.1%
    :height: 0.001px
    :scale: 1%

----------------------------
**Problem 2 - Code writing**
----------------------------

**Can you write the circuit for a 4 by 4 square chess set until you calculate the position of the piece to turn?**

.. raw:: html

    <style>
    .hint {
        width: 90%;
        padding: 20px;
        margin-top: 20px;
        background-color: lightblue;
        border: 1px solid #ddd;
        border-radius: 8px;
        display: none;
        text-align: left;
        transition: background-color 0.3s ease, color 0.3s ease;
    }

    .hint img {
        max-width: 100%;
        height: auto;
    }

    .hint.dark {
        background-color: #333;
        color: #fff;
    }

    .hint-button {
        margin: 10px 0;
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
    }

    .hint-button:hover {
        background-color: #45a049;
    }

    .hint-button.dark {
        background-color: #555;
        color: #fff;
    }

    .hint-button.dark:hover {
        background-color: #444;
    }

    .tempbtm {
        background:url(/documentation/source/images/chessboard.png) no-repeat;
        max-width: 100%;
        height: auto;
        }
    </style>

    <script>
    function toggleHint(id) {
        var hint = document.getElementById(id);
        hint.style.display = (hint.style.display === "block") ? "none" : "block";
    }

    var observer = new MutationObserver(function(mutations) {
        const dark = document.documentElement.dataset.theme === 'dark';
        const hints = document.getElementsByClassName('hint');
        const buttons = document.getElementsByClassName('hint-button');
        for (let hint of hints) {
            if (dark) {
                hint.classList.add('dark');
            } else {
                hint.classList.remove('dark');
            }
        }
        for (let button of buttons) {
            if (dark) {
                button.classList.add('dark');
            } else {
                button.classList.remove('dark');
            }
        }
    });
    observer.observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});
    </script>

    <button class="hint-button" onclick="toggleHint('hint1')">Click to reveal HINT 1</button>
    <div id="hint1" class="hint">
        Start by drawing a 4 by 4 chess board and number each square from 0 to 15 in decimal and binary numbers starting with the top row.
    </div>

    <button class="hint-button" onclick="toggleHint('hint2')">Click to reveal HINT 2</button>
    <div id="hint2" class="hint">
        The trick is now to add (modulo 2) all the squares that end with a 1 and to proceed the same way with all squares that have a 1 on their second bit counting from right to left and so on using four extra squares.
    </div>

    <button class="hint-button" onclick="toggleHint('hint3')">Click to reveal HINT 3</button>
    <div id="hint3" class="hint">
        In the following picture, all squares with green numbers must be added modulo 2 and the answer must be placed in the last qubit (<em>q</em><sub>20</sub>) of the focus. The same must take place for blue squares with their result on <em>q</em><sub>21</sub>, the yellow squares on <em>q</em><sub>22</sub>, and the red squares on <em>q</em><sub>23</sub>. The zeros and ones on the squares are only there as an example.
        <img src="../_images/chessboard.png" alt="Hint 3 Image">
    </div>

.. .. image:: ../images/4x4_chessboard.png
    :width: 100%

|

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

----------------------------
**Problem 3 - Code writing**
----------------------------

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

.. raw:: html

    <style>
        #fixed-content {
            position: fixed;
            right: 10px; /* Initial visible position */
            top: 250px;
            width: 210px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            padding: 10px;
            transition: right 0.3s;
            z-index: 1000;
        }

        #fixed-content.hidden {
            right: -210px; /* Hidden position */
        }

        #toggle-button {
            position: fixed;
            right: 220px; /* Position next to the visible content */
            top: 250px;
            width: 30px;
            background-color: #ccc;
            border: 1px solid #ddd;
            padding: 10px;
            cursor: pointer;
            transition: right 0.3s;
            z-index: 1001;
        }

        #toggle-button.hidden {
            right: 10px; /* Position when content is hidden */
        }

        .arrow {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-right: 2px solid black;
            border-bottom: 2px solid black;
            transform: rotate(-45deg);
            margin-left: -3px;
        }

        .arrow.right {
            transform: rotate(135deg);
            margin-left: 2px;
        }

        .thebe-status-light {
            color: #000; /* light theme text color */
        }

        .thebe-status-dark {
            color: #000; /* dark theme text color */
        }

        /* Color transition */
        .thebe-status {
            transition: color 0.3s ease;
        }
    </style>

    <div id="toggle-button">
        <span class="arrow"></span>
    </div>
    <script type="text/javascript">
    var observer = new MutationObserver(function(mutations) {
        const dark = document.documentElement.dataset.theme == 'dark';
        const thebeStatusElements = document.getElementsByClassName('thebe-status');
        for (let el of thebeStatusElements) {
            if (dark) {
                el.classList.add('thebe-status-dark');
                el.classList.remove('thebe-status-light');
            } else {
                el.classList.add('thebe-status-light');
                el.classList.remove('thebe-status-dark');
            }
        }
    });
    observer.observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});
    </script>
    <div id="fixed-content">
        <div class="thebe-status thebe-status-light"></div>
    </div>

    <script>
        document.getElementById('toggle-button').onclick = function() {
            var fixedContent = document.getElementById('fixed-content');
            var toggleButton = document.getElementById('toggle-button');
            var arrow = toggleButton.querySelector('.arrow');

            if (fixedContent.classList.contains('hidden')) {
                fixedContent.classList.remove('hidden');
                toggleButton.classList.remove('hidden');
                arrow.classList.remove('right');
            } else {
                fixedContent.classList.add('hidden');
                toggleButton.classList.add('hidden');
                arrow.classList.add('right');
            }
        };
    </script>