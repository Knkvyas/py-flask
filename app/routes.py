from flask import Flask, render_template, request, redirect, url_for, session, flash, request, make_response
from app.db import ClientDB
from app import app
import logging
import os
from werkzeug.utils import secure_filename
from app.utils import allowed_file, unzip_folder, get_dockerfile

log = logging.getLogger('pydrop')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        result = ClientDB().get_client_by_email(email)

        if result:
            if result['password'] != password:
                return render_template('access_denied.html',
                                       error_msg="Password doesn't match. Go back and re-renter the password")

            session['username'] = result['first_name']
            return redirect(url_for('home'))
        return render_template('access_denied.html', error_msg="Username doesn't exist")
    return redirect(url_for('home'))


@app.route('/')
def home():
    return render_template('home.html', title="Home")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET'])
def display_signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        client_info = {'first_name': request.form['firstname'], 'last_name': request.form['lastname'],
                       'company': request.form['company'], 'email': request.form['email'],
                       'password': request.form['password1']}

        password2 = request.form['password2']

        # if ClientDB().check_email_exists(client_info['email']):
        #   return render_template('access_denied.html', error_msg="User already exist")

        if client_info['password'] != password2:
            return render_template('access_denied.html',
                                   error_msg="Password doesn't match. Go back and re-renter the password")
        print(client_info)
        ClientDB().create_client(client_info)

    return redirect(url_for('home'))


@app.route('/upload', methods=['GET'])
def display_upload():
    return render_template('upload.html', message="Sankalp", title="About")


@app.route('/upload', methods=['POST'])
def upload_code_base():
    # return render_template('upload.html', message="Sankalp", title="About")
    log.info(request.form)
    log.info(request.files)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        if file and allowed_file(file.content_type):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded')
            unzip_folder()

            # searches for dockerfile in the extracted folder
            # call this function after the user presses on the submit button or so
            get_dockerfile()
            return redirect('/')
        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
            return redirect(request.url)
    print("Response came")
    return make_response(('ok', 200))
