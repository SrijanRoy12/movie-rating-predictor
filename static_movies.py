# ✅ static_movies.py
# Contains structured lists of top 20 Hindi, English, and Bengali movies with metadata

HINDI_MOVIES = [
    {"title": "Hera Pheri", "actors": ["Akshay Kumar", "Suniel Shetty", "Paresh Rawal"], "director": "Priyadarshan", "budget": 7.5e7},
    {"title": "Baazigar", "actors": ["Shah Rukh Khan", "Kajol"], "director": "Abbas–Mustan", "budget": 4e7},
    {"title": "Wake Up Sid", "actors": ["Ranbir Kapoor", "Konkona Sen Sharma"], "director": "Ayan Mukerji", "budget": 1.8e8},
    {"title": "Kaminey", "actors": ["Shahid Kapoor", "Priyanka Chopra"], "director": "Vishal Bhardwaj", "budget": 3.5e8},
    {"title": "Chori Chori Chupke Chupke", "actors": ["Salman Khan", "Rani Mukerji", "Preity Zinta"], "director": "Abbas–Mustan", "budget": 1.3e8},
    {"title": "Adipurush", "actors": ["Prabhas", "Saif Ali Khan", "Kriti Sanon"], "director": "Om Raut", "budget": 6e10},
    {"title": "Brahmastra: Part One – Shiva", "actors": ["Ranbir Kapoor", "Alia Bhatt"], "director": "Ayan Mukerji", "budget": 3.9e10},
    {"title": "Singham Again", "actors": ["Ajay Devgn"], "director": "Unknown", "budget": 3.625e10},
    {"title": "Bade Miyan Chote Miyan", "actors": ["Akshay Kumar"], "director": "Unknown", "budget": 3.5e10},
    {"title": "Saaho", "actors": ["Prabhas"], "director": "Sujeeth", "budget": 3.25e10},
    {"title": "Jawan", "actors": ["Shah Rukh Khan"], "director": "Atlee", "budget": 3e10},
    {"title": "Tiger 3", "actors": ["Salman Khan"], "director": "Unknown", "budget": 3e10},
    {"title": "Pathaan", "actors": ["Shah Rukh Khan"], "director": "Siddharth Anand", "budget": 2.5e10},
    {"title": "Fighter", "actors": ["Hrithik Roshan", "Deepika Padukone"], "director": "Unknown", "budget": 2.5e10},
    {"title": "Maidaan", "actors": ["Ajay Devgn"], "director": "Amit Sharma", "budget": 2.35e10},
    {"title": "2.0 (Hindi dubbed)", "actors": ["Rajinikanth"], "director": "S. Shankar", "budget": 5.75e10},
    {"title": "RRR (Hindi dubbed)", "actors": ["N.T. Rama Rao Jr.", "Ram Charan"], "director": "S.S. Rajamouli", "budget": 5.5e10},
    {"title": "Thugs of Hindostan", "actors": ["Aamir Khan", "Amitabh Bachchan"], "director": "Vijay Krishna Acharya", "budget": 3.1e10},
    {"title": "Laal Singh Chaddha", "actors": ["Aamir Khan"], "director": "Advait Chandan", "budget": 2.75e10},
    {"title": "Zero", "actors": ["Shah Rukh Khan"], "director": "Aanand L. Rai", "budget": 2.7e10},
]

ENGLISH_MOVIES = [
    {"title": "Star Wars: The Force Awakens", "actors": ["Harrison Ford", "Daisy Ridley", "John Boyega"], "director": "J.J. Abrams", "budget": 5.33e8},
    {"title": "Avatar: The Way of Water", "actors": ["Sam Worthington", "Zoe Saldana"], "director": "James Cameron", "budget": 4e8},
    {"title": "Avengers: Endgame", "actors": ["Robert Downey Jr.", "Chris Evans"], "director": "Anthony & Joe Russo", "budget": 4e8},
    {"title": "Mission: Impossible – Dead Reckoning Part One", "actors": ["Tom Cruise"], "director": "Christopher McQuarrie", "budget": 4e8},
    {"title": "Pirates of the Caribbean: On Stranger Tides", "actors": ["Johnny Depp"], "director": "Rob Marshall", "budget": 3.79e8},
    {"title": "Avengers: Age of Ultron", "actors": ["Robert Downey Jr.", "Chris Hemsworth"], "director": "Joss Whedon", "budget": 3.65e8},
    {"title": "Fast X", "actors": ["Vin Diesel"], "director": "Louis Leterrier", "budget": 3.4e8},
    {"title": "Solo: A Star Wars Story", "actors": ["Alden Ehrenreich"], "director": "Ron Howard", "budget": 3.3e8},
    {"title": "Pirates of the Caribbean: At World’s End", "actors": ["Johnny Depp"], "director": "Gore Verbinski", "budget": 3e8},
    {"title": "Avengers: Infinity War", "actors": ["Robert Downey Jr.", "Chris Hemsworth"], "director": "Anthony & Joe Russo", "budget": 3e8},
    {"title": "Justice League", "actors": ["Ben Affleck", "Gal Gadot", "Henry Cavill"], "director": "Zack Snyder", "budget": 3e8},
    {"title": "Indiana Jones and the Dial of Destiny", "actors": ["Harrison Ford"], "director": "James Mangold", "budget": 3e8},
    {"title": "The Lion King (2019)", "actors": ["Donald Glover", "Beyoncé", "James Earl Jones"], "director": "Jon Favreau", "budget": 2.6e8},
    {"title": "Tangled", "actors": ["Mandy Moore", "Zachary Levi"], "director": "Nathan Greno & Byron Howard", "budget": 2.6e8},
    {"title": "Batman v Superman: Dawn of Justice", "actors": ["Ben Affleck", "Henry Cavill"], "director": "Zack Snyder", "budget": 2.63e8},
    {"title": "John Carter", "actors": ["Taylor Kitsch"], "director": "Andrew Stanton", "budget": 2.64e8},
    {"title": "Snow White (2025)", "actors": ["Rachel Zegler", "Gal Gadot"], "director": "Marc Webb", "budget": 2.69e8},
    {"title": "Doctor Strange in the Multiverse of Madness", "actors": ["Benedict Cumberbatch"], "director": "Sam Raimi", "budget": 3.51e8},
    {"title": "Avatar (2009)", "actors": ["Sam Worthington"], "director": "James Cameron", "budget": 2.37e8},
    {"title": "Pirates of the Caribbean: Dead Man’s Chest", "actors": ["Johnny Depp"], "director": "Gore Verbinski", "budget": 2.25e8},
]

