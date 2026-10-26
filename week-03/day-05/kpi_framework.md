# Week 3 — Day 5: KPI Design

## Business Domain
Retail sales analysis using the Cynaris sales dataset.

## KPI Framework

| # | KPI | Formula | Owner | Frequency | Target | Type |
|---|---|---|---|---|---|---|
| 1 | Total Sales | Sum of sales amount | Sales Manager | Weekly | Increase by 10% quarter over quarter | Lagging |
| 2 | Total Orders | Count of unique sale IDs | Operations Manager | Weekly | Increase by 5% quarter over quarter | Lagging |
| 3 | Average Order Value | Total Sales / Total Orders | Sales Manager | Weekly | Increase by 5% quarter over quarter | Lagging |
| 4 | Electronics Sales | Sum of amount where category = Electronics | Category Manager | Weekly | Increase by 10% quarter over quarter | Lagging |
| 5 | Regional Sales Growth | (Current period regional sales - previous period regional sales) / previous period regional sales × 100 | Regional Manager | Monthly | At least 5% growth | Lagging |
| 6 | Discount Rate | Average discount percentage | Pricing Manager | Weekly | Stay within approved pricing policy | Leading |
| 7 | Discounted Order Share | Orders with discount > 0 / Total Orders × 100 | Pricing Manager | Monthly | Monitor against approved plan | Leading |
| 8 | Product Category Mix | Category sales / Total Sales × 100 | Merchandising Manager | Monthly | Meet category-specific sales plan | Leading |
| 9 | Sales Data Completeness | Records with required fields populated / Total records × 100 | Data Analyst | Weekly | At least 98% | Leading |
| 10 | Sales Target Attainment | Actual Sales / Planned Sales × 100 | Sales Manager | Monthly | At least 100% | Lagging |

*Targets are proposed examples for this exercise and should be agreed with business owners using historical performance and business plans.*

## Leading vs. Lagging Indicators

- **Leading indicators** provide early signals that may influence future results. Examples here include discount rate, discounted order share, category mix, and data completeness.
- **Lagging indicators** report outcomes that have already occurred. Examples include total sales, order count, average order value, regional sales growth, and target attainment.
- Some indicators can be classified differently depending on how the business uses them. The classification above reflects the intended use in this framework.

## KPI Dashboard Design

Build a single-page dashboard in Power BI using the existing sales dataset.

Recommended visuals:
1. Scorecard: Total Sales
2. Scorecard: Total Orders
3. Scorecard: Average Order Value
4. Bar chart: Sales by Region
5. Bar chart: Sales by Category
6. Line chart: Sales by Date
7. Slicers: Region, Category, and Sale Date

Use `amount` as the sales value, `sale_id` for order count, `category` and `region` for breakdowns, and `sale_date` for trends.

## KPI Narrative

The current dataset contains a small sample of sales records. Total sales and average order value summarize overall performance, while regional and category charts help identify where revenue is concentrated. The date trend can reveal peaks or dips, but conclusions should be treated cautiously because the dataset covers a limited period.

Discounts may help explain pricing patterns, but a high discount rate does not necessarily mean better performance. Compare discounts with sales targets and margin data before recommending changes. The dataset does not contain profit or cost fields, so profit margin cannot be calculated reliably.

Before presenting this dashboard to business stakeholders, compare actual values with historical periods and approved targets. Investigate unusual changes by region, category, and date rather than assuming that a single chart explains the cause.

## Viva Notes

### 1. Leading vs. lagging KPI
A leading KPI gives an early indication of possible future performance. A lagging KPI measures a result that has already happened.

### 2. How are KPI targets set?
Use business objectives, historical results, available resources, market conditions, and stakeholder agreement. Targets should be measurable and time-bound.

### 3. What is SMART?
- **S**pecific: Clearly defined
- **M**easurable: Quantifiable
- **A**chievable: Realistic
- **R**elevant: Connected to business goals
- **T**ime-bound: Has a deadline or reporting period

## KPI, Metric, and Measure

- **Metric:** A quantifiable value used to monitor activity or performance.
- **Measure:** A calculated or aggregated value, such as a sum or count.
- **KPI:** A metric selected because it tracks progress toward an important business objective.
