def format_movie_list(movies):
    if not movies:
        return "❌ No matching movies found."
    return "\n".join([f"🎬 {movie}" for movie in movies])
