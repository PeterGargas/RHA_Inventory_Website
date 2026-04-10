from website import create_app

app = create_app()
# only if we run this file directly, we will start the server. This allows us to import the app in other files without starting the server.
if __name__ == '__main__':
    app.run(debug=True)
