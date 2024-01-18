-- Creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id_param INT, IN project_name_param VARCHAR(255), IN score_param INT)
BEGIN
    DECLARE project_id_param INT;

    -- Check if the project already exists
    SELECT id INTO project_id_param FROM projects WHERE name = project_name_param;

    -- If project does not exist, create it
    IF project_id_param IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name_param);
        SET project_id_param = LAST_INSERT_ID();
    END IF;

    -- Add the bonus correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id_param, project_id_param, score_param);
END //

DELIMITER ;
