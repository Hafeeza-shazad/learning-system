# Programming App

A **Frappe backend application** designed for managing **primary school records**.  
It provides doctypes for handling **classes, students, parents, teachers, subjects, quizzes, assignments, and content**, with custom APIs to return only necessary data.

---

## Features

- Doctypes for:
  - Class
  - Student
  - Parent
  - Teacher
  - Subjects
  - Class Enrollment
  - Subject Enrollment
  - Content
  - Subject Content
  - Quiz & Questions
  - Assignment
  - Student–Parent relations
- Custom API (`api.py`) with lightweight responses:
  - Only essential fields are returned instead of full Frappe documents.
  - Reduces unnecessary payload to avoid overload.
- Backend-only:
  - Database structure
  - API endpoints for integration
- Work in Progress 🚧 (not feature-complete yet)

---

## Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/Hafeeza-shazad/Primary-school-learning-system.git
bench install-app programming_app



