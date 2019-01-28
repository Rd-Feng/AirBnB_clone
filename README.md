# AirBnB Clone
This project aim to make a clone of the AirBnB from scratch, in few steps. Please visit https://github.com/Rd-Feng/AirBnB_clone_v2 for continue development.<hr/>

# Step 1: Write a command interpreter (Console)
This console is written in Python3, and will be used to do CRUD operations (Create, Read, Update, Delete) on our AirBnB objects (User, City, Review, etc.). More information on the models will be described in the later section.<br/>

### Models:<br/>
At the moment, we have 7 models: BaseModel, User, State, City, Amenity, Place, and Review, each instance of which is given:
* a unique id generated using `uuid` package
* the attribute `created_at`, a `datetime` object, indicating when the object is created
* the attribute `updated_at`, a `datetime` object, indicating when the object is last updated
* the attribute `__class__`, a `str` object, indicating what is the object's type (model)

Other attributes will be given based on the model:
* User
  + first_name: `str` object
  + last_name: `str` object
  + password: `str` object
  + email: `str`
* State
  + name: `str` object
* City
  + state_id: `str` object
  + name: `str` object
* Amenity
  + name: `str` object
* Place
  + city_id: `str` object
  + user_id: `str` object
  + name: `str` object
  + description: `str` object
  + number_rooms: `int` object
  + number_bathrooms: `int` object
  + max_guest: `int` object
  + price_by_night: `int` object
  + latitude: `float` object
  + longitude: `float` object
  + amenity_ids: `list` object
* Review
  + place_id: `str` object
  + user_id: `str` object
  + text: `str object

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

# AUTHOR
Stephen Chu <stephen.chu530@gmail.com><br/>
Rui Feng <394@holbertonschool.com>
