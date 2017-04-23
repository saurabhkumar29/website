from threading import Thread

def even(x):
	for i in range(0, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False
def odd(x):
	for i in range(1, len(x)-1, 2):
			if x[i] > x[i+1]:
				x[i], x[i+1] = x[i+1], x[i]
				sorted = False

def oddevensort(x):
	sorted = False
	while not sorted:
		sorted = True
		t =Thread(target = even(x))
		t1 =Thread(target = odd(x))
		t.start()
		t1.start()
		t.join()
		t1.join()
	for i in range(0,len(x)-1):
		if x[i]<x[i+1]:
			sorted = False
		else:
			x=oddevensort(x)
	return x


.....oe.py.....
from flask import Flask
from flask import request
from flask import render_template
import concurrentOddEven
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form["elements"]
    a = map(int, text.split(','))
    n = len(a)

    concurrentOddEven.oddevensort(a)

    return render_template("index.html" , a=a)

if __name__ == '__main__':
    app.run()

..........index.html.....
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Enter elements (separated by ,) to be sorted : </h1>
    <form action="." method="POST">
        <input type="text" name="elements">
        <input type="submit" name="elementsForm" value="Enter">
    </form>

    <h2>{{ a }}</h2>
</body>
</html>

