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
- start serverless offline: `sls offline start --noTimeout`;

At this point everything should be set up. Local AppSync Simulator should be available at http://192.168.2.133:20002

## Deployment
```
sls deploy
```