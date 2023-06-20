SELECT
    a.*
    , b.number_of_emails
FROM {{ df_1 }} AS a
LEFT JOIN {{ df_2 }} AS b
ON a.id_user = b.id_user