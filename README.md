# Neo4j_CDC_5_Beta

```
create database cdc
```

```
alter database cdc SET OPTION txLogEnrichment "FULL"
```

```
GRANT EXECUTE PROCEDURE db.cdc.query ON DBMS TO admin
```

### Create sample  data for checking cdc event
```
CREATE (p1:Person {name: 'Alice', country: 'USA'})
CREATE (p2:Person {name: 'Bob', country: 'Canada'})
CREATE (p3:Person {name: 'Charlie', country: 'UK'})
```
### check cdc id
```
CALL db.cdc.earliest()
```

### Now view event
```
CALL db.cdc.query("A-cDExHKa0pEjQ1XoMjLgvoAAAAAAAAAAAAAAAAAAAAA")
```
![image](https://github.com/git-raka/Neo4j_CDC_5_Beta/assets/77326619/6f6a11a1-8395-4f06-b1e3-5adb24aee50a)

## Testing using cypher generator
```
python3 cdc_test.py
```

```
python3 cypher_generator.py
```
