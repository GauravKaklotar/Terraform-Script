# **Python-Terraform Integration**

This guide explains how to integrate Terraform with Python using the `python-terraform` package. It covers setting up a virtual environment, installing dependencies, using a `.env` file for AWS credentials, and automating infrastructure deployment.

---

## **1. Prerequisites**
Before proceeding, ensure you have the following installed:
- Python (≥3.7)
- Terraform (≥1.2.0)
- AWS CLI (for credential verification)

---

## **2. Set Up a Virtual Environment**
It is recommended to use a virtual environment for dependency management.

### **For macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **For Windows**
```bash
python -m venv venv
.\venv\Scripts\activate
```

---
## **3. Install Dependencies**
```bash
pip install -r requirements.txt
``` 

---

## **4. Create a `.env` File**
Create a `.env` file in the root directory and add your AWS credentials.

```bash
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
```

---

## **5. Run the Script**
Run the Python script to deploy the infrastructure using Terraform.

```bash
python main.py
```


