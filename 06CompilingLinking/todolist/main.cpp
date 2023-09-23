#include "TodoList.h"

int main() {
    TodoList todoList;
    todoList.addTask(Task("Learn about compiling and linking"));
    todoList.addTask(Task("Write a TodoList application"));
    
    // Display tasks before completing any
    todoList.displayTasks();
    
    // Complete the first task
    todoList.completeTask(0);
    
    // Display tasks after completing the first task
    todoList.displayTasks();
    
    
    return 0;
}
