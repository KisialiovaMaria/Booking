# Booking 


#### Booking application that allows users to fild and book rooms.


## How to start

1. To start this application you need docker and docker compose on your computer.

2. Create .env file in main folder (Booking) and fill it with values as in .env.template file<br>exampe:<br>`` DATABASE_NAME=some_name``
<br>``DATABASE_USER=another_name``
<br>``DATABASE_PASS=some_another_name``<br>

3. open Booking folder in terminal and run this command:
`` docker-compose up ``


## API

| Action                          | URL                                                   | Request body example                                                                                   | Query Params                                                                         |
|---------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Registry                        | ``POST /auth/users/``                                 | {<br/>"username": "masha",<br>"password": "1234"<br/>}                                                 |                                                                                      |
| Authorization                   | ``POST /auth/jwt/create/``                            | {<br/>"username": "masha",<br>"password": "1234"<br/>}                                                 |                                                                                      |
| Book room                       | ``POST /booking/api/v1/room-bookings/``               | {<br/>"book_start": "2023-09-10",<br/>"book_end": "2023-09-12",<br/>"room": 1<br/>}                    |                                                                                      |
| List authorized user bookings   | ``GET /booking/api/v1/room-bookings/``                |                                                                                                        |                                                                                      |
| Cancel booking                  | ``DELETE /booking/api/v1/room-bookings/{booking_id}`` |                                                                                                        |                                                                                      |
| List rooms + filtering, sorting | ``POST /booking/api/v1/rooms/``                       |                                                                                                        | beds_numder (int) <br/>cost_per_day (float) <br/>ordering (beds_numder/cost_per_day) | 
| Find free rooms in period       | ``POST /booking/api/v1/free-rooms/``                  |                                                                                                        | start_date (date)<br/>end_date (date)                                                |
| Open django admin panel         | ``GET /admin/``                                       |                                                                                                        |                                                                                      |





