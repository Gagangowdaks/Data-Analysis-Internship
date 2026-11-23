Write-Host "W6D3 PostgreSQL Sales Database Verification"
docker exec superset_db psql -U superset -d salesdb -c "SELECT COUNT(*) AS total_sales_rows FROM sales;"
