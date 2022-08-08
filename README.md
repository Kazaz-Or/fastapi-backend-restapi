<h3>What's in the repo?</h3>
<p>Just a simple FastAPI project that was created for learning purposes.</p>

<p>This REST API server was built using Python & FastAPI.</p>

<img width="194" alt="fastapi" src="https://user-images.githubusercontent.com/83350680/183465005-2cd62718-5a6c-4a74-afc0-50952a30c743.png">

<p>This little project's scope was a TODO application which the focus here is for backend rest API only.</p>

<p>Currently it includes two different services - </p>

- Authentication service which handles all things authentication related (such as JWT tokens, fastapi security library, users authentication & etc.
- Todos service which handles all methods for handling a TODO task (POST, GET, PUT, DELETE).


to run services:

authentication service:
```
uvicorn auth:app --reload --port <PORT>
```

todos service:
```
uvicorn app:app --reload --port <PORT>
```

You can browse the services docs (swagger) by browsing to the `url:port/docs`


![New Project](https://user-images.githubusercontent.com/83350680/183468795-6745ebbc-0380-41f1-aa19-674a23be9a4a.png)



<h4>This Project Covers:</h4>

- Python
- FastAPI (fastapi, fastapi.security)
- Pydantic (base model)
- SQLAlchemy as ORM
- SQLite3 as a local database
- OpenAPI for documentation
