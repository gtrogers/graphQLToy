# graphQLToy
Toy GraphQL Example in Python3

## Set Up

```Bash
> python3 -m pip install -r Requirements.txt
> python3 app.py
```

Point your browser to `localhost:5000/graphql` to see the query explorer

## Example queries

```json
query {
  blip(id: 0) {
    name
    info
    position {
      quadrant, ring
    }
  }
}

query {
  blips(quadrant: TOOLS, ring: TRIAL) {
    name, info
  }
}
```

