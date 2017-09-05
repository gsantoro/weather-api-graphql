import graphene
from flask_graphql import GraphQLView
from flask import Flask


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self, args, context, info):
        return 'Hello world!'


schema = graphene.Schema(query=Query)


app = Flask(__name__)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

app.run(host="0.0.0.0", port=8080)