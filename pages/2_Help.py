from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: sans-serif; line-height: 1.6; max-width: 900px; margin: auto; padding: 20px; color: #333; }
        header { border-bottom: 3px solid #003366; padding-bottom: 10px; margin-bottom: 20px; }
        nav { display: flex; gap: 10px; margin-bottom: 30px; flex-wrap: wrap; }
        button { padding: 10px 15px; border: 1px solid #ccc; cursor: pointer; border-radius: 4px; background: #f0f0f0; }
        .active { background: #003366; color: white; }
        h2 { color: #003366; }
        h3 { color: #d35400; border-bottom: 1px solid #ddd; margin-top: 30px; }
        h4 { color: #555; margin-bottom: 5px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { border: 1px solid #ddd; padding: 12px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <header>
        <h1>TxDOT - Proactive Construction Work Item Identifier (Pro-CWII)</h1>
    </header>

    <nav>
        <button>Home</button>
        <button class="active">Help</button>
        <button>Sample</button>
        <button>Find Similar Projects</button>
        <button>Identify Missing Items</button>
        <button>Verify Major Quantities</button>
    </nav>

    <h2>Welcome to the Help Page</h2>
    <p>Welcome to the Pro-CWII Help Center! This page provides comprehensive guidance on using the tool effectively. Whether you're a first-time user or need a quick refresher, you'll find all the information you need here.</p>

    <h3>📘 User Manual</h3>
    <p>Our comprehensive user manual contains detailed information about:</p>
    <ul>
        <li>Tool features and capabilities</li>
        <li>Step-by-step usage instructions</li>
        <li>Best practices for data preparation</li>
        <li>Understanding and interpreting results</li>
        <li>Troubleshooting common issues</li>
    </ul>

    <h3>🚀 Quick Start Guide</h3>
    <h4>Step 1: Prepare Your Data</h4>
    <ul>
        <li>Download the sample template to understand the required format</li>
        <li>Ensure your Excel file contains these columns: ItemCode (8-digit TxDOT item code), Quantity (numeric), UnitPrice (numeric)</li>
        <li>Save your file in standard Excel format (.xlsx)</li>
    </ul>
    <h4>Step 2: Choose Your Analysis</h4>
    <ul>
        <li>Find Similar Projects</li>
        <li>Identify Missing Work Items</li>
        <li>Verify Quantities for Major Pay Items</li>
    </ul>
    <h4>Step 3: Get Results</h4>
    <ul>
        <li>Upload your prepared Excel file</li>
        <li>Review the analysis results</li>
        <li>Download the detailed report or receive results via email</li>
    </ul>

    <h3>🔧 Common Issues and Solutions</h3>
    <table>
        <tr><th>Category</th><th>Problem</th><th>Solution</th></tr>
        <tr><td>File Upload</td><td>"Invalid file format"</td><td>Ensure your file is saved as .xlsx</td></tr>
        <tr><td>File Upload</td><td>"Incorrect column format"</td><td>Verify columns: ItemCode, Quantity, UnitPrice</td></tr>
        <tr><td>Analysis</td><td>No similar projects found</td><td>Try adjusting the district or project type filters</td></tr>
        <tr><td>Email</td><td>Results not received</td><td>Check spam folder and verify email address</td></tr>
    </table>

    <h3>💡 Best Practices</h3>
    <ul>
        <li><strong>Data Preparation:</strong> Remove formatting/formulas; ensure all item codes are numeric and correct.</li>
        <li><strong>Analysis Tips:</strong> Start with a broad search; prioritize items with high probability of being missed.</li>
    </ul>

    <h3>📞 Need More Help?</h3>
    <p>If you're still experiencing issues, review the user manual or email us at <a href="mailto:txdottamu@gmail.com">txdottamu@gmail.com</a>.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
