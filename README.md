Project Description
This project is the initial phase of an AirBnB clone, focusing on the backend development integrated with a console application using Python's cmd module. Data, represented as Python objects, are stored in a JSON file and accessed using the json module.

Description of the command interpreter:
The command interpreter functions similar to a Bash shell but with a limited set of commands tailored for the AirBnB website's use. It serves as the frontend for user interaction with the backend developed using Python's object-oriented programming paradigm.

The interpreter allows users to perform various actions, including creating, retrieving, updating, and destroying objects. These actions involve operations such as counting instances and computing statistics.

How to start it
To set up the project on a Linux distribution for development and testing, follow these instructions:

How to use it
The shell operates in two modes: Interactive and Non-interactive.

Interactive Mode: In this mode, the console displays a prompt (hbnb) where users can enter commands, execute them, and receive outputs. After executing a command, the prompt reappears, awaiting the next command.

Non-interactive Mode: In this mode, commands are provided to the shell via input piping. The shell executes the command and produces output without displaying a prompt.

Format of Command Input
To provide commands to the console, pipe them through echo in non-interactive mode. In interactive mode, type commands at the prompt.

Arguments
Commands may accept various options or arguments, separated by spaces.

Available commands and what they do
The interpreter recognizes several commands and their functionalities:

Command	Description
quit or EOF	Exits the program
Usage	By itself
-----	-----
help	Provides instructions on command usage
Usage	By itself --or-- help <command>
-----	-----
create	Creates a new instance of a valid Class and saves it, printing its id.
Usage	create <class name>
-----	-----
show	Prints the string representation of an instance based on the class name and id.
Usage	show <class name> <id>
-----	-----
destroy	Deletes an instance based on the class name and id.
Usage	destroy <class name> <id>
-----	-----
all	Prints string representations of all instances or those of a specific class.
Usage	By itself or all <class name>
-----	-----
update	Updates an instance based on the class name and id, adding or modifying attributes.
Usage	update <class name> <id> <attribute name> "<attribute value>"
-----	-----
count	Retrieves the number of instances of a class.
Usage	<class name>.count()
