---
title: PostgreSQL Cheatsheet
---


- default port **5432**


```bash
$ psql postgres://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE NAME}
```

#### json
```sql
-- concat
UPDATE users SET metadata = metadata || '{"country": "Brazil"}';

-- remove
UPDATE users SET metadata = metadata - 'country';

-- select
SELECT * FROM groups WHERE (metadata->'managed_by'->>'id') = 50;
SELECT * FROM enrollments WHERE (metadata->'created_at')::timestamptz) < '2018-01-30'
```

#### copy csv to stdout
```sql
COPY (select * from users) TO STDOUT DELIMITER ',' CSV HEADER;
```

Links
-----

- [Querying JSON in Postgres](http://schinckel.net/2014/05/25/querying-json-in-postgres/)
- [How to query JSONB, beginner sheet cheat](https://hackernoon.com/how-to-query-jsonb-beginner-sheet-cheat-4da3aa5082a3https://hackernoon.com/how-to-query-jsonb-beginner-sheet-cheat-4da3aa5082a3)
