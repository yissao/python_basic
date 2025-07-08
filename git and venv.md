## source:
https://www.darioz.ch/posts/venv-and-git/venv-and-git/#the-virtual-environment-part

In this post, we’ll look at how to effectively manage dependencies in your Python projects using virtual environments and git. By leveraging these powerful tools, you can keep your projects organized, maintain consistency across different development environments, and avoid common pitfalls such as dependency conflicts.

## TL;DR

```bash
cd your_project # Navigate to your project folder
python -m venv venv # Create virtual environment
source venv/bin/activate # Activate virtual environment
pip install pandas # Install your packages
pip freeze > requirements.txt # Freeze packages to text file
    python -m pip freeze > requirements.txt # funcionou com este comando
deactivate # Deactivate venv
git init # Initialize repo
echo 'venv' > .gitignore # Add venv to .gitignore
git add .
git commit -m 'initial commit'
git push
-------------------------------------------
python -m venv .venv
.venv\Scripts\Activate.ps1

pip freeze > requirements.txt # Freeze packages to text file
    python -m pip freeze > requirements.txt # funcionou com este comando
deactivate # Deactivate venv
git init # Initialize repo
echo '.venv' > .gitignore # Add venv to .gitignore
git add .
git commit -m 'initial commit'
git remote add origin https://github.com/yissao/convertEpub.git
git branch -M main
git push -u origin main
```

## Why should I care about virtual environments?

To understand the benefits of virtual environments, let’s consider the following scenario: you’re working on a new Python project that requires the latest version of a popular library, such as NumPy or Pandas. You install the library on your system, and everything seems to be working fine. However, a few days later, you start another project that requires (for whatever reason) an older version of the same library.

At this point, you have a dilemma: do you install the older version of the library, and potentially break your first project? Or do you stick with the latest version, and potentially run into compatibility issues with your second project? This is where virtual environments come in.

By using virtual environments, you can create separate, isolated environments for each of your projects, each with its own set of dependencies and version requirements. This way, you can avoid conflicts and ensure that your projects are always using the right versions of the libraries they need.

But that’s not all: virtual environments also make it easier to share your projects with other developers, or deploy them to production. Since all of your project dependencies are contained within the virtual environment, you don’t have to worry about whether other developers have the same versions of the libraries installed on their systems. And when it comes time to deploy your project, you can simply package the virtual environment along with your code, and be confident that it will run smoothly on the target system.

In short, using virtual environments can save you time, frustration, and potential headaches.

## So how does git fit into the equation?

In addition to the benefits of using virtual environments, there’s another important piece of the puzzle: git.

As you know, git is a version control system that allows you to track and manage changes to your codebase over time. This is especially useful when working on larger, more complex projects with multiple contributors, as it allows you to collaborate and coordinate your work effectively.

But git can also help you manage your virtual environments and project dependencies in a more efficient and organized way. By storing your virtual environments in a git repository alongside your code, you can easily track and share the specific versions of libraries and other dependencies that your project requires.

This is especially useful when working with other developers, as it ensures that everyone is using the same versions of the dependencies, and makes it easy to update or change those dependencies as needed. It also makes it easier to reproduce your project in a different environment, such as when deploying to production or sharing your work with others.

To sum up, using both virtual environments and git together can provide a powerful and flexible workflow for managing your Python projects and dependencies. By taking advantage of these tools, you can save time, avoid conflicts, and ensure that your projects are always running smoothly.

## Enough talk - How do you do it?

The process of setting up a virtual environment is super easy and should always be the first thing you do for every new project.

### The virtual environment part

1. First, make sure you have Python installed on your system (duh). If not, go ahead and download the latest version from [python.org](https://www.darioz.ch/posts/venv-and-git/venv-and-git/www.python.org).
2. Next, fire up your terminal or command prompt and navigate to your project directory.
3. Once you’re in the right directory, run the following command to create a new virtual environment: `python -m venv my_env`. Replace “my_env” with the name of your choice for the virtual environment (usually, people just call it “env” or “venv” - very creative, I know).
4. After the virtual environment is created, you’ll need to **activate** it in order to use it. To do this, run the following command: `source my_env/bin/activate`. Again, replace “my_env” with the name of your virtual environment.
5. Once your virtual environment is activated, you’ll notice that the prompt in your terminal or command prompt will change to indicate that you’re now working in the virtual environment. You can now `pip install` any libraries or dependencies that your project requires, and they will be installed in the virtual environment, separate from your global Python installation.
6. When you are done, you can just simply type `deactivate` to - you guessed it - deactivate the virtual environment.

### The git part

1. Now that you have your virtual environment set up and your packages installed, you can initialize a git repository in your project directory. To do this, just run `git init`.
2. In order to not track the virtual environment folder, you can run `echo 'my_env' > .gitignore` or simply write “my_env” into your `.gitignore` file.
3. You can now add your project files to the repository and make your first commit:

```bash
git add .
git commit -m "initial commit"
```

### Why exclude the venv?

Wait a second, why did we exclude our poor virtual environment from the git party? I thought one of the main reasons for using a virtual environment was that it makes it easier to share our project? We add the virtual environment folder to `.gitignore` because the packages and dependencies installed in the virtual environment are specific to your project and may not be needed or used by others who clone your repository. Additionally, virtual environments can often be quite large, and including them in your repository can make it unnecessarily large and slow to clone. By excluding the virtual environment from your repository, you can keep your repository lean and make it easier for others to clone and work with.

So what can we do in order for other people to be able to set up their environment in a way that our code for sure works? We will need to provide instructions for others to set up their own virtual environment and install the necessary packages. We can do this by including a `requirements.txt` file in your repository that lists all of the packages that your project requires.

For example, let’s say that your project requires the `numpy` and `flask` packages. You can create a `requirements.txt` file by running `pip freeze > requirements.txt` inside your activated virtual environment. Freezing reads all the installed dependencies and then produces a text file with the name of the dependency and the installed version number. Finally, we can `git add requirements.txt` to check the file into source control, commit everything and finally `git push` to the repository.

Congrats yet again! You have now properly set up your virtual environment with Git.