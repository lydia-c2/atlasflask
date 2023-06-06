## [Flask Portfolio Starter](https://github.com/nighthawkcoders/flask_portfolio)
Runtime link: https://flask.nighthawkcodingsociety.com/
## Quick way to get started
> Quick steps with MacOS or WSL; this uses Nix for programmatic way to build tools and dependencies.


### When on vscode you are editing the backend databases, to view these apis on the web, you need to run the repository locally:

- run python3 main.py in general terminal
- then if it gives you no errors, you should be able to add /api/(databasename) to the end of the link to print the api

### If there is an issue or you want to ensure your project is working, use postman

- Download postman using this link: https://www.postman.com/downloads/ and sign in
- create new public workspace and title it your repository name.
    - For example: flask_portfolio
- Create a new tab and follow the directions that correspond to your desired outcome

- Read:
    - Get ---> Body --> JSON ---> raw
    - paste local server in the given space with /api/(databasename)/read
    - Press send
    - It should print all tester data if it worked

- Create: 
    - Post ---> Body --> JSON ---> raw
    - past local server in the given space with /api/(databasename)/create
    - In the text box create a new addition following this format 
        - {"attribute1":"insert", "attribute2":"insert”, "attribute3":"insert", “attribute4:”insert”}
    - Press send
    - New additon will be shown in api

### Files needed in order to make database

- The first file needed is the api file
- In the api folder create a file called (databasename)/py

- Next create a model file
- In the model folder create a file called (databasenames)/py

### Initialization

- Move to the main.py file in the repository and add the following initialization steps:
    - from model.(databasename) import init(Databasename)
    - from api.(databasename) import (databasename)_api
    - app.register_blueprint((databasename)_api)
    - init(Databasename)()
- These steps are necessary for a working project and initialization

In order to connect all this backend data to a frontend, we need a subdomain.






cd
- Open a Terminal, install nix which requires admin password: 
```bash
sh <(curl -L https://nixos.org/nix/install)
```

- ***Restart Terminal***

- Install Python Package helper

```bash
nix-env -if https://github.com/DavHau/mach-nix/tarball/3.5.0 -A mach-nix
```


- Open a Terminal, cd to project area

```bash
mkdir ~/vscode; cd ~/vscode

git clone https://github.com/nighthawkcoders/flask_portfolio.git

cd flask_portfolio
```

- Build nix packages from requirements.txt

```bash
mach-nix env ./env -r requirements.txt
```

- End of nix shell setup, exit shell
```
exit
```

### Run Server or run VSCode

- Run nix shell (virtual environment)

```bash
nix-shell ./env
```

- Run from Terminal without VSCode

    - Run python from command line and check server
    ```bash
    python main.py
    ```

- Prepare VSCode and run
    
    - From Terminal run VSCode
    ```bash
    code .
    ```

    - In VSCode open Terminal, verify Nix python
    ```bash
    which python
    ```
    - Open Setting: Ctl-Shift P or Cmd-Shift
        - Search Python: Select Interpreter
        - Match interpreter to `which output` above

    - Try Play button and try to Debug
    

### Idea
> The purpose of project is to serve API.  It is the  backend piece of a Full-Stack project.  Review API folder for endpoints.

### Visual thoughts
> The Starter code should be fun and practical.
- Organize with Bootstrap menu 
- Add some color and fun through VANTA Visuals (birds, halo, solar, net)
- Show some practical and fun links (hrefs) like Twitter, Git, Youtube
- Show project specific links (hrefs) per page

### Implementation Summary
#### January 2023.
> This project started backend server.  Intentions are to add some Administrative UIs.
#### September 2021.
> Basic UI elements were implemented showing server side Flask with Jinja 2 capabilities.
- Project entry point is main.py, this enables Flask Web App and provides capability to renders templates (HTML files)
- The main.py is the  Web Server Gateway Interface, essentially it contains a HTTP route and HTML file relationship.  The Python code constructs WSGI relationships for index, kangaroos, walruses, and hawkers.
- The project structure contains many directories and files.  The template directory (containing html files) and static directory (containing js files) are common standards for HTML coding.  Static files can be pictures and videos, in this project they are mostly javascript backgrounds.
- WSGI templates: index.html, kangaroos.html, ... are aligned with routes in main.py.
- Other templates support WSGI templates.  The base.html template contains common Head, Style, Body, Script definitions.  WSGI templates often "include" or "extend" these templates.  This is a way to reuse code.
- The VANTA javascript statics (backgrounds) are shown and defaulted in base.html (birds), but are block replaced as needed in other templates (solar, net, ...)
- The Bootstrap Navbar code is in navbar.html. The base.html code includes navbar.html.  The WSGI html files extend base.html files.  This is a process of management and correlation to optimize code management.  For instance, if the menu changes discovery of navbar.html is easy, one change reflects on all WSGI html files. 
- Jinja2 variables usage is to isolate data and allow redefinitions of attributes in templates.  Observe "{% set variable = %}" syntax for definition and "{{ variable }}" for reference.
- The base.html uses combination of Bootstrap grid styling and custom CSS styling.  Grid styling in observe with the "<Col-3>" markers.  A Bootstrap Grid has a width of 12, thus four "Col-3" markers could fit on a Grid row.
- A key purpose of this project is to embed links to other content.  The "href=" definition embeds hyperlinks into the rendered HTML.  The base.html file shows usage of "href={{github}}", the "{{github}}" is a Jinja2 variable.  Jinja2 variables are pre-processed by Python, a variable swap with value, before being sent to the browser.
