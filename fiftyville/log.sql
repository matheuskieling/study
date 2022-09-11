-- Keep a log of any SQL queries you execute as you solve the mystery.

--FIND TRANSCRIPT OF INTERVIEWS
SELECT transcript FROM interviews WHERE day = 28 AND month = 7;

--JULY 28 10:15

--|Ten minutes of the thef, thief drive away.
--|Look for cars that left the parking lot in that time frame.
SELECT license_plate from bakery_security_logs
WHERE day = 28
AND month = 7
AND hour = 10
AND minute > 15
AND minute < 25;
--+---------------+
--| license_plate |
--+---------------+
--| 5P2BI95       |
--| 94KL13X       |
--| 6P58WS2       |
--| 4328GD8       |
--| G412CB7       |
--| L93JTIZ       |
--| 322W7JE       |
--| 0NTHK55       |
--+---------------+
--Who's the owner of the licenses plate?
SELECT name FROM people WHERE license_plate IN(
    SELECT license_plate FROM bakery_security_logs
    WHERE day = 28
    AND month = 7
    AND hour = 10
    AND minute > 15
    AND minute < 25
);
--LIST OF SUSPECTS:
--Vanessa = 1
--Barry = 1
--Iman = 1
--Sofia = 1
--Luca = 1
--Diana = 1
--Kelsey = 1
--Bruce = 1


--|Morning - ATM on Leggett Street the thief was withdrawing some money.
--FIND ACCOUNT NUMBERS FROM THIS:
SELECT account_number FROM atm_transactions
WHERE day = 28
AND month = 7
AND atm_location = 'Leggett Street'
AND transaction_type = 'withdraw';
--USE IT TO FIND PERSON ID's IN BANK:
SELECT person_id FROM bank_accounts
WHERE account_number IN(
    SELECT account_number FROM atm_transactions
    WHERE day = 28
    AND month = 7
    AND atm_location = 'Leggett Street'
    AND transaction_type = 'withdraw'
);
-- FIND PERSON NAME IN PEOPLE:
SELECT name FROM people WHERE id IN(
    SELECT person_id FROM bank_accounts
    WHERE account_number IN(
        SELECT account_number FROM atm_transactions
        WHERE day = 28
        AND month = 7
        AND atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw')
);
-- +---------+
-- |  name   |
-- +---------+
-- | Kenny   |
-- | Iman    |
-- | Benista |
-- | Taylor  |
-- | Brooke  |
-- | Luca    |
-- | Diana   |
-- | Bruce   |
-- +---------+
--LIST OF SUSPECTS:
--Iman = 2
--Luca = 2
--Diana = 2
--Bruce = 2


--|As the thief was leaving the bakery, they called someone for less than a minute.
-- GET SUSPECT NUMBERS:
SELECT phone_number FROM people WHERE name IN ('Iman', 'Luca', 'Diana', 'Bruce');
--CHECK FOR CALLS IN THE DAY OF THE ACT AND WITH LENGHT < 60:
SELECT caller FROM phone_calls
WHERE day = 28
AND month = 7
and duration < 60;
-- CHECK FOR NAME IN PEOPLE WITH THAT NUMBERS
SELECT name FROM people
WHERE phone_number IN(
    SELECT caller FROM phone_calls
    WHERE day = 28
    AND month = 7
    and duration < 60
);
--+---------+
--|  name   |
--+---------+
--| Kenny   |
--| Sofia   |
--| Benista |
--| Taylor  |
--| Diana   |
--| Kelsey  |
--| Bruce   |
--| Carina  |
--+---------+
--LIST OF SUSPECTS:
--Diana = 3
--Bruce = 3

--|In the call, take the earliest flight out of Fiftyville tomorrow.
--CHECK FOR EARLIEST FLIGHT FROM FIFTYVILLE ON JULY, 29:
SELECT id FROM airports
WHERE city = 'Fiftyville';
--FIFTYVILLE AIRPORT ID = 8
SELECT hour, minute FROM flights
WHERE origin_airport_id = 8
AND day = 29
AND month = 7
ORDER BY hour;
--FIRST FLIGHT IS AT 8:20
SELECT id FROM flights
WHERE origin_airport_id = 8
AND day = 29
AND month = 7
AND hour = 8;
-- ID = 36
--FIND PASSANGERS OF THE FLIGHT
SELECT passport_number FROM passengers
WHERE flight_id = 36;
--FIND NAME FROM PASSPORTS OF THE FLIGHT
SELECT name FROM people
WHERE passport_number IN(
    SELECT passport_number FROM passengers
    WHERE flight_id = 36
);
--+--------+
--|  name  |
--+--------+
--| Kenny  |
--| Sofia  |
--| Taylor |
--| Luca   |
--| Kelsey |
--| Edward |
--| Bruce  |
--| Doris  |
--+--------+
--LIST OF SUSPECTS:
--Bruce = 4
-- BRUCE IS THE THIEF, NOW FIND WHO DID HE CALL ON THAT DAY WITH DURATION < 60:
--|The other end of the phone to purchase the flight ticket | < ----- THIS IS THE HELPER
SELECT receiver FROM phone_calls
WHERE day = 28
AND month = 7
AND duration < 60
AND caller = (SELECT phone_number FROM people WHERE name = 'Bruce');
--+----------------+
--|    receiver    |
--+----------------+
--| (375) 555-8161 |
--+----------------+
-- FINALLY LETS FIND WHO THIS BELONGS TO:
SELECT name FROM people
WHERE phone_number = '(375) 555-8161';
--+-------+
--| name  |
--+-------+
--| Robin |
--+-------+
--ROBIN IS THE ASSISTANT

--NOW JUST FIND WHERE THE FLIGHT 36 LANDED:
SELECT destination_airport_id FROM flights
WHERE origin_airport_id = 8
AND day = 29
AND month = 7
AND hour = 8;
--DESTINATION AIRPORT ID IS 4
SELECT city FROM airports
WHERE id = 4;
--+---------------+
--|     city      |
--+---------------+
--| New York City |
--+---------------+
--AUTHOR = BRUCE, ASSISTANT = ROBIN, DESTINATION = NEW YORK CITY