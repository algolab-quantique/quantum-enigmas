====================================
Enigma 004 : The Monty Hall Exercice
====================================

The diamond you won has disappeared. Your search leads you to Monty Hall Manor, where Kettu has hidden your diamond in one of the three safes in front of you. If you choose the right safe, you can retrieve your diamond, otherwise Kettu will keep it forever. Can you determine the best approach to win to solving this enigma?

**Make sure to watch the following video before getting started with this exercise:**


.. raw:: html

    <iframe class="embed-responsive-item" width="560" height="315" src="https://www.youtube.com/embed/Hd9KhRts1uw?rel=0" allowfullscreen="">
    </iframe>

|

.. image:: ../images/E4_MCH.png
    :width: 0%
    :height: 0px
    :scale: 0%

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

.. image:: ../images/E4_P1.png
    :width: 0%
    :height: 0px
    :scale: 0%

------------------------------
**Exercice 1 - Code writing**
------------------------------

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

**Write a circuit that would only use 3 qubits instead of 4 (and still assuming that you initially chose safe number 2) for Enigma 004 - The Monty Hall Exercice.**

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

    <button class="hint-button" onclick="toggleHint('q1_hint1')">Click to reveal HINT 1</button>
    <div id="q1_hint1" class="hint">
        Use only two qubits to represent the three safes.
    </div>

    <button class="hint-button" onclick="toggleHint('q1_hint2')">Click to reveal HINT 2</button>
    <div id="q1_hint2" class="hint">
        Find a way to obtain <sup>1</sup>&frasl;<sub>3</sub> probability of measuring 00, 01, and 10 (the binary equivalent of 0, 1, and 2).
    </div>

|

.. raw:: html

    <pre data-executable="true" data-language="python">
    problem1_qc = QuantumCircuit(3)

    ### Start your work here ###

    problem1_qc.draw("mpl")
    </pre>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python

        problem1_qc = QuantumCircuit(3)

        prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))
        #Placing the diamond with 1/3 probability for each measure of 00, 01, and 10.
        problem1_qc.ry(prob_2on3, 0)
        problem1_qc.ch(0, 1)
        problem1_qc.cx(1, 0)
        problem1_qc.barrier()

        #Opening safe 1 if the diamond is in safe 0
        problem1_qc.mcx([0, 1], 2, ctrl_state='00')
        problem1_qc.barrier()

        #Opening safe 0 or 1 if the diamond is in safe 2
        problem1_qc.ch(1, 2)

        problem1_qc.draw("mpl")

    .. raw:: html

        <img class="zoomable" src="../_images/E4_P1.png" style="width:100%;cursor:pointer;">

.. image:: ../images/E4_P2.png
    :width: 0%
    :height: 0px
    :scale: 0%

------------------------------
**Exercice 2 - Code writing**
------------------------------

**Write a circuit (using three qubits to hide the diamond exactly like in the enigma) that would randomly determine the chest you choose at the start, and also determine which safe will be opened.**

You can use the following circuit that is the equivalent of a multicontrolled Hadamard gate:

.. code:: python

    problem2_qc.ry(np.pi/4, 2)
    problem2_qc.mcx([0, 1], 2)
    problem2_qc.ry(-np.pi/4, 2)

.. raw:: html

    <img class="zoomable" src="../_images/E4_MCH.png" style="width:50%;cursor:pointer">

|

.. raw:: html

    <button class="hint-button" onclick="toggleHint('q2_hint1')">Click to reveal HINT 1</button>
    <div id="q2_hint1" class="hint">
        You can use <em>q</em><sub>3</sub>, <em>q</em><sub>4</sub>, and <em>q</em><sub>5</sub> to determine the safe you put your hand on at first and <em>q</em><sub>6</sub>, <em>q</em><sub>7</sub>, and <em>q</em><sub>8</sub> to determine which safe will be opened (safe 0 is linked to <em>q</em><sub>0</sub>, <em>q</em><sub>3</sub>, and <em>q</em><sub>6</sub>; safe 1 is linked to <em>q</em><sub>1</sub>, <em>q</em><sub>4</sub>, and <em>q</em><sub>7</sub>; safe 2 is linked to <em>q</em><sub>2</sub>, <em>q</em><sub>5</sub>, and <em>q</em><sub>8</sub>).
    </div>

    <button class="hint-button" onclick="toggleHint('q2_hint2')">Click to reveal HINT 2</button>
    <div id="q2_hint2" class="hint">
        The circuit to randomly choose the safe you put your hand on at the start is the same as the one used to hide the diamond.
    </div>

    <button class="hint-button" onclick="toggleHint('q2_hint3')">Click to reveal HINT 3</button>
    <div id="q2_hint3" class="hint">
        For the circuit to determine which safe will be opened, start with the three cases where the diamond and your hand are on the same safe.
    </div>

