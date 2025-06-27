
import streamlit as st
import random
import sympy as sym
from sympy import *

# Set the title of the Streamlit app
st.title("Math Practice Quiz")

a, b = sym.symbols('a, b')
X, Y = sym.symbols('X, Y')

# Initialize session state for correct answers if not already present
if 'correct_answers' not in st.session_state:
    st.session_state['correct_answers'] = 0

def extend_prod_not_st():
    st.header("Exercise 1: Expand Notable Product")

    num1 = random.randint(2, 9)
    problem = a**num1 - b**num1
    solution = problem.factor()

    st.write("Expand the following notable product:")
    st.latex(latex(problem))

    # Define options and the correct one
    options = [solution * 1, solution * (b - a), solution * a, solution * b]
    #options = [latex(solution * 1), latex(solution * (b - a)), latex(solution * a),latex(solution * b)]
    # Shuffle the options randomly
    random.shuffle(options)

    st.write("Choose the correct answer:")

    # Store the correct option to compare later
    correct_option_str = latex(solution)

    # Display options using radio buttons
    selected_option = st.radio(
        "Options:",
        st.latex([latex(opt) for opt in options]),
        key='prod_not_options' # Use a unique key for this widget
    )

    # Get the index of the selected option
    selected_index = [latex(opt) for opt in options].index(selected_option)

    # Check the answer when a button is clicked (or automatically on change)
    # Let's use a button for clarity
    if st.button("Check Answer - Exercise 1", key='check_prod_not'):
        if selected_option == correct_option_str:
            st.success("Correct!")
            st.session_state['correct_answers'] += 1
        else:
            st.error("Incorrect.")


def simpl_exp_Agr_st():
    st.header("Exercise 2: Simplify Expression by Grouping")

    num1 = random.randint(2, 3)
    operations1 = ['+', '-']
    operation1 = random.choice(operations1)

    if operation1 == "+":
        expr1 = (X + Y) ** num1
    else:
        expr1 = (X - Y) ** num1

    solution1 = expr1.expand()

    num2 = random.randint(2, 4)
    operations2 = ['+', '-']
    operation2 = random.choice(operations2)

    if operation2 == "+":
        expr2 = (X + Y) ** num2
    else:
        expr2 = (X - Y) ** num2

    solution2 = expr2.expand()

    operations_combine = ['+', '-']
    operation_combine = random.choice(operations_combine)

    if operation_combine == "+":
        problema = expr1 + expr2
        simp = solution1 + solution2
    else:
        problema = expr1 - expr2
        simp = solution1 - solution2

    st.write("Simplify the following expression by grouping:")
    st.latex(latex(problema))

    # Define options and the correct one
    options = [simp * 1, simp * X, simp * Y, simp * 2]
    # Shuffle the options randomly
    random.shuffle(options)

    st.write("Choose the correct answer:")

    # Store the correct option to compare later
    correct_option_str = latex(simp)

    # Display options using radio buttons
    selected_option = st.radio(
        "Options:",
        [latex(opt) for opt in options],
        key='simpl_exp_options' # Use a unique key for this widget
    )

    # Check the answer when a button is clicked (or automatically on change)
    if st.button("Check Answer - Exercise 2", key='check_simpl_exp'):
        if selected_option == correct_option_str:
            st.success("Correct!")
            st.session_state['correct_answers'] += 1
        else:
            st.error("Incorrect.")

# Run the Streamlit functions to display questions
extend_prod_not_st()
st.markdown("---") # Add a separator
simpl_exp_Agr_st()

# Display the total number of correct answers
st.subheader(f"Total correct answers: {st.session_state['correct_answers']}")

# Optional: Add a button to reset the score
if st.button("Reset Score"):
    st.session_state['correct_answers'] = 0
    st.experimental_rerun() # Rerun the app to show the reset score
