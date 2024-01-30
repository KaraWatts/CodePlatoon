# A guide on copying a repo from one org (account) to another

When you want to upload a repository to your github account, **first** you must create your own repo.

2 ways this can be done:
- Use github's user interface (their website) to create the new repo
or
- Use the `gh` command line tool 
```sh
gh repo create `your-username`/`new-repo-name` --private
```

After you've created the repository, you can now move the code over..

## If you have the code already cloned onto your local machine 

1. change directories into the repo folder
2. add the new origin link (the link to the new repository you want the code to be pushed to)
3. push to that new origin

```sh
cd existing_repo

git remote set-url origin <new repo URL>

git push -u origin --all
```

## If you haven't cloned the repo yet
1. create a `bare` copy of the source repository into a temp folder
2. cd into the temp folder that was create
3. push the copy to the destination repository (the one you created on your account)
4. cd out of the temp directory
5. delete the temp directory and its contents 

```sh
git clone --bare <source url> copyrepo-temp

cd copyrepo-temp
git push --mirror <destination url>

cd ..
rm -rf copyrepo-temp
```
