# import streamlit as st
# import functions
#
# todos = functions.get_todos()
#
#
# def add_todo():
#     todo = st.session_state["new_todo"] + '\n'
#     todos.append(todo)
#     functions.write_todos(todos)
#     st.session_state["new_todo"] = ''
#
#
# st.title('My ToDo App')
#
# for index, todo in enumerate(todos):
#     checkbox = st.checkbox(todo, key=todo)
#     if checkbox:
#         todos.pop(index)
#         functions.write_todos(todos)
#         del st.session_state[todo]
#         st.experimental_rerun()
#
# st.text_input(label='', placeholder='Add new todo...',
#               on_change=add_todo, key='new_todo')


import streamlit as st
import functions

# Retrieve the list of todos
todos = functions.get_todos()

# Function to add a new todo
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ''  # Clear the input text box

# Set the page configuration
st.set_page_config(page_title="My ToDo App", page_icon="✅")

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        text-align: center;
        font-size: 48px;
        color: #4CAF50;
    }
    .new-todo-input input {
        width: 100% !important;
        padding: 10px !important;
        font-size: 20px !important;
    }
    .todo-item {
        font-size: 24px;
        margin: 10px 0;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888888;
    }
    </style>
    """, unsafe_allow_html=True)

# App title
st.markdown('<div class="title">My ToDo App</div>', unsafe_allow_html=True)

# Add a new todo input box
st.text_input(
    label='',
    placeholder='Add new todo...',
    on_change=add_todo,
    key='new_todo'
)

# Display the todo items
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

# Footer
st.markdown('<div class="footer">Built with Streamlit</div>', unsafe_allow_html=True)
