import pandas as pd

# Load CSV
df = pd.read_csv("../../ML/yq_task/notebooks/hyper_params.csv")

# Convert DataFrame to HTML
html_table = df.to_html(
    index=False,
    classes="table table-striped table-hover",
    border=0
)

# Wrap the table in a scrollable div
html_page = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Scrollable CSV Table</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
    <style>
        body {{
            background-color: #f8f9fa;
            padding: 40px;
        }}
        .table-container {{
            max-height: 80vh;   /* vertical scroll */
            overflow-y: auto;
            overflow-x: auto;   /* horizontal scroll */
            border: 1px solid #dee2e6;
            background: white;
        }}
        table {{
            font-size: 0.9rem;
            white-space: nowrap;  /* prevents wrapping long text */
        }}
    </style>
</head>
<body>
    <div class="container">
        <h2 class="mb-4">Hyper-parameters vs Results</h2>
        <div class="table-container">
            {html_table}
        </div>
    </div>
</body>
</html>
"""

# Save HTML
with open("hyper_params_update.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("✅ Scrollable HTML table generated successfully.")
