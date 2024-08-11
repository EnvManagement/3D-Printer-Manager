from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate, upgrade, downgrade, revision
from flask_session import Session
from model import db
import json
import os
import argparse

# import routes
from routes.filament import filament_bp
from routes.printer import printer_bp
from routes.login import login_bp
from routes.user import user_bp

try:
    config = {
        'DB_HOST': os.getenv("DB_HOST"),
        'DB_PORT': os.getenv("DB_PORT"),
        'DB_DATABASE': os.getenv("DB_DATABASE"),
        'DB_USER': os.getenv("DB_USER"),
        'DB_PASSWORD': os.getenv("DB_PASSWORD"),
        'CLIENT_ID': os.getenv("CLIENT_ID"),
        'CLIENT_SECRET': os.getenv("CLIENT_SECRET"),
        'ADMIN_LIST': json.loads(os.getenv("ADMIN_LIST")),
        'MAIN_URL': os.getenv("MAIN_URL"),
        'VITE_APP_BACKEND_URL': os.getenv("VITE_APP_BACKEND_URL"),
        'AUTO_MIGRATE': os.getenv("AUTO_MIGRATE", "false").lower() in {'true', '1', 't', 'y', 'yes'},
        'AUTHORITY': f"https://login.microsoftonline.com/{os.getenv('CLIENT_TENANT')}",
        'REDIRECT_PATH': "/api/getAToken",
        'ENDPOINT': 'https://graph.microsoft.com/v1.0/users',
        'SCOPE': ["User.ReadBasic.All"],
        'SESSION_TYPE': "filesystem",
    }
except Exception as e:
    raise Exception("Environment variables not set") from e

# Configure flask
app = Flask(__name__)
app.config.from_mapping(config)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}:{config['DB_PORT']}/{config['DB_DATABASE']}"
Session(app)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})
db.init_app(app)
migrate = Migrate(app, db)

# register blueprints
app.register_blueprint(filament_bp)
app.register_blueprint(printer_bp)
app.register_blueprint(login_bp)
app.register_blueprint(user_bp)


# argument functions
def create_migration():
    """Create a new migration script."""
    with app.app_context():
        message = input("Enter name of the migration:\n")
        revision(directory="./migrations", message=message, autogenerate=True)


def upgrade_migration():
    """Apply all database migrations."""
    with app.app_context():
        upgrade(directory="./migrations")


def downgrade_migration():
    """Revert the latest database migration."""
    with app.app_context():
        downgrade(revision="-1")


if __name__ == "__main__":
    FUNCTION_MAP = dict(run=app.run, migrate=create_migration, upgrade=upgrade_migration, downgrade=downgrade_migration)

    parser = argparse.ArgumentParser(description="Manage the Flask application.")
    parser.add_argument('command', choices=FUNCTION_MAP.keys())

    args = parser.parse_args()

    # Migrate if AUTO_MIGRATE == true and command run since we don't want to execute on downgrade for example
    if config['AUTO_MIGRATE'] and args.command == 'run':
        upgrade_migration()

    func = FUNCTION_MAP[args.command]
    func()