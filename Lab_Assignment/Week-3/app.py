wrong_details = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wrong Inputs</title>
</head>
<body>
    <h1>Wrong Inputs</h1>
    <p>Something went wrong</p>
</body>
</html>

"""

student_details = """ 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Details</title>
</head>
<body>
    <h1>Student Details</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Student id</th>
                <th>Course id</th>
                <th>Marks</th>
            </tr>
        </thead>
        <tbody>
            {% for row in rows %}
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
            </tr>
            {% endfor %}
        </tbody>
        <tfoot>
            <tr>
                <td colspan="2" align="center">Total Marks</td>
                <td>{{ sum }}</td>
            </tr>
        </tfoot>
    </table>
</body>
</html>

"""

course_details = """ 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course <Details></Details></title>
</head>
<body>
    <h1>Course Details</h1>
    <table border="1">
        <thead>
            <tr>
                <th>Average Marks</th>
                <th>Maximum Marks</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{{ avg }}</td>
                <td>{{ max }}</td>
            </tr>
        </tbody>
    </table>
    <img src="{{img}}" alt="histogram">
</body>
</html>

"""

import sys
from jinja2 import Template as t
import matplotlib.pyplot as plt 

name = sys.argv[1]
id = int(sys.argv[2])

data = []

with open('data.csv', 'r') as file:
    file.readline()
    if name == '-s':
        for rows in file:
            row = list(map(int, rows.strip().split(',')))
            if row[0] == id:
                data.append(row)
    elif name == '-c':
        for rows in file:
            row = list(map(int, rows.strip().split(',')))
            if row[1] == id:
                data.append(row)
    else:
        pass



if len(data) == 0:
    with open('output.html', 'w') as output:
        output.write(wrong_details)

elif name == '-s':
    total = sum(x[2] for x in data)
    template = t(student_details)
    with open('output.html', 'w') as output:
        output.write(template.render(rows=data, sum=total))

elif name == '-c':
    marks = [x[2] for x in data if x[1]==id]
    avg = sum(marks)/len(marks)
    maximum = max(marks)
    plt.hist(marks)
    plt.xlabel('Marks')
    plt.ylabel('Frequency')
    plt.savefig('graph.png')
    template = t(course_details)
    with open('output.html', 'w') as output:
        output.write(template.render(avg=avg, max=maximum, img='graph.png'))

else:
    pass