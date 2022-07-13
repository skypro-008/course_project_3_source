from project.config import Config
from project.server import create_app

app = create_app(Config)

if __name__ == '__main__':
    app.run(port=25000)

