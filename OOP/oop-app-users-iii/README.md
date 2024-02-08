# App Users III
Your `User` class should have several attributes and methods at this point.  That's great as a general purpose representation of a user.  However, as time has passed, your application's requirements have changed.  You want to start making money off your app's popularity, so you've created a two-tiered system: premium users and free users.

Feel free to either start from scratch or use your (or someone else's) `User` class from the previous User's assignment.

## Requirements
1. Your `User` class will now become a base class.
2. Create two subclasses `PremiumUser` and `FreeUser` that will inherit from `User`.
3. Override the `add_post` method for `FreeUser` so that an instance of `FreeUser` is only able to make two posts.
4. In the `runner.py` file, import `FreeUser` and `PremiumUser` and create at least one instance of each.
5. Add tests.
