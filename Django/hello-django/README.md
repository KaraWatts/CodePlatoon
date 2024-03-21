# Hello Django

## Summary
The purpose of this exercise is to get you familiar with setting up python projects, and the basics of writing route handlers. 

## Goals
- create, activate, and understand a virtual environment. The virtual environment should not be committed in git.
- install django in your virtual environment. Save your dependencies in a requirements.txt file, which should be committed in git. 
- Define the following routes in urls.py, that will perform various geometric calculations:
    - `/rectangle/area`
    - `/rectangle/perimeter`
    - `/circle/area`
    - `/circle/perimeter`
- Each of the above routes will need to access variables in the querystring (height, width, radius) in order to calculate the result. Return the answer to the client in any HTML tag. 
- Use appropriate status codes. For example, if the server can't process a request because it has too little information from the client, you might respond with a status code of 400 or 409.
- Next, define the following routes in urls.py:
    - `/rectangle/area/<int:height>/<int:width>`
    - `/rectangle/perimeter/<int:height>/<int:width>`
    - `/circle/area/<int:radius>`
    - `/circle/perimeter/<int:radius>`
- These route should behave the same as the above routes, but they should get their input from these ordered URL parameters instead of the querystring. 
