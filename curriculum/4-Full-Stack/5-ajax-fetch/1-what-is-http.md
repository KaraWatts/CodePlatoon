# What is HTTP?

## Introduction

There are strict rules about how applications can communicate with each other over the internet, known as a protocol. However, communication on the web is not defined by a single protocol, but by a stack of protocols, known as the OSI model.

### IP - Internet Protocol

> The first protocol you should be aware of is IP, Internet Protocol. IP is concerned with WHERE a server is located on the internet. This location is described with a number called an IP address, which is similar to a physical address. Most of the world currently uses the fourth version of the IP protocol (IPv4), in which an IP address is a series of 4 numbers, separated by periods, like '192.0.2.1'. Whenever you type a domain name into your browser's url bar, your browser has to convert that into an IP address to know where to send the request. This is done using the Domain Name System (DNS).

### TCP - Transmission Control Protocol

> IP is only concerned with WHERE a server is, but not HOW to get there. TCP (transmission control protocol) provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating via an IP network. The reliability makes this protocol a little bit slower, since every single TCP connection actually requires multiple requests to initiate, known as a 3-way handshake. TCP was designed alongside IP, so they're often referred to together as TCP/IP.

### HTTP - Hypertext Transfer Protocol

> TCP is only concerned with HOW data is transferred, but not WHAT data is transferred, or how the data is formatted. The format of our application data is determined by the HTTP protocol.

- [HTTP Slides](https://docs.google.com/presentation/d/15Mq7xn5nQVDjShPOZd4cwVi807oQvNfLE3irJDrlgwU/edit#slide=id.p)

### APIs - Application Programing Interface

> An API is an Application Programming Interface. An API is essentially a contract between two pieces of software that determines how they can interact with each other. For example, every library or framework you'll use has an API that describes what methods you can call from the library/framework, and what you can expect them to do. Today, we'll be using a JSON API that lets our front end request data from someone else's database. There are [many free, public APIs](https://github.com/public-apis/public-apis) that you might want to use.

### AJAX - Asynchronous Javascript and XML

> There are many ways to send an HTTP request, such as clicking a link, submitting a form, or just typing a url into your browser. However, most ways of sending HTTP requests from your browser will unload the page, and replace it entirely with the contents of the HTTP response. To build a more elegant, modern application, we need a way to send an HTTP request in the background without interrupting the user's experience. This technique is known as AJAX: 'asynchronous javascript and xml'. 'asynchronous javascript' just means that we're doing work with javascript in the background, while other processes continue. XML is a data type that can potentially be returned by an AJAX request. In modern applications, XML is not commonly used, but JSON (javascript object notation) is used instead. However, even though we typically get JSON, not XML, from AJAX requests, we still call this technique 'AJAX', because that sounds cool, and 'AJAJ' sounds weird.
> This technique was first made possible in 1999 in Internet explorer, through an object that is now known as `XMLHttpRequest`, or XHR. XHR enabled developers to build many kinds of applications that wouldn't have been possible otherwise, although it was pretty awkward to work with. More recently, modern browsers have started supporting `fetch()`, which provides more convenient access to the same functionality. However, neither of these options is as powerful and convenient as some 3rd party AJAX tools.
