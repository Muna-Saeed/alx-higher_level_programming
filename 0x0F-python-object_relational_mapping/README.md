# 0x0F. Python - Object-relational mapping

# Python SQLAlchemy Project

This project involves creating a simple application that interacts with a MySQL database using SQLAlchemy. The tasks are organized based on the objectives achieved in the project.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Tasks](#tasks)
  - [Task 0: List Databases](#0-list-databases)
  - [Task 1: Filter States](#1-filter-states)
  - [Task 2: Filter States with Injection](#2-filter-states-with-injection)
  - [Task 3: Safe Filter States](#3-safe-filter-states)
  - [Task 4: Cities by States](#4-cities-by-states)
  - [Task 5: Filter Cities](#5-filter-cities)
  - [Task 6: First State Model](#6-first-state-model)
  - [Task 7: All States via SQLAlchemy](#7-all-states-via-sqlalchemy)
  - [Task 8: First State](#8-first-state)
  - [Task 9: Contains 'a'](#9-contains-a)
  - [Task 10: Get a State](#10-get-a-state)
  - [Task 11: Add a New State](#11-add-a-new-state)
  - [Task 12: Update a State](#12-update-a-state)
  - [Task 13: Delete States](#13-delete-states)
  - [Task 14: Cities in State](#14-cities-in-state)
  - [Task 15: City Relationship](#15-city-relationship)
  - [Task 16: List Relationship](#16-list-relationship)
  - [Task 17: From City](#17-from-city)

## Introduction

This project focuses on building a Python application that utilizes SQLAlchemy to interact with a MySQL database. Each task represents a specific feature or functionality implemented in the project.

## Requirements

- Python 3.x
- SQLAlchemy

## Installation

Clone the repository and install the dependencies:

```bash
pip install -r requirements.txt
```

## Tasks

### 0. List Databases
A script that lists all databases in a MySQL server.

### 1. Filter States

A script that displays all values in the states table of a database where the name matches the argument.

### 2. Filter States with Injection

A script vulnerable to SQL injection that deletes all records of a table.

### 3. Safe Filter States

A secure script using parameterized queries to prevent SQL injection.

### 4. Cities by States

A script that lists all cities from a specific database.

### 5. Filter Cities

A script that lists all cities of a given state, SQL injection-free.

### 6. First State Model

Defines a State class using SQLAlchemy, representing a states table.

### 7. All States via SQLAlchemy

Lists all State objects from the database using SQLAlchemy.

### 8. First State

Prints the first State object from the database.

### 9. Contains 'a'

Lists all State objects containing the letter 'a' from the database.

### 10. Get a State

Prints the State object with the specified name from the database.

### 11. Add a New State

Adds the State object "Louisiana" to the database.

### 12. Update a State

Changes the name of a State object in the database.

### 13. Delete States

Deletes all State objects with a name containing the letter 'a' from the database.

### 14. Cities in State

Defines a City class and lists all City objects from the database.

### 15. City Relationship

Extends State class with a relationship to City, ensuring automatic deletion of linked City objects when a State is deleted.

### 16. List Relationship

Lists all State objects and corresponding City objects from the database.

### 17. From City

Lists all City objects from the database, including their associated State.

Feel free to refer to the respective script files for detailed implementations of each task.
```
