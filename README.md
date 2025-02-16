# bcn-rainfall-api-client

[![PyPI version](https://badge.fury.io/py/bcn-rainfall-api-client.svg)](https://badge.fury.io/py/bcn-rainfall-api-client)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

Client who serves routes from the Barcelona Rainfall API; it is recommended to use it to retrieve rainfall data instead of directly calling the API code.

## Usage

```python
from bcn_rainfall_api_client import APIClient
from bcn_rainfall_api_client.utils import APIServerSettings

# With configuration file in default path `config.yml`
api_clt = APIClient.from_config()

# With configuration file in other path
api_clt_with_path = APIClient.from_config(path="new/path/to/config.yml")

# With your own configuration
api_clt_with_cfg = APIClient.from_config(
   cfg=APIServerSettings(host="localhost", port=8080, root_path="/api")
)

# Have fun with client!
data = api_clt.get_rainfall_average(time_mode="yearly", begin_year=1991, end_year=2020)
print(data)
...
```

### About time-related parameters

```python
time_mode in ["yearly", "seasonal", "monthly"]
month in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
season in ["winter", "spring", "summer", "fall"]
```