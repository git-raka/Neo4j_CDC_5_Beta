import random
import string
import time
from neo4j import GraphDatabase

# Function to generate a random name
def random_name(length=6):
    letters = string.ascii_letters  # Both upper and lower case
    return ''.join(random.choice(letters) for _ in range(length))

# Function to generate a random country name
def random_country():
    countries = [
        "USA", "Canada", "UK", "Australia", "Germany", "France", "India",
        "Brazil", "Japan", "South Korea", "South Africa", "Mexico", "Russia"
    ]
    return random.choice(countries)

# Function to generate a Cypher query to create a random Person node
def generate_random_cypher():
    name = random_name()
    country = random_country()
    return f"CREATE (p:Person {{name: '{name}', country: '{country}'}})"

# Function to continuously execute Cypher queries in a specific Neo4j database
def execute_cypher_queries(uri, user, password, database, rate=1):
    driver = GraphDatabase.driver(uri, auth=(user, password))
    with driver.session(database=database) as session:
        while True:
            query = generate_random_cypher()  # Generate a random query
            session.run(query)  # Execute the query
            print(query)  # Optionally, print the query for monitoring
            time.sleep(1 / rate)  # Control the rate of query generation
    driver.close()

# Example usage
neo4j_uri = "bolt://192.168.18.9:7687"  # Change to your Neo4j instance
neo4j_user = "neo4j"
neo4j_password = "Ddi12345!"  # Change to your Neo4j password
database_name = "cdc"  # Target database name

# Execute Cypher queries continuously with a rate of 1 query per second
execute_cypher_queries(neo4j_uri, neo4j_user, neo4j_password, database_name, rate=1)
