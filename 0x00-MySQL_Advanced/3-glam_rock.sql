-- this script lists all bands with <Glam rock> as their main style, ranked by their longevity

SELECT band_name, (2022 - formed) AS Lifespan FROM bands
WHERE style = 'Glam rock' AND (split IS NULL or split >= 2022)
ORDER BY lifespan DESC;
