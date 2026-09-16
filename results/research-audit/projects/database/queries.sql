SELECT s.sample_id, s.condition, sum(c.count) AS assigned_fragments
                   FROM sample s JOIN gene_count c USING(sample_id)
                   GROUP BY s.sample_id, s.condition ORDER BY s.sample_id;
