# Example

import yaml

with open("config.yaml") as config:
    data = yaml.safe_load(config)
    print(data)

data = {
    "aws_access_token": "qweasdzxc",
    "services": [
        {
            "mongo_db": {
                "password": 12345,
                "port": 123456,
                "schema": "users",
            }
        },
        {
            "postgres": {
                "password": 67890,
                "port": 678901,
                "schema": "passwords",
            }
        }
    ]
}

with open("new_config.yaml", "w") as config:
    yaml.dump(data, config)
