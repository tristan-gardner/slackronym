# Precommit hooks
Precommit hooks ensure your project adhears to formatting guidelines

Before contributing make sure to install pre-commit hooks from within the venv shell

```
pip install pre-commit
pre-commit install
```

# slackronym
slack acronym bot for defining bespoke lingo

Support definition creation, listing, and deletion
built as an azure function that can serve custom slack app

Requires a database - currently configured for MsSQL.  And a slack app
