-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "airbnbs" (
    "id" int   NOT NULL,
    "neighbourhood" varchar(66)   NOT NULL,
    "latitude" DECIMAL(9,5)   NOT NULL,
    "longitude" decimal(9,5)   NOT NULL,
    "room_type" varchar(66)   NOT NULL,
    "price" int   NOT NULL,
    CONSTRAINT "pk_airbnbs" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "crash_locations" (
    "number" int   NOT NULL,
    "collision_date" date   NOT NULL,
    "collition_time" time   NOT NULL,
    "day_of_week" varchar(66)   NOT NULL,
    "longitude" decimal(9,6)   NOT NULL,
    "latitude" decimal(8,6)   NOT NULL,
    CONSTRAINT "pk_crash_locations" PRIMARY KEY (
        "number"
     )
);

CREATE TABLE "crime" (
    "neighborhood" varchar(66)   NOT NULL,
    "murder" int   NOT NULL,
    "rape" int   NOT NULL,
    "armed_robbery" int   NOT NULL,
    "strong_arm_robbery" int   NOT NULL,
    "total_violent_crime" int   NOT NULL,
    "residential_burglary" int   NOT NULL,
    "non-residential_burglary" int   NOT NULL,
    "total_burglary" int   NOT NULL,
    "theft_over_400" int   NOT NULL,
    "theft_under_400" int   NOT NULL,
    "total_thefts" int   NOT NULL,
    "motor_vehicle_theft" int   NOT NULL,
    "total_property_crime" int   NOT NULL,
    "crime_index" int   NOT NULL
);

ALTER TABLE "crime" ADD CONSTRAINT "fk_crime_neighborhood" FOREIGN KEY("neighborhood")
REFERENCES "airbnbs" ("neighbourhood");

