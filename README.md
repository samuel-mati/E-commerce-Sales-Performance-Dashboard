# E-commerce-Sales-Performance-Dashboard
## Project Overview
This project is focused on developing an interactive e-commerce sales performance dashboard. The dashboard will provide actionable insights into sales trends, customer behavior, product performance, and inventory management. Using MySQL as the backend database, Python for data processing, and Tableau for visualization, this tool will aid e-commerce managers in making data-driven decisions to enhance sales growth and optimize operational efficiency.

### Objectives
Sales Analysis: Analyze sales data over time to identify trends, seasonality, and potential growth opportunities.
Customer Insights: Delve into customer demographic and behavioral data to tailor marketing strategies effectively.
Product Performance: Evaluate which products are selling well and which are not to adjust purchasing decisions and promotional tactics.
Inventory Management: Monitor and manage inventory levels to prevent stockouts and minimize excess stock.
### Tools Used
**MySQL**: Utilized for database management and advanced querying.

**Python**: Used for data manipulation and integration with MySQL. Key libraries include Pandas for data frames and SQLAlchemy for database connections.

**Tableau Public**: Employed for creating and publishing interactive visualizations of the data online.

### Data Model
The database is structured into the following key tables:

**Customers:** Contains information such as customer_id, name, email, and location.
**Products:** Stores details like product_id, name, category, price, and stock_quantity.
**Orders:** Records transactions with fields like order_id, customer_id, order_date, and total_amount.
**Order Details**: Acts as a junction table linking Orders to Products, with fields including order_id, product_id, quantity, and price.
