import graphene
from flask_graphql import GraphQLView
from flask import Flask

from starwars.data import setup
from starwars.schema import schema


# class Query(graphene.ObjectType):
#     hello = graphene.String()

#     def resolve_hello(self, args, context, info):
#         return 'Hello world!'


def create_app():
    # schema = graphene.Schema(query=Query)
    setup()

    app = Flask(__name__)

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
