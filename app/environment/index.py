from dotenv import load_dotenv
import os


def load_dotenv_file():
    dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    load_dotenv(dotenv_path=dotenv_path)


def get_env_variable(str):
    value = os.getenv(str)
    if value is None:
        raise Exception(f"{str} environment variable is not set")
    return value


load_dotenv_file()

MONGO_URI = get_env_variable("MONGO_URI")
JWT_TOKEN = get_env_variable("JWT_TOKEN")
