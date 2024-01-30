# Lesson: Tokens as HTTP Cookies

In this lesson, we will cover how to set tokens as HTTP cookies with a set lifespan when working within a deployed site with a Django API and a React frontend. We will walk through the provided code and explain why we are doing it and how it works.

## Why are we doing this?

When building web applications with Django as the backend and React as the frontend, it's common to use token-based authentication for securing API endpoints. Tokens provide a secure way to authenticate users without the need to store sensitive information like passwords on the client side.

To make token-based authentication more secure and prevent potential security vulnerabilities like Cross-Site Scripting (XSS), we are setting tokens as HTTP-only cookies. HTTP-only cookies can only be accessed by the server and are not accessible through JavaScript, making them less susceptible to XSS attacks.

Additionally, we are setting a limited lifespan for the tokens by specifying an expiration date for the cookie. This enhances security by automatically invalidating the token after a certain period, reducing the window of opportunity for potential attackers.

## Configuring Django Settings

So far our site has been hosted on an AWS Ec2 instance with an SSL certificate from Certbot for standard encryption. Our site is pretty secure but we will be handling user authentication a bit differently now that we are in a production environment.

```python
# settings.py
ALLOWED_HOSTS = ["0.0.0.0"]

CORS_ALLOWED_ORIGINS = ["0.0.0.0"]

CORS_ALLOW_CREDENTIALS = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True
```

In the `settings.py` file, we are setting the following configurations:

1. `ALLOWED_HOSTS`: It specifies which hostnames are allowed to access the Django site. In this case, we allow requests from the domain "0.0.0.0".

2. `CORS_ALLOWED_ORIGINS`: This allows domain "0.0.0.0" (front-end domain) to make requests to the Django API. CORS (Cross-Origin Resource Sharing) is needed when the front-end and backend are on different domains.

3. `CORS_ALLOW_CREDENTIALS`: This enables sending and receiving cookies across different domains, essential for token-based authentication.

4. `SESSION_COOKIE_SECURE`: This ensures that the cookie is only sent over secure (HTTPS) connections.

5. `SESSION_COOKIE_HTTPONLY`: This sets the session cookie to be HTTP-only, making it inaccessible to JavaScript.

## Setting Tokens as HTTP cookies

In previous lessons we learned how to set `Tokens` to `local storage` during development. It's worked great and it's very simple to manipulate, or set our tokens with JavaScript in the Front-End.

Well that just happens to be the problem. Our Tokens are not secured at all and are easily manipulated with JavaScript when they're placed withing `local storage`. Instead we want our Back-End server to handle the placement, life span, and removal of our users token and keep it in a location where JavaScript itself can't interact with it.

```python
# views.py
from datetime import datetime, timedelta

class Log_in(APIView):
    def post(self, request):
        request.data["username"] = request.data["email"]
        user = authenticate(**request.data)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            life_time = datetime.now() + timedelta(days=7)
            format_life_time = life_time.strftime("%a, %d %b %Y %H:%M:%S GMT")
            response = Response({"user": {"email": user.email}})
            response.set_cookie(key="token", value=token.key, httponly=True, secure=True, samesite="Lax", expires=format_life_time)
            return response
        else:
            return Response("Something went wrong", status=HTTP_400_BAD_REQUEST)
```

You'll notice two major differences in our `Response`:

