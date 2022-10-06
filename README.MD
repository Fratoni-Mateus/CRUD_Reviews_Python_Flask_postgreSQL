#Product review API
The goal of this API is to receive and display reviews for a product.


##How to use this API

The following routes and methods are available:

###Connection test
<code>/, method=GET </code>
Use this route to test iw the API is connected and running. It will return a JSON with the following information: 
<code>{'message': 'Welcome to my API'}</code>
If this route is not available, then the API is not connected or running.

###Getting all the reviews
<code>/reviews, method=GET </code>
Returns all the reviews in JSON format.

###Getting an specific review
<code>/reviews/<id>, method=GET </code>
Returns the review with the given ID in JSON format. If the ID does not exists, an error 404 will be returned.

###Creating a new review
<code>/reviews, method=POST </code>
Used to create a new review, you need to provide the following parameters as JSON:

Mandatory parameters are marked with an *.
*"name" for the name of the person giving the review as a string;
*"rating" for the rating given by the person to the product as an integer from 1 to 5,
"pros" for the positive attributes of the product as a string. The value is optional and will be given "" if left blank;
"cons" for the negative attributes of the product as a string. The value is optional and will be given "" if left blank;
"comment" for general comments about the product as a string. The value is optional and will be given "" if left blank;

###Editing a review
<code>/reviews/<id>, method=PUT </code>
Used to edit parameters of the review with the given ID. The information should be provided following the same principles as the ones defined in the POST method. If the ID does not exists, an error 404 will be returned.

###Deleting a review
<code>/reviews/<id>, method=DELETE </code>
Deletes the review with the given ID in JSON format. If the ID does not exists, an error 404 will be returned.