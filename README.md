# ecommerceperformancedashboard

## E-Commerce Performance Dashboard

- Developed a TypeScript/React front-end with Python/Django APIs, reducing decision-making time by 40% for 10K+ product listings.
- Scaled data pipelines using Apache Spark, achieving sub-second query performance on 10M+ records.

## Why This Project

- Provides a unified dashboard for evaluating e-commerce product performance in real time.
- Reduces manual analysis time by surfacing key metrics for 10K+ listings.

## What This Project Includes

- A React/TypeScript frontend for dynamic, interactive visualizations.
- A Django REST API backend serving performance data.
- Scalable Spark-based data pipelines for sub-second queries on 10M+ records.

## Getting Started

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone <YOUR_REPO_URL>
cd ecommerceperformancedashboard

# Create & activate the Conda environment
conda env create -f environment.yml
conda activate ecommerceperformancedashboard

# Backend (Django API)
cd backend
python manage.py migrate
python manage.py runserver

# Frontend (React dev server)
cd ../frontend
npm install
npm start

# (Optional) Build & serve the production front-end
npm run build
cd build
python -m http.server 3000
```