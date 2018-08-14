## Installation

- `pip install -r requirements.txt`
- change DB settings in `moberries_cc/settings.py` or create new file `moberries_cc/local_settings.py`:

```python
POSTGRES_DB_NAME = ''
POSTGRES_DB_USER = ''
POSTGRES_DB_PASSWORD = ''
POSTGRES_DB_HOST = '127.0.0.1'
POSTGRES_DB_PORT = '5432'
```


- `./manage.py migrate`
- load fixture data[*](#Sources) for pizzas

    - `./manage.py loaddata order/fixtures/pizza_fixtures.json --format JSON` 

- `./manage.py runserver`


#### Sources
- [Pizza fixtures source](https://en.wikipedia.org/wiki/List_of_pizza_varieties_by_country#Malta)