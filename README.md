# CS50_Final_Assignment
Final Assignment for CS50 2026

# Quick Setup on your Local Device:
### Initializing a Git repository

```git init -b main```

### Set Up Git Repository on your Local Device:

```git remote add origin https://github.com/Ben168-stack/CS50_Final_Assignment```

### To Check If URL Set Correctly:

```git remote -v```

### Pull Repo From Main:

```git pull origin main```

## Merging Dev Branch with Main (Please Check Carefully when merging)
```
git checkout main              # switch to main
git pull origin main          # make sure it's up to date
git merge development         # merge your dev branch into main
git push origin main          # push updated main to remote
```

# Setting Up Virtual Environment
```
python -m venv venv
venv/Scripts/activate

```


## Git Commands To Note

### Adding Commits:

```git add .```

### Staging File to Repo:

```git commit -m "First commit"```

### Pushing Your Changes in Your Current Branch
```git push origin current_branch_name```

### Installing Requirements.txt
```pip install -r requirements.txt```

### Update Requirements.txt
``` pip freeze > requirements.txt ```

### run website
``` python main.py ```



Practice Git Commands Here:
https://learngitbranching.js.org/
