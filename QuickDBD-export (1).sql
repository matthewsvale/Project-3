-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "airbnbs" (
    "id" int   NOT NULL,
    "neighbourhood" VARCHAR(66)   NOT NULL,
    "latitude" INT   NOT NULL,
    "longitude" INT   NOT NULL,
    "room_type" VARCHAR(66)   NOT NULL,
    "price" money   NOT NULL,
    CONSTRAINT "pk_airbnbs" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "Crash_Locations" (
    "number" int   NOT NULL,
    "accident_year" int   NOT NULL,
    "collision_date" date   NOT NULL,
    "collision_time" int   NOT NULL,
    "Day_of_week" int   NOT NULL,
    "longitude" int   NOT NULL,
    "latitude" int   NOT NULL,
    CONSTRAINT "pk_Crash_Locations" PRIMARY KEY (
        "number"
     )
);

ALTER TABLE "Crash_Locations" ADD CONSTRAINT "fk_Crash_Locations_number_longitude_latitude" FOREIGN KEY("number", "longitude", "latitude")
REFERENCES "airbnbs" ("id", "longitude", "latitude");

CREATE INDEX "idx_airbnbs_neighbourhood"
ON "airbnbs" ("neighbourhood");

