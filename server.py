from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
#print(__name__)
#prints __main__

# Flask interprets <…> as something we can pass on as a variable.  These are governed by the Flask feature 'Variable Rules'.
@app.route('/') # decorator for any time we get / requests
def home():
#    return 'Hello, You!'
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
        return 'all good'

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return ' did not save to db '
    else:
        return 'something went wrong'