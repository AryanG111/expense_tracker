# 💰 Personal Finance Tracker

A beautiful, feature-rich web application built with Flask and SQLite to help you take control of your finances. Track income, expenses, set budgets, and achieve your savings goals with an intuitive dark-themed interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 📊 Dashboard
- **Real-time Financial Overview** - View your total income, expenses, and balance at a glance
- **Quick Transaction Entry** - Add income or expenses with a single form
- **Recent Activity Feed** - See your latest 10 transactions
- **Category Breakdown** - Visual representation of spending by category
- **Savings Goals Widget** - Track progress towards your financial goals

### 💳 Transaction Management
- **Complete Transaction History** - View all your financial transactions
- **Advanced Filtering** - Filter by type (income/expense), category, and date range
- **Easy Deletion** - Remove incorrect transactions with confirmation
- **Category Organization** - Automatically categorizes your spending
- **Search & Sort** - Find specific transactions quickly

### 💰 Budget Tracking
- **Monthly Budget Setting** - Set spending limits for different categories
- **Real-time Tracking** - See how much you've spent vs. your budget
- **Visual Progress Bars** - Color-coded indicators (green, yellow, red)
- **Budget Alerts** - Get warnings when approaching or exceeding limits
- **Multi-category Support** - Set budgets for unlimited categories

### 🎯 Savings Goals
- **Goal Creation** - Set specific financial targets with deadlines
- **Progress Tracking** - Visual progress bars showing completion percentage
- **Incremental Updates** - Add funds to your goals anytime
- **Goal Analytics** - See total savings, remaining amount, and completion rate
- **Deadline Management** - Optional deadlines to stay motivated

### 📈 Reports & Analytics
- **Monthly Trends** - 6-month historical view of income, expenses, and savings
- **Interactive Charts** - Line charts, pie charts, and bar graphs using Chart.js
- **Category Analysis** - See which categories consume most of your budget
- **Savings Rate** - Calculate and track your monthly savings percentage
- **Financial Insights** - AI-powered recommendations based on your spending

### 🎨 User Experience
- **Dark Theme** - Easy on the eyes with a modern aesthetic
- **Animated Background** - Dynamic floating gradient orbs
- **Glassmorphism UI** - Frosted glass effect on cards and panels
- **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- **Smooth Animations** - Hover effects, transitions, and micro-interactions
- **Custom Scrollbar** - Styled to match the dark theme

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/personal-finance-tracker.git
cd personal-finance-tracker
```

2. **Install required packages**
```bash
pip install flask
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
```
http://127.0.0.1:5000
```

## 📁 Project Structure

```
personal-finance-tracker/
│
├── app.py                      # Main Flask application
├── finance_tracker.db          # SQLite database (auto-created)
├── README.md                   # Project documentation
│
└── templates/                  # HTML templates
    ├── base.html              # Base template with navigation
    ├── index.html             # Dashboard
    ├── transactions.html      # Transaction management
    ├── budgets.html           # Budget tracking
    ├── savings.html           # Savings goals
    └── reports.html           # Analytics and reports
```

## 🗄️ Database Schema

### Transactions Table
- `id` - Primary key
- `type` - Income or Expense
- `category` - Transaction category
- `amount` - Transaction amount
- `description` - Optional notes
- `date` - Transaction date
- `created_at` - Record creation timestamp

### Budgets Table
- `id` - Primary key
- `category` - Budget category
- `amount` - Budget limit
- `month` - Month (YYYY-MM format)

### Savings Goals Table
- `id` - Primary key
- `name` - Goal name
- `target_amount` - Target amount
- `current_amount` - Current savings
- `deadline` - Optional deadline
- `created_at` - Goal creation date

## 💻 Technologies Used

- **Backend**: Flask (Python Web Framework)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js 4.4.0
- **Templating**: Jinja2

## 🎯 Use Cases

- **Personal Finance Management** - Track daily expenses and income
- **Budget Planning** - Set and monitor spending limits
- **Savings Tracking** - Work towards financial goals systematically
- **Expense Analysis** - Understand spending patterns
- **Financial Reporting** - Generate insights for better decisions

## 📸 Screenshots

### Dashboard
The main hub showing your financial overview with animated cards and real-time stats.

### Transaction History
Comprehensive list with powerful filtering options and color-coded badges.

### Budget Tracking
Visual progress indicators with warnings when approaching limits.

### Savings Goals
Track multiple goals with deadlines and incremental progress updates.

### Reports & Analytics
Interactive charts showing monthly trends and category breakdowns.

## 🛠️ Customization

### Changing Colors
Edit the CSS variables in `base.html`:
```css
/* Primary colors */
background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);

/* Income color */
color: #34d399;

/* Expense color */
color: #f87171;
```

### Adding Categories
Categories are dynamically created when you add transactions. No configuration needed!

### Database Configuration
To switch from SQLite to MySQL/PostgreSQL, modify the database connection in `app.py`:
```python
# Replace sqlite3 connection with your preferred database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="finance_tracker"
)
```

## 🔐 Security Considerations

For production deployment:
1. Change the `app.secret_key` in `app.py`
2. Add user authentication
3. Implement CSRF protection
4. Use environment variables for sensitive data
5. Enable HTTPS
6. Add input validation and sanitization

## 🚀 Deployment

### Heroku
```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Create requirements.txt
pip freeze > requirements.txt

# Deploy
git push heroku main
```

### PythonAnywhere
1. Upload your files
2. Create a new web app
3. Configure WSGI file
4. Reload web app

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Export data to CSV/PDF
- [ ] Recurring transactions
- [ ] Bill reminders and notifications
- [ ] Mobile app version
- [ ] Bank account integration
- [ ] Currency conversion support
- [ ] Tax calculation features
- [ ] Investment tracking
- [ ] AI-powered spending predictions

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Flask documentation and community
- Chart.js for beautiful visualizations
- Inspiration from modern fintech applications
- MCA curriculum for project guidance

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Email: your.email@example.com

---

⭐ If you found this project helpful, please consider giving it a star!

**Made with ❤️ for MCA Semester Project**
