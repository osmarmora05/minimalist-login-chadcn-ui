<div align="center"> 
    <h1>Minimalist login chadcn-ui</h1>
</div>

<div align="center"> 
   
   ![GitHub top language](https://img.shields.io/github/languages/top/osmarmora05/minimalist-login-chadcn-ui?style=for-the-badge&color=%23eaacd3)
   ![GitHub last commit](https://img.shields.io/github/last-commit/osmarmora05/minimalist-login-chadcn-ui?style=for-the-badge&color=%2331306b)
   ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/osmarmora05/minimalist-login-chadcn-ui?style=for-the-badge&color=%23c9b477)

</div>

<div align="center">
  <br/>
  <a href="./README.es.md">Spanish</a> | <a href="./README.md">English</a>
  <br/>
</div>

# Project Overview

"minimalist-login-chadcn-ui" is a minimalist login, as its name suggests, inspired by the component library shadcn/ui. It features a connection to Turso, implements encryption techniques to protect user data, and uses SQLModel for database management. This project was created for the Web Application Engineering class as practice on the topic of web page vulnerabilities, implementing techniques such as SQL Injection and other things that I can't remember :v

# Preview

| <center><b>Galeria</b></center>                                              |
| ---------------------------------------------------------------------------- |
| <img src="./screenshots/1.png" height="450px" style="aspect-ratio: 64/27;"/> |
| <img src="./screenshots/2.png" height="450px" style="aspect-ratio: 64/27;"/> |
| <img src="./screenshots/3.png" height="450px" style="aspect-ratio: 64/27;"/> |

## Prerequisites

- Python

# Installation Guide

1. **Clone the Repository:**
   Use the following command to clone the project repository and navigate into the project directory:

   ```sh
   git clone https://github.com/osmarmora05/minimalist-login-chadcn-ui.git && cd minimalist-login-chadcn-ui
   ```

2. **Set Up a Virtual Environment:**
   Create a virtual environment to manage the project's dependencies separately:

   ```sh
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   Depending on your operating system, activate the virtual environment using one of these commands:

   - Windows:

   ```sh
   .\venv\Scripts\activate
   ```

   - Unix/Linux:
     ```sh
     source venv/bin/activate
     ```

4. **Install Required Dependencies**

   ```sh
    pip install -r requirements.txt
   ```

5. **Set the Environment Variables**
   You need to create the following file in the root directory of the project: `.env` with the following content:

   ```JavaScript
   TURSO_DATABASE_URL=*****
   TURSO_AUTH_TOKEN"*******"
   CRYPTOGRAPHY_KEY='******'
   ```

   To obtain the values for the environment variables, please contact me.

6. **Run the Project**
   ```sh
    reflex run
   ```
   _The command to run the project might not work or may be different, as Reflex is still under development and subject to changes at the time I am creating this project._

# Technologies

<div style="display: flex; flex-direction: row; width: 100%; gap: 10px">

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png" alt="Python Logo" width="60px"/>
<img src="https://reflex.dev/logos/dark/reflex.svg" alt="Reflex Logo" width="60px"/>
<img src="https://avatars.githubusercontent.com/u/139391156?s=200&v=4" alt="Turso Logo" width="60px"/>
<img src="https://sqlmodel.tiangolo.com/img/logo-margin/logo-margin-vector.svg" alt="SQLModel Logo" width="60px"/>

</div>

# Authors

- Osmar Adrian Mora Cerna [@osmarmora05](https://github.com/osmarmora05)
