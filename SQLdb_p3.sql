DROP TABLE airbnbs; 
DROP TABLE crash_locations;
DROP TABLE crime;

CREATE TABLE "airbnbs" (
    "id" int   NOT NULL,
    "neighborhood" varchar(66)   NULL,
    "latitude" DECIMAL(9,5)   NOT NULL,
    "longitude" decimal(9,5)   NOT NULL,
    "room_type" varchar(66)   NOT NULL,
    "price" money   NOT NULL,
    CONSTRAINT "pk_airbnbs" PRIMARY KEY (
        "id"
     )
);


CREATE TABLE "crash_locations" (
    "number" int   NOT NULL,
    "collision_date" date   NOT NULL,
    "collision_time" time   NOT NULL,
    "day_of_week" varchar(66)   NOT NULL,
    "longitude" decimal(9,6)   NOT NULL,
    "latitude" decimal(8,6)   NOT NULL,
    CONSTRAINT "pk_crash_locations" PRIMARY KEY (
        "number"
     )
);


CREATE TABLE "crime" (
    "neighborhood" varchar(66)   NOT NULL,
    "crime_index" int   NOT NULL,
    "motor_vehicle_theft" int   NOT NULL,
    "total_violent_crime" int   NOT NULL,
    "total_burglary" int   NOT NULL,
    "total_thefts" int   NOT NULL,
    CONSTRAINT "pk_crime" PRIMARY KEY (
        "neighborhood"
     )
);

ALTER TABLE "crime" 
ADD CONSTRAINT "fk_crime_neighborhood" 
FOREIGN KEY("neighborhood")
REFERENCES "airbnbs" ("neighborhood");

ALTER TABLE airbnbs
ALTER COLUMN neighborhood DROP NOT NULL;

SELECT * FROM crash_locations
WHERE day_of_week = 'Friday';

SELECT * FROM crime
WHERE crime_index > 75;

SELECT * FROM airbnbs
WHERE neighborhood = 'East Village';

