# Reminding FFXIV raid schedule

This container reminds a schedule on Google Sheets, notifying it to a discord channel.
This is specific to our raid team.

## Usage

### via crontab

```
30 12   * * *   root    docker run --rm -v /opt/xiv-reminder/eden-resurrection.json:/config.json:ro xiv-raid-reminder
```
