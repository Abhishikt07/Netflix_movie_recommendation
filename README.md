Netflix Movie Recommendation System 🎬
📖 Project Overview
Welcome to the Netflix Movie Recommendation System! This project leverages movie metadata from TMDB 5000 Movie Details and TMDB Credits datasets to build a content-based recommendation engine. By analyzing features like genres, cast, and crew, this system suggests movies similar to a user-selected title.

The recommendation system is deployed using Streamlit, providing an interactive interface for users to explore movie recommendations.

✨ Features
Content-Based Filtering: Recommends movies similar to the input movie based on genres, cast, and crew metadata.
Text Preprocessing: Applied stemming, lowercasing, and removal of stopwords using NLP techniques.
Cosine Similarity: Implemented to measure the similarity between movies based on their textual features.
Interactive Web App: Built using Streamlit, allowing users to input their favorite movie and receive personalized recommendations.
Efficient Processing: Stored preprocessed data and similarity matrices using Pickle for faster loading and scalability.
📊 Datasets
TMDB 5000 Movie Details: Contains metadata for 5000+ movies, including features such as genres, overview, and popularity.
TMDB Credits: Includes cast and crew information for each movie.
You can find the datasets here.

🛠️ Project Structure
bash
Copy code
├── Netflix_Movie_Recommendation
│   ├── data
│   │   ├── tmdb_5000_movies.csv
│   │   ├── tmdb_5000_credits.csv
│   ├── movie_recommendation.py      # Main Python script
│   ├── movies_dict.pkl              # Preprocessed movie data (Pickle file)
│   ├── similarity.pkl               # Similarity matrix (Pickle file)
│   ├── README.md                    # Project overview
└── ...
🚀 Installation and Setup
Follow these steps to get the project running on your local machine:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/Netflix_Movie_Recommendation.git
Navigate to the project directory:

bash
Copy code
cd Netflix_Movie_Recommendation
Install the required packages: Make sure you have Python 3.x installed. Then, install the necessary libraries:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run movie_recommendation.py
🎯 Usage
Choose a Movie: Select a movie from the dropdown menu.
Get Recommendations: Click the Recommend button to get a list of 5 movies similar to your selected movie.
Explore the System: You can edit and experiment with the movie_recommendation.py script to further customize the recommendation engine.
🔍 Project Highlights
Bag of Words (BOW): Used CountVectorizer to create numerical vectors from text data for movie metadata (genres, keywords, cast, crew, overview).
Cosine Similarity: Calculated similarity between movies based on their vectors, allowing the system to recommend the closest matches.
Streamlit Deployment: Deployed the recommendation system with a simple and interactive UI for user input.
📈 Visualizations
Wordcloud of Movie Genres:

Top Actors:

🤝 Contributing
Contributions are welcome! Here’s how you can help:

Fork the repository.
Create a new branch for your feature (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add feature').
Push to your branch (git push origin feature-branch).
Open a pull request, and I will review your contribution.

🙌 Acknowledgments
This project was inspired by various recommendation systems used in streaming platforms. Special thanks to the contributors of the TMDB 5000 Movies and Credits datasets.
