cmake_minimum_required(VERSION 3.10)

project(TodoListApp)

set(CMAKE_CXX_STANDARD 14)

add_executable(TodoListApp main.cpp Task.cpp TodoList.cpp)
