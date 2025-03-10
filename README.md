# bcn-rainfall-api-client

[![PyPI version](https://badge.fury.io/py/bcn-rainfall-api-client.svg)](https://badge.fury.io/py/bcn-rainfall-api-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

Client who serves routes from the [Barcelona Rainfall API](https://github.com/paul-florentin-charles/bcn-rainfall-api); it is recommended to use it to retrieve rainfall data instead of directly calling the API code.

## Usage

```python
from bcn_rainfall_api_client import APIClient

# You can replace base_url with your own instance URL if you have one running
base_url = "https://bcn-rainfall-api.onrender.com/rest"

# Instantiate client
api_clt = APIClient(base_url=base_url)

# Have fun with client!
data = api_clt.get_rainfall_average(
    time_mode="yearly",
    begin_year=1991,
    end_year=2020
)
print(data)
...
```

### About time-related parameters

```python
time_mode = "monthly"
month = "may"
season = "winter"

assert time_mode in ["yearly", "seasonal", "monthly"]
assert month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
assert season in ["winter", "spring", "summer", "fall"]
```