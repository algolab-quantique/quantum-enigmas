==================================
Enigma 001 : The Treasure Door
==================================

The adventure starts here! Alice is walking on a distant planet. Suddenly, she comes across two guardians, two doors and a treasure. Will she be able to answer the riddle correctly to win the key to the treasure? A classic problem that can be translated on a quantum computer. It's a nice way to make the leap into quantum programming and apply the concepts of state superposition, entanglement and quantum parallelism.

**Make sure to watch the following video before getting started with these exercises:**

.. raw:: html

    <iframe class="embed-responsive-item" width="560" height="315" src="https://www.youtube.com/embed/c1beJIg8lRs?si=pdDX5MuQiBQPkc_R" allowfullscreen="">
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
    <script src="https://unpkg.com/thebe@latest/lib/index.js"></script>

.. margin::

    .. dropdown:: :material-regular:`info;1.2em;sd-text-info` Note
        :animate: fade-in
        :color: info
        :open:

        When running your code, you'll know that the code is running if you see :code:`kernel thebe.ipynb status changed to ready[busy]`. If it seems to stay on :code:`ready[idle]` when running your code and/or you're not getting an output when you're supposed to, it most likely means that there's an error in your code. Since the code editor seems to be struggling with outputting error messages, there is no output.

|

Run the cell below to install the necessary packages.

.. raw:: html

    <pre data-executable="true" data-language="python" data-readonly>
    import sys
    !{sys.executable} -m pip install qiskit==1.1.1
    !{sys.executable} -m pip install qiskit_aer==0.14.2
    !{sys.executable} -m pip install pylatexenc==2.10

    # Import necessary modules
    import numpy as np
    from qiskit import QuantumCircuit
    </pre>

.. image:: ../images/E2_P1-2.png
    :width: 0.1%
    :height: 0.001px
    :scale: 1%

--------------------------------
**Exercise 1 - Code writing**
--------------------------------

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
        max-height: 80%;
        max-width: 80%;
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


Sometimes a quantum circuit can be simplified. One way of achieving this is by cancelling some quantum gates. Could you simplify the following circuit?

.. code:: python

    problem_qc = QuantumCircuit(3)

    problem_qc.h(0)
    problem_qc.h(2)
    problem_qc.cx(0, 1)
    problem_qc.barrier(0, 1, 2)
    problem_qc.cx(2, 1)
    problem_qc.x(2)
    problem_qc.cx(2, 0)
    problem_qc.x(2)
    problem_qc.barrier(0, 1, 2)
    problem_qc.swap(0, 1)
    problem_qc.x(1)
    problem_qc.cx(2, 1)
    problem_qc.x(0)
    problem_qc.x(2)
    problem_qc.cx(2, 0)
    problem_qc.x(2)

    problem_qc.draw()

.. raw:: html

    <img class="zoomable" src="../_images/E2_P1-1.png" style="width:100%;cursor:pointer;">

|

Try simplifying the circuit and rerun the calculation between each simplification to make sure you always get the same histogram. You can compare your answer to the solution.

.. raw:: html

    <pre data-executable="true" data-language="python">
    problem_qc = QuantumCircuit(12)

    ### Start writing your code here. ###


    # Visualize the circuit
    problem_qc.draw('mpl')
    </pre>

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
        The NOT, CNOT, and Hadamard gates are their own inverse. That means that if two of these gates are placed side by side they can simply be taken off.
    </div>

    <button class="hint-button" onclick="toggleHint('hint2')">Click to reveal HINT 2</button>
    <div id="hint2" class="hint">
        The SWAP gate can be taken off if the subsequent operations are adjusted between the two qubits.
    </div>

    <button class="hint-button" onclick="toggleHint('hint3')">Click to reveal HINT 3</button>
    <div id="hint3" class="hint">
        If a CNOT has the same control and target as another CNOT for which two NOT gates are applied before and after the control qubit, this can be simplified to a single NOT gate on the target qubit of the CNOT as a NOT gate is applied to the target whether the control qubit is initially in state 0 or 1.
    </div>
    <button class="hint-button" onclick="toggleHint('hint4')">Click to reveal HINT 4</button>
    <div id="hint4" class="hint">
        The circuit can be simplified until only three gates remain in the algorithm.
    </div>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python

        problem_qc = QuantumCircuit(3)
        problem_qc.h(0)
        problem_qc.cx(0,1)
        problem_qc.h(2)

        # Visualize the circuit
        problem_qc.draw('mpl')

    .. raw:: html

        <img class="zoomable" src="../_images/E2_P1-2.png" style="width:100%;cursor:pointer;">

