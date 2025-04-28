SQA Project Report

1. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (Campbell)
<<<<<<< HEAD
   We developed a pre-commit hook that runs Bandit on all Python files when committing to check for security vulnerabilities. We tested the script by making changes to Python files and ensuring the Bandit report was generated. For this script to be used, it needs to be placed in .git/hooks, and when it is, outputs the results in bandit_report.csv. 
   
2. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (Yeshenia)
   - Some things I noticed while working on fuzz.py and also the only bug I noticed is that on the evens method if x%2 wasn't enclosed in parenthesis then double-digit even numbers would not be detected. For example if 22 was passed then it would not be recognized as an even number. Same thing with negative numbers.
3. Integrate forensics by modifying 5 Python methods of your choice. (Dorothy)
   - Developing a system to construct taint graphs for kubernetes and Helm configurations based on different types of security weaknesses. The code automatically mines relationships between values, tracks how secretsand configurations propagate across YAML templates and identifies files impacted by tainted data. I also added a forensics module that generates a forensics report for finding what went wrong, how serious the problem is, where it happened, and how to fix it faster. 
=======
>>>>>>> 79e8c25d83d0c7cc2caafd0fb9810ee6f7f0d5f5
