# Masonite Asset Management

This package aims to provide an easier way to compile front-end assets, using Sass and Babel.

**This module is stil in development**

## Roadmap

- Don't re-compile unchanged assets
- Minify compiled files, for production builds
- Add support for PostCSS
- Add support for Vue

## Installation

Set up a new Masonite app:

```
craft new test-masonite-assets
cd test-masonite-assets
craft install
```

Clone this repo inside it:

```
git clone git@github.com:assertchris/masonite-assets.git assets
```

Install this repo, for local package dev:

```
cd assets
pip install -e .
```

Add the service provider:

```python
# ...
from assets.providers import AssetsProvider

PROVIDERS = [
    # ...
    AssetsProvider,
]
```
> This is from `test-masonite-assets/config/providers.py`

Run the install command (to add new config):

```
craft install:assets
```

Run the server:

```
craft serve
```

If you have Sass and/or Js files to compile, you should see messages about them in the terminal.
