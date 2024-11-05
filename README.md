# Match and Count

This repository contains a Python function called calculate_matches that processes a list of words, identifying how 
many of them can be fully constructed from the letters of other words within the same list. It also includes tests 
that verify the functionality.

**_NOTE_**: *This code could be optimized, but it has been left in its current form to preserve the original sequence in 
which it was written, with corresponding comments provided directly in the code.*

## Task Description
The goal of this function is to take a list of words as input and determine how many words can be formed by using 
the letters of other words within the same list. The function outputs a string indicating:

+ The count of such words,
+ The list of words that can be matched from other words.

### Constraints
+ **No Imports**: The function must not use any imported libraries (e.g., collections.Counter). The solution 
should be implemented purely with built-in Python constructs.
+ **Single Function**: Only one function, calculate_matches, is allowed to perform the task. Helper functions 
are not permitted.

## Testing
The project includes a test file that uses pytest to verify the correctness of the function calculate_matches. 
Each test case addresses different scenarios, including cases with and without matches, empty lists, single words, 
duplicate words, and words with partial overlaps.

## Linting
The project uses flake8 for code style checking. 

## Running the Code on Your Computer
To run this code on your own computer, it’s recommended to set up a virtual environment, install the dependencies, 
and then run the tests.

1. Create and activate a virtual environment:

```bash
# On macOS and Linux:
python3 -m venv venv
source venv/bin/activate
# On Windows:
python -m venv venv
venv\Scripts\activate
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
pytest
```

4. To check the code style of the main function, run:

```bash
flake8
```

The .flake8 configuration file can be adjusted as needed for specific style requirements.
<hr>
This README.md provides instructions for setting up a virtual environment, installing dependencies, running tests, 
and checking code style. Adjustments can be made as needed for additional project requirements.