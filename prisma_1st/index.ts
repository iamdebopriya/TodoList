import express, { Request, Response } from 'express';
import dotenv from 'dotenv';
import cors from 'cors';
import { createTodo } from './controllers/todo';
import { getTodos } from './controllers/todo';
import { getTodo } from './controllers/todo';   
import { updateTodo } from './controllers/todo';
import { deleteTodo } from './controllers/todo';    
import { deleteAllTodos } from './controllers/todo';

dotenv.config();
const PORT = process.env.PORT || 3000;

const app = express();
app.use(express.json());
app.use(cors());

app.get('/', (req: Request, res: Response) => {
    res.json({ message: 'Hello World, TO DO LIST' });
});

app.post('/todos', async (req: Request, res: Response) => {
    try {
        const { desc } = req.body;
        const newtodo = await createTodo(desc);
        res.json({ message: 'Todo created', success: true, newtodo: newtodo });
    } catch (err) {
        res.json(err);
    }
});
app.get('/todos', async (req: Request, res: Response) => {
    try {
        const todos = await getTodos();
        res.json({ message: 'Get all todos' ,
        success: true,
            todos:todos
        }
                   
        );
        
    } catch (err) {
        res.json(err);
    }
});
app.get('/todos/:id', async (req: Request, res: Response) => {
    try {
        const { id } = req.params;
        const todo =await getTodo(Number(id));
        res.json({ message: 'Get one todo' ,success: true, todo: todo});
     
    } catch (err) {
        res.json(err);
    }
});
app.put('/todos/:id', async (req: Request, res: Response) => {
    try {
        const { id } = req.params;
        const { desc ,completed} = req.body;
        const uptodo = await updateTodo(Number(id), desc, completed);
        res.json({ message: 'Update one todo' , success: true, uptodo: uptodo });
    } catch (err) {
        res.json(err);      
    }
}
);
app.delete('/todos/:id', async (req: Request, res: Response) => {
    try {
        const { id } = req.params;
        const deltodo = await deleteTodo(Number(id));
        res.json({ message: 'Delete one todo' , success: true, deltodo: deltodo });
    } catch (err) {
        res.json(err);
    }
});
app.delete('/todos', async (req: Request, res: Response) => {
    try {
        await deleteAllTodos();
        res.json({ message: 'Delete all todo' ,sucess: true});
    } catch (err) {
        res.json(err);
    }
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
