# Exercise 10: Conditionals 

Objectives:

* To practice with conditional statements and loop constructs
* To import modules and use methods

Question 1:

1. Create a new PyCharm project: Exercise10.
2. Copy the file ex10_starter.py into this project
3. Get the directory name from the environment using os.environ: HOMEPATH on Windows, HOME on Linux (we have done that part for you, notice the test of system.platform).
4. Construct a portable wildcard pattern using os.path.join (we have done that part for you as well)
5. Use the glob.glob() function to obtain the list of filenames
6. Use os.path.getsize() to find each file's size
7. Add a test to only display files that are not zero length
8. Use os.path.basename() to remove the leading directory name(s) from each filename before you print it.

Question 2:

Write a Python program that emulates the high-street bank mechanism for checking a PIN. Keep taking input from the keyboard (see below) until it is identical to a password number which is hard-coded by you in the program.

To output a prompt and read from the keyboard:

`supplied_pin = input("Enter your PIN: ")`

Restrict the number of attempts to 3 (be sure to use a variable for that, we may wish to change it later), and output a suitable message for success and failure. Be sure to include the number of attempts in the message.

Question 3 (Optional):

Passwords, and PINs, would not normally be displayed (echoed) to the screen, for security reasons. So now we will add the functionality to hide the characters typed. That could be a lot of work, but one of the advantages of using a language like Python is that "there's a module for it".
You will need to import a module called getpass, which is part of the standard library.
Instead of input use getpass.getpass, in the same place in the program, with the same parameters.