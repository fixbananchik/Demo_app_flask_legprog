from flask import Flask

app = Flask(__name__)

@app.route('/how-are-you')
def haha():
    return 'iam fine!'

@app.route('/')
def main():
    return 'server works!'

from User import User
players = [ User('Вася', 1), User('Петя', 2), User('Даша', 3) ]


from listToJSON import listToJSON

@app.route('/users')
def players_____():
    return {
        "users": listToJSON(players),
        "count": len(listToJSON(players))
        }
    


if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=8080)