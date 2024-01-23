from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"fio": "rupasovk"}

@app.get("/users")
def read_item():
    return {"phone_number": "89132399999"}

@app.get("/tools")
def read_item():
    return {"skills": "C#, ASP.NET SQL, T-SQL, EntityFramework"}

# Rupasov 402