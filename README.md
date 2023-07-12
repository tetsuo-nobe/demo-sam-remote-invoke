
* [AWS Blog](https://aws.amazon.com/jp/blogs/compute/testing-aws-lambda-functions-with-aws-sam-remote-invoke/)
* [AWS Document](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-remote-invoke.html)

---

## OK

```
sam remote invoke --stack-name demo-sam-remote-invoke --event  '{\"first_name\": \"Tetsu\",\"last_name\": \"Nobe\" }'  
```

```
sam remote invoke --stack-name demo-sam-remote-invoke --event  '{\"first_name\": \"Tetsu\",\"last_name\": \"Nobe\" }'  DemoSamRemoteInvokeFunction 
```

```
sam remote invoke --stack-name demo-sam-remote-invoke --event-file './events/event.json' DemoSamRemoteInvokeFunction
```

```
sam remote invoke --stack-name demo-sam-remote-invoke --event-file './events/event.json' 
```

----

## NG

* --stack-name が必要

```
sam remote invoke  --event-file './events/event.json' 
```

* --profile のオプションが効いていない

```
sam remote invoke --stack-name demo-sam-remote-invoke --profile devserverless   --event  '{\"first_name\": \"Tetsu\",\"last_name\": \"Nobe\" }' DemoSamRemoteInvokeFunction 
```