.. raw:: html

    <pre data-executable="true" data-language="python">
    problem2_qc = QuantumCircuit(9)
    prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))

    ### Start your work here ###

    problem2_qc.draw("mpl")
    </pre>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python

        problem2_qc = QuantumCircuit(9)

        #hiding the diamond in one of the three safes
        prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))
        problem2_qc.ry(prob_2on3, 0)
        problem2_qc.ch(0, 1)
        problem2_qc.cx(1, 2)
        problem2_qc.cx(0, 1)
        problem2_qc.x(0)

        #choosing one of the three safes
        problem2_qc.ry(prob_2on3, 3)
        problem2_qc.ch(3, 4)
        problem2_qc.cx(4, 5)
        problem2_qc.cx(3, 4)
        problem2_qc.x(3)
        problem2_qc.barrier()

        #door to open in case the diamond and your hand are on safe 0
        problem2_qc.mcx([0, 3], 7)
        problem2_qc.ch(7, 8)
        problem2_qc.cx(8, 7)
        problem2_qc.barrier(6, 7, 8)

        #door to open in case the diamond and your hand are on safe 1
        problem2_qc.mcx([1, 4], 6)
        problem2_qc.ch(6, 8)
        """
        we must use an extra control on q1 or q4 for the case
        q8 is in the 1 state to avoid carelessly changing the state of q6
        """
        problem2_qc.mcx([4, 8], 6)
        problem2_qc.barrier(6, 7, 8)

        #door to open in case the diamond and your hand are on safe 2
        problem2_qc.mcx([2, 5], 6)
        problem2_qc.ry(np.pi/4, 7)
        """
        we must use an extra control on q2 or q5 for the case
        q6 is in the 1 state to avoid carelessly changing the state of q7
        """
        problem2_qc.mcx([5, 6], 7)
        problem2_qc.ry(-np.pi/4, 7)
        """
        we must use an extra control on q2 or q5 for the case
        q7 is in the 1 state to avoid carelessly changing the state of q6
        """
        problem2_qc.mcx([5, 7], 6)
        problem2_qc.barrier()

        #door to open in case the diamond is in safe 0 and your hand are on safe 1
        problem2_qc.mcx([0, 4], 8)
        #door to open in case the diamond is in safe 0 and your hand are on safe 2
        problem2_qc.mcx([0, 5], 7)
        #door to open in case the diamond is in safe 1 and your hand are on safe 0
        problem2_qc.mcx([1, 3], 8)
        #door to open in case the diamond is in safe 1 and your hand are on safe 2
        problem2_qc.mcx([1, 5], 6)
        #door to open in case the diamond is in safe 2 and your hand are on safe 0
        problem2_qc.mcx([2, 3], 7)
        #door to open in case the diamond is in safe 2 and your hand are on safe 1
        problem2_qc.mcx([2, 4], 6)

        problem2_qc.draw("mpl")

    .. raw:: html

        <img class="zoomable" src="../_images/E4_P2.png" style="width:100%;cursor:pointer">

.. image:: ../images/E4_P3-1.png
    :width: 0%
    :height: 0px
    :scale: 0%

------------------------------
**Exercice 3 - Code writing**
------------------------------

.. raw:: html

    <p><em><span style="font-size: 24px;">Time travel</span></em></p>

One very important aspect of quantim computing is that all quantum logic gates have an inverse. This means that it is possible to simulate time traveling by going to the end of an algorithm and coming back at the start simply using the inverse of every gate in a backward manner.

The following circuit shows the algorithm seen in the video with an extra qubit used for deciding which door will be opened in the case the diamond is in safe 2 at the beginning **(and assuming that you initially chose safe 2)**. The circuit has been written up to the point in time a safe has been opened by Kettu.