BENGALI_MOVIES = [
    {"title": "Amazon Obhijaan", "actors": ["Dev"], "director": "Kamaleshwar Mukherjee", "budget": 2e8},
    {"title": "Chander Pahar", "actors": ["Dev"], "director": "Kamaleshwar Mukherjee", "budget": 1.5e8},
    {"title": "Devi Chowdhurani", "actors": ["Prosenjit Chatterjee", "Srabanti Chatterjee", "Sabyasachi Chakraborty"], "director": "Subhrajit Mitra", "budget": 2.5e8},
    {"title": "Bhai Amar Bhai", "actors": ["Prosenjit Chatterjee"], "director": "Swapan Saha", "budget": 6.5e6},
    {"title": "MLA Fatakeshto", "actors": ["Mithun Chakraborty", "Koel Mallick"], "director": "Swapan Saha", "budget": 2e7},
    {"title": "Paglu", "actors": ["Dev", "Koel Mallick"], "director": "Rajiv Kumar Biswas", "budget": 5e7},
    {"title": "ProjaPoti", "actors": ["Dev", "Mithun Chakraborty"], "director": "Avijit Sen", "budget": 1.3e8},
    {"title": "Boss 2: Back to Rule", "actors": ["Jeet", "Subhashree Ganguly"], "director": "Baba Yadav", "budget": 1e8},
    {"title": "Khadaan", "actors": ["Dev", "Jisshu Sengupta"], "director": "Soojit Rino Dutta", "budget": 2.5e8},
    {"title": "Bohurupi", "actors": ["Abir Chatterjee", "Ritabhari Chakraborty"], "director": "Shiboprosad Mukherjee, Nandita Roy", "budget": 2.1e8},
    {"title": "Sathi", "actors": ["Jeet"], "director": "Haranath Chakraborty", "budget": 9.8e7},
    {"title": "Poran Jai Joliya Re", "actors": ["Dev", "Subhashree Ganguly"], "director": "Rabi Kinagi", "budget": 9.5e7},
    {"title": "Rangbaaz", "actors": ["Dev", "Koel Mallick"], "director": "Raja Chanda", "budget": 9e7},
    {"title": "Praktan", "actors": ["Prosenjit Chatterjee", "Rituparna Sengupta"], "director": "Nandita Roy & Shiboprosad Mukherjee", "budget": 8.5e7},
    {"title": "Chaamp", "actors": ["Dev"], "director": "Raj Chakraborty", "budget": 8.9e7},
    {"title": "Mishawr Rawhoshyo", "actors": ["Prosenjit Chatterjee"], "director": "Srijit Mukherji", "budget": 7e7},
    {"title": "Boss: Born to Rule", "actors": ["Jeet"], "director": "Baba Yadav", "budget": 6.75e7},
    {"title": "Chengiz", "actors": ["Jeet"], "director": "Rajesh Ganguly", "budget": 6.65e7},
    {"title": "Karnasubarner Guptodhon", "actors": ["Abir Chatterjee"], "director": "Dhrubo Banerjee", "budget": 9.8e7},
    {"title": "Golondaaj", "actors": ["Dev"], "director": "Dhrubo Banerjee", "budget": 1.6e8},
]

def get_movies_by_language(language):
    if language == "Hindi":
        return HINDI_MOVIES
    elif language == "English":
        return ENGLISH_MOVIES
    elif language == "Bengali":
        return BENGALI_MOVIES
    else:
        return []
