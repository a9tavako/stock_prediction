from dotenv import dotenv_values

def get_dotenv():
    env_variables = dotenv_values(".env")
    return env_variables