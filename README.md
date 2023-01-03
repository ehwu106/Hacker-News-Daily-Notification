# Hacker-News-Daily-Notification
Python service that parse through RSS feed from The Hacker News and return daily cybersecurity news. The service will send a discord notification with the article title and the link to it as well. This is a good way to group and keep up to daily cybersecurity related news in my discord inboxes every morning. I have this app running as a cloud function service hosted on Google Cloud service and is being scheduled to run daily using a Cloud Scheduler.

## Intructions
1.) Add your own ServerID, ChannelID, and Token from your discord accordingly in app.py.

2.) Install all the requirement libraries in requirements.txt: `pip install -r requirements.txt`

3.) Run `Python app.py`.

## Local Docker
`docker build -t hacker-news .`

`docker run -it --rm -p 8080:8080 hacker-news:latest`
# License
[GNU General Public License v3.0](LICENSE)
