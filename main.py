from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def name():
    return {"Меньшаков Борис Юрьевич 2"}

@app.get('/tools')
async def skills():
    return "Начинающий"

@app.get('/users')
async def number():
    return "89130825741"