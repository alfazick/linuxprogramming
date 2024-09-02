# Linux Project Structure Lab: Building a Simple Personal Website

## Introduction

In this lab, you'll create a basic directory structure for a personal website project. This hands-on approach will help you practice Linux navigation and file management skills while building a simple project structure.

## Objectives

- Practice creating directories and files using the command line
- Navigate efficiently between directories
- Use relative and absolute paths
- Organize a simple project structure

## Project Overview

You'll be creating a structure for a personal website with the following sections:
- Home
- About
- Portfolio

## Lab Tasks

### Task 1: Setting Up the Project Root

1. Create a directory called `my_website` in your home folder.
2. Navigate into this new directory.

### Task 2: Creating Main Sections

From the `my_website` directory:

1. Create directories for each main section: `home`, `about`, and `portfolio`.
2. In the `home` directory, create a file called `index.html`.
3. In the `about` directory, create a file called `about.html`.
4. In the `portfolio` directory, create a file called `projects.html`.

### Task 3: Adding CSS and JavaScript

1. Create a `css` directory in the project root.
2. Inside `css`, create a file called `styles.css`.
3. Create a `js` directory in the project root.
4. Inside `js`, create a file called `script.js`.

### Task 4: Setting Up the Portfolio

1. Navigate to the `portfolio` directory.
2. Create two subdirectories: `project1` and `project2`.
3. In each project subdirectory, create an `index.html` file.
4. Use a single command to create a file called `description.txt` in both project directories.

### Task 5: Adding Images

1. Create an `images` directory in the project root.
2. Inside `images`, create three subdirectories: `home`, `about`, and `portfolio`.
3. In the `images/home` directory, create an empty file called `hero.jpg`.
4. In the `images/about` directory, create an empty file called `profile.jpg`.
5. In the `images/portfolio` directory, create two empty files: `project1.jpg` and `project2.jpg`.

### Task 6: Final Touch and Verification

1. Return to the project root directory.
2. Create a `README.md` file in the project root.
3. Use the `find` command to list all `.html` files in your project.
4. Use the `tree` command (if available) to display your entire project structure.

## Final Project Structure

After completing all the tasks, your project structure should look like this:

```
my_website/
│
├── README.md
├── home/
│   └── index.html
├── about/
│   └── about.html
├── portfolio/
│   ├── projects.html
│   ├── project1/
│   │   ├── index.html
│   │   └── description.txt
│   └── project2/
│       ├── index.html
│       └── description.txt
├── css/
│   └── styles.css
├── js/
│   └── script.js
└── images/
    ├── home/
    │   └── hero.jpg
    ├── about/
    │   └── profile.jpg
    └── portfolio/
        ├── project1.jpg
        └── project2.jpg
```

## Conclusion

By completing this lab, you've practiced essential Linux navigation and file management skills while creating a basic structure for a personal website. This structure provides a foundation for a simple yet well-organized web project, demonstrating the importance of logical file organization in web development.

