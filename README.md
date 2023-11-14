# dive-into-design-patterns
Implementing with Python the 22 classic patterns explained in the book by Alexander Shvets.

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
