-- SQL script that lists all bands with
-- glam rock as  main style, ranked by their longevity

SELECT band_name, 
       (IFNULL(split, 2022) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
