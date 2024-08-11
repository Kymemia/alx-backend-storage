-- this script lists all bands with <Glam rock> as their main style, ranked by their longevity

SELECT 
	band_name,
       	COALESCE(split, 2022) AS lifespan FROM bands
	WHERE style = 'Glam rock'
	ORDER BY lifespan DESC;
