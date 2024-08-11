-- this script lists all bands with <Glam rock> as their main style, ranked by their longevity

SELECT band_name, (2022 - formed) - COALESCE(split, 2022) AS Lifespan FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
