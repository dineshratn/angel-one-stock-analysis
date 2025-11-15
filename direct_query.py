#!/usr/bin/env python3
"""
Direct database query to get table overview
"""
import os
import psycopg2
import pandas as pd

def main():
    # Get database URL from environment
    database_url = os.getenv('DATABASE_URL')

    if not database_url:
        print("Error: DATABASE_URL not set in environment")
        return

    try:
        # Connect to database
        conn = psycopg2.connect(database_url)

        # Get schema
        schema_query = """
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = 'stock_data'
            ORDER BY ordinal_position;
        """
        schema = pd.read_sql_query(schema_query, conn)

        # Get row count
        count_query = "SELECT COUNT(*) as count FROM stock_data;"
        count = pd.read_sql_query(count_query, conn)

        # Get sample data
        sample_query = "SELECT * FROM stock_data LIMIT 5;"
        sample = pd.read_sql_query(sample_query, conn)

        conn.close()

        # Format overview
        overview = f"""
DATABASE OVERVIEW
=================

Total Records: {count['count'].iloc[0]}

TABLE SCHEMA:
{schema.to_string(index=False)}

SAMPLE DATA (First 5 rows):
{sample.to_string(index=False)}
"""

        print(overview)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
