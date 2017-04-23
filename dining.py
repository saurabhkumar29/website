import sys,threading,time
from pymongo import MongoClient

client = MongoClient()
db = client.dining                  # the name of the database
collection = db.diningCollection    # name of the collection

doc0 = {
"number" : 0,
"name" : "Descartes",
"thought" : "A donut's hope proves it's existence."
}
doc1 = {
"number" : 1,
"name" : "Marx",
"thought" : "Everybody desires donuts."
}
doc2 = {
"number" : 2,
"name" : "Aristotle",
"thought" : "A donut contains it's donut-ness."
}
doc3 = {
"number" : 3,
"name" : "Hume",
"thought" : "Donuts exist because I imagine donuts."
}
doc4 = {
"number" : 4,
"name" : "Nietzsche",
"thought" : "Stop at nothing to get your donut."
}

doc_id = collection.insert_one(doc0)
doc_id = collection.insert_one(doc1)
doc_id = collection.insert_one(doc2)
doc_id = collection.insert_one(doc3)
doc_id = collection.insert_one(doc4)

#Uses a semaphore as the "butler" to avoid deadlock.

class Semaphore(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1

class ChopStick(object):

    def __init__(self, number):
        self.number = number           # chop stick ID
        self.user = -1                 # keep track of philosopher using it
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):              # used for synchronization
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write("p[%s] took c[%s]\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):              # used for synchronization
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            doc = collection.find_one({"number" : user})
            sys.stdout.write("p[%s] i.e. %s dropped c[%s] and thinks -> %s\n" % (user,doc["name"], self.number, doc["thought"]))
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, number, left, right, butler):
        threading.Thread.__init__(self)
        self.number = number                # philosopher number
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for i in range(20):
            self.butler.down()              # start service by butler
            time.sleep(0.1)                 # think
            self.left.take(self.number)     # pickup left chopstick
            time.sleep(0.1)                 # (yield makes deadlock more likely)
            self.right.take(self.number)    # pickup right chopstick
            time.sleep(0.1)                 # eat
            self.right.drop(self.number)    # drop right chopstick
            self.left.drop(self.number)     # drop left chopstick
            self.butler.up()                # end service by butler
        sys.stdout.write("p[%s] finished thinking and eating\n" % self.number)


if __name__ == "__main__":
    n = 5                                   # number of philosophers / chop sticks
    butler = Semaphore(n-1)                 # butler for deadlock avoidance (n-1 available)
    c = [ChopStick(i) for i in range(n)]    # list of chopsticks
    p = [Philosopher(i, c[i], c[(i+1)%n], butler) for i in range(n)]    # list of philsophers
    for i in range(n):
        p[i].start()
