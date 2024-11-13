# Simple GDB C++ Tutorial

## Step 1: Create the Sample Program
Create a file named `simple.cpp`:

```cpp
#include <iostream>
#include <vector>

// Function to calculate array sum
int calculateSum(const std::vector<int>& numbers) {
    int sum = 0;
    // Bug: Off-by-one error
    for (size_t i = 0; i <= numbers.size(); i++) {  // Should be <
        sum += numbers[i];
    }
    return sum;
}

// Function to print array
void printArray(const std::vector<int>& numbers) {
    std::cout << "Array contents: ";
    // Bug: Accessing invalid index
    for (size_t i = 0; i < numbers.size() + 1; i++) {  // Should not have +1
        std::cout << numbers[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> numbers = {1, 2, 3, 4, 5};
    
    std::cout << "Starting program...\n";
    
    printArray(numbers);
    
    int sum = calculateSum(numbers);
    std::cout << "Sum of array: " << sum << std::endl;
    
    return 0;
}
```

## Step 2: Compile the Program
```bash
g++ -g simple.cpp -o simple
```

## Step 3: Basic Debugging Session

Start GDB:
```bash
gdb ./simple
```

### Debug the Print Function
```bash
# Set breakpoint at main
(gdb) b main
(gdb) run

# Program stops at main
(gdb) n                    # Execute vector initialization
(gdb) p numbers           # Examine vector contents
Outputs: numbers = std::vector of length 5, capacity 5 = {1, 2, 3, 4, 5}

# Set breakpoint in printArray
(gdb) b printArray
(gdb) c                    # Continue to printArray

# Inside printArray, examine the loop
(gdb) p numbers.size()    # Check vector size
(gdb) n                   # Step through loop
(gdb) p i                 # Check loop counter
```

### Debug the Sum Function
```bash
# Set breakpoint in calculateSum
(gdb) b calculateSum
(gdb) c                    # Continue to calculateSum

# Watch the sum variable
(gdb) watch sum
(gdb) n                    # Step through calculation
(gdb) p i                 # Check loop counter
(gdb) p numbers.size()    # Check vector size
```

## Step 4: Common Debugging Tasks

### Print Vector Contents
```bash
(gdb) p numbers
(gdb) p numbers.size()
```

### Check Current Location
```bash
(gdb) bt                  # Show backtrace
(gdb) list               # Show current source code
```

### Examine Variables
```bash
(gdb) info locals        # Show all local variables
(gdb) p sum              # Print specific variable
```

## Step 5: Finding the Bugs

Bug 1 in printArray:
```cpp
// Bug:
for (size_t i = 0; i < numbers.size() + 1; i++)
// Fix:
for (size_t i = 0; i < numbers.size(); i++)
```

Bug 2 in calculateSum:
```cpp
// Bug:
for (size_t i = 0; i <= numbers.size(); i++)
// Fix:
for (size_t i = 0; i < numbers.size(); i++)
```

## Quick Reference Commands
- `run` (or `r`): Start program
- `break` (or `b`): Set breakpoint
- `continue` (or `c`): Continue execution
- `next` (or `n`): Execute next line
- `print` (or `p`): Print variable
- `quit` (or `q`): Exit GDB

## Practice Exercises

1. Find the Array Access Bug:
```bash
gdb ./simple
(gdb) b printArray
(gdb) run
(gdb) p numbers.size()
(gdb) watch i
(gdb) n                   # Step until crash
(gdb) p i                 # Check index at crash
```

2. Find the Sum Bug:
```bash
gdb ./simple
(gdb) b calculateSum
(gdb) run
(gdb) watch sum
(gdb) n                   # Watch sum change
(gdb) p numbers[i]        # Will crash at invalid index
```


