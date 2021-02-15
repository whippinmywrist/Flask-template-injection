# Flask-template-injection
The simplest example of a template injection vulnerability.

If user enters the "Ivan" into the form, the server will return "Ivan". What if the user tries to enter the jinja2 code? 


## Exploitation

**The way of exploitation is very simple:**

In our Flask app we have dictionary of data. The logic of the example is built in such a way that the object with the data is completely given to the template engine.   

Attacker can insert his own templating code instead of a name to extract data.

To retrieve secret data, you need to send the following GET request 

```
http://localhost:5000/?person={{data}}
```

## How to use it? There 2 ways

### 1. Virtualenv
The application can be easily executed in a python virtual enviroment. The steps:
```bash
# Get the code
git clone https://github.com/whippinmywrist/Flask-template-injection.git
cd Flask-template-injection
# Virtualenv modules installation (Unix based systems)
pip install virtualenv
virtualenv venv
source venv/bin/activate
# Virtualenv modules installation (Windows based systems)
pip install virtualenv
virtualenv env
.\env\Scripts\activate
# Install Flask
pip install flask
# Run server
python run.py
# Access the example in browser: http://127.0.0.1:5000/
```

### 2. Docker
The application can be easily executed in a docker container. The steps:
```bash
# Get the code
git clone https://github.com/whippinmywrist/Flask-template-injection.git
cd Flask-template-injection
# Build an Docker image
docker build -t template_injection .
# Run server
docker run -d -p  5000:5000 template_injection
# Access the example in browser: http://127.0.0.1:5000/

```
