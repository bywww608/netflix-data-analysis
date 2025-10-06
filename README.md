# Data Analysis Project Template / 数据分析项目模板

This repository is a **ready-to-use template** for data analysis projects.  
It includes a recommended folder structure, example scripts for cleaning and visualization, a minimal Jupyter notebook, and instructions to run everything on Windows + VS Code.

这个仓库是一个**数据分析项目模板**，包含推荐的文件结构、示例清洗/可视化脚本、一个最小的 Jupyter Notebook，以及在 Windows + VS Code 上运行的说明。

---

## Repository structure / 仓库结构
```
data-analysis-project-template/
├── data/
│   ├── raw/        # Put raw/original data here (do NOT commit sensitive/private data)
│   └── cleaned/    # Cleaned data outputs (gitignored by default)
├── notebooks/
│   └── example_analysis.ipynb
├── scripts/
│   ├── data_cleaning.py
│   └── visualization.py
├── charts/         # generated charts (gitignored)
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Quick start (Windows + VS Code)
1. Clone or download this repo.  
2. Open the folder in VS Code (`File -> Open Folder`).  
3. Open a terminal in VS Code (`View -> Terminal`) and run:
```powershell
python -m venv venv
# If using PowerShell:
.env\Scripts\Activate
# If activation fails, run (temporary scope):
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
pip install -r requirements.txt
jupyter lab   # or: jupyter notebook
```
4. Place your raw CSV files into `data/raw/`.  
5. Use the included cleaning script:
```powershell
python scripts/data_cleaning.py --input data/raw/your_file.csv --output data/cleaned/your_file_cleaned.csv
```
6. Open `notebooks/example_analysis.ipynb` and follow the cells to do EDA and plotting.

---

## How to push to GitHub
```bash
git init
git add .
git commit -m "Initial: data analysis project template"
git branch -M main
# create repo on GitHub website, then:
git remote add origin https://github.com/YOURUSERNAME/data-analysis-project-template.git
git push -u origin main
```
> If `git push` asks for credentials: use your GitHub username and a Personal Access Token (PAT) as password, or sign in via VS Code's GitHub integration.

---

## Notes / 注意事项
- Keep **raw** data out of public repos if it contains private or sensitive information.  
- This template is designed for quick starts: replace `example_analysis.ipynb` with your own notebooks for each project.

---

## Author
Yiwen Bai (Curtin University Singapore) — project template generated for Data Analyst portfolio work.
