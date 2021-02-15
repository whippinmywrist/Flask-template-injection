from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = {'Name': 'Dmitriy', 'Age': '24', 'Token': 'Secret Token'}
    if request.args.get('person'):
        data['person'] = request.args.get('person')
        template = '''<p> Hello, %s 
        ''' % data['person']
    else:
        template = '''
        <p> What yor name? </p>
        <form method="get" action="/">
        <p>
            Enter your name:
            <input type="text" name="person">
        </p>
        <input type="submit" value="Submit">
        </form>'''
    return render_template_string(template, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
