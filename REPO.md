SQA Project Report

1. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file is changed and committed. (Campbell)
<<<<<<< HEAD
   We developed a pre-commit hook that runs Bandit on all Python files when committing to check for security vulnerabilities. We tested the script by making changes to Python files and ensuring the Bandit report was generated. For this script to be used, it needs to be placed in .git/hooks, and when it is, outputs the results in bandit_report.csv. 
   
3. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (Yeshenia)
   - report goes here
5. Integrate forensics by modifying 5 Python methods of your choice. (Dorothy)
   - report goes here
=======
2. Create a fuzz.py file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the fuzz.py file. fuzz.py will be automatically executed from GitHub actions. (Yeshenia)
3. Integrate forensics by modifying 5 Python methods of your choice. (Dorothy)
>>>>>>> 79e8c25d83d0c7cc2caafd0fb9810ee6f7f0d5f5
