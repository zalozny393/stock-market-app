# Stock Market App

## Requirements:
- Python 3.9;
- Pipenv;
- nodejs 14+ (for serverless framework);
- npm;
- aws account (for deployment).

## Getting started:
- install nodejs packages: `npm install`;
- install python packages: `pipenv install`;
- create a `.env` file based on `.env.sample` (some variables are reuired for deployment only);
- fill `.env` file;
- start serverless offline: `sls offline start --noTimeout`;

At this point everything should be set up. Local AppSync Simulator should be available at http://192.168.2.133:20002

## Deployment
```
sls deploy
```

Populate `Authorised JavaScript origins` and `Authorised redirect URIs` in Google APIs & Services to allow athontificate trough Google.
