How you can retrieve the official CIA answer yourself
Step	Where to go in the portal	What to do
1️⃣	Dashboard → 360° Assessment (or the Career Tools → Assess / Grow section)	Look for the “SQL – CTE vs. Subquery” knowledge‑article or the SQL Best Practices module.
2️⃣	Aptitude / Placement Hub → SQL Practice	There is usually a “Help / FAQ” icon next to each practice question. Click it and type: “When should I use a CTE versus a subquery – performance trade‑offs?”
3️⃣	Documents → Conversation History (if you’ve previously asked the question)	Open the most recent “Interaction” file; CIA’s reply will be saved there.
4️⃣	Chat/Help widget (available on every page)	Type the same question; CIA will generate the response in real time.
Once you locate the reply, you can copy it into your evidence log.

Quick reference you can use while you fetch the official answer
Below is a concise, CIA‑style summary of the typical trade‑offs between Common Table Expressions (CTEs) and subqueries. Feel free to compare it with the portal’s exact wording once you have it.

Aspect	CTE (WITH clause)	Subquery
Readability / Maintenance	✔️ Named result set makes complex logic easier to follow; can be reused in the same statement.	❌ Nested inside the main query; can become hard to read when deeply nested.
Reusability within a single statement	✔️ Can be referenced multiple times (unless the optimizer decides to materialize it).	❌ Must repeat the subquery each time you need it.
Recursive processing	✔️ Supports recursion (e.g., employee hierarchies, bill‑of‑materials).	✖️ Not possible.
Performance (general)	• Often same execution plan as an equivalent subquery because most modern engines (PostgreSQL, SQL Server, MySQL 8+, Snowflake) inline the CTE.
• May be slower if the optimizer materializes the CTE (e.g., in older versions of SQL Server or when the CTE is referenced many times).	• Usually inlined automatically, so no extra materialization overhead.
• Correlated subqueries can cause row‑by‑row execution, which can be expensive.
When to prefer	• Complex, multi‑step logic that benefits from naming each step.
• Need recursion.
• Want to write the query once and reuse the result within the same statement.	• Simple filtering or aggregation that fits naturally in a single SELECT.
• When you need a correlated subquery that depends on each outer row (e.g., “latest order per customer”).
Typical pitfalls	• Assuming a CTE is always materialized; on some engines it is, on others it isn’t, leading to unexpected memory usage.
• Over‑using CTEs can make the plan harder for the optimizer to see opportunities for push‑down predicates.	• Deeply nested subqueries can hide performance problems.
• Correlated subqueries may cause the engine to execute the inner query repeatedly (N+1 problem).
How to verify	Use the database’s EXPLAIN / Query Plan to see if the CTE is materialized or merged.	Same – check the plan for “Nested Loop” or “Hash Join” that indicates repeated execution.
Bottom line:

Start with a subquery if the logic is simple and you don’t need to reuse the result.
Switch to a CTE when the query becomes hard to read, you need recursion, or you must reference the intermediate result multiple times.
Always check the execution plan for your specific RDBMS; the optimizer ultimately decides the fastest path.