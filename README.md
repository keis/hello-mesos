# hello-mesos

dockerized hello world with mesos

## Trouble shooting

no route to host between docker containers, try

```bash
sudo iptables -A DOCKER -p tcp -j ACCEPT
```
