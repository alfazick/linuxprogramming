#pragma once

#include <string>

class Task {
    public:
        Task(const std::string& description);
        void complete();
        std::string getDescription() const;
        bool isCompleted() const;
        void printTaskDetails() const;
    private:
        std::string description;
        bool completed;
};

