custom_css = """
.row {
    display: flex;
    align-items: center;
}
.box {
    height: 10px;
    width: 10px;
    border: 1px solid black; /* Black border for the box */
    background-color: white; /* White background */
    margin-right: 5px;
    padding: 0px;
    text-align: center;
    font-size: 14px;
    cursor: pointer;
}
#legend {
    position: absolute;
    top: 50%;
    right: 0;
    transform: translateY(-50%);
    max-height: 400px; /* Limit height for scrolling */
    overflow-y: auto; /* Enable scrolling for overflow */
    border: 1px solid #ccc; /* Optional: Add a border around the legend */
    background-color: #fff; /* Optional: Add a background color */
    padding: 10px; /* Optional: Add padding */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Optional: Add shadow */
}
#title-container {
    max-width: 75%;
}
"""





custom_html = """
<div id="legend" class="container-box">
"""
for field in color_mapping.keys():  # Only iterate through field names
    custom_html += f'    <div class="row"><div id="{field}" class="box"></div>{field}</div>\n'
custom_html += """
</div>
"""
