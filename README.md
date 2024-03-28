#Python practice:

Marking Scheme & Submission Guideline: Create a text file and add your GitHub repository link (the name of the GitHub repository should be: ‘git_assignment_HeroVired’ and it should be a private repository) into it and upload that file in the submission section in Vlearn.

a. Each question is mandatory to solve.

b. Question number 1 consists of 20 points in total where 18 points are for completing the task and 2 points are for helping at least one of your classmates in their GitHub repository by reviewing code.

c. Question number 2 consists of 10 points.

d. Question number 3 consists of 20 points in total where 18 points are for completing the task and 2 points are for helping at least one of your classmates in their GitHub repository by reviewing code.

e. Assignment related steps should be clearly mentioned in the README.md file of the GitHub repository with steps performed to complete each task. f. Make the GitHub repository private and after the due submission date, make it public for the assignment to be corrected.

g. No commitment after the due date will be considered as part of the submission.

Q.1: You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number.

a. Create a repository name: git_assignment_HeroVired

b. Create a ‘dev’ branch and add this code.

import math

class Calculator:

def add(self, a, b):

return a + b

def subtract(self, a, b):

return a - b

def multiply(self, a, b):

return a * b

def divide(self, a, b):

return a / b

# TODO: Implement the following function to calculate the square root of a number.

# def square_root(self, x):

# return math.sqrt(x)

# You need to uncomment the above function and complete its implementation to add the square root feature.

if __name__ == "__main__":

calculator = Calculator()

num1 = 16

num2 = 4

print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

# TODO: Uncomment and test the square root feature.

# num3 = 25

# print(f"The square root of {num3} = {calculator.square_root(num3)}")

c. Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.

d. Add any of your classmates as collaborators.

e. Implement a feature by creating a new branch called ‘feature/sqrt’. f. Add the ‘sqrt’ code to it.

g. While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create

The bug fixation is in the divide function and the new function should be: def divide(self, a, b):

if b == 0:

raise ValueError("Cannot divide by zero.")

return a / b

h. After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.

i. Request a code review from a team member and make any necessary improvements based on the review feedback.

j. Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.

k. Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.

Q.2: For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly.

In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository.

Q.3: In this same GitHub repository, create a new branch ‘geometry-calculator’, we'll work on a simple Python program that calculates the area of a circle and the area of a rectangle. We'll use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

import math

class GeometryCalculator:

def calculate_circle_area(self, radius):

return math.pi * radius ** 2

def calculate_rectangle_area(self, length, width):

return length * width

if __name__ == "__main__":

calculator = GeometryCalculator()

# TODO: Implement the feature to calculate the area of a circle

# radius = 5

# print(f"The area of the circle with radius {radius} =

{calculator.calculate_circle_area(radius)}")

# TODO: Implement the feature to calculate the area of a rectangle # length = 10

# width = 6

# print(f"The area of the rectangle with length {length} and width {width} = {calculator.calculate_rectangle_area(length, width)}")

Workflow Steps:

a. Create a New Branch:

- Create a new branch named "feature/circle-area" to work on the circle area feature

b. Stash Changes for Circle Area Feature:

- Before committing the changes, stash them using git stash to save the incomplete feature implementation.

- Verify that the working directory is clean

c. Create a New Branch for Rectangle Area Feature:

- Create a new branch named "feature/rectangle-area" to work on the rectangle area

d. Stash Changes for Rectangle Area Feature:

- Before committing the changes, stash them using git stash to save the incomplete feature implementation.

- Verify that the working directory is clean

e. Switch Back to Circle Area Branch:

- Switch back to the "feature/circle-area" branch to continue working on the circle area feature.

- Retrieve the stashed changes

- Complete the circle area feature implementation and save the changes. f. Commit and Push Circle Area Feature:

g. Switch Back to Rectangle Area Branch:

- Switch back to the "feature/rectangle-area" branch to continue working on the rectangle area feature.

- Retrieve the stashed changes

- Complete the rectangle area feature implementation and save the changes. h. Commit and Push Rectangle Area Feature

i. Create Pull Requests:

- Create a pull request to the ‘dev’ branch.

j. Review and Merge

- Have another team member or reviewer review your pull requests. - After receiving approval, merge both pull requests into the main branch.
