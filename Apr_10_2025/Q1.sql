SELECT 
    -- First Pokémon
    p1.pokemon_id as first_pokemon_id,
    p1.name AS first_pokemon_name,
    p1.type1 AS first_type1,
    p1.type2 AS first_type2,
    (p1.hp + p1.attack + p1.defense + p1.sp_attack + p1.sp_defense + p1.speed) AS first_total_stats,

    -- Second Pokémon
    p2.pokemon_id as second_pokemon_id,
    p2.name AS second_pokemon_name,
    p2.type1 AS second_type1,
    p2.type2 AS second_type2,
    (p2.hp + p2.attack + p2.defense + p2.sp_attack + p2.sp_defense + p2.speed) AS second_total_stats,

    -- Winner
    pw.pokemon_id as winner_pokemon_id,
    pw.name AS winner_name,

    -- Who was stronger?
    CASE 
        WHEN (p1.hp + p1.attack + p1.defense + p1.sp_attack + p1.sp_defense + p1.speed) > 
             (p2.hp + p2.attack + p2.defense + p2.sp_attack + p2.sp_defense + p2.speed)
             THEN 'First'
        WHEN (p2.hp + p2.attack + p2.defense + p2.sp_attack + p2.sp_defense + p2.speed) > 
             (p1.hp + p1.attack + p1.defense + p1.sp_attack + p1.sp_defense + p1.speed)
             THEN 'Second'
        ELSE 'Equal'
    END AS stronger_pokemon,

    -- Did stronger Pokémon win?
    CASE
        WHEN (p1.hp + p1.attack + p1.defense + p1.sp_attack + p1.sp_defense + p1.speed) >
             (p2.hp + p2.attack + p2.defense + p2.sp_attack + p2.sp_defense + p2.speed)
             AND c.winner_pokemon_id = c.first_pokemon_id THEN 'Yes'

        WHEN (p2.hp + p2.attack + p2.defense + p2.sp_attack + p2.sp_defense + p2.speed) >
             (p1.hp + p1.attack + p1.defense + p1.sp_attack + p1.sp_defense + p1.speed)
             AND c.winner_pokemon_id = c.second_pokemon_id THEN 'Yes'

        WHEN (p1.hp + p1.attack + p1.defense + p1.sp_attack + p1.sp_defense + p1.speed) =
             (p2.hp + p2.attack + p2.defense + p2.sp_attack + p2.sp_defense + p2.speed)
             THEN 'Tie'

        ELSE 'No'
    END AS stronger_won

FROM combats c
JOIN pokemon p1 ON c.first_pokemon_id = p1.pokemon_id
JOIN pokemon p2 ON c.second_pokemon_id = p2.pokemon_id
JOIN pokemon pw ON c.winner_pokemon_id = pw.pokemon_id;