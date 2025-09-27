# scheduling-ethos

This project generates a schedule for a **2 vs 2 competitive programming contest** from a list of participants.  
It takes an Excel file with participant names and produces another Excel file with scheduled time slots.

---

## How to Use

1. **Prepare an Excel file** called `participants.xlsx` with one column of participant names.  

   Example:

   | Name    |
   |---------|
   | Alice   |
   | Bob     |
   | Charlie |
   | David   |
   | Eve     |
   | Frank   |
   | Grace   |
   | Helen   |

2. **Run the script** (make sure you have Python and the required libraries installed: `pandas`, `openpyxl`).

   ```bash
   python schedule.py

