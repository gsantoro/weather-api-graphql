from flask_graphql import GraphQLView
from flask import Flask

from starwars.data import setup
from starwars.schema import schema

# from hello.data import setup
# from hello.schema import schema

def create_app():
    setup()

    app = Flask(__name__)

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
