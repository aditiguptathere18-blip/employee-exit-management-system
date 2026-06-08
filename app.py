from flask import Flask, render_template, request, redirect, url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = "secret123"

import os

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:jessie32@localhost/employee_exit_management"
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class EmployeeForm(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    # SECTION 1

    employee_name = db.Column(db.String(100))
    employee_id = db.Column(db.String(50))
    department = db.Column(db.String(100))
    joining_date = db.Column(db.String(50))
    duration = db.Column(db.String(50))
    reporting_manager = db.Column(db.String(100))
    contact_number = db.Column(db.String(20))
    personal_email = db.Column(db.String(100))
    communication_address = db.Column(db.Text)

    # SECTION 2

    reason = db.Column(db.String(200))
    other_reason = db.Column(db.Text)
    resignation_submitted_by = db.Column(db.String(100))
    notice_period = db.Column(db.String(100))

    # SECTION 3

    work_environment = db.Column(db.String(10))
    team_cooperation = db.Column(db.String(10))
    learning = db.Column(db.String(10))
    career = db.Column(db.String(10))
    manager_support = db.Column(db.String(10))
    communication = db.Column(db.String(10))
    recognition = db.Column(db.String(10))
    compensation = db.Column(db.String(10))
    work_life = db.Column(db.String(10))
    overall = db.Column(db.String(10))

    positives = db.Column(db.Text)
    concerns = db.Column(db.Text)
    challenges = db.Column(db.Text)

    # SECTION 4

    manager_rating = db.Column(db.String(10))
    leadership_rating = db.Column(db.String(10))
    feedback_taken = db.Column(db.String(50))
    evaluation_fair = db.Column(db.String(50))
    managerial_concerns = db.Column(db.Text)

    # SECTION 5

    improvements = db.Column(db.Text)
    additional_suggestions = db.Column(db.Text)

    rejoin_organization = db.Column(db.String(20))
    recommend_organization = db.Column(db.String(20))
    resignation_process = db.Column(db.String(20))

    final_comments = db.Column(db.Text)
    manager_reviewed = db.Column(db.Boolean, default=False)

    pwe_reviewed = db.Column(db.Boolean, default=False)

    top_reviewed = db.Column(db.Boolean, default=False)

class ManagerForm(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    employee_name = db.Column(db.String(100))
    employee_id = db.Column(db.String(50))
    department = db.Column(db.String(100))
    joining_date = db.Column(db.String(50))
    resignation_date = db.Column(db.String(50))

    primary_reason = db.Column(db.String(100))
    other_reason = db.Column(db.Text)
    retention_attempt = db.Column(db.String(10))
    retention_outcome = db.Column(db.String(100))

    overall_performance = db.Column(db.String(50))

    technical_knowledge = db.Column(db.String(50))
    accuracy_work = db.Column(db.String(50))
    productivity = db.Column(db.String(50))
    communication_skills = db.Column(db.String(50))
    team_collaboration = db.Column(db.String(50))
    learning_ability = db.Column(db.String(50))
    ownership = db.Column(db.String(50))
    client_handling = db.Column(db.String(50))
    adaptability = db.Column(db.String(50))
    process_compliance = db.Column(db.String(50))

    strengths = db.Column(db.Text)
    other_strength = db.Column(db.Text)

    improvements = db.Column(db.Text)
    other_improvement = db.Column(db.Text)

    behaviour = db.Column(db.String(50))
    attendance = db.Column(db.String(50))
    insurance_knowledge = db.Column(db.String(50))

    handover_status = db.Column(db.String(50))
    knowledge_transfer = db.Column(db.String(50))
    pending_task = db.Column(db.String(50))
    replacement_urgency = db.Column(db.String(100))

    continue_org = db.Column(db.String(10))
    improve_performance = db.Column(db.String(10))
    self_improvement = db.Column(db.String(10))
    feedback_discussion = db.Column(db.String(10))
    retention_feasible = db.Column(db.String(10))

    rehire = db.Column(db.String(20))

    future_roles = db.Column(db.Text)

    overall_remarks = db.Column(db.Text)
    pwe_reviewed = db.Column(db.Boolean, default=False)

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(100), unique=True, nullable=False)

    password = db.Column(db.String(100), nullable=False)

    role = db.Column(db.String(50), nullable=False)

class PWEForm(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    employee_name = db.Column(db.String(100))
    employee_id = db.Column(db.String(50))
    department = db.Column(db.String(100))
    joining_date = db.Column(db.String(50))
    last_working_day = db.Column(db.String(50))
    reporting_manager = db.Column(db.String(100))
    contact_number = db.Column(db.String(20))
    personal_email = db.Column(db.String(100))
    communication_address = db.Column(db.Text)

    exit_discussion_date = db.Column(db.String(50))
    separation_reason = db.Column(db.String(100))
    other_reason = db.Column(db.Text)
    notice_period_served = db.Column(db.String(100))

    recovery_applicable = db.Column(db.String(20))
    recovery_type = db.Column(db.Text)
    recovery_remarks = db.Column(db.Text)

    assets_returned = db.Column(db.Text)
    asset_return_status = db.Column(db.String(50))

    access_deactivation = db.Column(db.Text)
    access_closure_status = db.Column(db.String(50))

    pending_dues = db.Column(db.Text)

    fnf_initiated = db.Column(db.String(50))
    fnf_status = db.Column(db.String(50))

    exit_documents = db.Column(db.Text)
    documentation_status = db.Column(db.String(50))

    rehire_eligibility = db.Column(db.String(50))
    rehire_reason = db.Column(db.Text)

    genuine_resignation = db.Column(db.String(10))
    emotional_decision = db.Column(db.String(10))
    better_opportunity = db.Column(db.String(10))
    performance_concern = db.Column(db.String(10))
    managerial_conflict = db.Column(db.String(10))
    retention_possible = db.Column(db.String(10))
    strong_performer = db.Column(db.String(10))
    attendance_concern = db.Column(db.String(10))
    behavioral_concern = db.Column(db.String(10))
    communication_gap = db.Column(db.String(10))
    policy_violation = db.Column(db.String(10))

    hr_recommendation = db.Column(db.String(200))

    final_hr_remarks = db.Column(db.Text)

class FinalReview(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    employee_name = db.Column(db.String(100))

    employee_id = db.Column(db.String(50))

    department = db.Column(db.String(100))

    manager_recommendation = db.Column(db.String(100))

    hr_recommendation = db.Column(db.String(100))

    final_status = db.Column(db.String(50))

    top_management_remarks = db.Column(db.Text)        

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(
        email=email,
        password=password
    ).first()

    if user:

        session['user_id'] = user.id
        session['role'] = user.role

        if user.role == 'employee':
            return redirect(url_for('employee_form'))

        elif user.role == 'manager':
            return redirect(url_for('manager_dashboard'))

        elif user.role == 'pwe':
            return redirect(url_for('pwe_dashboard'))
        
        elif user.role == 'top_management':
           return redirect(url_for('top_management_dashboard'))

    return "Invalid Email or Password"

@app.route('/employee-form')
def employee_form():

    if session.get('role') != 'employee':
        return redirect(url_for('login'))

    return render_template('employee_form.html')

@app.route('/manager-form')
def manager_form():

    if session.get('role') != 'manager':
        return redirect(url_for('login'))

    return render_template('manager_form.html')

@app.route('/pwe-form')
def pwe_form():

    if session.get('role') != 'pwe':
        return redirect(url_for('login'))

    return render_template('pwe_form.html')

@app.route('/manager-dashboard')
def manager_dashboard():

    employees = EmployeeForm.query.order_by(
    EmployeeForm.id.desc()
    ).all()
    employee_reviews = {}

    for employee in employees:

        employee_reviews[employee.employee_id] = (
            employee.manager_reviewed
        )

    return render_template(
        'manager_dashboard.html',
        employees=employees,
        employee_reviews=employee_reviews
    )

@app.route('/review-employee/<int:id>')
def review_employee(id):

    employee = EmployeeForm.query.get_or_404(id)

    return render_template(
        'manager_form.html',
        employee=employee
    )

@app.route('/view-employee-form/<int:id>')
def view_employee_form(id):

    employee = EmployeeForm.query.get_or_404(id)

    return render_template(
        'view_employee_form.html',
        employee=employee
    )

@app.route('/pwe-dashboard')
def pwe_dashboard():

    managers = ManagerForm.query.order_by(
    ManagerForm.id.desc()
    ).all()

    employee_reviews = {}

    employee_ids = {}

    for manager in managers:

        employee = EmployeeForm.query.filter_by(
            employee_id=manager.employee_id
        ).first()

        if employee:
            employee_reviews[manager.employee_id] = employee.pwe_reviewed
            employee_ids[manager.employee_id] = employee.id

    return render_template(
        'pwe_dashboard.html',
        managers=managers,
        employee_reviews=employee_reviews,
        employee_ids=employee_ids
    )

@app.route('/review-manager/<int:id>')
def review_manager(id):

    manager = ManagerForm.query.get_or_404(id)

    return render_template(
        'pwe_form.html',
        manager=manager
    )

@app.route('/view-manager-form/<int:id>')
def view_manager_form(id):

    manager = ManagerForm.query.get_or_404(id)

    return render_template(
        'view_manager_form.html',
        manager=manager
    )

@app.route('/top-management-dashboard')
def top_management_dashboard():

    pwe_forms = PWEForm.query.order_by(
    PWEForm.id.desc()
    ).all()
    employee_reviews = {}

    employee_ids = {}

    manager_ids = {}

    for pwe in pwe_forms:

        employee = EmployeeForm.query.filter_by(
            employee_id=pwe.employee_id
        ).first()

        manager = ManagerForm.query.filter_by(
            employee_id=pwe.employee_id
        ).first()

        if employee:
            employee_reviews[pwe.employee_id] = employee.top_reviewed
            employee_ids[pwe.employee_id] = employee.id

        if manager:
            manager_ids[pwe.employee_id] = manager.id

    return render_template(
        'top_management_dashboard.html',
        pwe_forms=pwe_forms,
        employee_reviews=employee_reviews,
        employee_ids=employee_ids,
        manager_ids=manager_ids
    )

@app.route('/final-review/<int:id>')
def final_review(id):

    pwe = PWEForm.query.get_or_404(id)

    return render_template(
        'final_review.html',
        pwe=pwe
    )

@app.route('/final-reports')
def final_reports():

    reports = FinalReview.query.all()

    return render_template(
        'final_reports.html',
        reports=reports
    )

@app.route('/view-pwe-form/<int:id>')
def view_pwe_form(id):

    pwe = PWEForm.query.get_or_404(id)

    return render_template(
        'view_pwe_form.html',
        pwe=pwe
    )

@app.route('/submit-employee', methods=['POST'])
def submit_employee():

    employee = EmployeeForm(

        # SECTION 1

        employee_name=request.form.get('employee_name'),
        employee_id=request.form.get('employee_id'),
        department=request.form.get('department'),
        joining_date=request.form.get('joining_date'),
        duration = (
        request.form.get('duration_years') + " Years " +
        request.form.get('duration_months') + " Months"
        ),
        reporting_manager=request.form.get('reporting_manager'),
        contact_number=request.form.get('contact_number'),
        personal_email=request.form.get('personal_email'),
        communication_address=request.form.get('communication_address'),

        # SECTION 2

        reason=request.form.get('reason'),
        other_reason=request.form.get('other_reason'),
        resignation_submitted_by=request.form.get('resignation_submitted_by'),
        notice_period=request.form.get('notice_period'),

        # SECTION 3

        work_environment=request.form.get('work_environment'),
        team_cooperation=request.form.get('team_cooperation'),
        learning=request.form.get('learning'),
        career=request.form.get('career'),
        manager_support=request.form.get('manager_support'),
        communication=request.form.get('communication'),
        recognition=request.form.get('recognition'),
        compensation=request.form.get('compensation'),
        work_life=request.form.get('work_life'),
        overall=request.form.get('overall'),

        positives=', '.join(request.form.getlist('positives')),
        concerns=', '.join(request.form.getlist('concerns')),
        challenges=request.form.get('challenges'),

        # SECTION 4

        manager_rating=request.form.get('manager_rating'),
        leadership_rating=request.form.get('leadership_rating'),
        feedback_taken=request.form.get('feedback_taken'),
        evaluation_fair=request.form.get('evaluation_fair'),

        managerial_concerns=', '.join(
            request.form.getlist('managerial_concerns')
        ),

        # SECTION 5

        improvements=', '.join(
            request.form.getlist('improvements')
        ),

        additional_suggestions=request.form.get(
            'additional_suggestions'
        ),

        rejoin_organization=request.form.get(
            'rejoin_organization'
        ),

        recommend_organization=request.form.get(
            'recommend_organization'
        ),

        resignation_process=request.form.get(
            'resignation_process'
        ),

        final_comments=request.form.get('final_comments')

    )

    db.session.add(employee)
    db.session.commit()

    return render_template('success.html')

@app.route('/submit-manager', methods=['POST'])
def submit_manager():

    manager = ManagerForm(

        employee_name=request.form.get('employee_name'),
        employee_id=request.form.get('employee_id'),
        department=request.form.get('department'),
        joining_date=request.form.get('joining_date'),
        resignation_date=request.form.get('resignation_date'),

        primary_reason=request.form.get('primary_reason'),
        other_reason=request.form.get('other_reason'),
        retention_attempt=request.form.get('retention_attempt'),
        retention_outcome=request.form.get('retention_outcome'),

        overall_performance=request.form.get('overall_performance'),

        technical_knowledge=request.form.get('technical_knowledge'),
        accuracy_work=request.form.get('accuracy_work'),
        productivity=request.form.get('productivity'),
        communication_skills=request.form.get('communication_skills'),
        team_collaboration=request.form.get('team_collaboration'),
        learning_ability=request.form.get('learning_ability'),
        ownership=request.form.get('ownership'),
        client_handling=request.form.get('client_handling'),
        adaptability=request.form.get('adaptability'),
        process_compliance=request.form.get('process_compliance'),

        strengths=', '.join(
            request.form.getlist('strengths')
        ),

        other_strength=request.form.get('other_strength'),

        improvements=', '.join(
            request.form.getlist('improvements')
        ),

        other_improvement=request.form.get('other_improvement'),

        behaviour=request.form.get('behaviour'),
        attendance=request.form.get('attendance'),
        insurance_knowledge=request.form.get('insurance_knowledge'),

        handover_status=request.form.get('handover_status'),
        knowledge_transfer=request.form.get('knowledge_transfer'),
        pending_task=request.form.get('pending_task'),
        replacement_urgency=request.form.get('replacement_urgency'),

        continue_org=request.form.get('continue_org'),
        improve_performance=request.form.get('improve_performance'),
        self_improvement=request.form.get('self_improvement'),
        feedback_discussion=request.form.get('feedback_discussion'),
        retention_feasible=request.form.get('retention_feasible'),

        rehire=request.form.get('rehire'),

        future_roles=', '.join(
            request.form.getlist('future_roles')
        ),

        overall_remarks=request.form.get('overall_remarks')

    )

    db.session.add(manager)

    employee = EmployeeForm.query.filter_by(
    employee_id=request.form.get('employee_id')
    ).order_by(EmployeeForm.id.desc()).first()

    if employee:
      employee.manager_reviewed = True

    db.session.commit()
    return render_template(
    'success.html',
    dashboard_url=url_for('manager_dashboard')
)

@app.route('/submit-pwe', methods=['POST'])
def submit_pwe():

    pwe = PWEForm(

        employee_name=request.form.get('employee_name'),
        employee_id=request.form.get('employee_id'),
        department=request.form.get('department'),
        joining_date=request.form.get('joining_date'),
        last_working_day=request.form.get('last_working_day'),
        reporting_manager=request.form.get('reporting_manager'),
        contact_number=request.form.get('contact_number'),
        personal_email=request.form.get('personal_email'),
        communication_address=request.form.get('communication_address'),

        exit_discussion_date=request.form.get('exit_discussion_date'),
        separation_reason=request.form.get('separation_reason'),
        other_reason=request.form.get('other_reason'),
        notice_period_served=request.form.get('notice_period_served'),

        recovery_applicable=request.form.get('recovery_applicable'),

        recovery_type=', '.join(
            request.form.getlist('recovery_type')
        ),

        recovery_remarks=request.form.get('recovery_remarks'),

        assets_returned=', '.join(
            request.form.getlist('assets_returned')
        ),

        asset_return_status=request.form.get('asset_return_status'),

        access_deactivation=', '.join(
            request.form.getlist('access_deactivation')
        ),

        access_closure_status=request.form.get('access_closure_status'),

        pending_dues=request.form.get('pending_dues'),

        fnf_initiated=request.form.get('fnf_initiated'),
        fnf_status=request.form.get('fnf_status'),

        exit_documents=', '.join(
            request.form.getlist('exit_documents')
        ),

        documentation_status=request.form.get('documentation_status'),

        rehire_eligibility=request.form.get('rehire_eligibility'),

        rehire_reason=', '.join(
            request.form.getlist('rehire_reason')
        ),

        genuine_resignation=request.form.get('genuine_resignation'),
        emotional_decision=request.form.get('emotional_decision'),
        better_opportunity=request.form.get('better_opportunity'),
        performance_concern=request.form.get('performance_concern'),
        managerial_conflict=request.form.get('managerial_conflict'),
        retention_possible=request.form.get('retention_possible'),
        strong_performer=request.form.get('strong_performer'),
        attendance_concern=request.form.get('attendance_concern'),
        behavioral_concern=request.form.get('behavioral_concern'),
        communication_gap=request.form.get('communication_gap'),
        policy_violation=request.form.get('policy_violation'),

        hr_recommendation=request.form.get('hr_recommendation'),

        final_hr_remarks=request.form.get('final_hr_remarks')
    )

    db.session.add(pwe)

    employee = EmployeeForm.query.filter_by(
    employee_id=request.form.get('employee_id')
    ).order_by(EmployeeForm.id.desc()).first()

    if employee:
     employee.pwe_reviewed = True

    db.session.commit()

    return render_template(
    'success.html',
    dashboard_url=url_for('pwe_dashboard')
)

@app.route('/submit-final-review', methods=['POST'])
def submit_final_review():

    final = FinalReview(

        employee_name=request.form.get('employee_name'),

        employee_id=request.form.get('employee_id'),

        department=request.form.get('department'),

        manager_recommendation=request.form.get(
            'manager_recommendation'
        ),

        hr_recommendation=request.form.get(
            'hr_recommendation'
        ),

        final_status=request.form.get('final_status'),

        top_management_remarks=request.form.get(
            'top_management_remarks'
        )

    )

    db.session.add(final)

    employee = EmployeeForm.query.filter_by(
    employee_id=request.form.get('employee_id')
    ).order_by(EmployeeForm.id.desc()).first()

    if employee:
      employee.top_reviewed = True

    db.session.commit()

    return redirect(url_for('final_reports'))

@app.route('/mis-report')
def mis_report():

    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    employees = EmployeeForm.query.order_by(
        EmployeeForm.id.desc()
    ).all()

    mis_data = []

    for employee in employees:

        pwe = PWEForm.query.filter_by(
            employee_id=employee.employee_id
        ).first()

        last_working_day = (
            pwe.last_working_day
            if pwe else "-"
        )

        if from_date and last_working_day != "-":
         if last_working_day < from_date:
          continue

        if to_date and last_working_day != "-":
         if last_working_day > to_date:
          continue

        mis_data.append({
            "employee": employee,
            "last_working_day": last_working_day
        })

    total_exits = len(mis_data)

    completed = len([
        row for row in mis_data
        if row["employee"].top_reviewed
    ])

    pending = total_exits - completed

    return render_template(
        'mis_report.html',
        mis_data=mis_data,
        total_exits=total_exits,
        completed=completed,
        pending=pending,
        from_date=from_date,
        to_date=to_date
    )

@app.route('/logout')
def logout():

    session.clear()

    return redirect(url_for('login'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':

    app.run(debug=True)