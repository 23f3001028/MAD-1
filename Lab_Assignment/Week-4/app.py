from flask import Flask, request, render_template, url_for
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def details():
    if request.method == 'GET':
        return render_template("index.html")
    
    elif request.method == 'POST':
        type = request.form['ID']
        id = request.form['id_value']

        if id == "":
            return render_template('error.html')
        
        id = int(id)
        data = []
        with open('data.csv', 'r') as file:
            file.readline()
            if type == 'student_id':
                for row in file:
                    row = list(map(int, row.strip().split(',')))
                    if row[0] == id:
                        data.append(row)
            elif type == 'course_id':
                for row in file:
                    row = list(map(int, row.strip().split(',')))
                    if row[1] == id:
                        data.append(row)

        if len(data) == 0:
            return render_template("error.html")
        
        elif type == 'student_id':
            tm = 0
            for x in data:
                tm += x[2]
            return render_template('student_details.html', data=data, total_marks=tm)
        
        else:
            marks = [x[2] for x in data if x[1]==id]
            a = sum(marks)/len(marks)
            m = max(marks)
            plt.hist(marks)
            plt.xlabel('Marks')
            plt.ylabel('Frequency')
            plt.savefig('static/plot.png')
            return render_template('course_details.html', avg_marks=a, max_marks=m, img='static/plot.png')

app.debug = True
app.run