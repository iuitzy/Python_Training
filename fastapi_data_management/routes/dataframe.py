from fastapi import APIRouter
import pandas as pd
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/dataframe", tags=["dataframe"])

@router.get("/", response_class=HTMLResponse)
def get_dataframe():
    df = pd.read_csv("data.csv")

    table_rows = "".join(
        f"""
        <tr>
            <td>{row['product']}</td>
            <td class="price">{row['price']}</td>
            <td class="quantity">{row['quantity']}</td>
            <td>
                <button onclick="modifyQuantity({i}, 1)">+</button>
                <button onclick="modifyQuantity({i}, -1)">-</button>
            </td>
        </tr>
        """
        for i, row in df.iterrows()
    )

    return f"""
    <html>
    <head>
        <script>
            function updateTotal() {{
                let total = 0;
                document.querySelectorAll('.price').forEach((priceCell, i) => {{
                    let price = parseFloat(priceCell.innerText);
                    let quantity = parseInt(document.querySelectorAll('.quantity')[i].innerText);
                    total += price * quantity;
                }});
                document.getElementById("total").innerText = "Total: $" + total;
            }}

            function modifyQuantity(index, change) {{
                let quantityCell = document.querySelectorAll('.quantity')[index];
                let current = parseInt(quantityCell.innerText);
                if (current + change >= 0) {{
                    quantityCell.innerText = current + change;
                    updateTotal();
                }}
            }}
        </script>
    </head>
    <body>
        <h2>Product List</h2>
        <table border="1">
            <tr><th>Product</th><th>Price</th><th>Quantity</th><th>Actions</th></tr>
            {table_rows}
        </table>
        <h3 id="total">Total: $0</h3>
        <script>updateTotal();</script>
    </body>
    </html>
    """


# from fastapi import APIRouter
# import pandas as pd
# from fastapi.responses import HTMLResponse

# router = APIRouter(prefix="/dataframe", tags=["dataframe"])

# # @router.get("/")
# # def get_dataframe():
# #     df = pd.read_csv("data.csv") 
# #     return df.to_dict(orient="records")

# @router.get("/", response_class=HTMLResponse)
# def get_dataframe():
#     df = pd.read_csv("data.csv")
#     return df.to_html(index=False)

# from fastapi import APIRouter
# import pandas as pd
# from fastapi.responses import HTMLResponse

# router = APIRouter(prefix="/dataframe", tags=["dataframe"])

# @router.get("/", response_class=HTMLResponse)
# def get_dataframe():
#     df = pd.read_csv("data.csv")
    
#     # Generate HTML table with interactive elements
#     table_html = """
#     <html>
#     <head>
#         <script>
#             function updateTotal() {
#                 let total = 0;
#                 document.querySelectorAll('.price').forEach((priceCell, index) => {
#                     let price = parseFloat(priceCell.innerText);
#                     let quantity = parseInt(document.querySelectorAll('.quantity')[index].innerText);
#                     total += price * quantity;
#                 });
#                 document.getElementById("total").innerText = "Total: $" + total;
#             }

#             function modifyQuantity(index, change) {
#                 let quantityCells = document.querySelectorAll('.quantity');
#                 let current = parseInt(quantityCells[index].innerText);
#                 if (current + change >= 0) {
#                     quantityCells[index].innerText = current + change;
#                     updateTotal();
#                 }
#             }
#         </script>
#     </head>
#     <body>
#         <h2>Product List</h2>
#         <table border="1">
#             <tr><th>Product</th><th>Price</th><th>Quantity</th><th>Actions</th></tr>"""
    
#     for index, row in df.iterrows():
#         table_html += f"""
#             <tr>
#                 <td>{row['product']}</td>
#                 <td class="price">{row['price']}</td>
#                 <td class="quantity">{row['quantity']}</td>
#                 <td>
#                     <button onclick="modifyQuantity({index}, 1)">+</button>
#                     <button onclick="modifyQuantity({index}, -1)">-</button>
#                 </td>
#             </tr>"""
    
#     table_html += """
#         </table>
#         <h3 id="total">Total: $0</h3>
#         <script>updateTotal();</script>
#     </body>
#     </html>
#     """
    
#     return table_html