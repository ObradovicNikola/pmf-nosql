docker run -d --name neo4jpmf --publish=7474:7474 --publish=7687:7687 --env NEO4JLABS_PLUGINS='["graph-data-science"]' neo4j:5.3.0

nodes:

KDrama:
    - title
    - number_of_episodes
    - content_rating
    - synopsis (description, summary)
    - rank

Release:
    (KDrama RELEASED)
    - year

Network:
    (KDrama ORIGINATED_FROM)
    - title

Day:
    (KDrama AIRED_ON)
    - title

Duration:
    (KDrama DURATION)
    - value

Rating:
    (KDrama RATING)
    - value

Genre:
    (KDrama GENRE)
    - title

Tag:
    (KDrama TAG)
    - title
    
Director
    (KDrama DIRECTED_BY)
    - name

Cast
    (KDrama CAST)
    - name
