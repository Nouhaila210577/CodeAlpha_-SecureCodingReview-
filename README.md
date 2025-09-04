# CodeAlpha_-SecureCodingReview-

This project contains two versions of a simple Python user registration program:   
1. A **vulnerable version** with security problems.
2. A **secured version** with improvements applied.
The goal is to learn how to find and fix common security issues in code.

## Objective

The original program was a simple Python login and registration system, but it had multiple security issues:

- SQL injection vulnerability 
- Passwords not hashed 
- No input validation
- No check if username already exists
  ...

### Improvements Made
- Switched to **parameterized queries** to prevent SQL injection  
- Added **SHA-256 hashing** for passwords
- Checked for existing usernames  
- Showed only usernames
