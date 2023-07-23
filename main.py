from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from router.sys import area
from router import user, listsize, org, home
from auth import authentication

app = FastAPI()
app.include_router(listsize.router)
app.include_router(home.router)


list_router = [
    area.router,
]
for router in list_router:
      app.include_router(router,prefix="/mobirun")

app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(org.router)
origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*'],
)

#models.Base.metadata.create_all(bind=engine)