import yaml

with open("../src/config.yaml", "r") as file:
    file_yaml = yaml.safe_load(file)


name = ""

for i, y in enumerate(file_yaml["resources"]["jobs"]):
    name = y


print(file_yaml["resources"]["jobs"][name]["tags"]["prod_target"])
