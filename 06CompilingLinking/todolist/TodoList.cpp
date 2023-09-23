#include <iostream>
#include "TodoList.h"

void TodoList::addTask(const Task& task) {
    tasks.push_back(task);
}

void TodoList::completeTask(int index) {
    if (index >= 0 && index < tasks.size()) {
        tasks[index].complete();
    }
}

void TodoList::displayTasks() const {
    for (const auto& task : tasks) {
        std::cout << (task.isCompleted() ? "[x] " : "[ ] ") << task.getDescription() << std::endl;
    }
}
