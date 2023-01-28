from py2neo import Graph, Node, Relationship
import csv


def neo4j_import(csv_path):
    # user: neo4j
    # pass: password

    graph = Graph("bolt://localhost:7687",
                  auth=("neo4j", "password"), name="neo4j")
    # reset database
    graph.delete_all()

    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for (i, line) in enumerate(reader):
            # if(i > 80):
            #     break
            title = line['Name']
            release_year = line['Year of release']

            original_networks = line['Original Network']
            # split, and strip
            original_networks = original_networks.split(',')
            original_networks = [x.strip() for x in original_networks]

            aired_days = line['Aired On']
            # split, and strip
            aired_days = aired_days.split(',')
            aired_days = [x.strip() for x in aired_days]

            number_of_episodes = line['Number of Episodes']
            number_of_episodes = int(number_of_episodes)

            duration = line['Duration']
            duration = duration.split('.')
            total = 0
            for e in duration:
                if ('min' in e):
                    total += int(e.split('min')[0].strip())
                elif ('hr' in e):
                    total += int(e.split('hr')[0].strip()) * 60
            duration = total

            content_rating = line['Content Rating']
            content_rating = content_rating.split('+')
            content_rating = int(content_rating[0])

            rating = line['Rating']
            rating = float(rating)

            synopsis = line['Synopsis']

            genres = line['Genre']
            # split, and strip
            genres = genres.split(',')
            genres = [x.strip() for x in genres]

            tags = line['Tags']
            # split, and strip
            tags = tags.split(',')
            tags = [x.strip() for x in tags]

            director = line['Director']
            director = director.split(',')
            director = [x.strip() for x in director]

            cast = line['Cast']
            cast = cast.split(',')
            cast = [x.strip() for x in cast]

            rank = line['Rank']
            rank = rank.strip('#')
            rank = int(rank)

            # comment this line to actually save data
            # continue

            drama_node = graph.nodes.match("KDrama", title=title).first()
            if drama_node is None:
                drama_node = Node(
                    "KDrama", title=title, number_of_episodes=number_of_episodes, content_rating=content_rating, synopsis=synopsis, rank=rank)
                graph.create(drama_node)

            release_node = graph.nodes.match(
                "Release", year=release_year).first()
            if release_node is None:
                release_node = Node("Release", year=release_year)
                graph.create(release_node)

            rel = Relationship(drama_node, "RELEASED", release_node)
            graph.create(rel)

            for network in original_networks:
                network_node = graph.nodes.match(
                    "Network", title=network).first()
                if network_node is None:
                    network_node = Node("Network", title=network)
                    graph.create(network_node)

                rel = Relationship(drama_node, "ORIGINATED_FROM", network_node)
                graph.create(rel)

            for day in aired_days:
                day_node = graph.nodes.match("Day", title=day).first()
                if day_node is None:
                    day_node = Node("Day", title=day)
                    graph.create(day_node)

                rel = Relationship(drama_node, "AIRED_ON", day_node)
                graph.create(rel)

            duration_node = graph.nodes.match(
                "Duration", value=duration).first()
            if duration_node is None:
                duration_node = Node("Duration", value=duration)
                graph.create(duration_node)

            rel = Relationship(drama_node, "DURATION", duration_node)
            graph.create(rel)

            rating_node = graph.nodes.match("Rating", value=rating).first()
            if rating_node is None:
                rating_node = Node("Rating", value=rating)
                graph.create(rating_node)

            rel = Relationship(drama_node, "RATING", rating_node)
            graph.create(rel)

            for genre in genres:
                genre_node = graph.nodes.match("Genre", title=genre).first()
                if genre_node is None:
                    genre_node = Node("Genre", title=genre)
                    graph.create(genre_node)

                rel = Relationship(drama_node, "GENRE", genre_node)
                graph.create(rel)

            for tag in tags:
                tag_node = graph.nodes.match("Tag", title=tag).first()
                if tag_node is None:
                    tag_node = Node("Tag", title=tag)
                    graph.create(tag_node)

                rel = Relationship(drama_node, "TAG", tag_node)
                graph.create(rel)

            for director_name in director:
                director_node = graph.nodes.match(
                    "Director", name=director_name).first()
                if director_node is None:
                    director_node = Node("Director", name=director_name)
                    graph.create(director_node)

                rel = Relationship(drama_node, "DIRECTED_BY", director_node)
                graph.create(rel)

            for cast_name in cast:
                cast_node = graph.nodes.match("Cast", name=cast_name).first()
                if cast_node is None:
                    cast_node = Node("Cast", name=cast_name)
                    graph.create(cast_node)

                rel = Relationship(drama_node, "CAST", cast_node)
                graph.create(rel)


csv_path = 'kdrama.csv'
neo4j_import(csv_path)