.. image:: ../images/E2_P2.png
    :width: 0.1%
    :height: 0.001px
    :scale: 1%

--------------------------------
**Exercise 2 - Quick quiz**
--------------------------------

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

Can you interpret the results of Question 1?

 .. raw:: html

    <style>
        #log3 {
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

    <form id="question2-form">
        <div id="answers-container-q2"></div>
        <button type="submit" class="button-23">Submit Answer</button>
    </form>
    <pre id="log2"></pre>

.. raw:: html

    <script>
        // List of answers
        const answersQ2 = [
            { id: 'q2a', value: 'a', text: 'After simplification, q0, q1, and q2 remain entangled altogether.' },
            { id: 'q2b', value: 'b', text: 'After simplification, q0 and q1 are entangled with a H and a CNOT gates, while q2 only has a H gate.' },
            { id: 'q2c', value: 'c', text: 'After simplification, we finally know which guardian is lying.' }
        ];

        // Function to shuffle the answers
        function shuffle(array) {
            for (let i = array.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [array[i], array[j]] = [array[j], array[i]];
            }
        }

        // Shuffle the answers
        shuffle(answersQ2);

        // Insert shuffled answers into the form
        const containerQ2 = document.getElementById('answers-container-q2');
        answersQ2.forEach(answer => {
            const input = document.createElement('input');
            input.type = 'radio';
            input.id = answer.id;
            input.name = 'q2';
            input.value = answer.value;

            const label = document.createElement('label');
            label.htmlFor = answer.id;
            label.textContent = answer.text;

            containerQ2.appendChild(input);
            containerQ2.appendChild(label);
            containerQ2.appendChild(document.createElement('br'));
        });

        // Handle form submission
        document.querySelector('#question2-form').onsubmit = function(e) {
            e.preventDefault();
            const log = document.getElementById('log2');
            const selectedAnswer = document.querySelector('input[name="q2"]:checked');
            if (selectedAnswer) {
                if (selectedAnswer.value === 'a') {
                    log.textContent = 'Incorrect! q2 is not entangled with the other two qubits.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                } else if (selectedAnswer.value === 'b') {
                    log.textContent = 'Correct! The first two qubits are entangled while the third (q2) is not.';
                    log.classList.remove('incorrect-answer');
                    log.classList.add('correct-answer');
                } else if (selectedAnswer.value === 'c') {
                    log.textContent = 'Incorrect! A measurement on q2 is needed to know which guardian is lying.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                }
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

.. image:: ../images/E2_P1-1.png
    :width: 0%
    :height: 0px
    :scale: 0%

--------------------------------
**Exercise 3 - Quick quiz**
--------------------------------

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

Launching algorithms on modern quantum computers does not always lead to 100% successful results, as some noise sometime causes bad results. If you launch the whole circuit on a real quantum computer, multiple times, what percentage of good answers might you get?

 .. raw:: html

    <style>
        #log3 {
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

    <form id="question3-form">
        <div id="answers-container-q3"></div>
        <button type="submit" class="button-23">Submit Answer</button>
    </form>
    <pre id="log3"></pre>

.. raw:: html

    <script>
        // List of answers
        const answersQ3 = [
            { id: 'q3a', value: 'a', text: 'Less than 100%.' },
            { id: 'q3d', value: 'b', text: '100%.' }
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
                    log.textContent = 'Correct! The noise existing in real quantum hardware induces bad results.';
                    log.classList.remove('incorrect-answer');
                    log.classList.add('correct-answer');
                } else if (selectedAnswer.value === 'b') {
                    log.textContent = 'Incorrect! Think again about the noise.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                }
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

.. image:: ../images/E2_P1-1.png
    :width: 0%
    :height: 0px
    :scale: 0%


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

        .thebe-activate-light {
            color: #111; /* light theme text color */
        }

        .thebe-activate-dark {
            color: #111; /* dark theme text color */
        }

        /* Color transition */
        .thebe-activate {
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
        };
        const thebeActivateElements = document.getElementsByClassName('thebe-activate');
        for (let el of thebeStatusElements) {
            if (dark) {
                el.classList.add('thebe-activate-dark');
                el.classList.remove('thebe-activate-light');
            } else {
                el.classList.add('thebe-activate-light');
                el.classList.remove('thebe-activate-dark');
            }
        }
    });
    observer.observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});
    </script>
    <div id="fixed-content">
        <div class="thebe-activate thebe-activate-light"></div>
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