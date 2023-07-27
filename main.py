from flask import Flask

app = Flask(__name__)

@app.route('/how-are-you')
def haha():
    return 'iam fine!'

@app.route('/')
def main():
    return 'server works!'

from User import User
players = [ User('Вася', 'Пупкин', 1), User('Петя', 'Тряпкин', 2), User('Даша', 'Корейка', 3) ]

def user_list_to_str_list(new_players):
    str_players = []

    for user in new_players:
        str_players.append(str(user))
    return str_players

id_players = []

for user in players:
    id_players.append(user.id)



@app.route('/users')
def playesr():
    return {'id': id_players, 'users': user_list_to_str_list(players)}


if __name__ == '__main__':
    # app.run(port=3000, debug=True)
    app.run(port=80)