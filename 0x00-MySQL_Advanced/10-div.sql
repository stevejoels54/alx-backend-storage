--SQL script that creates a function SafeDiv

DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DECIMAL(10, 4)
BEGIN
    DECLARE result DECIMAL(10, 4);

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END $$
DELIMITER ;
