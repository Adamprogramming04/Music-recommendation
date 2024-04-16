import random

class MusicRecommendation:
    def __init__(self, user_preferences):
        self.user_preferences = user_preferences
        self.music_catalog = [
            "Classical Symphony",
            "Jazz Fusion Groove",
            "Rock Anthems",
            "Electronic Dance Party",
            "Chill Acoustic Vibes",
            "Hip-Hop Beats",
        ]

    def generate_recommendations(self, num_recommendations):
        recommendations = random.sample(self.music_catalog, num_recommendations)
        return recommendations

if __name__ == "__main__":
    user_preferences = {
        "genre": "Jazz",
        "mood": "Relaxed",
        "instrumentation": "Piano",
    }

    music_recommendation_system = MusicRecommendation(user_preferences)
    num_recommendations = 3

    recommendations = music_recommendation_system.generate_recommendations(num_recommendations)

    print("Recommended Music:")
    for i, recommendation in enumerate(recommendations):
        print(f"{i + 1}. {recommendation}")
