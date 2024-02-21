frappe.views.calendar["Tasks"] = {
    field_map: {
      "start": "start_date",
      "end": "end_date",
      "id": "task_name",
    },
    gantt: true,
    filters: [
		{
			"fieldtype": "Link",
			"fieldname": "employee",
			"options": "Employee",
			"label": __("الموظف"),
		}
	],
	get_events_method: "frappe.desk.calendar.get_events"
  };
  