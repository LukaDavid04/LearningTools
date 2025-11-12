# Learning Tools 📚✨

![Repository banner showing abstract educational graphics](https://img.shields.io/badge/learning-lab-blueviolet?style=for-the-badge) ![Status badge](https://img.shields.io/badge/status-evolving-success?style=for-the-badge) ![License badge](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)

Welcome to **Learning Tools**, a curated collection of mini-projects, coding challenges, and study artefacts created while exploring software engineering, data science, and UI/UX concepts. This repository is designed as a living notebook—each folder captures a self-contained experiment or learning journey with clear entry points so you can explore, remix, and extend the work.

---

## 🌐 Table of Contents
- [Repository Highlights](#-repository-highlights)
- [Quick Start](#-quick-start)
- [Project Spotlights](#-project-spotlights)
  - [Interactive Front-End Builds](#interactive-front-end-builds)
  - [Algorithm Practice (LeetCode)](#algorithm-practice-leetcode)
  - [Data & Assessment Prep](#data--assessment-prep)
  - [Academic Assignments](#academic-assignments)
- [Suggested Study Paths](#-suggested-study-paths)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🗂️ Repository Highlights

| Area | Description | Tech & Topics |
| --- | --- | --- |
| `Brick Destroyer/` | A classic arcade-style browser game built with vanilla JavaScript and Parcel bundler. Experiment with game loops, collision detection, and asset management. | HTML, CSS, JS, Parcel |
| `Portfolio/` | A modern personal portfolio powered by Vite + React + Tailwind. Includes routing, manifest files, and deployment-ready configuration. | React, TypeScript, Tailwind, Vite |
| `LeetCode/` | Grab bag of algorithmic practice solutions in Python and Java. Perfect for studying data structures and interview patterns. | Arrays, stacks, sorting, graph tricks |
| `Data Science Assessment Prep/` | Utility scripts for crunching through practice problems and debugging tricky assessment prompts. | Python scripting |
| `Software Engineering Code Cracking Challenged/` | Cryptography puzzles and challenge solutions exploring security-minded programming. | Python, Crypto basics |
| `University Assignments/` | Coursework submissions organized by assignment, capturing academic explorations and prototypes. | Academic deliverables |

> 💡 **Tip:** Each directory is self-contained—open it in your editor to browse detailed READMEs, assets, and source code relevant to that topic.

---

## ⚡ Quick Start

### Clone the Repository
```bash
git clone https://github.com/<your-user>/LearningTools.git
cd LearningTools
```

### Install Dependencies for JavaScript Projects
Some front-end projects include a `package.json`. Install dependencies from the project folder:
```bash
cd "Brick Destroyer"
npm install
npm run start
```
Similarly, the `Portfolio/` project uses Vite:
```bash
cd Portfolio
npm install
npm run dev
```

### Run Python Utilities
Python-based folders contain standalone scripts. For example:
```bash
cd "Data Science Assessment Prep"
python prep.py
```

> ✅ **Requirements:** Node.js ≥ 18 and Python ≥ 3.10 are recommended to ensure compatibility across the projects.

---

## 🌟 Project Spotlights

### Interactive Front-End Builds
- **Brick Destroyer** – Recreate the nostalgic brick-breaking experience. Customize levels, tweak physics constants, or reskin the UI to sharpen DOM manipulation and animation skills.
- **Portfolio** – A polished personal site scaffold with Tailwind styling, manifest support, and SEO-ready metadata. Great for exploring modern front-end tooling.

### Algorithm Practice (LeetCode)
- Collection spans string manipulation, stack design (`frequencyStack.py`), scheduling (`scheduler.py`), and classical challenges like `RomanToInteger.java`.
- Solutions are grouped by problem, making it easy to compare approaches in Python vs. Java where available.

### Data & Assessment Prep
- `prep.py` and `bugPrep.py` encapsulate exploratory scripts for data science interview prep. They’re intentionally lightweight—ideal for experimentation or porting into notebooks.

### Academic Assignments
- Directories such as `Assignment 1/` and `Assignment 2 SEG4105/` capture university coursework, including design docs, prototypes, and reference implementations. Use them as inspiration for structuring your own submissions.

---

## 🧭 Suggested Study Paths

Choose a track depending on what you’d like to practice:

1. **Game Dev & UI Polish** – Start with `Brick Destroyer/` to understand canvas animations, then refactor styles using Tailwind components from `Portfolio/`.
2. **Interview Drills** – Work through Python solutions in `LeetCode/`. Implement the same logic in another language to solidify the concepts.
3. **Data Science Sprint** – Explore the scripts under `Data Science Assessment Prep/` and extend them into Jupyter notebooks for deeper analysis.
4. **Security Curiosity** – Dive into the cryptography exercises inside `Software Engineering Code Cracking Challenged/` to sharpen your reverse-engineering instincts.

---

## 🤝 Contributing

This repository doubles as a personal learning playground, but contributions that improve clarity, fix bugs, or add new study notes are always welcome!

1. Fork the repo and create a topic branch.
2. Make your changes with clear commit messages.
3. Run relevant project commands (tests, linters) in the subdirectories you touched.
4. Open a pull request describing the motivation and key changes.

Feel free to file issues if you spot typos, outdated dependencies, or have ideas for new learning modules.

---

## 📄 License

Distributed under the **MIT License**. See the [LICENSE](LICENSE) file (or project-specific licenses) for more information.

Happy learning! 🎓
