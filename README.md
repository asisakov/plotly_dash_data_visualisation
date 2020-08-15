**Status:** On progress

## Usage

This repository is meant to be a playground for dashboards visualisation using 'plotly' and 'dash'.

### Run

To start with web-app, run `index.py`. 

```
python index.py
```

This command runs the code. After there will be a message in the command line with url. By defuault:

```
http://localhost:8050/home
```

### Enjoy

### Docker

Also, there is 'Dockerfile' in 'image-gpt/Docker' directory. To make a docker-container of the app and use it, you should use the 'build' command to create an image (including dot in the end):

```
docker build -t plotly-dash-visualisation -f docker/Dockerfile .
```

After, you can run it by typing:

```
python run plotly-dash-visualisation
```

### Literature

```
https://medium.com/swlh/dashboards-in-python-for-beginners-using-dash-exporting-data-from-a-dashboard-fe0c5dec3ddb
```

## License

[Modified MIT](./LICENSE)
