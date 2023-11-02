class NetflixRecommendationEngine:
    def __init__(self):
        self.users = {}
        self.movies = {}
    
    def add_user(self, user_id):
        self.users[user_id] = {}
    
    def add_movie(self, movie_id, title, genres):
        self.movies[movie_id] = {'title': title, 'genres': genres, 'ratings': {}}
    
    def rate_movie(self, user_id, movie_id, rating):
        if user_id in self.users and movie_id in self.movies:
            self.movies[movie_id]['ratings'][user_id] = rating
    
    def get_recommendations(self, user_id):
        if user_id in self.users:
            user_ratings = self.users[user_id]
            # Implement your recommendation algorithm here
            # This could be collaborative filtering, content-based filtering, or a hybrid approach
            
            # For simplicity, let's return a list of top-rated movies for now
            return sorted(self.movies.values(), key=lambda x: sum(x['ratings'].values()), reverse=True)[:5]
        else:
            return None

# Example Usage
engine = NetflixRecommendationEngine()

# Add users
engine.add_user('user1')
engine.add_user('user2')

# Add movies
engine.add_movie(1, 'Movie 1', ['Action', 'Adventure'])
engine.add_movie(2, 'Movie 2', ['Comedy', 'Romance'])

# Rate movies
engine.rate_movie('user1', 1, 5)
engine.rate_movie('user1', 2, 4)
engine.rate_movie('user2', 1, 4)

# Get recommendations for a user
recommendations = engine.get_recommendations('user1')

if recommendations:
    for movie in recommendations:
        print(f"Title: {movie['title']}, Genres: {', '.join(movie['genres'])}")
else:
    print("User not found.")
