Welcome to the AirBnB clone project!

General objectives of project
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function


Execution
the shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: 

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$


Console commands:
create : Creates a new instance of the class passed by argument.
show : Prints the string representation of an instance.
destroy : Deletes an instance that was already created.
all : Prints string representation of all instances or of all instances of a specified class.
update : Updates an instance attribute if exists otherwise create it.
help : Show all commands or display information about a specific command.
quit : Exit the console.
EOF : Exit the console.
Commands usage:
create : create <class_name>
show : show <class_name> <object_id> ; <class_name>.show(<object_id>)()
destroy : destroy <class_name> <object_id ; <class_name>.destroy(<object_id>)()
all : all <class_name> ; <class_name>.all()
update : update <class_name> <object_id> "" ; .update(<object_id>, , ) ; .update(<object_id>, )
help : help ; help <command_name>
quit : quit
EOF : EOF ; (ctrl + d)
Concepts:
* Python package
* cmd module
* Unit testing
* serialize and deserialize a Class
* JSON file
* datetime modual
* What is an UUID
* *args and **kwargs;
