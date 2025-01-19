CREATE TABLE users (
  user_id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  phone VARCHAR(20)
);

CREATE TABLE orders (
  order_id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(user_id),
  departure_pier VARCHAR(255),
  destination_pier VARCHAR(255),
  requested_time TIMESTAMP
);

CREATE TABLE piers (
  pier_id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  location GEOGRAPHY
);

CREATE TABLE taxis (
  taxi_id SERIAL PRIMARY KEY,
  current_pier INTEGER REFERENCES piers(pier_id),
  status VARCHAR(50) -- available, occupied, en route
);

CREATE TABLE routes (
  route_id SERIAL PRIMARY KEY,
  pier1 INTEGER REFERENCES piers(pier_id),
  pier2 INTEGER REFERENCES piers(pier_id),
  travel_time INTERVAL
);
