# Dash Application CLI Tool
## Description
This Command Line Interface Tool (CLI) is inspired by React "the industry standard" for building web application.
This is a CLI tool that helped generated a somewhat more sophisticated Fullstack file structure and connector for plotly dash application.

## Installation
`pip install git+https://github.com/CVolticz/dash-create.git@master`

## Usage
Because I'm a real cool data scientist, The CLI tool has a help feature that can be call whenever.

```
iff-dash-create --help

Usage: iff-dash-create [OPTIONS] COMMAND [ARGS]...

  Simple CLI wrapper for interfacing

Options:
  --help  Show this message and exit.

Commands:
  build    CLI Builder Tool to generate a file structure for plotly dash...
  run-app  CLI Tool to run plotly application on dev mode Features: -...
```

To generate a project:
```
    dash-create build
    [project-name]: <project name>

    - A File Structure with Frontend/Backend will be Generated
```

To run a project:
```
    dash-create run-app

    - If inside project directory -> spin up a project
```

## File Structure

- FrontEnd: 
```
1) index.py:            Main compiler for the application -> spin up an app in https://localhost:3000/
2) waitress.py:         Server compiler for the application -> change port number upon use
3) components:          Store Pieces of dash module generated for the application
    3a) assets:         contains stylesheet to make application look nice
    3b) app.py:         component compiler (really important 3 line of code that need to be import to every components)
```

- Backend: 
```
Whatever you desire:
1) class, superclass, functions, modules
2) files storage
3) kedro
```

## Roadmap
Add more functionality to the CLI


## Contributing
To contribute, create your own branch, develop, test and make a pull request to develop branch. 


## Authors and acknowledgment
Ken Trinh

## License
MIT License