.. code:: python

    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(1, 'c')
    creg_d = ClassicalRegister(1, 'd')
    creg_f = ClassicalRegister(1, 'f')
    creg_g = ClassicalRegister(1, 'g')
    problem3_qc = QuantumCircuit(qreg_q, creg_c, creg_d, creg_f, creg_g)
    prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))

    problem3_qc.ry(prob_2on3, 0)
    """"
    ## q4 is used to decide which door will be opened in case
       the diamond is in safe 2 at the beginning.
    ## This is necessary since we don't want this information to be lost
       when measuring q3 again after going back in time.
    """
    problem3_qc.h(4)
    problem3_qc.ch(0, 1)
    problem3_qc.cx(1, 2)
    problem3_qc.cx(0, 1)
    problem3_qc.x(0)
    problem3_qc.barrier()
    problem3_qc.cx(0, 3)
    problem3_qc.mcx([2, 4], 3)
    problem3_qc.measure(3, 0)

    problem3_qc.draw("mpl")

.. raw:: html

    <img class="zoomable" src="../_images/E4_P3-1.png" style="width:80%;cursor:pointer">

|

**Write the rest of the algorithm to travel in time going back to the beginning, choosing a strategy that will allow you to proceed with the rest of the algorithm and win the diamond everytime.**

.. raw:: html

    <style>
        .code-inline {
            font-size: 0.85em;
            background-color: #ECECEC;
            padding: 4px 4px;
            border-radius: 4px;
            color: #92418B;
        }
    </style>

    <button class="hint-button" onclick="toggleHint('q3_hint1')">Click to reveal HINT 1</button>
    <div id="q3_hint1" class="hint">
        Place the gates in reverse order upto the barrier and choose a safe the diamond is not in.
    </div>

    <button class="hint-button" onclick="toggleHint('q3_hint2')">Click to reveal HINT 2</button>
    <div id="q3_hint2" class="hint">
        Use conditional swap to make sure you choose a safe the diamond is not in. For example, here is how you would apply a NOT gate on <em>q</em><sub>0</sub> with the condition that the classical register g has the value 1: <code class=code-inline>problem3_qc.x(0).c_if(creg_g, 1)</code>
    </div>

.. raw:: html

    <pre data-executable="true" data-language="python">
    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(1, 'c')
    creg_d = ClassicalRegister(1, 'd')
    creg_f = ClassicalRegister(1, 'f')
    creg_g = ClassicalRegister(1, 'g')
    problem3_qc = QuantumCircuit(qreg_q, creg_c, creg_d, creg_f, creg_g)

    prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))
    problem3_qc.ry(prob_2on3, 0)
    problem3_qc.h(4)
    problem3_qc.ch(0, 1)
    problem3_qc.cx(1, 2)
    problem3_qc.cx(0, 1)
    problem3_qc.x(0)
    problem3_qc.barrier()
    problem3_qc.cx(0, 3)
    problem3_qc.mcx([2, 4], 3)
    problem3_qc.measure(3, creg_g[0])


    ### Start your work here ###

    problem3_qc.barrier()
    problem3_qc.measure(0, creg_c[0])
    problem3_qc.measure(1, creg_d[0])
    problem3_qc.measure(2, creg_f[0])
    problem3_qc.measure(3, creg_g[0])

    problem3_qc.draw("mpl")
    </pre>

.. dropdown:: Click to reveal the answer
    :color: muted
    :icon: eye

    .. code:: python

        qreg_q = QuantumRegister(5, 'q')
        creg_c = ClassicalRegister(1, 'c')
        creg_d = ClassicalRegister(1, 'd')
        creg_f = ClassicalRegister(1, 'f')
        creg_g = ClassicalRegister(1, 'g')
        problem3_qc = QuantumCircuit(qreg_q, creg_c, creg_d, creg_f, creg_g)

        prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))
        problem3_qc.ry(prob_2on3, 0)
        problem3_qc.h(4)
        problem3_qc.ch(0, 1)
        problem3_qc.cx(1, 2)
        problem3_qc.cx(0, 1)
        problem3_qc.x(0)
        problem3_qc.barrier()
        problem3_qc.cx(0, 3)
        problem3_qc.mcx([2, 4], 3)
        problem3_qc.measure(3, creg_g[0])

        problem3_qc.mcx([2, 4], 3)
        problem3_qc.cx(0, 3)
        problem3_qc.barrier()
        problem3_qc.swap(0, 2).c_if(creg_g, 0)
        problem3_qc.swap(1, 2).c_if(creg_g, 1)
        problem3_qc.cx(0, 3)
        problem3_qc.mcx([2, 4], 3)

        problem3_qc.barrier()
        problem3_qc.measure(0, creg_c[0])
        problem3_qc.measure(1, creg_d[0])
        problem3_qc.measure(2, creg_f[0])
        problem3_qc.measure(3, creg_g[0])

        problem3_qc.draw("mpl")

    .. raw:: html

        <img class="zoomable" src="../_images/E4_P3-2.png" style="width:100%;cursor:pointer">

