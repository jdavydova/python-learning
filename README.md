# 📊 Python Inventory Automation with OpenPyXL

## 📌 Project Overview

This Python script reads an Excel inventory file, analyzes product data, calculates inventory values, and saves the updated results into a new Excel file.

The project is useful for learning how Python can automate work with Excel files using the `openpyxl` library.

---

## 🛠️ Technologies Used

- Python
- OpenPyXL
- Excel `.xlsx` files

---

## 📁 Project Files

```text
my-python-project/
├── main.py
├── inventory.xlsx
└── inventory_with_total_values.xlsx
```

---

## 📦 Install Dependencies

Install `openpyxl`:

```bash
pip install openpyxl
```

---

## 📄 Input File

The script uses this Excel file:

```text
inventory.xlsx
```

The worksheet name must be:

```text
Sheet1
```

Expected columns:

| Column | Description |
|------|-------------|
| 1 | Product number |
| 2 | Inventory quantity |
| 3 | Product price |
| 4 | Supplier name |
| 5 | Total inventory value |

---

## 🚀 What the Script Does

The script performs the following actions:

1. Opens the Excel inventory file
2. Reads product rows from the worksheet
3. Counts how many products each supplier has
4. Calculates the total inventory value for each supplier
5. Finds products with inventory quantity less than 10
6. Writes inventory value into column 5
7. Saves a new Excel file

---

## 🧠 Python Code

```python
import openpyxl

inv_file = openpyxl.load_workbook("inventory.xlsx")
product_list = inv_file["Sheet1"]

products_per_supplier = {}
total_value_per_supplier = {}
product_under_10_inv = {}

print(product_list.max_row)

for product_row in range(2, product_list.max_row + 1):
    supplier_name = product_list.cell(product_row, 4).value
    inventory = product_list.cell(product_row, 2).value
    price = product_list.cell(product_row, 3).value
    product_num = product_list.cell(product_row, 1).value
    inventory_price = product_list.cell(product_row, 5)

    print(supplier_name)

    # Calculate number of products per supplier
    if supplier_name in products_per_supplier:
        current_num_products = products_per_supplier[supplier_name]
        products_per_supplier[supplier_name] = current_num_products + 1
    else:
        print("adding a new supplier")
        products_per_supplier[supplier_name] = 1

    # Calculate total value of inventory per supplier
    if supplier_name in total_value_per_supplier:
        current_total_value = total_value_per_supplier[supplier_name]
        total_value_per_supplier[supplier_name] = current_total_value + inventory * price
    else:
        total_value_per_supplier[supplier_name] = inventory * price

    # Find products with inventory less than 10
    if inventory < 10:
        product_under_10_inv[product_num] = int(inventory)

    # Add total inventory price to column 5
    inventory_price.value = inventory * price

print(products_per_supplier)
print(total_value_per_supplier)
print(product_under_10_inv)

inv_file.save("inventory_with_total_values.xlsx")
```

---

## 📊 Output

The script prints:

### Products per supplier

```text
{
  "Supplier A": 3,
  "Supplier B": 5
}
```

### Total inventory value per supplier

```text
{
  "Supplier A": 2500,
  "Supplier B": 7300
}
```

### Products with inventory under 10

```text
{
  101: 5,
  203: 8
}
```

---

## 💾 Generated File

After running the script, a new Excel file is created:

```text
inventory_with_total_values.xlsx
```

This file includes calculated total inventory values in column 5.

---

## ▶️ How to Run

Run the script:

```bash
python main.py
```

Make sure `inventory.xlsx` is in the same folder as `main.py`.

---

## 🧠 Notes

- The loop starts from row 2 because row 1 usually contains headers.
- Dictionaries are used to store calculated values.
- `openpyxl` allows Python to read, modify, and save Excel files.

---

## ✅ Summary

This project demonstrates basic Python automation for Excel files:

- Reading Excel data
- Working with loops
- Using dictionaries
- Performing calculations
- Saving updated Excel files
