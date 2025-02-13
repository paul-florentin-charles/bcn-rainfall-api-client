## Changelog

### v1.0.2
_13/02/2025_

- Fix `config.yml` to fit pydantic model `APIClientSettings`.
- Remove useless `ABC` class inheritance for `BaseConfig`.
- Fix configuration singleton behaviour when path is incorrect.

### v1.0.1
_13/02/2025_

- Fix module name from `client` to `bcn_rainfall_api_client`
- Allow to pass `path` parameter directly in `APIClient.from_config` class method

### v1.0.0 
_13/02/2025_

- Initial release.
- Code is taken from [this repository](https://github.com/paul-florentin-charles/bcn-rainfall-models).