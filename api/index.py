from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime, timedelta
import os

# IMPORTANT: Templates folder is one level up from api/
app = Flask(__name__, template_folder='../templates')
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-this')

# In-memory storage (resets on each deployment)
# For persistent storage, you'd need to add a database
class DataStore:
    def __init__(self):
        self.transactions = []
        self.budgets = []
        self.savings_goals = []
        self.transaction_id = 1
        self.goal_id = 1
    
    def add_transaction(self, data):
        data['id'] = self.transaction_id
        self.transaction_id += 1
        self.transactions.append(data)
        return data
    
    def add_goal(self, data):
        data['id'] = self.goal_id
        self.goal_id += 1
        self.savings_goals.append(data)
        return data

# Global data store
db = DataStore()

@app.route('/')
def index():
    current_month = datetime.now().strftime('%Y-%m')
    
    # Calculate totals
    total_income = sum(t['amount'] for t in db.transactions if t['type'] == 'income')
    total_expenses = sum(t['amount'] for t in db.transactions if t['type'] == 'expense')
    balance = total_income - total_expenses
    
    # Get recent transactions
    recent_transactions = sorted(db.transactions, key=lambda x: x['date'], reverse=True)[:10]
    
    # Calculate expense by category
    expense_by_category = {}
    for t in db.transactions:
        if t['type'] == 'expense':
            cat = t['category']
            expense_by_category[cat] = expense_by_category.get(cat, 0) + t['amount']
    
    expense_list = [{'category': k, 'total': v} for k, v in expense_by_category.items()]
    
    return render_template('index.html',
                         total_income=total_income,
                         total_expenses=total_expenses,
                         balance=balance,
                         recent_transactions=recent_transactions,
                         expense_by_category=expense_list,
                         savings_goals=db.savings_goals)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    transaction = {
        'type': request.form['type'],
        'category': request.form['category'],
        'amount': float(request.form['amount']),
        'description': request.form.get('description', ''),
        'date': request.form['date']
    }
    db.add_transaction(transaction)
    return redirect(url_for('index'))

@app.route('/transactions')
def transactions():
    filter_type = request.args.get('type', 'all')
    filter_category = request.args.get('category', 'all')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    
    # Apply filters
    filtered = db.transactions
    if filter_type != 'all':
        filtered = [t for t in filtered if t['type'] == filter_type]
    if filter_category != 'all':
        filtered = [t for t in filtered if t['category'] == filter_category]
    if start_date:
        filtered = [t for t in filtered if t['date'] >= start_date]
    if end_date:
        filtered = [t for t in filtered if t['date'] <= end_date]
    
    # Get unique categories
    categories = list(set([{'category': t['category']} for t in db.transactions]))
    
    filtered = sorted(filtered, key=lambda x: x['date'], reverse=True)
    
    return render_template('transactions.html',
                         transactions=filtered,
                         categories=categories,
                         filter_type=filter_type,
                         filter_category=filter_category,
                         start_date=start_date,
                         end_date=end_date)

@app.route('/delete_transaction/<int:id>')
def delete_transaction(id):
    db.transactions = [t for t in db.transactions if t['id'] != id]
    return redirect(url_for('transactions'))

@app.route('/budgets')
def budgets():
    current_month = datetime.now().strftime('%Y-%m')
    
    # Calculate spending by category
    spending = {}
    for t in db.transactions:
        if t['type'] == 'expense' and t['date'].startswith(current_month):
            cat = t['category']
            spending[cat] = spending.get(cat, 0) + t['amount']
    
    # Create budget data
    budget_data = []
    for budget in db.budgets:
        if budget['month'] == current_month:
            spent = spending.get(budget['category'], 0)
            budget_data.append({
                'id': budget['id'],
                'category': budget['category'],
                'budget': budget['amount'],
                'spent': spent,
                'remaining': budget['amount'] - spent,
                'percentage': (spent / budget['amount'] * 100) if budget['amount'] > 0 else 0
            })
    
    return render_template('budgets.html',
                         budgets=budget_data,
                         current_month=current_month)

@app.route('/add_budget', methods=['POST'])
def add_budget():
    category = request.form['category']
    amount = float(request.form['amount'])
    month = request.form.get('month', datetime.now().strftime('%Y-%m'))
    
    # Check if exists
    existing = next((b for b in db.budgets if b['category'] == category and b['month'] == month), None)
    
    if existing:
        existing['amount'] = amount
    else:
        db.budgets.append({
            'id': len(db.budgets) + 1,
            'category': category,
            'amount': amount,
            'month': month
        })
    
    return redirect(url_for('budgets'))

@app.route('/savings')
def savings():
    goals = sorted(db.savings_goals, key=lambda x: x.get('deadline', '9999-12-31'))
    return render_template('savings.html', goals=goals)

@app.route('/add_savings_goal', methods=['POST'])
def add_savings_goal():
    goal = {
        'name': request.form['name'],
        'target_amount': float(request.form['target_amount']),
        'current_amount': float(request.form.get('current_amount', 0)),
        'deadline': request.form.get('deadline', '')
    }
    db.add_goal(goal)
    return redirect(url_for('savings'))

@app.route('/update_savings/<int:id>', methods=['POST'])
def update_savings(id):
    amount = float(request.form['amount'])
    goal = next((g for g in db.savings_goals if g['id'] == id), None)
    if goal:
        goal['current_amount'] += amount
    return redirect(url_for('savings'))

@app.route('/delete_savings/<int:id>')
def delete_savings(id):
    db.savings_goals = [g for g in db.savings_goals if g['id'] != id]
    return redirect(url_for('savings'))

@app.route('/reports')
def reports():
    # Calculate monthly data (last 6 months)
    monthly_data = []
    for i in range(5, -1, -1):
        month = (datetime.now() - timedelta(days=30*i)).strftime('%Y-%m')
        income = sum(t['amount'] for t in db.transactions if t['type'] == 'income' and t['date'].startswith(month))
        expense = sum(t['amount'] for t in db.transactions if t['type'] == 'expense' and t['date'].startswith(month))
        monthly_data.append({
            'month': month,
            'income': income,
            'expense': expense,
            'savings': income - expense
        })
    
    # Category spending (current month)
    current_month = datetime.now().strftime('%Y-%m')
    category_spending = {}
    for t in db.transactions:
        if t['type'] == 'expense' and t['date'].startswith(current_month):
            cat = t['category']
            category_spending[cat] = category_spending.get(cat, 0) + t['amount']
    
    spending_list = sorted([{'category': k, 'total': v} for k, v in category_spending.items()], 
                          key=lambda x: x['total'], reverse=True)
    
    return render_template('reports.html',
                         monthly_data=monthly_data,
                         category_spending=spending_list)

# Vercel will call this
app.debug = False

# For local testing
if __name__ == '__main__':
    app.run(debug=True, port=5000)