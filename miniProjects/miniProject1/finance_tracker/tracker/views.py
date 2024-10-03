# tracker/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Income, Expense, Budget
from .forms import IncomeForm, ExpenseForm, BudgetForm
from django.contrib.auth.decorators import login_required

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'tracker/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'tracker/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    income = Income.objects.filter(user=request.user)
    expenses = Expense.objects.filter(user=request.user)
    budget = Budget.objects.filter(user=request.user)
    total_income = sum(i.amount for i in income)
    total_expense = sum(e.amount for e in expenses)
    context = {
        'income': income,
        'expenses': expenses,
        'budget': budget,
        'total_income': total_income,
        'total_expense': total_expense,
    }
    return render(request, 'tracker/dashboard.html', context)

# Add income, expense, and budget views remain the same

# View to add income
@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user  # Assign the logged-in user to the income entry
            income.save()
            return redirect('dashboard')  # Redirect to dashboard after adding income
    else:
        form = IncomeForm()

    return render(request, 'tracker/add_income.html', {'form': form})

# View to add expenses
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Assign the logged-in user to the expense entry
            expense.save()
            return redirect('dashboard')  # Redirect to dashboard after adding expense
    else:
        form = ExpenseForm()

    return render(request, 'tracker/add_expense.html', {'form': form})

# View to add a budget
@login_required
def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user  # Assign the logged-in user to the budget entry
            budget.save()
            return redirect('dashboard')  # Redirect to dashboard after adding budget
    else:
        form = BudgetForm()

    return render(request, 'tracker/add_budget.html', {'form': form})
