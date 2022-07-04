from project import config
from project.server import create_app


if __name__ == '__main__':
    app = create_app(config)
    app.run(port=25000)

