# ddns-cloudflare

Use cloudflare package v4 to update the DNS records.

### Build Docker image

```bash
docker build -t ddns-updater:production .
```

### Set Up a Cron Job 

Use a cron job on host system to run the Docker container periodically. For example, to run it every day:

Edit your crontab by running `crontab -e`.
Add the following line:

```bash
0 0 * * * docker run --rm --env-file .env ddns-updater:production
```