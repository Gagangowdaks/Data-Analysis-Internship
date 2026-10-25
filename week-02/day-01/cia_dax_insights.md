# Power BI - CIA Interaction: DAX Measures vs Calculated Columns

## Question
Explain the difference between a DAX measure and a calculated column in Power BI, with examples, use cases, and the effect of report filters.

## Calculated Column
- Computed row by row during data load or refresh.
- Stored in the data model.
- Evaluated in row context.
- Suitable for static attributes and categorisations.

Example:
`Profit = Sales[Revenue] - Sales[Cost]`

## Measure
- Calculated during query execution when a visual renders.
- Does not store a value for every row.
- Evaluated in filter context, including slicers and visual filters.
- Suitable for aggregations and ratios that should respond to report filters.

Example:
`Total Profit = SUM(Sales[Profit])`

## Effect of Report Filters
- Calculated column values remain fixed until the model is refreshed.
- Measures recalculate based on the current filter context.

## Practical Guidance
- Use a calculated column for a static row-level value or flag.
- Use a measure for a dynamic aggregation that should respond to filters.
- Calculated columns consume model memory; measures avoid storing a value for every row.

## Evidence Note
Summary based on the CIA response provided for this task.
