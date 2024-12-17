# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Payroll',
    'category': 'Human Resources/Payroll',
    'sequence': 290,
    'summary': 'Manage your employee payroll records',
    'installable': True,
    'application': True,
    'depends': [
        'hr_work_entry_contract_enterprise',
        'mail',
        'web_editor',
    ],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'wizard/hr_payroll_index_wizard_views.xml',
        'wizard/hr_payroll_edit_payslip_lines_wizard_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_payroll_structure_views.xml',
        'views/hr_payroll_structure_type_views.xml',
        'views/hr_salary_rule_category_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_line_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_payslip_run_views.xml',
        'views/hr_payslip_input_type_views.xml',
        'views/hr_salary_attachment_views.xml',
        'views/hr_employee_views.xml',
        'views/res_users_views.xml',
        'views/hr_payroll_employee_declaration_views.xml',
        'data/hr_payroll_dashboard_warning_data.xml',
        'data/hr_payroll_sequence.xml',
        'data/report_paperformat_data.xml',
        'views/hr_payroll_report.xml',
        'data/hr_payroll_data.xml',
        'data/mail_activity_type_data.xml',
        'data/mail_template_data.xml',
        'data/ir_cron_data.xml',
        'data/ir_actions_server_data.xml',
        'data/note_data.xml',
        'data/hr_payroll_tour.xml',
        'views/res_config_settings_views.xml',
        'views/report_contributionregister_templates.xml',
        'views/report_payslip_templates.xml',
        'views/report_light_payslip_templates.xml',
        'views/hr_work_entry_type_views.xml',
        'views/resource_calendar_views.xml',
        'views/hr_rule_parameter_views.xml',
        'views/hr_payroll_report_views.xml',
        'views/hr_work_entry_report_views.xml',
        'views/hr_payroll_dashboard_views.xml',
        'views/hr_payroll_dashboard_warning_views.xml',
        'views/hr_payroll_headcount_views.xml',
        'views/hr_payroll_menu.xml',
        'views/hr_work_entry_export_mixin_views.xml',
        'report/hr_contract_history_report_views.xml',
        'wizard/hr_payroll_payment_report_wizard.xml',
    ],
    'demo': ['data/hr_payroll_demo.xml'],
    'assets': {
        'web.assets_backend': [
            'hr_payroll/static/src/**/*',
            ('remove', 'hr_payroll/static/src/js/hr_payroll_report_graph_view.js'),
            ('remove', 'hr_payroll/static/src/js/hr_payroll_report_pivot_*'),
            ('remove', 'hr_payroll/static/src/js/hr_work_entries_gantt.*'),
        ],
        'web.assets_backend_lazy': [
            'hr_payroll/static/src/js/hr_payroll_report_graph_view.js',
            'hr_payroll/static/src/js/hr_payroll_report_pivot_*',
            'hr_payroll/static/src/js/hr_work_entries_gantt.*',
        ],
        'web.assets_tests': [
            'hr_payroll/static/tests/**/*.js',
        ],
    },
    'license': 'OEEL-1',
    'post_init_hook': '_post_init_hook',
}
