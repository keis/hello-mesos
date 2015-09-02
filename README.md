# hello-mesos

dockerized hello world with mesos

## Running

Start zookeeper, mesos master cluster and mesos slaves
```bash
./start
```
Run the hello world framework
```bash
docker-compose run framework
```

## Trouble shooting

no route to host between docker containers, try

```bash
sudo iptables -A DOCKER -p tcp -j ACCEPT
```
