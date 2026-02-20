# Cafe Sales Data Cleaning 

## Overview
This project focuses on cleaning and validating a raw cafe sales dataset to make it reliable for analysis and reporting.
The raw data contains missing values, inconsistent formats, invalid quantities, incorrect totals, and non-standard labels.

The goal is to apply clear business rules, enforce data integrity, and produce a clean dataset ready for downstream analysis.

## Dataset
- **Input:** `dirty_cafe_sales.csv`
- **Output:** `cleaned_transaction.csv`

## Cleaning & Validation Steps

### 1. Column Name Normalization
- Removed leading and trailing spaces from column names to ensure consistency.

### 2. Quantity Cleaning
**Business rule:** Quantity must be a positive whole number for billing calculations.
- Converted values to numeric.
- Removed invalid, missing, zero, and negative quantities.

### 3. Price Per Unit Cleaning
**Business rule:** Price per unit must be a positive numeric value.
- Converted values to numeric.
- Removed invalid and non-positive prices.

### 4. Transaction Date Normalization
**Business rule:** Transaction date must be valid and cannot be in the future.
- Parsed dates using `pd.to_datetime`.
- Removed invalid and future-dated transactions.

### 5. Transaction ID Validation
**Business rule:** Transaction ID must be present and unique.
- Standardized formatting.
- Removed invalid placeholders.
- Ensured uniqueness.

### 6. Total Spent Recalculation
**Business rule:** Total spent must equal `Quantity × Price Per Unit`.
- Recomputed total spent instead of trusting raw values.
- Ensured consistency across all transactions.

### 7. Payment Method Standardization
- Normalized text formatting.
- Mapped equivalent labels such as CREDIT CARD and DEBIT CARD to CARD.

### 8. Location Normalization
- Cleaned and standardized location names.
- Removed invalid placeholders.

### 9. Item Cleaning
- Standardized item names.
- Removed missing or invalid items.

### 10. Potential Duplicates Identification
**Business rule:** The dataset does not provide a guaranteed unique transaction
  identifier that can conclusively distinguish individual customer purchases.

**Approach** Rather than removing records and risking loss of valid transactions, 
  potential duplicates are *flagged* based on shared transactional attributes:
  - Transaction Date
  - Item
  - Location
  - Quantity
  - Price Per Unit
A boolen column `is_potential_duplicate` is added to indicate records that share indentical values across these attributes.

**Rationale:** Muliple customers may legitimately purchase the same item in the same quantity,
location and time window. Flagging preserves data intergity while allowing analysts to make
context-aware decisions during dowmstream analysis.


## Output
The final cleaned dataset is saved as
`cleaned_transaction.csv`


This dataset is consistent, validated, and ready for analysis.

## Tools Used
- Python
- Pandas
- Git and GitHub
- VS Code

## Assumptions & Limitations:
- Invalid rows are removed rather than logged for simplicity.
- The data set does not contain a guaranteed unique transaction key for definitive
  duplicate detection.
- Potential duplicates are indentified based on shared transactional attributes and flagged
  instead of removed.
- Flagged duplicates may represent either genuine repeat purchase or data duplication.
- Business rules are hard coded for this dataset and would be externalized
  in production pipeline.
- The pipeline prioritizes clean analytical output over audit level traceability
  for this project's scope.
