# QA-with-IA
Pruebas automatizadas: pruebas unitarias básicas e integrarlas con TensorFlow y PyTorch

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
