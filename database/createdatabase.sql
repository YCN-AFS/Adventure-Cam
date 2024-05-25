CREATE TABLE players (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE player_profiles (
    profile_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    display_name VARCHAR(50) NOT NULL,
    avatar VARCHAR(200),
    bio TEXT,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
CREATE TABLE player_settings (
    setting_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    sound_enabled BOOLEAN DEFAULT TRUE,
    music_enabled BOOLEAN DEFAULT TRUE,
    language VARCHAR(10) DEFAULT 'en',
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);
CREATE TABLE player_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT NOT NULL,
    session_token VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (player_id) REFERENCES players(player_id)
);