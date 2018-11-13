# AirBnB Clone
This project aim to make a clone of the AirBnB from scratch, in few steps. Please stay tuned to the repo for update.<hr/>
# Step 1: Write a command interpreter (Console)
This console will be used to do CRUD operations (Create, Read, Update, Delete) on our AirBnB objects (User, City, Review, etc.). These models will be listed in the later section.<br/>
### Usage:<br/>
Run `./console` at the root directory of the repo to start the console<br/>
### Commands:
#### `create <type>`
Create an object of type `<type>`. `id` of the newly created object will be printed after creation.<br/><br/>
#### `update <type of the object> <object id> <attribute name> "<attribute value>"`<br/>
Update the attribute `attribute name` of the object specified by the `object id` with value `attribute value`.<br/><br/>
#### `destroy <type> <object id>`
Delete an object of `type` with id `object id`<br/><br/>
#### `show <type> <object id>`
Display an of type `type` with id `object id`<br/><br/>
#### `all [<type>]`
Display all objects of type `type`. If `type` is not specified, display all objects.<br/><br/>
#### `help [command]`
Show help information of `command`. If `command` is not specified, display all documented commands.
