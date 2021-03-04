from main import create_app

app = create_app("TestConfig")

app.app_context().push()
