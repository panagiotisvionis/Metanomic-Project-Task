# Metanomic-Project-Task
Project that receives an ID (type string) as input from a RESTfull API, and does a simple database lookup, using the input. The result is returned as JSON dictionary.

In this project an attempt was made to implement a rest api through flask.
At first I had to import libraries such as flask, jsonify and pymongo.
Then, I connected to the MongoDb database and to the Car collection, in which I had previously imported data with car details such as id, owner brand, etc.
Then, after initializing the application, I set the path (127.0.0.1/5000) and the flask method ( GET ).
Finally, I defined a function with which, after finding a specific id, it returns the data to the application in json dictionary format.

In order to recieve the data I had to input the id of one of the cars of my collection (QFA8685)
There are many choices such as JFN7648, LOI8434, JDT4904 etc.

The process took me less than two hours for the application and the unittest.
It would have finished much faster I believe if I didn't waste a lot of time installing flask_restful module, which for some reason didn't work.
For about an hour I read on the internet about it so that I could be in a position to implement it.
