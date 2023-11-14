# dive-into-design-patterns
Implementing with Python the 22 classic patterns explained in the book by Alexander Shvets.

## Learn the 22 design patterns with the examples from this repo
Each design pattern is implemented in the backend of this API.

#### One router = One design pattern applied:

Each design pattern is represented behind its own router. E.g: under `/builder` (See [`dive/api/routers/builder.py`](https://github.com/gonza56d/dive-into-design-patterns/blob/master/dive/api/routers/builder.py)) you will find an example of how the Builder Pattern can be applied to solve a particular problem.

## Required
In order to run the app, docker and docker compose are required in your system.


## How to run
When running for the first time, first build images:
```
make build
```

To run the api, run the command:
```
make up
```

## Debugging
For debugging, you can run:
```
make debug
```
In this way, you're able to put breakpoint() function calls to open pdb in your terminal.
