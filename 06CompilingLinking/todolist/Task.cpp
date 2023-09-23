
#include "Task.h"
#include <iostream> 

Task::Task(const std::string& description)
    : description(description), completed(false) {}


void Task::printTaskDetails() const {
    std::cout << "Task: " << description << " - " << (completed ? "Completed" : "Not Completed") << std::endl;
}

void Task::complete(){
    completed = true;
    // For demonstration purposes, print details when a task is completed.
    printTaskDetails();
}

std::string Task::getDescription() const {
    return description;
}


bool Task::isCompleted() const {
    return completed;
}

