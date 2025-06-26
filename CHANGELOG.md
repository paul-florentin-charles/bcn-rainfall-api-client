## Changelog

### v1.0.9
_26/06/2025_

- Add `percentages_of_normal` query param to `get_percentage_of_years_above_and_below_normal_as_plotly_json` method
to map `/graph/percentage_of_years_above_and_below_normal` route.

### v1.0.8
_19/06/2025_

- Add `get_rainfall_standard_deviations_as_plotly_json` method to client to map `graph/standard_deviations` route.

### v1.0.7
_18/06/2025_

- Update `get_rainfall_by_year_as_plotly_json` signature with optional integer `kmeans_cluster_count`.

### v1.0.6
_10/03/2025_

- Remove configuration pattern since it is overkill to keep it for one line.
  - Subsequently, remove class method `from_config`.

### v1.0.5
_16/02/2025_

- Simplify configuration and adapt subsequently `APIServerSettings` schema.

### v1.0.4
_16/02/2025_

- Set some default values for `APIClient` instantiation.
- Make `api.root_path` entry optional in configuration.

### v1.0.3
_14/02/2025_

- Update `README.md`.
- Reset dependencies version to working conditions to ensure compatibility.

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