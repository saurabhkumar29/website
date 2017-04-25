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
    concurrentOddEven.oddevensort(a)
    return render_template("index.html" , a=a)

if __name__ == '__main__':
    app.run()



///*** concurrentOddEven.py***//
from threading import Thread
sorted = False
def sort(a,s):
	global sorted
	for i in range(s, len(a)-1, 2):
			if a[i] > a[i+1]:
				a[i], a[i+1] = a[i+1], a[i]
				sorted = False

def oddevensort(a):
	global sorted
	sorted = False
	while not sorted:
		sorted = True
		t =Thread(target = sort(a,0))
		t1 =Thread(target = sort(a,1))
		t.start()
		t1.start()
		t.join()
		t1.join()
	return a
///***templates/index.html****///
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

