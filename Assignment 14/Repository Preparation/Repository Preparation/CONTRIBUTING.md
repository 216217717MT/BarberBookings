
## Contributing to BarberBookings

Thank you for considering contributing to the **BarberBookings** project! This document will guide you through the process of setting up your environment, following coding standards, and submitting a pull request (PR).

----------

###  Prerequisites

-   Python 3.10+ or any language of your choice
    
-   FastAPI
    
-   PostgreSQL or SQLite (for local testing)
    
-   Git and GitHub account
    
-   Docker (optional but recommended for isolated testing)
    

###  Project Setup

```bash
# Clone the repo
$ git clone https://github.com/your-username/BarberBookings.git
$ cd BarberBookings

# Create and activate virtual environment
$ python -m venv venv
$ source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
$ pip install -r requirements.txt

# Run tests to confirm setup
$ pytest

```

----------

###  How to Contribute

1.  **Fork the Repository**
    
    -   Click the "Fork" button at the top of the GitHub page.
        
    -   Clone your fork locally.
        
2.  **Pick an Issue**
    
    -   Choose an issue labeled `good-first-issue` or `feature-request`.
        
    -   Comment on the issue to let others know you're working on it.
        
3.  **Create a Branch**
    

```bash
$ git checkout -b feature/your-feature-name

```

4.  **Write Code & Tests**
    
    -   Stick to the coding standards (see below).
        
    -   Write or update unit/integration tests.
        
5.  **Lint Your Code**
    

```bash
$ black .
$ flake8

```

6.  **Commit & Push**
    

```bash
$ git add .
$ git commit -m "Add: brief description of what you did"
$ git push origin feature/your-feature-name

```

7.  **Submit a Pull Request**
    
    -   Go to your fork on GitHub and click "Compare & Pull Request".
        
    -   Add a clear title and description.
        
    -   Wait for code review and CI tests to pass.
        

----------

###  Coding Standards

-   Follow [PEP8](https://www.python.org/dev/peps/pep-0008/) guidelines.
    
-   Use descriptive commit messages.
    
-   Keep functions and classes small and single-purpose.
    
-   Write docstrings for functions and classes.
    

----------

###  Code of Conduct

Please be respectful and inclusive in your communication. We value every contribution.

Happy coding! 



# A. Label 5+ Issues as `good-first-issue`

-   **Fix typo in README**
    
-   **Add docstrings to service layer**
    
-   **Improve error handling in booking API**
    
-   **Add loading spinner to barber schedule page**
    
-   **Write unit test for `BookingService.cancel_booking`**


# EXAMPLE

Name:  Good First Issue
About:  Easy task suitable for new contributors
Title: Good First Issue "task" <summary>
labels:  good-first-issue
---

## Task Description
Explain what needs to be done.

## Files or Code Involved
List relevant files or functions.

## Help Provided
- Reference examples (if any)
- Where to find the function/module
- Tags or tips

## Acceptance Criteria
- [ ] Task is completed.
- [ ] Code is committed with tests (if applicable).
- [ ] PR follows the contribution guide.


---
# B. Label 3+ Issues as `feature-request`

These are suggest improvements or new features to be added

1.  **Add Google login support**
    
2.  **Enable SMS notifications for bookings**
    
3.  **Dark mode toggle for UI**


#  Example 
name: Feature Request
about: Suggest a new feature or improvement
title: Feature   "short description"
labels: feature-request
---

## Summary
Brief explanation of the proposed feature.

## Motivation
Why is this feature important or valuable?

## Proposed Implementation
How should this feature work?

## Alternatives
Any alternative solutions you've considered?

## Additional Notes
Any other information, links, or references.


# `LICENSE` (MIT License)

**MIT License**

Copyright (c) 2025 **Tshepang Molefe**

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, or sell     
copies of the Software, and to permit persons to whom the Software is         
furnished to do so, subject to the following conditions:                       

The above copyright notice and this permission notice shall be included in    
all copies or substantial portions of the Software.                           

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     
THE SOFTWARE.


