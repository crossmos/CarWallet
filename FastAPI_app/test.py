import os
from dotenv import load_dotenv


load_dotenv()

print(os.getenv('APP_CONFIG__DB__URL'))