import streamlit as st
import requests

# Backend base URL (running on your local Prisma backend)
BASE_URL = "http://localhost:3000/todos"  # Update if needed
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #a8edea, #fed6e3); /* Light Ocean to Light Pink */
        font-family: 'Arial', sans-serif;
    }
    .stTextInput>div>div>input, .stButton>button, .stCheckbox>div {
        color: #4B0082;  /* Dark Purple */
        font-weight: bold;
    }
    .stCheckbox>div>label {
        color: #4B0082 !important; /* Checkbox label */
    }
    .stMarkdown {
        color: #4B0082; /* General text */
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("📋 Todo List - Full CRUD with Prisma Backend")

# Utility function to fetch all todos
def fetch_todos():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json().get('todos', [])
    else:
        st.error(f"Failed to fetch todos. Status: {response.status_code}")
        return []

# Utility function to add a new todo
def add_todo(desc):
    response = requests.post(BASE_URL, json={"desc": desc})
    if response.status_code in [ 200, 201 ]:
        st.success("✅ Todo added successfully!")
        st.rerun()
    else:
        st.error(f"❌ Failed to add todo. Status: {response.status_code}")

# Utility function to update a todo
def update_todo(todo_id, desc=None, completed=None):
    payload = {}
    if desc is not None:
        payload['desc'] = desc
    if completed is not None:
        payload['completed'] = completed

    response = requests.put(f"{BASE_URL}/{todo_id}", json=payload)
    if response.status_code == 200:
        st.success("✅ Todo updated successfully!")
        st.rerun()
    else:
        st.error(f"❌ Failed to update todo. Status: {response.status_code}")

# Utility function to delete a todo
def delete_todo(todo_id):
    response = requests.delete(f"{BASE_URL}/{todo_id}")
    if response.status_code == 200:
        st.success("✅ Todo deleted successfully!")
        st.rerun()
    else:
        st.error(f"❌ Failed to delete todo. Status: {response.status_code}")

# --- Fetch and display all todos ---
todos = fetch_todos()

if not todos:
    st.write("🚀 No todos found. Add some tasks!")

# --- Todo list display with edit, delete, and checkbox toggle ---
for todo in todos:
    col1, col2, col3, col4 = st.columns([0.05, 0.5, 0.2, 0.2])

    # Completed Checkbox
    completed = col1.checkbox("", value=todo['completed'], key=f"todo-{todo['id']}")
    if completed != todo['completed']:
        update_todo(todo['id'], completed=completed)

    # Description and Edit Button
    new_desc = col2.text_input(f"Edit desc {todo['id']}", value=todo['desc'], key=f"edit-{todo['id']}")
    if new_desc != todo['desc']:
        update_todo(todo['id'], desc=new_desc)

    # Update Button (optional since auto-updates on change)
    if col3.button("Update", key=f"update-{todo['id']}"):
        update_todo(todo['id'], desc=new_desc)

    # Delete Button
    if col4.button("❌ Delete", key=f"delete-{todo['id']}"):
        delete_todo(todo['id'])

st.write("---")

# --- Add new todo ---
with st.form("add_todo_form"):
    new_todo_desc = st.text_input("📝 New Todo Description")
    submitted = st.form_submit_button("➕ Add Todo")

    if submitted and new_todo_desc.strip():
        add_todo(new_todo_desc)

