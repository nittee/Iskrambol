# Technical Design Document (TDD)

## Table of Contents

- [Technical Design Document (TDD)](#technical-design-document-tdd)
  - [Table of Contents](#table-of-contents)
  - [Title and People](#title-and-people)
  - [Introduction](#introduction)
    - [Overview, Context, or Background](#overview-context-or-background)
    - [Design Goals and Constraints](#design-goals-and-constraints)
      - [Functional Requirements, Goals, or Product](#functional-requirements-goals-or-product)
      - [Non-Functional Requirements or Non-Goals](#non-functional-requirements-or-non-goals)
      - [Future Goals](#future-goals)
      - [Assumptions](#assumptions)
  - [Architectural Overview](#architectural-overview)
    - [Data Design](#data-design)
    - [System Components and Modules](#system-components-and-modules)
      - [System Directories](#system-directories)
      - [System Components](#system-components)
      - [Python Modules](#python-modules)
        - [Standard / Built-in Python Modules](#standard--built-in-python-modules)
        - [Third Party Modules](#third-party-modules)
        - [Locally Created Modules](#locally-created-modules)
    - [APIs and Interfaces](#apis-and-interfaces)
    - [Algorithms and Design Patterns](#algorithms-and-design-patterns)
    - [Error Handling and Exception Management](#error-handling-and-exception-management)
    - [Testing and Quality Assurance](#testing-and-quality-assurance)
  - [Deployment and Release Strategy](#deployment-and-release-strategy)
  - [References](#references)

## Title and People

- Title: Technical Specification for Iskrambol Game by Nittee
- Author(s): jiroblea, servin
- Team:
- Reviewer(s):
- Created on: 2024 July 8
- Last Updated: 2024 July 8 | 9:45 AM
- GitHub Issue: #5

## Introduction

### Overview, Context, or Background

*A high level summary and a description of the project, why this is necessary (purpose), and the problems it aims to solve.*

- a wireless local PvP mobile game that gauge players' vocabulary skills
- to teach young and small people the importance of learning vocabulary while they are having fun and fighting with their friends at the same time (what's the importance of vocabulary? to boast your intellectual capacity)

### Design Goals and Constraints

*Specify the design goals and constraints that may impact the system's architecture and implementation. This aligns with the project objectives and sets the context for the design decisions.*

#### Functional Requirements, Goals, or Product

- a wireless local PvP mobile game that tests players' vocabulary skills
- will consists of the following game modes:
  - campaign (single-player, point-based)
  - multiplayer (wireless, local PvP, point-based)
  - daily puzzle (single-player, random word, time-strict)
  - challenge (a player can post a word that other players can reshuffle to obtain new words)

#### Non-Functional Requirements or Non-Goals

- can't think of anything at the moment

#### Future Goals

*Product and technical requirements slated for a future time.*

- online multiplayer

#### Assumptions

*Conditions and resources that need to be present and accessible for the solution to work as described.*

- developers' interest in the project
- developer's free time to work on the project

Back to [Table of Contents](#table-of-contents)

## Architectural Overview

*A high-level architectural overview of the system. It describes the major components and their interactions. This section highlight the system's overall structure, including modules, layers, and subsystems.*

### Data Design

*Outline the data model and database design considerations. Describe the database schema, entity relationships, and any data migration or storage requirements. Also cover data access patterns and caching strategies.*

- data storage type: don't have an idea

### System Components and Modules

*Detail the individual components and modules that make up the system. Explain their responsibilities, interfaces, and dependencies. Use diagrams, such as class diagrams or component diagrams, to visualize the system's structure.*

#### System Directories

- docs directory
  - contain documentation files

- iskrambol directory
  - the main python package for the game
  - contain the main python file and modules for the game

- tests directory
  - modules for testing the codes

- utils directory
  - a python package
  - contain locally created python modules

#### System Components

- system: Ubuntu 22.04
- software applications:
  - git
  - python3
  - python3-pip
  - docker

#### Python Modules

##### Standard / Built-in Python Modules

- logging
- unittest

##### Third Party Modules

- kivy - multiplatform graphical library framework for mobile apps
- buildozer - for creating app packages easily

##### Locally Created Modules

- utils

Back to [Table of Contents](#table-of-contents)

### APIs and Interfaces

*If the system provides APIs or interacts with external services, outline the APIs' specifications, including input parameters, return types, and error handling mechanisms. Specify any communication protocols or standards to be used.*

- are we going to use an API? jiroblea don't think so
- communication between different mobile devices will be wifi and hotspot

### Algorithms and Design Patterns

*Describe any specific algorithms, algorithms, or design patterns that are relevant to the system's implementation. Explain the rationale behind their selection and how they address the system's requirements.*

- TODO

### Error Handling and Exception Management

*Address how the system will handle errors and exceptions, including error codes, error logging, and recovery mechanisms. Detail the strategies for handling unexpected scenarios and ensuring robustness.*

- add try except code blocks
- use some kind of logger (info and error)

### Testing and Quality Assurance

*Outline the testing approach and quality assurance measures to be taken. Describe the test cases, test scenarios, and any automation frameworks or tools to be used for testing. Specify the performance and security testing requirements.*

- use unittest module
- will study the point of using pytest
- will find ways to automate the testing process of the UI of the game

## Deployment and Release Strategy

*Discuss the deployment strategy, including the environment setup, configuration management, and version control. Document the steps involved in deploying the system to various environments and the release process.*

- will use the 'main' branch to deploy the game
- will use the 'development' branch for developing the game
- will release the game when the base features are met

Back to [Table of Contents](#table-of-contents)

## References

- [Demystifying TDD](https://dev.to/siddharth_g/demystifying-the-technical-design-document-a-guide-for-software-engineers-1fk1)
- [Practical Guide to Writing Technical Specs](https://stackoverflow.blog/2020/04/06/a-practical-guide-to-writing-technical-specs/)
- [Write a good software design doc](https://www.freecodecamp.org/news/how-to-write-a-good-software-design-document-66fcf019569c/)

Back to [Table of Contents](#table-of-contents)