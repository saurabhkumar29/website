
from flask import Flask
from flask import request
from flask import render_template
import stringComparison

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text1 = request.form['text1']
    text2 = request.form['text2']
    plagiarismPercent = stringComparison.PlagiarisChecker(text1,text2)
    if plagiarismPercent > 70 :
        return "<h1>Plagiarism Detected !</h1>"
    else :
        return "<h1>No Plagiarism Detected !</h1>"

if __name__ == '__main__':
    app.run()


.....sc.......

import difflib



def PlagiarismChecker(text1 , text2) :
    matches = 0
    smallerLength = 0
    if (len(text1) <= len(text2)) :
        smallerLength = len(text1)
    else :
        smallerLength = len(text2)

    i = 0
    while i < smallerLength :
        if text1[i] == text2[i] :
            matches = matches + 1
        i = i + 1

    similarityPercent = (matches/smallerLength) * 100
    return similarityPercent

def PlagiarisChecker(text1 , text2) :
    a=difflib.SequenceMatcher(None,text1,text2).ratio()*100
    return a

if __name__ == "__main__":
    print("")


.......my-form.html......
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Enter the texts to be compared</h1>
    <form action="." method="POST">
        <input type="text" name="text1">
        <input type="text" name="text2">
        <input type="submit" name="my-form" value="Check !">
    </form>
</body>
</html>

