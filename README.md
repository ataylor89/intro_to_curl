# intro to curl

## Introduction

As far as I know, there are two types of programs: command-line programs and graphical programs.

Apple's built-in web browser, Safari, is an example of a graphical program.

curl, which comes preinstalled with macOS, is an example of a command-line program.

We run command-line programs in a terminal environment, like the macOS Terminal application.

We run graphical programs by clicking, or double-clicking, on an icon.

curl is a really useful command-line program.

I often use it at work, to test our APIs, or to give another developer a way to test my API.

According to the manual page for curl, curl is "a tool for transferring data from or to a server using URLs".

That's one way of putting it.

But I like to say that curl allows us to download a webpage.

We can use curl to download a web page and write the result to file or stdout.

We can also use curl to call a web service, in a web API, and write the result to file or stdout.

## Example curl commands

First we start up the server on port 8080.

    % python server.py
    Starting HTTP server on port 8080...

Now we open a new tab in Terminal. We'll run curl commands in the new tab.

    # Lookup a product by its ID
    % curl 'http://localhost:8080/products?id=1'    
    {"resultCount": 1, "results": [{"id": 1, "name": "MacBook Neo", "price": 600}]}

    # Lookup a product by its name
    % curl 'http://localhost:8080/products?name=macbook+pro'
    {"resultCount": 1, "results": [{"id": 3, "name": "MacBook Pro", "price": 800}]}

    # Search on a search term
    % curl 'http://localhost:8080/products?term=mac'    
    {"resultCount": 4, "results": [{"id": 1, "name": "MacBook Neo", "price": 600}, {"id": 2, "name": "MacBook Air", "price": 700}, {"id": 3, "name": "MacBook Pro", "price": 800}, {"id": 5, "name": "iMac", "price": 800}]}

    # Get all products that are $600 or less
    % curl 'http://localhost:8080/products?price=600'
    {"resultCount": 4, "results": [{"id": 1, "name": "MacBook Neo", "price": 600}, {"id": 4, "name": "iPhone", "price": 600}, {"id": 6, "name": "Apple Watch", "price": 250}, {"id": 7, "name": "Apple TV", "price": 300}]}

    # Search on a search term, run in silent mode, and pipe the output to Python's json module
    % curl -s 'http://localhost:8080/products?term=macbook' | python -m json
    {
        "resultCount": 3,
        "results": [
            {
                "id": 1,
                "name": "MacBook Neo",
                "price": 600
            },
            {
                "id": 2,
                "name": "MacBook Air",
                "price": 700
            },
            {
                "id": 3,
                "name": "MacBook Pro",
                "price": 800
            }
        ]
    }

You can see how, in our first tab in Terminal, the server logs the GET requests.

You can see how, in our second tab in Terminal, we use curl to call the web services of our API.

In case you're wondering, I use the key sequence command+T to open a new tab in Terminal.

I also use the key sequences command+shift+leftarrow and command+shift+rightarrow to toggle between tabs in Terminal.

Now, we were able to spin up a simple HTTP server and create a web API.

We called the web services in our web API using the curl command.

But we can also do so by opening a web browser and pointing it to a URL like http://localhost:8080/products?term=macbook.

I thought it would be neat to give an introduction to curl, by writing a simple web server in Python.

We used built-in modules like http, urllib, and json to build the web server.

Now, if you want to see a log of the communication stream, between the HTTP client (curl) and the HTTP server (server.py), you can use the --trace and --trace-ascii options in curl.

    # Use the trace option to produce a hex dump of all incoming and outgoing data
    % curl 'http://localhost:8080/products?term=macbook' --trace hexdump.txt        
    {"resultCount": 3, "results": [{"id": 1, "name": "MacBook Neo", "price": 600}, {"id": 2, "name": "MacBook Air", "price": 700}, {"id": 3, "name": "MacBook Pro", "price": 800}]}

    # Inspect the hexdump.txt file
    % cat hexdump.txt

    # Use the trace-ascii option to produce an ASCII dump of all incoming and outgoing data
    % curl 'http://localhost:8080/products?term=macbook' --trace-ascii asciidump.txt
    {"resultCount": 3, "results": [{"id": 1, "name": "MacBook Neo", "price": 600}, {"id": 2, "name": "MacBook Air", "price": 700}, {"id": 3, "name": "MacBook Pro", "price": 800}]}

    # Inspect the asciidump.txt file
    % cat asciidump.txt

You can see that curl is full of surprises :)

I really like the trace and trace-ascii options.

For one thing, if you search hard enough, you can find the raw HTTP request in the trace dump.

Now, I think this is a good stopping point.

I might add more to this readme file later.
