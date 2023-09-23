#pragma once

#include <vector>
#include "Task.h"

class TodoList {
    public:
        void addTask(const Task& task);
        void completeTask(int index);
        void displayTasks() const;
    private:
        std::vector<Task> tasks;
};
