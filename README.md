# container-brand-voting-app

## URLs
- URL to application image on [Docker.io image registry](https://hub.docker.com/r/gerundium/brand-voting-app)

## Infos
- Application runs on port 8501
- Prometheus Python metrics exporter runs on port 9090 (Since image version ***v4***)

## Docker run example
```bash
docker run -it --rm -p 8501:8501 -p 9090:9090 gerundium/brand-voting-app
```