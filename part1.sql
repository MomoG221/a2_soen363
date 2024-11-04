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

create table movies_genre();

create table genre();

create table ratings();

create country movies_country();

create country country();


