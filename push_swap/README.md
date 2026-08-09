*This project has been created as part of the 42 curriculum by cebouhad and mabrugger.*

# 🔄 Push Swap

## 📖 Description

**Push Swap** is a sorting algorithm project from the 42 curriculum.

The objective is to sort a list of integers using two stacks (`A` and `B`) while minimizing the number of operations performed. The challenge is not only to sort the data correctly but also to find an efficient sequence of instructions.
We represent both stacks (**Stack A** and **Stack B**) using two pointers operating on the same array of values.

Stack A is traversed in the forward memory direction. Operations move the pointer using a++.
When the pointer goes beyond the array boundaries, the stack is considered empty: the pointer is set to NULL and its size (size_a) becomes 0.

Stack B follows the same principle but in the opposite direction. Operations move the pointer using b--.
When the pointer moves outside the array boundaries, the stack is also considered empty: the pointer is set to NULL and its size (size_b) becomes 0.

The available operations are:

* `sa`, `sb`, `ss` : swap the first elements
* `pa`, `pb` : push an element from one stack to another
* `ra`, `rb`, `rr` : rotate stacks
* `rra`, `rrb`, `rrr` : reverse rotate stacks

This implementation uses different sorting strategies depending on the size of the input:

* 🔹 Special cases for 2, 3 and 5 values
* 🔹 Selection-based sorting for small datasets
* 🔹 Rank-based strategy for medium datasets
* 🔹 Turkish sort strategy for larger datasets

The goal is to produce a valid and optimized sequence of operations while respecting the project's constraints.

---

## ⚙️ Instructions

### Compilation

```bash
make
```

This will generate the executable:

```bash
./push_swap
```

### Usage

Sort a list of integers:

```bash
./push_swap 2 1 3
```

Example output:

```text
sa
```

## 🏁 Example for three differents algos:


```bash
make simple
```

```bash
make medium
```

```bash
make complexe
```

The program will print the sequence of operations required to sort the numbers.

### Cleaning

Remove object files:

```bash
make clean
```

Remove object files and executable:

```bash
make fclean
```

Rebuild the project:

```bash
make re
```

---

## 🏗️ Project Structure

```text
.
├── checker_bonus/
├── include/
├── srcs/
│   ├── algo/
│   ├── initialisation/
│   ├── move/
│   ├── utils/
│   └── main.c
├── lib/
├── Makefile
└── README.md
```

---

## 🧠 Algorithm Overview

The program dynamically selects a sorting strategy depending on the input size.

## 🧠 Sorting Strategies

To achieve good performance across different input sizes, the project uses multiple sorting strategies. Each algorithm was selected according to its complexity, efficiency, and suitability for a specific range of values.

### Small inputs

For very small datasets, dedicated algorithms are used:

* 2 values
* 3 values
* 5 values

### 🔹 Selection Sort (Simple Cases)

**Why we chose it**

For very small datasets, sophisticated algorithms provide little benefit. Selection Sort is predictable, and generates a small number of operations when sorting only a few values.

**How it works**

The algorithm repeatedly finds the smallest unsorted value and moves it to its correct position until the stack is fully sorted.

---

### 🔹 Range-based sorting (Medium Cases)

**Why we chose it**

As the number of values grows, simple sorting methods become inefficient. Range-based sorting allows values to be processed in groups, reducing the number of decisions and operations required.

**How it works**

Values are divided into ranked ranges. Elements are pushed and processed bucket by Range-based, making it easier to organize the stacks and progressively build a sorted sequence.

---

### 🔹 Turkish Sort (Complex Cases)

**Why we chose it**

For large datasets, minimizing the total number of operations becomes the primary objective. Turkish Sort is widely used in the Push Swap project because it focuses on move optimization rather than traditional sorting complexity.

**How it works**

Each element in Stack B is associated with a target position in Stack A. The algorithm calculates the movement cost required to place every element correctly, selects the cheapest operation, and repeats the process until all values have been reinserted into Stack A in sorted order.

## 💵 Bonus

The checker for the bonus part of the project receives, through a pipe, the instructions printed by the main program.

It dispatches these instructions and applies the corresponding operations to the list initialized with the arguments passed to the checker. When the checker receives an EOF (End Of File), meaning that the main program has stopped outputting instructions, a function verifies whether the list is sorted in ascending order.

### Bonus Implementation

The checker calls the get_next_line function on STDIN_FILENO, allowing it to read each operation printed by the main program.

Each line is compared against the list of valid instructions:

If the line matches a valid instruction, the corresponding operation is applied to the list using the movement functions.
If the line does not match any valid instruction, the program prints Error and terminates immediately.

Upon receiving an EOF (line == NULL), the checker function ft_is_sort traverses the list and verifies that it is sorted in ascending order.

If the list is sorted, the program displays OK; otherwise, it displays KO.

## 📚 Resources

### Push Swap

* 42 Push Swap Subject
* Stack data structure documentation
* Sorting algorithms (Insertion Sort, Selection Sort, Quick Sort)
* Cost-based sorting strategies
* Turkish Sort explanations from the 42 community

## 🤖 AI Usage

Artificial Intelligence tools were used as development assistants during the project.

AI assistance was used for:

* Creates Readme.

All design decisions, implementation, debugging, testing, and final validation were performed manually.

---

## 🎯 Learning Objectives

Through this project, we practiced:

* Algorithm design
* Optimization under constraints
* Stack manipulation
* Cost evaluation strategies
* Memory management in C
* Code organization
---

The exact output may vary depending on the chosen strategy, but the final stack must always be sorted.

Happy sorting! 🚀