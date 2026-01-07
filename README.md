# Cafe Sales Data Cleaning Project

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

## Output
The final cleaned dataset is saved as:

`cleaned_transaction.csv`

This dataset is consistent, validated, and ready for analysis.

## Tools Used
- Python
- Pandas
- Git and GitHub
- VS Code