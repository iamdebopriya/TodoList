import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();


async function createTodo(todoDesc: string): Promise<any> {
    const newtodo = await prisma.todo.create({
        data: {
            desc: todoDesc,
        },
    });
    return newtodo;
}
async function getTodos(): Promise<any> {
    return await prisma.todo.findMany();
}
async function getTodo(id: number): Promise<any> {
    return await prisma.todo.findUnique({
        where: { id }
    });
}
//  Update a todo by ID (desc and completed status)
async function updateTodo(id: number, desc: string, completed: boolean): Promise<any> {
    return await prisma.todo.update({
        where: { id },
        data: {
            desc,
            completed
        }
    });
}

//  Delete a single todo by ID
async function deleteTodo(id: number): Promise<any> {
    return await prisma.todo.delete({
        where: { id }
    });
}

// Delete all todos
async function deleteAllTodos(): Promise<any> {
    return await prisma.todo.deleteMany();
}

// Export all the functions
export {
    createTodo,
    getTodos,
    getTodo,
    updateTodo,
    deleteTodo,
    deleteAllTodos
};
