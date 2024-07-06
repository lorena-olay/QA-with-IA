# QA-with-IA
Automated testing: basic unit testing and integration with TensorFlow and PyTorch
# Steps for docker set up
## Built a docker image
```bash
docker build -t mi_aplicacion .
```
## Execute docker image
```bash
docker run -d -p 5000:5000 mi_aplicacion
```
if you have a problem maybe your system is using **podman**, then we use the next command
```bash
podman run -d -p 5000:5000 mi_aplicacion
```

## other solution, use docker-compose
create a file "docker-compose.yml"
```yaml
version: '3.8'

services:
  mi_aplicacion:
    build: .
    ports:
      - "5000:5000"

```
execute docker-compose:
```bash
docker-compose up --build
```
