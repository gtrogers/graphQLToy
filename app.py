from flask import Flask, redirect
from flask_graphql import GraphQLView

from blip import data
from blip.schema import schema


app = Flask(__name__)
app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True))


@app.route('/')
def index():
  return redirect('/graphql', 302)


if __name__ == '__main__':
    data.setup()
    app.run()
