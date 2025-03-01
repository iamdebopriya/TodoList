# **Todo Fullstack App**

This is a fullstack **Todo Application** built using:

- **Backend:** Node.js + Prisma + Supabase (Database)
- **Frontend:** Streamlit (Python)

---

## **Features**
- ✅ Add, Update, Delete Todos.
- ✅ View Todo List with Checkboxes.
- ✅ Backend with Prisma + Supabase Integration.
- ✅ Modern UI with Streamlit.

---

## **Tech Stack**
- **Backend:** Node.js, TypeScript, Express.js, Prisma ORM, Supabase, CORS
- **Frontend:** Python, Streamlit
- **Tools:** Nodemon, Prisma CLI, Supabase Studio

---

## **How to Run**

### **Backend Setup**

1. **Navigate to the backend folder:**
    ```bash
    cd prisma_1st
    ```

2. **Install dependencies (TypeScript, Prisma, CORS, Express, Nodemon, etc.):**
    ```bash
    npm install
    ```

3. **Set up the `.env` file with your Supabase URL and Database credentials.**

4. **Run database migration:**
    ```bash
    npx prisma migrate dev --name init
    ```

5. **Generate Prisma client:**
    ```bash
    npx prisma generate
    ```

6. **Validate Prisma schema:**
    ```bash
    npx prisma validate
    ```

7. **Compile TypeScript files:**
    ```bash
    npx tsc
    ```

8. **Run the backend server using Nodemon:**
    ```bash
    npx nodemon dist/index.js
    ```

---

### **Frontend Setup**

1. **Navigate to the frontend folder:**
    ```bash
    cd streamlit_frontend
    ```

2. **Run the Streamlit application:**
    ```bash
    streamlit run todo.py
    ```

---

## **Deployment**

- **Backend:** Deploy to **Render** / **Railway**.
- **Frontend:** Deploy to **Streamlit Community Cloud**.

---

## **License**
**MIT**
