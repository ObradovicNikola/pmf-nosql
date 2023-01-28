# Projections:

## list

```
CALL gds.graph.list()
YIELD graphName, nodeCount, relationshipCount
RETURN graphName, nodeCount, relationshipCount
ORDER BY graphName ASC
```

## project

<!-- all -->

```
CALL gds.graph.project.cypher(
    'WholeGraph',
    'MATCH (n) RETURN id(n) as id',
    'MATCH ()-[r]->() RETURN id(startNode(r)) as source, id(endNode(r)) as target'
)
```

<!-- Day -->

```
CALL gds.graph.project.cypher(
    'DayProjection',
    'MATCH (n:Day) RETURN id(n) AS id, labels(n) AS labels',
    'MATCH (n:Day)<-[r0:AIRED_ON]-(s:KDrama)-[r1:AIRED_ON]->(m:Day) RETURN id(n) AS source, id(m) AS target'
)
```

## Removal, deletion

<!-- delete one -->

CALL gds.graph.drop('WholeGraph')

# Algorithms:

## Centrality, PageRank

```
CALL gds.pageRank.stream('WholeGraph')
YIELD nodeId, score
RETURN nodeId as id, labels(gds.util.asNode(nodeId)), gds.util.asNode(nodeId).title as title, score
ORDER BY score DESC, title ASC
```

```
CALL gds.pageRank.stream('DayProjection')
YIELD nodeId, score
RETURN nodeId as id, labels(gds.util.asNode(nodeId)), gds.util.asNode(nodeId).title as title, score
ORDER BY score DESC, title ASC
```


## Community detection

### Louvain

CALL gds.louvain.stream('WholeGraph',{maxIterations:10})
YIELD nodeId, communityId
RETURN nodeId as id, gds.util.asNode(nodeId).title AS title, communityId
ORDER BY nodeId
LIMIT 100

CALL gds.louvain.stream('DayProjection')
YIELD nodeId, communityId
RETURN nodeId as id, gds.util.asNode(nodeId).title AS title, communityId
ORDER BY id

### labelPropagation (alternative)

CALL gds.labelPropagation.stream('DayProjection')
YIELD nodeId, communityId
RETURN nodeId as id, gds.util.asNode(nodeId).title AS title, communityId
ORDER BY id