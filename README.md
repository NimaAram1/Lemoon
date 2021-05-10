# Lemoon
lemoon! is a application like snapp food you can order some foods!
you can see demo version from [here](https://lemoonad.herokuapp.com/)
## Setup
for setup first change `.env.sample` to `.env`
and fill the blank gaps with your information
so, this:
```python
DEBUG=
SECRET_KEY=
ADMIN_PANEL_URL=


POSTGRES_NAME_DB=
POSTGRES_USER=
POSTGRES_PORT=
POSTGRES_HOST=
POSTGRES_PASSWORD=
```
must be this:
```python
DEBUG=True
SECRET_KEY=yoursecretkey
ADMIN_PANEL_URL=yourlinkadmin
DATABASE_TYPE=sqlite 

fill this blanks if database_type = postgres

POSTGRES_NAME_DB=
POSTGRES_USER=
POSTGRES_PORT=
POSTGRES_HOST=
POSTGRES_PASSWORD=
```
then, run `$ pip install -r requirements.txt`
now you can ran project with `$ python3 manage.py runserver`
## Todo
- [x] creating basics of project
- [x] resturant model
- [x] add environment variables to django
- [x] create registeration api end-point
- [ ] need login method in registeration
- [ ] complete resturant model 
- [ ] and a lot of things must be do
