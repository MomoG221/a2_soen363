create table movies (
    movies_id SERIAL PRIMARY KEY,
    watchmode_id INT,
    title VARCHAR(255),
    original_title VARCHAR(255),
    plot_overview TEXT,
    type VARCHAR(255),
    runtime_minutes INT,
    year INT,
    end_year INT,
    release_date DATE,
    imdb_id VARCHAR(255),
    tmdb_id INT,
    tmdb_type VARCHAR(255),
);

create table movies_genre(
    movies_id INT,
    genre_id INT,
    foreign key(movies_id) references movies(movies_id),
    foreign key(genre_id) references genre(genre_id)
    );

create table genre(
    genre_id SERIAL PRIMARY KEY,
    genre_name VARCHAR(255)
);

create table ratings(
    movies_id INT,
    ratings_id SERIAL PRIMARY KEY,
    user_rating FLOAT,
    critics_score INT,
    foreign key(movies_id) references movies(movies_id)
);

create country movies_country(
    movies_id INT,
    country_id INT,
    foreign key(movies_id) references movies(movies_id),
    foreign key(country_id) references country(country_id)
    );

create country country(
    country_id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    country_code VARCHAR(255)
);

create table movies_keywords(
    movies_id INT,
    keywords_id INT,
    foreign key(movies_id) references movies(movies_id),
    foreign key(keywords_id) references keywords(keywords_id)
    );

create table keywords(
    keywords_id SERIAL PRIMARY KEY,
    keywords_name VARCHAR(255)
);
