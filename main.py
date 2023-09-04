from fastapi import FastAPI, Body

app = FastAPI()
app.title = "My movie API"
app.version = "0.0.1"

movies = [
    {"id": 1,"name": "The Godfather", "year": 1972, "rating": 9.2},
    {"id": 2, "name": "The Shawshank Redemption", "year": 1994, "rating": 9.3},
    {"id": 3, "name": "Schindler's List", "year": 1994, "rating": 8.9},
    {"id": 4, "name": "Raging Bull", "year": 1980, "rating": 8.2},
    {"id": 5, "name": "Casablanca", "year": 1942, "rating": 8.5},
    {"id": 6, "name": "Citizen Kane", "year": 1941, "rating": 8.3},
    {"id": 7, "name": "Gone with the Wind", "year": 1939, "rating": 8.1},
    {"id": 8, "name": "The Wizard of Oz", "year": 1939, "rating": 8},
    {"id": 9, "name": "One Flew Over the Cuckoo's Nest", "year": 1975, "rating": 8.7},
    {"id": 10, "name": "Lawrence of Arabia", "year": 1962, "rating": 8.3},
    {"id": 11, "name": "Vertigo", "year": 1958, "rating": 8.3},
]

@app.get("/", tags=["home"])
def read_root():
    return {"Hello": "World"}

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

@app.get("/movies/{movie_id}", tags=["movies"])
def get_movie(movie_id: int):
    for movie in movies:
        if(movie["id"] == movie_id):
            return movie
    return []

@app.get("/movies/", tags=["movies"])
def get_movies_by_year(year: int):
    movie_list = []
    for movie in movies:
        if(movie["year"] == year):
            movie_list.append(movie)
    return movie_list

@app.post("/movies", tags=["movies"])
def add_movie(id: int = Body(), name: str = Body(), year: int = Body(), rating: float = Body()):
    movies.append({"id": id, "name": name, "year": year, "rating": rating})
    return movies

@app.put("/movies/{movie_id}", tags=["movies"])
def update_movie(movie_id: int, name: str = Body(), year: int = Body(), rating: float = Body()):
    for movie in movies:
        if(movie["id"] == movie_id):
            movie["name"] = name
            movie["year"] = year
            movie["rating"] = rating
            return movie
    return []

@app.delete("/movies/{movie_id}", tags=["movies"])
def delete_movie(movie_id: int):
    for movie in movies:
        if(movie["id"] == movie_id):
            movies.remove(movie)
            return movies
    return []