We are no longer passing the users `Token` as part of our API response but instead we are passing our token as a cookie. `set_cookie` is a response method that will set cookies to a browser when a secured connection is established (that's why our site has to be served with an SSL certificate otherwise Django would not be able to set cookies for our Front-End). There's a couple of parameters this method takes and we should take the time to break them down.

The key of our cookie (think of a cookie as a dictionary with a key, value pair) is set to "token". This key could be named anything we want it's only a variable and has no hidden meaning to it, but we would like the key to explain it's content. The value of this cookie is set to the actual users Token. The httponly flag is set to True, which means the cookie will not be accessible through JavaScript, adding some security against cross-site scripting (XSS) attacks. The secure flag is set to True, which means the cookie will only be sent over HTTPS connections. The samesite attribute is set to "Lax", which provides some protection against cross-site request forgery (CSRF) attacks. The expires attribute is set to the format_life_time, which is set to mark a cookies (NOT THE TOKENS) expiration date and force the user to sign in after a set amount of time.

Finally on our Front-End axios `api` instance we will need to update it to ensure that cookies are sent with the request by setting the `withCredentials: true` option.

```jsx
const api = axios.create({
  baseURL: "https://tango-dep.com/api/",
  withCredentials: true,
});
```

When a user signs in now we can inspect the browsers developer tools cookies section to find the tokens key and value!

## Configuring Token Based Authentication

Currently we are utilizing `DRF's TokenAuthentication` as our authentication class. Let's take a deeper look at how the `TokenAuthentication` class works in authenticating and returning the correct `user` model.

```python
def authenticate(self, request):
    # Looks for the Authorization header within the request and turns it into a list
    # by spliting the string into two elements
    auth = get_authorization_header(request).split()
    # if this there is not an Authorization header or the fist work of the value is
    # not "Token", the authentication class will return None
    if not auth or auth[0].lower() != self.keyword.lower().encode():
        return None
    # If there is an Authorization header and the first word is Token but
    # there is no second token provided we will get an error stating we did
    # not provide the proper credentials
    if len(auth) == 1:
        msg = _('Invalid token header. No credentials provided.')
        raise exceptions.AuthenticationFailed(msg)
    # If there is more than 2 values within the Authorization header we
    # will see an exception telling us the Token header is "broken"
    elif len(auth) > 2:
        msg = _('Invalid token header. Token string should not contain spaces.')
        raise exceptions.AuthenticationFailed(msg)
    # the function will now try to grab the provided Token and decode it. If it
    # fails we will raise an invalid token error
    try:
        token = auth[1].decode()
    except UnicodeError:
        msg = _('Invalid token header. Token string should not contain invalid characters.')
        raise exceptions.AuthenticationFailed(msg)

    return self.authenticate_credentials(token)

def authenticate_credentials(self, key):
    model = self.get_model()
    # once the token is decoded it is passed to this function where
    # the get model method will fetch the correct token from our database
    # and then use that token to grab the user through their related name
    # fields
    try:
        token = model.objects.select_related('user').get(key=key)
    except model.DoesNotExist:
        raise exceptions.AuthenticationFailed(_('Invalid token.'))
    # if the user is not active we will raise an authentication error stating this
    # user no longer rates a valid token
    if not token.user.is_active:
        raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))
    # finally the tokens user and the token itself is returned to the request.
    return (token.user, token)
```

Now that we are aware of how this class authenticates our users, we can use `inheritance` and `polymorphism` to tell `APIViews` to authenticate users by grabbing tokens from HTTP cookies rather than request headers.

```python
#utilities.py

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

class HttpOnlyTokenAuthentication(TokenAuthentication):
    def get_auth_token_from_cookie(self, request):
        # Extract the token from the 'auth_token' HttpOnly cookie
        return request.COOKIES.get('token')

    def authenticate(self, request):
        # Get the token from the HttpOnly cookie
        auth_token = self.get_auth_token_from_cookie(request)

        if not auth_token:
            # If the token is not found, return None and let other authentication classes handle the authentication
            return None

        # The original TokenAuthentication class handles token validation and user retrieval
        return self.authenticate_credentials(auth_token)
```

In the `utilities.py` file, we are creating a custom authentication class `HttpOnlyTokenAuthentication`. This class extends Django Rest Framework's `TokenAuthentication` class and overrides the `authenticate` method to handle token authentication from HTTP-only cookies.

The `get_auth_token_from_cookie` method is used to extract the token from the `token` cookie in the request.

The `authenticate` method uses the extracted token to call the `authenticate_credentials` method of the base class, which handles token validation and user retrieval.

### Applying HTTP Authentication to APIVies

```python
from .utilities import HttpOnlyTokenAuthentication

class Info(APIView):
    authentication_classes = [HttpOnlyTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})

class Log_out(APIView):
    authentication_classes = [HttpOnlyTokenAuthentication]
    permission_classes = [IsAuthenticated]
```

Now you'll when a user signs in and re-renders our site we can see that the `whoAmI` function is working properly with out `Info` view, even though the token is no longer in the requests headers.

## Deleting HTTP Cookies

Our HTTP cookies aren't able to interact with JavaScript so we can't handle the deletion of a cookie through our Front-End. Instead we will have our `Log_out` view send back a response to the browser that will instruct the browser to delete the cookie which will force the user to sign in and request a new token before carrying on.

```python
class Log_out(APIView):
    authentication_classes = [HttpOnlyTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        response = Response(status=HTTP_204_NO_CONTENT)
        response.delete_cookie("token")
        return response
```

## Conclusion

In this lesson, we covered how to set tokens as HTTP cookies with a set lifespan when working with a Django API and a React frontend. We explained the purpose of using HTTP-only cookies and how it enhances security by preventing certain types of attacks. Additionally, we explored the provided code and the logic behind setting the token as a cookie in the API response, and how it can be used for subsequent authenticated requests from the React frontend.