.. image:: ../images/E4_P3-2.png
    :width: 0%
    :height: 0px
    :scale: 0%

----------------------------
**Exercice 4 - Quick quiz**
----------------------------

Let's run the time travel circuit on a simulator to see the results. Run the cell below.

.. raw:: html

    <pre data-executable="true" data-language="python">
    # Time travel circuit
    qreg_q = QuantumRegister(5, 'q')
    creg_c = ClassicalRegister(1, 'c')
    creg_d = ClassicalRegister(1, 'd')
    creg_f = ClassicalRegister(1, 'f')
    creg_g = ClassicalRegister(1, 'g')
    problem3_qc = QuantumCircuit(qreg_q, creg_c, creg_d, creg_f, creg_g)

    prob_2on3 = 2 * np.arcsin(np.sqrt(2/3))
    problem3_qc.ry(prob_2on3, 0)
    problem3_qc.h(4)
    problem3_qc.ch(0, 1)
    problem3_qc.cx(1, 2)
    problem3_qc.cx(0, 1)
    problem3_qc.x(0)
    problem3_qc.barrier()
    problem3_qc.cx(0, 3)
    problem3_qc.mcx([2, 4], 3)
    problem3_qc.measure(3, creg_g[0])

    problem3_qc.mcx([2, 4], 3)
    problem3_qc.cx(0, 3)
    problem3_qc.barrier()
    problem3_qc.swap(0, 2).c_if(creg_g, 0)
    problem3_qc.swap(1, 2).c_if(creg_g, 1)
    problem3_qc.cx(0, 3)
    problem3_qc.mcx([2, 4], 3)

    problem3_qc.barrier()
    problem3_qc.measure(0, creg_c[0])
    problem3_qc.measure(1, creg_d[0])
    problem3_qc.measure(2, creg_f[0])
    problem3_qc.measure(3, creg_g[0])

    # Executing the circuit on a simulator
    simulator = AerSimulator()
    result = simulator.run(transpile(problem3_qc, simulator), shots=1000).result()
    counts = result.get_counts(problem3_qc)
    plot_histogram(counts)
    </pre>

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

**What is the meaning of the result?**

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
            { id: 'q1a', value: 'a', text: 'You always choose a safe the diamond is not in.' },
            { id: 'q1b', value: 'b', text: 'The diamond is always in safe 2.' },
            { id: 'q1c', value: 'c', text: 'There is no more diamond.' }
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
            label.textContent = answer.text;

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
                    log.innerHTML = 'Correct! The result shows that there are only 2 possible states: either the diamond is in safe 0 and safe 1 is open, or safe 1 has the diamond and safe 0 is open. Since we are assuming you initially chose safe 2, you always win by switching safes at the end. The result might suggest that the diamond in never in safe 2, but that is not the case. In the circuit, when the diamond is in safe 2-meaning you will lose-we use conditional SWAP gates to interchange the &#8739;1&#10217; state of <em>q</em><sub>2</sub> with the &#8739;0&#10217; state of <em>q</em><sub>0</sub> or <em>q</em><sub>1</sub>, depending on which door will be opened, ensuring that you always win. This operation may seem like we are moving the diamond to a different safe, but that wouldn\'t make sense in the context of the problem. Instead, you can think of it as swapping the positions of the safes without changing your initial choice. Essentially, you\'re keeping your hand on the same safe position (which started as safe 2), but the safes have been rearranged so that your hand is now on the safe that was open in the past, ensuring that your choice is correct.';
                    log.classList.remove('incorrect-answer');
                    log.classList.add('correct-answer');
                } else if (selectedAnswer.value === 'b') {
                    log.innerHTML = 'Incorrect! In the 2 possible states, the first 3 qubits (starting from the right) are in the state &#8739;100&#10217; or &#8739;010&#10217;, meaning the diamond is in safe 0 or 1. <b>However, that does not mean the diamond is never in safe 2. See the correct answer for more details.</b>';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                } else if (selectedAnswer.value === 'c') {
                    log.innerHTML = 'Incorrect! If there was no diamond, then first 3 qubits (starting from the right) would be in the &#8739;0&#10217; state.';
                    log.classList.remove('correct-answer');
                    log.classList.add('incorrect-answer');
                }
            } else {
                log.textContent = 'Select an answer before submitting.';
            }
        };
    </script>

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
        <div class="thebe-activate"></div>
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