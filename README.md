[![python](https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)


<img src="./docs/assets/banner.png" width=900 align="middle">


An awesome Discord bot with Server automation, Utility features and more!
[ Still at development stage ]

* Written in python using [`hikari`](https://github.com/hikari-py/hikari) and [`hikari-lightbulb`](https://github.com/tandemdude/hikari-lightbulb).
* Can be self-hosted and used ( [see guide](https://github.com/sarthhh/anya/blob/main/README.md#self-hosting) ).
* Contact me: [sarth#0460](https://discord.com/users/580034015759826944)


<a href="https://discord.com/api/oauth2/authorize?client_id=979906554188939264&permissions=378025593921&scope=bot%20applications.commands">
<img src="./docs/assets/invite_me_pls.png" width=165 height=36 align="middle" target="_blank">
</a>

## SELF HOSTING

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




