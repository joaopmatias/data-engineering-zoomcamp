# Data Engineering zoomcamp 2023 - Homework 1

## Question 1

We use the followning command.

```bash
docker build --help | grep "image ID"
```

and the answer is

* `--iidfile string`

## Question 2

We use the following commands.

```bash 
docker run --rm --entrypoint=bash  -it python:3.9

pip list
```

and the answer is

* 3

## Question 3

After uploading the green taxi data a table with the name `green_taxi_data` we run the following SQL query

```SQL
  select count(*) 
  from green_taxi_data
  where lpep_pickup_datetime >= '2019-01-15 00:00:00' AND
  lpep_pickup_datetime < '2019-01-16 00:00:00' AND
  lpep_dropoff_datetime >= '2019-01-15 00:00:00' AND
  lpep_dropoff_datetime < '2019-01-16 00:00:00';
```

and the answer is

* 20530

## Question 4

We run the following SQL query

```SQL
  select green_taxi_data.*, dist.max_dist
  from green_taxi_data,
  (
    select max(trip_distance)
	from green_taxi_data
  ) dist(max_dist)
  where green_taxi_data.trip_distance >= dist.max_dist;
```

and the answer is

* 2019-01-15

## Question 5

We run the following SQL query

```SQL
  select count(*) 
  from green_taxi_data
  where passenger_count in (2, 3) AND
  lpep_pickup_datetime >= '2019-01-01 00:00:00' AND
  lpep_pickup_datetime < '2019-01-02 00:00:00'
  group by passenger_count;
```

and the answer is

* 2: 1282 ; 3: 254

## Question 6

We run the following SQL query

```SQL
  select *
  from 
  (
    select *
    from green_taxi_data 
    full join
	(
	  select "LocationID", "Zone"
	  from taxi_zone_lookup
	) pickup(pickup_loc_id, pickup_zone)
    on green_taxi_data."PULocationID" = pickup.pickup_loc_id
	full join 
	(
	  select "LocationID", "Zone"
	  from taxi_zone_lookup
	) dropoff(dropoff_loc_id, dropoff_zone)
    on green_taxi_data."DOLocationID" = dropoff.dropoff_loc_id
  ) trip,
  (
    select max(green_taxi_data.tip_amount)
    from green_taxi_data 
    full join taxi_zone_lookup
    on green_taxi_data."PULocationID" = taxi_zone_lookup."LocationID"
    where taxi_zone_lookup."Zone" = 'Astoria'
  ) tip(max_tip)
  where trip.pickup_zone = 'Astoria' and
    trip.tip_amount >= tip.max_tip;
```

and the answer is

* Long Island City/Queens Plaza
