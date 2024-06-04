from fastapi import APIRouter


order_router=APIRouter(
    prefix='/oders',
    tags=['auth']
)

@order_router.get('/')
async def hello():
    return {'message':'Hello World'}

