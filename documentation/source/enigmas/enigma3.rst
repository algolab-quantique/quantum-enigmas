.. meta:: 
    :description: Quantum Enigma 003: The Four-Square Chessboard
    :title: Enigma 003

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

    <pre data-executable="true" data-language="python" data-readonly>
    import sys
    !{sys.executable} -m pip install qiskit==1.1.1
    !{sys.executable} -m pip install qiskit_aer==0.14.2
    !{sys.executable} -m pip install pylatexenc==2.10
    </pre>

Now, run the cell below to import the necessary packages.

.. raw:: html

    <pre data-executable="true" data-language="python" data-readonly>
    import numpy as np
    from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, transpile
    from qiskit.visualization import plot_histogram
    from qiskit_aer import Aer, AerSimulator
    </pre>

.. image:: ../images/E3_P1.png
    :width: 0.1%
    :height: 0px
    :scale: 0%

---------------------------
**Problem 1 - Quick quiz**
---------------------------

.. raw:: html

    <style>
    .zoomable-container {
        display: inline-block;
        cursor: pointer;
        position: relative;
    }

    .zoomable {
        max-width: 100%;
        height: auto;
        border-radius: 5px;
        transition: transform 0.3s ease;
    }

    #imageModal {
        display: none;
        position: fixed;
        z-index: 9999;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.8);
        justify-content: center;
        align-items: center;
    }

    #imageModal img {
        margin: auto;
        display: block;
        max-width: 80%;
        max-height: 80%;
        border-radius: 5px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        object-fit: contain;
    }

    #imageModal .close {
        position: absolute;
        top: 20px;
        right: 35px;
        color: #fff;
        font-size: 40px;
        font-weight: bold;
        transition: color 0.3s ease;
        cursor: pointer;
        z-index: 10000;
    }

    #imageModal .close:hover,
    #imageModal .close:focus {
        color: #bbb;
    }
    </style>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const modal = document.getElementById("imageModal");
            const modalImg = document.getElementById("img01");

            document.querySelectorAll('.zoomable').forEach(function(image) {
                image.onclick = function() {
                    modal.style.display = "block";
                    modalImg.src = this.src;
                }
            });

            var closeBtn = document.getElementsByClassName("close")[0];
            closeBtn.onclick = function() {
                modal.style.display = "none";
            }
        });
    </script>
    <div id="imageModal">
        <span class="close">&times;</span>
        <img class="modal-content" id="img01">
    </div>

The enigma uses a modulo 2 addition like this one:

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

Meaning that adding any two of them gives the third one as an answer (this is true for any numbers). Playing with modulo 2 additions also has other interesting characteristics. In the enigma, adding the first number to the second is done by applying a CNOT between *q*\ :sub:`4`\  and *q*\ :sub:`6`\  (and *q*\ :sub:`5`\  and *q*\ :sub:`7`\). Here is the code of the algorithm in the enigma. 

.. code:: python

    #qubits 0 to 3 are the 4 squares
    #qubits 4 and 5 is where the key is hidden
    #qubits 6 and 7 is where the focus first lands
    #qubits 8 and 9 is where the focus lands at the end which is the key location
    problem1_qc = QuantumCircuit(10)

    #coin distribution on each square
    for i in range(4):
        problem1_qc.h(i)

    problem1_qc.barrier([4,5])

    #hiding the key under one of the 4 squares
    problem1_qc.h(4)
    problem1_qc.h(5)

    problem1_qc.barrier([4,5,6,7])

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q5
    problem1_qc.cx(1, 6)
    problem1_qc.cx(3, 6)
    problem1_qc.barrier([6,7])

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q6
    problem1_qc.cx(2, 7)
    problem1_qc.cx(3, 7)
    problem1_qc.barrier([6,7])

    #adding modulo 2 the position of the key and the position of the focus
    problem1_qc.cx(4, 6)
    problem1_qc.cx(5, 7)
    problem1_qc.barrier([6,7])

    #turning the right coin
    problem1_qc.ccx(7,6,3)
    problem1_qc.barrier([6,7])
    problem1_qc.x(6)
    problem1_qc.ccx(7,6,2)
    problem1_qc.x(6)
    problem1_qc.barrier([6,7])
    problem1_qc.x(7)
    problem1_qc.ccx(7,6,1)
    problem1_qc.x(7)
    problem1_qc.barrier([6,7])
    problem1_qc.x(6)
    problem1_qc.x(7)
    problem1_qc.ccx(7,6,0)
    problem1_qc.x(7)
    problem1_qc.x(6)
    problem1_qc.barrier([6,7,8,9])

    #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q8
    problem1_qc.cx(1, 8)
    problem1_qc.cx(3, 8)
    problem1_qc.barrier([6,7,8,9])

    #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q9
    problem1_qc.cx(2, 9)
    problem1_qc.cx(3, 9)

    problem1_qc.draw(output='mpl')

