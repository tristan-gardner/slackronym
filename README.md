# azure-django-boilerplate
Example repo for how to set up an azure function app with django

Can be pulled down as starter code to build a function app which uses django for business logic and DB ORM

Follows the tutorial [here](https://szwarc.ai/azure/serverless-django-with-azure-function-apps/)


# Precommit hooks
Precommit hooks ensure your project adhears to formatting guidelines

Before contributing make sure to install pre-commit hooks from within the venv shell

```
pip install pre-commit
pre-commit install
```

# Modifying the stater code
- If you want to change the name of your function,
1. alter the name of the manage folder to the desired name
2. in manage/function.json, alter the route paramter, replace "manage" with new function name
3. in django_project.settings, alter the constant FUNCTION_APP_PATH, replace "manage" with the new name

- Make sure to replace the secret key value in the settings.py file
- Also connect up the db you plan to use in the settings.py file
- Feel free to rename the folder django_project to a more descriptive name
- By default on get and post methods are allowed, you can greenlight other methods by adding them in the function.json config
