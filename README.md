# lukin.be

Personal website of Maarten Huijsmans.

## SCSS

Styles are written in SCSS and compiled to CSS. The compiled CSS is checked into the repo.

### Install Dart Sass

```bash
brew install sass/sass/sass
```

### Compile SCSS

```bash
sass scss/main.scss css/main.css --style=compressed --no-source-map
```

### Watch for changes (during development)

```bash
sass --watch scss/main.scss css/main.css --style=compressed --no-source-map
```
