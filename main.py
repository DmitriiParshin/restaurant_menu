import uvicorn
from fastapi import FastAPI

from api.hendlers import menu, submenu, dish

app = FastAPI(title='Y_Lab')

app.include_router(
    menu.router,
    prefix='/api/v1/menus',
    tags=['menus']
)
app.include_router(
    submenu.router,
    prefix='/api/v1/menus/{menu_id}/submenus',
    tags=['submenus']
)
app.include_router(
    dish.router,
    prefix='/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes',
    tags=['dishes']
)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
