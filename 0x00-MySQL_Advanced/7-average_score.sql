-- Creates a stored procedure that computes and stores the average score for a student

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id_param INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_projects INT;

    -- Initialize total score and total projects
    SET total_score = 0;
    SET total_projects = 0;

    -- Loop through corrections for the specified user
    FOR each_correction IN (SELECT score FROM corrections WHERE user_id = user_id_param) DO
        SET total_score = total_score + each_correction.score;
        SET total_projects = total_projects + 1;
    END FOR;

    -- Calculate and update the average score
    IF total_projects > 0 THEN
        UPDATE users SET average_score = total_score / total_projects WHERE id = user_id_param;
    END IF;
END //

DELIMITER ;