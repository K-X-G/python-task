use ip;

CREATE TABLE ip_location(
    id int not null AUTO_INCREMENT,
    ip VARCHAR(20) NOT NULL,
    country VARCHAR(20) NOT NULL,
    org VARCHAR(20) NOT NULL,
    PRIMARY KEY (id)
);