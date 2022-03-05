# Extractor
Allows you to extract all dependencies from a package.json to reinstall them using a command instead of editing directly package.json. Won't save your day, but it might save your next five minutes :P 

> Notes: it requires python 3.10.2 or higher to work /!\

# install
just git clone this repository.

# usage

```bash
./cli --filepath <targetted_package.json_uri>```

The result will be output in dependencies and devDependencies files.

to install recursively all your dependencies using yarn/npm:

```bash
cat dependencies | xargs yarn add
```



