# web_server_socket


##Web Server  
Mandatory assignment Part 2
The Mandatory assignment in the course, means that it needs to be both handed-in and approved in order for the student to be able to do the exam, or he/she will miss an exam attempt otherwise. 

##Objective

The main objective of this assignment is to learn the basics of socket programming for TCP connections in Python (creating a socket, binding it to a specific address and port, receive an HTTP packet..), by developing a web server to which web browsers or other kind of clients can send requests to. 
Why a web server? They are one of the most targeted public faces of an organization. You will learn in this education how they can be attacked and how to make them more secure, but before that, it’s important to understand how they work.

##Description of the mandatory task

Develop a web server that handles one HTTP request at a time (no multi-threading allowed). The web server should:
1. Accept and parse the HTTP request.
2. Get the requested file from the server’s file system. If no specific file is requested, the file index.html should be used. 
3. Create a valid HTTP response message consisting of the requested file preceded by the corresponding header lines.
4. Send the response to the client. If the file requested by the client is not present in the server’s file system, then the server should send an HTTP “404 Not Found” message back to the client (remember also in this case, to precede it by the corresponding header lines). If you wish, you can make the server to send in this case an HTML file prepared to be used to inform the user about the file not existing in the system.
5. Keep a log file of all HTTP requests received. Try to do the logging in apache format. An example of that can be found in the end of this document.
6. You are NOT allowed to use the http.server or similar library. Instead you should build it using what you learned about TCP sockets.

##How to run and test the server?

Create two HTML files, one of them being “index.html”, and the other one, for instance, being “test.html”. Place these two files in the same directory that the server is in, and then run the server program. Determine the IP address of the host that is running the server (e.g., 128.238.251.26). Then, from another computer, open a browser and enter the corresponding URL. For example:
http://128.238.251.26:6789/test.html

Note the use of the port number after the colon. This number needs to be replaced with whatever port your server is listening from. 

#What you should see

Following the same example as above, if you enter the URL http://128.238.251.26:6789/test.html, the content of the file “test.html” should be displayed in the browser.

If you enter the URL http://128.238.251.26:6789 , you should then see the content of the file “index.html”.
And finally, if you enter, for instance, the URL http://128.238.251.26:6789/blabla.html where “blabla.html” is the name of a file that doesn’t exist in the server (it could be anything: an HTML file, an image..), then you should get a “404 Not Found”.

Note that if you omit the port part in the URL, that is you type http://128.238.251.26/, then any standard browser will always assume port 80 by default and you will be able to connect to your web server only if the server is indeed listening at port 80.

###Some hints or things to keep in mind

Have a look at the format of HTTP response (see next page) and remember to add the special characters \r\n wherever they required by the HTTP protocol, including after the body of the message.
Remember to handle the corresponding Python exception that is raised when the server tries to open and read a file that doesn’t exist in the file system. 

##Mandatory task requirements
The programming language should be Python. 

