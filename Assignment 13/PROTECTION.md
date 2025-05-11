

# Branch Protection Rules

To ensure high code quality and safe collaboration, i have enabled the following rules for the `main` branch:

## 1. Pull Request Review Required
All changes must go through at least one peer review to catch errors early and maintain team accountability.

## 2. Required Status Checks
My CI pipeline must pass all tests before code can be merged. This prevents broken or untested code from entering production.

## 3. No Direct Pushes
Disabling direct pushes ensures that all code goes through the proper pull request and review workflow.

## 4. Require Branch to Be Up-to-Date
This ensures that the latest changes in `main` are incorporated before merging, preventing integration issues.

These rules align with best practices in Continuous Integration and Deployment (CI/CD) to ensure stable, high-quality software delivery.


