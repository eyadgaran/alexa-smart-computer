# alexa-smart-computer
Control any computer as an alexa smart device


Repo contains two projects:
1) Server (computer) side app to listen for requests
2) HTTPS -> HTTP AWS Lambda Skill to forward requests to http domains

Separately, it is required to set up an Alexa Skill in the developer portal
to add intents for the service - Instructions included below


## Setting up Alexa Skill
1) Navigate to developer portal: developer.amazon.com
2) Create skill - follow prompts
3) Choose invocation name (`my computer`) - used as "alexa, tell `my computer` to blah"
4) Build interaction model
  - Create intents and the keywords that trigger them
5) Configure the endpoint to reach out to
  - Use httpsForwarder lambda ARN here if ultimate endpoint doesn't support HTTPS
  - Otherwise put your endpoint here


*Note: HTTPS forwarder is only necessary for compatibility with HTTP
endpoint (AWS restricts to using HTTPS)
