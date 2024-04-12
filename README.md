# pw

The world's first unhackable password manager.
Fully featured with revolutionary functions such as:
 
 - Checking passwords
 - A menu
 - 

## Warning
This project is fun thing I made on the side that is not intended
for actual use. There are several free password managers with more
features and actual security that you should always use over this.
I take 0 responsibility if your entire network gets hacked due to
vulnerabilities in the project.

## Installation
Eventually I will probably get an actual build for this but for now 
it is just a couple python scripts. Download them, and make sure
to install:

 - Python (obviously)
 - cryptography (for encryption/decryption)
 - pyperclip (for copying passwords)
 - secrets (for more secure random number generation)

Run the program with
```sh
path/to/python pw
```

## Usage
### Normal Operation
By default, the program will create the password file as well as the 
backups in the same directory as itself. ~~This can be changed in the 
config file to any desired location~~ NOT YET IMPLEMENTED

If the program cannot locate a password file, it will assume you are a
new user, and will prompt you to create a password. **THIS IS YOUR
MASTER PASSWORD. Do not forget it or you will permanently lose
access to your passwords.**

Once completed and from that point onwards, the program will display
a menu with several options. Inputting 'quit' at any point will take you back
to the main menu. If you made a mistake, "ohno" will undo all actions from
that session.

When checking accounts, the password will not be displayed. This makes
it *slightly* more safe to use around other people. Instead, it will be directly
copied to the clipboard.

### Restoring Backups
The program creates several backups to (hopefully) prevent total data loss
when it inevitably crashes horribly. To restore from a backup, navigate to the
backups folder (script directory/backups by default) and copy the backup
you wish to restore to. Delete your current passwords file, and paste the
backup into its place. Rename it to whatever your password file name is set
to  (default pwds.txt) and rerun the program.

### Faster Useage
> This feature has been tested minimally and greatly increases the 
chances for malfunction. It is not recommended for use for any
operations that will make changes.

The program can take several inputs at a time, and will process them
in order. So, when running the program,
```sh
path/to/python pw check google
```
will automatically check for google accounts. If you know beforehand the
exact string of inputs, this may save time.

The master password will not be taken in this way by default, but adding
the -l flag to the front and your password immediately after will work.
Otherwise, it will ask for your password before executing the inputs.
```sh
path/to/python pw -l password check google
```
To generate passwords without logging in, just use gen when running.
```sh
path/to/python pw gen
```
This will not ask for a password, however, other features of the program
cannot be accessed.

There are several places where a yes/no input is prompted. If you are
inputting a stream, you can skip those, and they will (mostly) default to
"yes".

## Future Features
Needs error checking and handling haha.
### QOL
 - [ ] GUI
 - [ ] Actual builds
 - [ ] Mobile ver
 - [ ] Restore function built in
 - [ ] Notes for sites
 - [ ] Help text
 - [ ] Browser extension
 - [ ] Username searching
 - [ ] Fuzzy searching (for sites and usernames)

### Functions
 - [ ] Config file actually works
 - [ ] Change your master password
 - [ ] Show all accounts over all sites
 - [ ] Dump all passwords to a file (for migration, etc)
 - [ ] Input stream can handle spaces in a single input
