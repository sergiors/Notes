Checks if has a field
```
GET {es_endpoint}/{index_name}/_search
{
    "query": {
        "exists": {
            "field": "documents.cpf"
        }
    }
}
```
https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-exists-query.html
