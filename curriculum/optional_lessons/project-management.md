
# Project Management (GitHub)

In this lesson we will learn how to follow the development process by creating development branches, creating Pull Request, Implementing reviewers comments, and merging branches.

## Creating Repository

While working on a project, we don't want code that hasn't been reviewed by at least two coworkers to end up on our main branch. Instead we want our main branch on our repository to be protected and have developers do their work on separate branches that will require approval to merge with the main branch.

Lets go over the steps to create our repository with a protected main branch.

Create a repository on github with an `Readme.md`.

<img width="1512" alt="Screenshot 2023-04-01 at 8 58 53 PM" src="https://user-images.githubusercontent.com/105952966/229330561-3a6bfc32-cba9-45e0-a404-d8197e7f90a3.png">

Now that our `main` branch has been created, lets add some protection onto it. Click on the settings tab, than branches and you'll see a button to `add branch protection rule` click on it.

<img width="1512" alt="Screenshot 2023-04-01 at 9 01 35 PM" src="https://user-images.githubusercontent.com/105952966/229330855-6eef6c79-5c8c-435e-857b-0736d733a210.png">

Under branch name patterns we will write `main` and under `Protect matching branches` we will check the checkbox for `Require a pull request before merging`. Lastly at the very bottom of the file we will click on the button labeled `create` and create our protection rule for our main branch.

<img width="1512" alt="Screenshot 2023-04-01 at 9 03 41 PM" src="https://user-images.githubusercontent.com/105952966/229330876-64f863ca-3c85-4dc7-bf36-fa12d4c83392.png">

Now development branches will need to be reviewed and approved by at least one coworker before being elligible to merge with the main branch.

## Creating Development Branches

Now that our `main` branch is protected, we want to conduct any and all development pertaining to a task on a developtment branch. For example lets say we were part of the Front-End development team and received the following ticket with this title `PROJECT-001: Create React + Vite Project`.

- First lets clone our repository and open our project.

```bash
    git clone <repository_name>
    cd <repository_name>
    code .
```

- Now that we are inside our projects root we can create and checkout a development branch for the specified ticket.

```bash
    git branch PROJECT-001
    git checkout PROJECT-001
    #YOU'LL SEE THE FOLLOWING AS A CONFIRMATION
    Switched to branch 'PROJECT-001'
```

- Inside this branch we could create our React + Vite project, add the new directory to git and create a descriptive commit message, ex:
  - First portion of the commit message should be the ticket you are currently working on. 
  - The first letter after the ticket should be capitalize
  - The tense of the commit message should be present and in an imperative style.
  - `PROJECT-001: Create React App`

```bash
    npm create vite <finish creating the project>
    git add .
    git commit -m 'PROJECT-001: Create React App'
```

- Now we can push our code up to our `PROJECT-001` branch and create a Pull Request to merge with our `main` branch.

```bash
    git push origin PROJECT-001
```

## Pull Request

Now that we have a development branch with code pushed up to GitHub, we can  create a pull request to get our development branch merged with main.

- When we go back to our repository on GitHub we will be able to click on the branch icon and select the `PROJECT-001` branch.

<img width="1512" alt="Screenshot 2023-04-01 at 9 38 17 PM" src="https://user-images.githubusercontent.com/105952966/229331673-6cd63ff6-81f8-4db8-a2d0-badc804e99f7.png">

- Now we could go to our branch and create a Pull Request. With a descriptive message of our branches acceptance criteria.

<img width="1512" alt="Screenshot 2023-04-01 at 10 46 58 PM" src="https://user-images.githubusercontent.com/105952966/229334092-66a82558-f3f8-497d-92bd-2bca83b2d428.png">

- Once our pull request is created we will see that merging to main is blocked and will remain blocked until an approval is provided by a reviewer.

<img width="1512" alt="Screenshot 2023-04-01 at 10 49 11 PM" src="https://user-images.githubusercontent.com/105952966/229334218-796b4027-3691-42ac-ab68-30681e65af44.png">

## Adding Collaborators

Now we need some collaborators on our project to review our work and provide us with solid applicable feedback to either improve code quality or our overall project implementation.

- On your GitHub repository go over to `settings` and then click on `collaborators`. Here you'll see an `add collaborators` button to add people onto your project repository.

<img width="1512" alt="Screenshot 2023-04-01 at 10 53 46 PM" src="https://user-images.githubusercontent.com/105952966/229334404-24d9f89a-e5a1-4917-a663-0c5c20f77725.png">

- Now your collaborators can accept your request for collaboration and provide reviews for your pull request.

- Once you have an approval from a reviewer, you can merge your development branch with main and move on to the next ticket.
