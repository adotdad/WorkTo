import binascii
import hashlib
import json
import os
import flask
import uuid
from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'eojwfweodcw'


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


@app.route('/form', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'POST':
        if 'submit' in flask.request.form:
            f = open('content.json', 'r')
            content_dict = json.loads(f.read())
            f.close()
            string = uuid.uuid4().hex[:15].upper()
            f = open(string, 'w')
            f.write(flask.request.form['post'])
            f.close()
            content_dict['user id'].append(session.get('user')['id'])
            content_dict['post id'].append(string)
            f = open('content.json', 'w')
            f.write(json.dumps(content_dict))
            f.close()
        elif 'login' in flask.request.form:
            return redirect('/login')
        else:
            return redirect('/register')
    f = open('content.json', 'r')
    content_dict = json.loads(f.read())
    f.close()
    try:
        if session['user'] is not None:
            return render_template('form_user.html', user=session.get('user')['name'],
                                   links=content_dict['post id'], id=3)
        else:
            return render_template('form.html', links=content_dict['post id'], id=3)
    except KeyError:
        return render_template('form.html', links=content_dict['post id'], id=3)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'POST':
        f = open("users.json", "r")
        users_dict = json.loads(f.read())
        f.close()
        index = users_dict['username'].index(flask.request.form['username'])
        if verify_password(users_dict['password'][index], flask.request.form['password']):
            session['user'] = {"name": users_dict['name'][index], "id": index}
            return redirect('/form')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        f = open("users.json", "r")
        users_dict = json.loads(f.read())
        f.close()
        users_dict['name'].append(flask.request.form['name'])
        users_dict['username'].append(flask.request.form['username'])
        key = hash_password(flask.request.form['password'])
        users_dict['password'].append(key)
        f = open("users.json", "w")
        f.write(json.dumps(users_dict))
        f.close()
        session['user'] = {"name": flask.request.form['name'], "id": len(users_dict['name']) - 1}
        return redirect('/form')

    return render_template('register.html')


@app.route('/form/<id>', methods=['GET', 'POST'])
def form_id(id):
    f = open('content.json', 'r')
    content_dict = json.loads(f.read())
    f.close()
    index = content_dict['post id'].index(id)
    if flask.request.method == 'POST':
        if 'delete' in flask.request.form:
            del content_dict['post id'][index]
            del content_dict['user id'][index]
            os.remove(id)
            f = open('content.json', 'w')
            f.write(json.dumps(content_dict))
            f.close()
            return redirect('/form')
        elif 'edit' in flask.request.form:
            f = open(id, 'w')
            f.write(flask.request.form['post'])
            f.close()
            return redirect('/form')
        elif 'logout' in flask.request.form:
            session['user'] = None
            return redirect('/form')
        elif 'login' in flask.request.form:
            return redirect('/login')
        elif 'register' in flask.request.form:
            return redirect('/register')
        else:
            return redirect('/form')
    f = open(id, 'r')
    text = f.read()
    f.close()
    try:
        if session['user'] is not None:
            if content_dict['user id'][index] == session.get('user')['id']:
                return render_template('form_user.html', user=session.get('user')['name'], post=text,
                                       links=content_dict['post id'], id=1)
            else:
                return render_template('form_user.html', user=session.get('user')['name'], post=text,
                                       links=content_dict['post id'], id=2)
        else:
            return render_template('form.html', post=text, links=content_dict['post id'], id=2)
    except KeyError:
        return render_template('form.html', post=text, links=content_dict['post id'], id=2)


def hash_password(password):
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


if __name__ == "__main__":
    app.run(debug=True)