.. raw:: html

    <img class="zoomable" src="../_images/E3_P1.png" style="width:100%;cursor:pointer;">

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

    <p><strong>What is the meaning of the values of <em>q</em><sub>6&nbsp;</sub>and <em>q</em><sub>7&nbsp;</sub>after all the gates in the circuit have been applied?</strong></p>
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
            { id: 'q1a', value: 'a', text: '<em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> correspond to the binary digits of the square on which to flip the coin' },
            { id: 'q1b', value: 'b', text: '<em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> had a meaning at one point, but don\'t correspond to anything at the end of the circuit' },
            { id: 'q1c', value: 'c', text: '<em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> correspond to the binary digits of the square your focus is on' },
            { id: 'q1d', value: 'd', text: '<em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> now correspond to the binary digits of the square where the key is located' }
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
                    log.innerHTML = 'Correct! After the first 4 CNOT gates, <em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> correspond to the binary digits of the focus square. Then, the next 2 CNOT gates between <em>q</em><sub>4</sub> and <em>q</em><sub>6</sub>, and between <em>q</em><sub>5</sub> and <em>q</em><sub>7</sub>, add the key position to the focus position. Thus, <em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> correspond to the binary digit of the square on which to flip the coin.'; ;
                    log.classList.remove('incorrect-answer');
                    log.classList.add('correct-answer');
                } else if (selectedAnswer.value === 'b') {
                    log.innerHTML = 'Incorrect! After the first 6 CNOT gates, <em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> have a meaning. Since all the following operations on them are either CNOT controls or X gates applied twice, their values do not change, and they retain their meaning.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                } else if (selectedAnswer.value === 'c') {
                    log.innerHTML = 'Incorrect! <em>q</em><sub>6</sub> and <em>q</em><sub>7</sub> corresponded to the binary digits of the square your focus was on after the first 4 CNOT gates. However, after the next 2 CNOT gates, this is no longer the case.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                } else if (selectedAnswer.value === 'd') {
                    log.innerHTML = 'Incorrect! The qubits that represent the binary digits of the square where the key is located are either <em>q</em><sub>4</sub> and <em>q</em><sub>5</sub> or <em>q</em><sub>8</sub> and <em>q</em><sub>9</sub>.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                }
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

.. image:: ../images/chessboard.png
    :width: 0%
    :height: 0px
    :scale: 0%

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

.. image:: ../images/E3_P2.png
    :width: 0%
    :height: 0px
    :scale: 0%

.. raw:: html

    <pre data-executable="true" data-language="python">
    nb_coins = 16
    nb_key = 4
    nb_focus_first = 4
    nb_focus_key = 4
    nb_qubits = nb_coins + nb_key + nb_focus_first + nb_focus_key

    #qubits 0 to 15 are the 16 squares
    #qubits 16 to 19 is where the key is hidden
    #qubits 20 to 23 is where the focus first lands
    #qubits 24 to 27 is where the focus lands at the end which is the key location
    problem2_qc = QuantumCircuit(nb_qubits)

    # The code for this problem is similar to the one in Problem 1, simply longer.
    ### Start your work here ###


    problem2_qc.draw(output='mpl')
    </pre>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python
        
        nb_coins = 16
        nb_key = 4
        nb_focus_first = 4
        nb_focus_key = 4
        nb_qubits = nb_coins + nb_key + nb_focus_first + nb_focus_key

        #qubits 0 to 15 are the 16 squares
        #qubits 16 to 19 is where the key is hidden
        #qubits 20 to 23 is where the focus first lands
        #qubits 24 to 27 is where the focus lands at the end which is the key location
        problem2_qc = QuantumCircuit(nb_qubits)

        #coin distribution on each square
        for i in range(16):
            problem2_qc.h(i)

        problem2_qc.barrier()

        #hiding the key under one of the 16 squares
        for i in range(16, 20):
            problem2_qc.h(i)

        problem2_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q20
        problem2_qc.cx(1, 20)
        problem2_qc.cx(3, 20)
        problem2_qc.cx(5, 20)
        problem2_qc.cx(7, 20)
        problem2_qc.cx(9, 20)
        problem2_qc.cx(11, 20)
        problem2_qc.cx(13, 20)
        problem2_qc.cx(15, 20)
        problem2_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q21
        problem2_qc.cx(2, 21)
        problem2_qc.cx(3, 21)
        problem2_qc.cx(6, 21)
        problem2_qc.cx(7, 21)
        problem2_qc.cx(10, 21)
        problem2_qc.cx(11, 21)
        problem2_qc.cx(14, 21)
        problem2_qc.cx(15, 21)
        problem2_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers have a 1 as their 3rd digit from the right and putting the answer on q22
        problem2_qc.cx(4, 22)
        problem2_qc.cx(5, 22)
        problem2_qc.cx(6, 22)
        problem2_qc.cx(7, 22)
        problem2_qc.cx(12, 22)
        problem2_qc.cx(13, 22)
        problem2_qc.cx(14, 22)
        problem2_qc.cx(15, 22)
        problem2_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers have a 1 as their 4th digit from the right and putting the answer on q23
        problem2_qc.cx(8, 23)
        problem2_qc.cx(9, 23)
        problem2_qc.cx(10, 23)
        problem2_qc.cx(11, 23)
        problem2_qc.cx(12, 23)
        problem2_qc.cx(13, 23)
        problem2_qc.cx(14, 23)
        problem2_qc.cx(15, 23)
        problem2_qc.barrier()

        #adding modulo 2 the position of the key and the position of the focus
        problem2_qc.cx(16, 20)
        problem2_qc.cx(17, 21)
        problem2_qc.cx(18, 22)
        problem2_qc.cx(19, 23)

        problem2_qc.draw(output='mpl')
    
    .. raw:: html

        <img src="../_images/E3_P2.png" class="zoomable" style="width:100%;cursor:pointer;">

.. image:: ../images/E3_P3.png
        :width: 0%
        :height: 0px
        :scale: 0%

----------------------------
**Problem 3 - Code writing**
----------------------------

**Complete the circuit to allow Alice to turn the right coin knowing that the MCX gate is the multi-control X gate.**

To avoid using a lot of X gates to control the 0 state, we can specify the control state of each control qubit.
Here is the way to use the MCX gate if we wanted to have the control-qubits 20, 21, 22, and 23 control the state 1, 1, 1, and 0 respectively, and qubit 14 as the target-qubit:

:code:`problem3_qc.mcx([20, 21, 22, 23], 14, ctrl_state='0111')`.

.. raw:: html

    <pre data-executable="true" data-language="python">
    ctrl_qubits = [20, 21, 22, 23]
    problem3_qc = problem2_qc.copy()
    problem3_qc.barrier()

    # turning the right coin on the bottom row
    problem3_qc.mcx(ctrl_qubits, 15, ctrl_state='1111')

    problem3_qc.mcx(ctrl_qubits, 14, ctrl_state='0111')

    ### Continue writing the code here ###


    problem3_qc.draw(output='mpl')
    </pre>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python

        ctrl_qubits = [20, 21, 22, 23]
        problem3_qc = problem2_qc.copy()
        problem3_qc.barrier()

        #turning the right coin on the bottom row
        problem3_qc.mcx(ctrl_qubits, 15, ctrl_state='1111')

        problem3_qc.mcx(ctrl_qubits, 14, ctrl_state='0111')

        problem3_qc.mcx(ctrl_qubits, 13, ctrl_state='1011')

        problem3_qc.mcx(ctrl_qubits, 12, ctrl_state='0011')

        #turning the right coin on the 3rd row
        problem3_qc.mcx(ctrl_qubits, 11, ctrl_state='1101')

        problem3_qc.mcx(ctrl_qubits, 10, ctrl_state='0101')

        problem3_qc.mcx(ctrl_qubits, 9, ctrl_state='1001')

        problem3_qc.mcx(ctrl_qubits, 8, ctrl_state='0001')

        #turning the right coin on the 2nd row
        problem3_qc.mcx(ctrl_qubits, 7, ctrl_state='1110')

        problem3_qc.mcx(ctrl_qubits, 6, ctrl_state='0110')

        problem3_qc.mcx(ctrl_qubits, 5, ctrl_state='1010')

        problem3_qc.mcx(ctrl_qubits, 4, ctrl_state='0010')

        #turning the right coin on the top row
        problem3_qc.mcx(ctrl_qubits, 3, ctrl_state='1100')

        problem3_qc.mcx(ctrl_qubits, 2, ctrl_state='0100')

        problem3_qc.mcx(ctrl_qubits, 1, ctrl_state='1000')

        problem3_qc.mcx(ctrl_qubits, 0, ctrl_state='0000')

        #now that the right coin has been turned, it is time to put the focus on the square where the key is located
        problem3_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers finish by 1 and putting the answer on q24
        problem3_qc.cx(1, 24)
        problem3_qc.cx(3, 24)
        problem3_qc.cx(5, 24)
        problem3_qc.cx(7, 24)
        problem3_qc.cx(9, 24)
        problem3_qc.cx(11, 24)
        problem3_qc.cx(13, 24)
        problem3_qc.cx(15, 24)
        problem3_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers have a 1 as second to last digit and putting the answer on q25
        problem3_qc.cx(2, 25)
        problem3_qc.cx(3, 25)
        problem3_qc.cx(6, 25)
        problem3_qc.cx(7, 25)
        problem3_qc.cx(10, 25)
        problem3_qc.cx(11, 25)
        problem3_qc.cx(14, 25)
        problem3_qc.cx(15, 25)
        problem3_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers have a 1 as their 3rd digit from the right and putting the answer on q26
        problem3_qc.cx(4, 26)
        problem3_qc.cx(5, 26)
        problem3_qc.cx(6, 26)
        problem3_qc.cx(7, 26)
        problem3_qc.cx(12, 26)
        problem3_qc.cx(13, 26)
        problem3_qc.cx(14, 26)
        problem3_qc.cx(15, 26)
        problem3_qc.barrier()

        #finding the parity of 1's on squares for which binary numbers have a 1 as their 4th digit from the right and putting the answer on q27
        problem3_qc.cx(8, 27)
        problem3_qc.cx(9, 27)
        problem3_qc.cx(10, 27)
        problem3_qc.cx(11, 27)
        problem3_qc.cx(12, 27)
        problem3_qc.cx(13, 27)
        problem3_qc.cx(14, 27)
        problem3_qc.cx(15, 27)

        problem3_qc.draw(output='mpl')

    .. raw:: html

        <img class="zoomable" src="../_images/E3_P3.png" style="width:100%;cursor:pointer;">

|

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