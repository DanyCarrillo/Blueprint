from flask_script import Manager, Server

from apps import app

manager = Manager(app)
server = Server(host=app.config['HOST'],port=app.config['PORT'])

if __name__ == '__main__':
    manager.run()