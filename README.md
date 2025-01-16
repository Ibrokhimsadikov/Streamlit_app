custom_css = """
.row {
    display: flex;
    align-items: center;
}
.box {
    height: 10px;
    width: 10px;
    border-radius: 2px;
    margin-right: 5px;
    padding: 0px 0 1px 0;
    text-align: center;
    color: white;
    font-size: 14px;
    cursor: pointer;
}
#legend {
    position: absolute;
    top: 0;
    right: 0;
    max-height: 200px; /* Restricts height */
    overflow-y: auto; /* Enables vertical scrolling */
    border: 1px solid #ccc; /* Adds a border */
    padding: 5px; /* Adds padding */
    background-color: white; /* Background color */
}
#title-container {
    max-width: 75%;
}
"""

custom_html = """
<div id="legend" class="container-box">
"""
for field, color in color_mapping.items():
    custom_html += f'    <div class="row"><div id="{field}" class="box" style="background-color:{color};"></div>{field}</div>\n'
custom_html += """
</div>
"""
