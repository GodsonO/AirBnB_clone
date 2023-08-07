# **The AirBnB Clone Project**

![AirBnB clone](AirBnB.jpg)

The goal of the project is to deploy on my server a simple copy of the [AirBnB website](https://www.airbnb.com/).
The project will be a complete web application composed by:
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## **The Command Interpreter**

It’s exactly the same as Shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

The console.py that contains the entry point of the command interpreter
- use the module cmd
- The class definition is:  class HBNBCommand(cmd.Cmd):

The command interpreter implements:
- quit and EOF to exit the program
- help
- a custom prompt: (hbnb)
- an empty line + ENTER shouldn’t execute anything
