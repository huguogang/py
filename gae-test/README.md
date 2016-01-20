Deploy

```
appcfg.py -A developertips-1 update gae-test/
```

Run Local Development Server

```
dev_appserver.py gae-test/
```

Built-in URLs
  * `/form/`
  * `/_ah/`
  
os.environ
  * APPLICATION_ID
  * CURRENT_VERSION_ID
  * AUTH_DOMAIN
  * SERVER_SOFTWARE
Or any other defined in app.yaml's env_variables section.