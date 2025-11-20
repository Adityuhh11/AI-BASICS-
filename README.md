AI Basics: Forward Search Reasoning Engine
==========================================

Project Overview
----------------

This repository contains the implementation of a **Forward Search (Forward Chaining)** algorithm designed to solve propositional logic problems. The system takes a knowledge base (a set of known facts and implication rules) and a query, then iteratively infers new knowledge to prove or disprove the query.

This project was completed as part of the **SE_14 Artificial Intelligence Basics** module assessment.

Repository Structure
--------------------

The codebase is organized into the following components:

-   **`main.py`**: The entry point of the application. It defines several logic test problems (knowledge bases + queries) and compares the performance of the custom Forward Search algorithm against a reference Model Checker.

-   **`solvers/`**: Contains the core algorithms.

    -   `forward_search.py`: My implementation of the Forward Search algorithm.

    -   `model_check.py`: The reference model checking algorithm used for verification and performance comparison.

-   **`logic/`**: Contains the classes representing propositional logic components.

    -   `symbol.py`: Represents atomic logical symbols (e.g., A, B).

    -   `sentence.py`: Base class for logical sentences.

    -   `implication.py`, `biconditional.py`, `conjunction.py`, `disjunction.py`, `negation.py`: Implementations of logical connectives.

Prerequisites
-------------

-   **Python 3.x**: This project relies on the Python standard library. No external dependencies (like `numpy` or `pandas`) are required.

How to Run
----------

1.  Open your terminal or command prompt.

2.  Navigate to the root directory of this repository (where `main.py` is located).

3.  Execute the main script:

    ```
    python main.py

    ```

Expected Output
---------------

The script will run 5 test problems sequentially. For each problem, it will:

1.  Run the **Model Checking** algorithm (Reference).

2.  Run the **Forward Search** algorithm (My Implementation).

3.  Display the result (`True`, `False`, or `None`) and the execution time for both.

**Example Output:**

```
Testing Problem 2
... running model checking
... running forward search
... done.

- result - model checking:  True
- result - forward search:  True
- time for model checking 25720500 ns
- time for forward search 0 ns

```

Algorithm Details
-----------------

The **Forward Search** algorithm (`solvers/forward_search.py`) utilizes a data-driven approach:

1.  It repeatedly scans the knowledge base for `Implication` and `Biconditional` rules.

2.  If the premises of a rule are satisfied by currently known facts, the conclusion is inferred and added to the knowledge base.

3.  This process repeats until the query is proven, disproven, or no further inferences can be made.