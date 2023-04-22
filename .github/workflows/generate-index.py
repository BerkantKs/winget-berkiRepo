import os
import json
import yaml

manifests_folder = "manifests"
index_file = "index.json"

def main():
    packages = []
    for filename in os.listdir(manifests_folder):
        if filename.endswith(".yaml"):
            with open(os.path.join(manifests_folder, filename)) as file:
                manifest = yaml.safe_load(file)
                package = {
                    "id": manifest["PackageIdentifier"],
                    "version": manifest["PackageVersion"],
                    "publisher": manifest["PackagePublisher"],
                    "url": manifest["PackageUrl"],
                    "manifest": f"https://raw.githubusercontent.com/{os.environ['GITHUB_REPOSITORY']}/main/{manifests_folder}/{filename}"
                }
                packages.append(package)
    index = {"packages": packages}
    with open(index_file, "w") as file:
        json.dump(index, file, indent=4)

if __name__ == "__main__":
    main()
