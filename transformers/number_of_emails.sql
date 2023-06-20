SELECT
    COUNT(*) AS number_of_emails
    , id_user
FROM {{ df_1 }}
GROUP BY id_user