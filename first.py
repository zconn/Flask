from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "the secret"
app.config['SESSION_TYPE'] = 'filesystem'


def factors(num):
    return [x for x in range(1, num+1) if num % x == 0]


# @app.route('/')
# def hello_world():
#     return 'Hello World! Here it is.'

@app.route('/')
def home_limit():
    x = session.get('x', None)
    if not x:
        session['x'] = 1
    elif x >= 10:
        session.clear()
        return "Session Cleared"
    else:
        session['x'] += 1
    return "This is loaded time " + str(session['x'])


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello ' + name.title() + '!'


@app.route('/factors/<int:n>')
def factors_display(n):  #Jinja template
    return render_template("factors.html", #name of template
                           number=n, #value for number in template
                           factors=factors(n) #value for factors in render_template
                          )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
