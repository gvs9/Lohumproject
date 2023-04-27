# Lohumproject


The lohumproject code is a Python Flask API that extracts the current price of a Lithium-ion battery from a website called https://www.metal.com/Lithium-ion-Battery/202303240001

the code uses the requests and BeautifulSoup libraries to extract the webpage's HTML content and find the price value using the class "price-value".

If the price value is found it returns a JSON object containing the price value under the "price" key. If the price value is not found it returns a JSON object containing an error message as "price not found" under the "error" key.

the Flask app runs on the default port of 5000 and has a single route "/price".
when the user makes a GET request to this route "/price" it returns the current price of the Lithium-ion battery. If an invalid URL is provided it returns a 404 error message as "Invalid url".

Run this command in terminal-> pip install flask requests beautifulsoup4 
 after  that run python file
 this will start the Flask server and you can access the API by sending a GET request to the URL "http://localhost:5000/price" in your browser or any HTTP client.
