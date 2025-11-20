# Flask Hello App

This repository demonstrates how to create a very basic [Flask](https://flask.palletsprojects.com/en/stable/) application and deploy it for free on [render.com](https://render.com/docs). 

Flask is a Python framework used for building web applications. It includes its own development server; this is not optional, and Flask apps cannot be deployed on static-only platforms such as GitHub Pages.

Flask works by placing the main application code in [app.py](https://github.com/EDGENortheastern/if-combined-flask-start/blob/main/app.py) and linking it to HTML files stored in a folder called [templates](https://github.com/EDGENortheastern/if-combined-flask-start/tree/main/templates). These HTML files can in turn link to a `style.css` file, which must be stored in a [static folder](https://github.com/EDGENortheastern/if-combined-flask-start/tree/main/static).

The following instructions explain how to get started with Flask. The very first step in building any Python application is to create a virtual environment. 

## 🔧 Creating a Virtual Environment (venv)

Below are instructions for macOS, Linux, and Windows.

### macOS / Linux

Create the virtual environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

Install Flask:

```bash
pip install flask
```

### Windows (PowerShell)

Create the virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\Activate
```

Install Flask:

```bash
pip install flask
```

## To run the app locally

```bash
python3 app.py
```

or

```bash
python app.py
```
