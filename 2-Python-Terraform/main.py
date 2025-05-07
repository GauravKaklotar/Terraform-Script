import os
from dotenv import load_dotenv
from python_terraform import Terraform

load_dotenv()

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

if not all([aws_access_key, aws_secret_key]):
    raise ValueError("AWS credentials are missing. Check your .env file.")

os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key
os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_key

tf = Terraform(working_dir="./Terraform")

return_code, stdout, stderr = tf.init()
print(f"INIT OUTPUT:\n{stdout}\nERRORS:\n{stderr}")

return_code, stdout, stderr = tf.plan()
print(f"PLAN OUTPUT:\n{stdout}\nERRORS:\n{stderr}")

return_code, stdout, stderr = tf.apply(skip_plan=True)
print(f"APPLY OUTPUT:\n{stdout}\nERRORS:\n{stderr}")