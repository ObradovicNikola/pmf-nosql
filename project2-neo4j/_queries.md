CALL db.schema.visualization()

MATCH (n:KDrama) WHERE (n.number_of_episodes < 10) RETURN n

MATCH (n:KDrama)-[:AIRED_ON]->(d:Day) WHERE n.number_of_episodes < 10
RETURN n, d

MATCH (n:KDrama)-[:AIRED_ON]->(d:Day)
MATCH (n)-[:ORIGINATED_FROM]->(network:Network)
WHERE n.number_of_episodes < 10
RETURN n, d, network

MATCH (n:KDrama)-[:AIRED_ON]->(d:Day)
MATCH (n)-[:ORIGINATED_FROM]->(network:Network {title: "Netflix"})
WHERE n.number_of_episodes < 10
RETURN n, d, network

MATCH (d:KDrama) WHERE d.title =~ "Squid.\*" WITH d MATCH (a)-[r]-(d) RETURN d, a
MATCH (d:KDrama {title: "Squid Game"}) RETURN d

<!-- count Cast in each KDrama -->

MATCH (d:KDrama)
WITH d MATCH (d)-[r]-(c:Cast)
RETURN d.title as title, count(c) as cast_count
ORDER BY cast_count DESC

<!-- min, max, avg -->

MATCH (d:KDrama) return min(d.number_of_episodes), max(d.number_of_episodes), avg(d.number_of_episodes)
MATCH (p:Rating) return min(p.value), max(p.value), avg(p.value)

<!-- collect cast -->

MATCH (d:KDrama)
WITH d MATCH (d)-[r]-(c:Cast)
RETURN d.title as title, collect(c.name) as cast

<!-- DISTINCT -->

MATCH (d:KDrama) RETURN DISTINCT d.number_of_episodes as episodes ORDER BY episodes DESC

<!-- broj serija svakog glumca -->

MATCH (c:Cast)-[r]-(p)
RETURN c.name AS name, COUNT(p) AS broj_serija
ORDER BY broj_serija DESC

<!-- MATCH (c:Cast)
WITH c
MATCH (c)-[r]-(p)
RETURN c.name AS name, COUNT(p) AS broj_serija
ORDER BY broj_serija DESC -->

<!-- broj serija veci od 6 -->

MATCH (c:Cast)-[r]-(p)
WITH c, COUNT(p) AS broj_serija
WHERE broj_serija > 6
RETURN c.name AS name, broj_serija
ORDER BY broj_serija DESC

MATCH p= (b:Cast {name: "Lee Joon Hyuk"})-[r*1..4]-(m:Cast {name: "Ahn Bo Hyun"}) RETURN p
