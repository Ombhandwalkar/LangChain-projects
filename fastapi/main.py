from fastapi import FastAPI

# Initialize FastAPI
app=FastAPI()

@app.get('/ok')
async def ok_endpoint():
    return {'message':'ok'}

@app.get('/hello')
async def hello_endpoint(name:str='world'):
    return {'message':f'hello,{name}!'}

