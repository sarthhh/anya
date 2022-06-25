# SELF HOSTING 

* **1. CREATING ENVIRONMENTAL VARIABLES**

    Create a `.env` file in the same directory as the bot's files using the template provided in `.env.example` file.

* **2. INSTALLING REQUIRED PACKAGES AND RESOURCES**
    
    You can use pip or [`poetry`](https://pypi.org/project/poetry/) to install the required pacakges. Both `requirements.txt` and `pyproject.toml` have been provided
    
    STEPS: 
    ```bash
    $python -m pip install -rU requirements.txt
    
    # or 
    $python -m pip install poetry
    $poetry install 
    ``` 
    
    **NOTE**: 
    * Requirements include git sourced packages so you need git to be installed and added to path.
    * Bot uses MySQL database so you need a mysql database server setup and use its credentails for env variables provided as in `.env.example` file.
    
* **3. RUNNING THE BOT**
    
    Move to the bot's directory, and use `python .`/`python __main__.py`
    
    Alternatively you can use you IDE/editor's code runner to run the `__main__.py` file.
