 # Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Welcome message
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Create a dictionary of service categories and hourly rates
# Store in variable: services
services = {
    "Web Development": 150,
    "Mobile App Development": 180,
    "Cybersecurity": 220,
    "Cloud Consulting": 200,
    "Technical Support": 95
}

# TODO 2: Create customer dictionaries
# Each customer should have: company_name, contact_person, email, phone
customer1 = {
    "company_name": "ABC Corp",
    "contact_person": "John Smith",
    "email": "john@abccorp.com",
    "phone": "222-1234"
}

customer2 = {
    "company_name": "iCloud Solutions",
    "contact_person": "Sarah White",
    "email": "sarah@icloudsolutions.com",
    "phone": "222-2345"
}

customer3 = {
    "company_name": "Silver Systems",
    "contact_person": "Michael Walker",
    "email": "michael@silversystems.com",
    "phone": "222-3456"
}

customer4 = {
    "company_name": "NorthStar Enterprises",
    "contact_person": "Emily Carter",
    "email": "emily@northstarenterprises.com",
    "phone": "222-4567"
}

# TODO 3: Create a master customers dictionary
# Store in variable: customers
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)
for cust_id, info in customers.items():
    print(f"{cust_id}: {info}")

# TODO 5: Look up specific customers
# - Get and display customer C002's information (store in c002_info)
# - Get and display customer C003's contact person (store in c003_contact)
# - Try to get customer C999 (doesn't exist) using .get() with a default message (store in c999_info)

print("\n\nCustomer Lookups:")
print("-" * 60)

c002_info = customers["C002"]
c003_contact = customers["C003"]["contact_person"]
c999_info = customers.get("C999", "Customer not found")

print("C002 info:", c002_info)
print("C003 contact person:", c003_contact)
print("C999 lookup:", c999_info)

# TODO 6: Update customer information
# - Change customer C001's phone number
# - Add a new field "industry" to customer C002
# - Display the updated customer information

print("\n\nUpdating Customer Information:")
print("-" * 60)

customers["C001"]["phone"] = "555-9999"
customers["C002"]["industry"] = "Technology"

print("Updated C001:", customers["C001"])
print("Updated C002:", customers["C002"])

# TODO 7: Create project dictionaries for each customer
# Each project: {"name": "Project Name", "service": "Service Type", "hours": X, "budget": Y}

project1 = {
    "name": "Corporate Website Redesign",
    "service": "Web Development",
    "hours": 80,
    "budget": 12000,
    "status": "completed"
}

project2 = {
    "name": "Network Security Assessment",
    "service": "Cybersecurity",
    "hours": 40,
    "budget": 8800,
    "status": "active"
}

project3 = {
    "name": "Cloud Setup",
    "service": "Cloud Consulting",
    "hours": 60,
    "budget": 12000,
    "status": "pending"
}

project4 = {
    "name": "Help Desk Setup",
    "service": "Technical Support",
    "hours": 50,
    "budget": 4750,
    "status": "completed"
}

project5 = {
    "name": "Customer Mobiel App Development",
    "service": "Mobile App Development",
    "hours": 70,
    "budget": 12600,
    "status": "active"
}

project6 = {
    "name": "Cloud Migration",
    "service": "Cloud Consulting",
    "hours": 75,
    "budget": 15000,
    "status": "pending"
}

# Create a projects dictionary where customer IDs map to lists of projects
# Store in variable: projects
projects = {
    "C001": [project1, project2],
    "C002": [project3],
    "C003": [project4, project5],
    "C004": [project6]
}

print("\n\nProject Information:")
print("-" * 60)
for cust_id, proj_list in projects.items():
    print(f"{cust_id}:")
    for project in proj_list:
        print(" ", project)

# TODO 8: Calculate project costs
# For each project, calculate: cost = hourly_rate * hours
# Display each project with its calculated cost

print("\n\nProject Cost Calculations:")
print("-" * 60)

for cust_id, proj_list in projects.items():
    for project in proj_list:
        hourly_rate = services[project["service"]]
        cost = hourly_rate * project["hours"]
        print(f"{cust_id} - {project['name']} ({project['service']}): ${cost}")

# TODO 9: Customer statistics using dictionary methods
# Display:
# - All customer IDs using .keys()
# - All customer companies using .values() and extracting company names
# - Count of total customers using len()

print("\n\nCustomer Statistics:")
print("-" * 60)

print("Customer IDs:", list(customers.keys()))
company_names = [info["company_name"] for info in customers.values()]
print("Company names:", company_names)
print("Total customers:", len(customers))

# TODO 10: Service usage analysis
# Create a dictionary that counts how many projects use each service
# Store in variable: service_counts

print("\n\nService Usage Analysis:")
print("-" * 60)

service_counts = {}

for proj_list in projects.values():
    for project in proj_list:
        service = project["service"]
        service_counts[service] = service_counts.get(service, 0) + 1

print("Service usage counts:", service_counts)

# TODO 11: Financial aggregations
# Calculate and display:
# - Total hours across all projects (store in total_hours)
# - Total budget across all projects (store in total_budget)
# - Average project budget (store in avg_budget)
# - Most expensive and least expensive projects (store in max_budget, min_budget)

print("\n\nFinancial Summary:")
print("-" * 60)

all_projects = []

for project_list in projects.values():
    for project in project_list:
        all_projects.append(project)
        
total_hours = sum(p["hours"] for p in all_projects)
total_budget = sum(p["budget"] for p in all_projects)

avg_budget = total_budget / len(all_projects)

min_budget = min(p["budget"] for p in all_projects)
max_budget = max(p["budget"] for p in all_projects)

print("Total hours:", total_hours)
print("Total budget:", total_budget)
print("Average project budget:", avg_budget)
print("Most expensive project:", max_budget)
print("Least expensive project:", min_budget)

# TODO 12: Customer summary report
# For each customer, show:
# - Customer details
# - Number of projects
# - Total hours
# - Total budget

print("\n\nCustomer Summary Report:")
print("-" * 60)

for cust_id, cust_info in customers.items():
    customer_projects = projects.get(cust_id, [])
    num_projects = len(customer_projects)
    cust_total_hours = sum(project["hours"] for project in customer_projects)
    cust_total_budget = sum(project["budget"] for project in customer_projects)

    print(f"\nCustomer ID: {cust_id}")
    print(f"Details: {cust_info}")
    print(f"Number of projects: {num_projects}")
    print(f"Total hours: {cust_total_hours}")
    print(f"Total budget: ${cust_total_budget}")

# TODO 13: Create rate adjustments using dictionary comprehension
# Create a new dictionary with all service rates increased by 10%
# Store in variable: adjusted_rates

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)

adjusted_rates = {service: rate * 1.1 for service, rate in services.items()}
print(adjusted_rates)

# TODO 14: Filter customers using dictionary comprehension
# Create a dictionary of only customers who have projects
# Store in variable: active_customers

print("\n\nActive Customers (with projects):")
print("-" * 60)

active_customers = {cust_id: info for cust_id, info in customers.items() if cust_id in projects and len(projects[cust_id]) > 0}
print(active_customers)

# TODO 15: Create project summaries using dictionary comprehension
# Create a dictionary mapping customer IDs to their total project budgets
# Store in variable: customer_budgets

print("\n\nCustomer Budget Totals:")
print("-" * 60)

customer_budgets = {
    cust_id: sum(project["budget"] for project in proj_list)
    for cust_id, proj_list in projects.items()
}
print(customer_budgets)

# TODO 16: Service pricing tiers using dictionary comprehension
# Create a dictionary categorizing services as "Premium" (>= 200), "Standard" (100-199), or "Basic" (< 100)
# Store in variable: service_tiers

print("\n\nService Pricing Tiers:")
print("-" * 60)

service_tiers = {
    service: ("Premium" if rate >= 200 else "Standard" if rate >= 100 else "Basic")
    for service, rate in services.items()
}
print(service_tiers)

# TODO 17: Customer validation function
# Create a function validate_customer(customer_dict) that:
# - Checks if all required fields are present (company_name, contact_person, email, phone)
# - Returns True if valid, False otherwise

def validate_customer(customer_dict):
    required_fields = ["company_name", "contact_person", "email", "phone"]
    for field in required_fields:
        if field not in customer_dict:
            return False
    return True

print("\n\nCustomer Validation:")
print("-" * 60)

for cust_id, info in customers.items():
    print(f"{cust_id}: {validate_customer(info)}")

# TODO 18: Project status tracking with loops and conditionals
# Add a "status" field to each project ("active", "completed", "pending")
# Use a loop to count projects by status
# Store counts in status_counts dictionary

for project in projects["C001"]:
    if project["name"] == "Website Redesign":
        project["status"] = "active"
    else:
        project["status"] = "completed"

for project in projects["C002"]:
    project["status"] = "pending"

for project in projects["C003"]:
    if project["name"] == "Cloud Migration":
        project["status"] = "active"
    else:
        project["status"] = "completed"

for project in projects["C004"]:
    project["status"] = "pending"

print("\n\nProject Status Summary:")
print("-" * 60)

status_counts = {
    "active": 0,
    "completed": 0,
    "pending": 0
}

for project_list in projects.values():
    for project in project_list:
        status = project["status"]
        status_counts[status] += 1

print(status_counts)

# TODO 19: Budget analysis function with aggregation
# Create a function analyze_customer_budgets(projects_dict) that:
# - Takes the projects dictionary as input
# - Uses loops to calculate total and average budget per customer
# - Returns a dictionary with customer IDs as keys and budget stats as values
# - Each value should be a dict with 'total', 'average', and 'count' keys

def analyze_customer_budgets(projects_dict):
    budget_stats = {}

    for cust_id, proj_list in projects_dict.items():
        total = sum(project["budget"] for project in proj_list)
        count = len(proj_list)
        average = total / count if count > 0 else 0

        budget_stats[cust_id] = {
            "total": total,
            "average": average,
            "count": count
        }

    return budget_stats

print("\n\nDetailed Budget Analysis:")
print("-" * 60)

budget_analysis = analyze_customer_budgets(projects)
print(budget_analysis)

# TODO 20: Service recommendation system
# Create a function recommend_services(customer_id, customers, projects, services) that:
# - Analyzes the customer's past projects
# - Identifies services they haven't used yet
# - Returns a list of recommended services based on their budget range

def recommend_services(customer_id, customers, projects, services):
    used_services = {project["service"] for project in projects.get(customer_id, [])}
    customer_projects = projects.get(customer_id, [])

    if customer_projects:
        avg_budget = sum(project["budget"] for project in customer_projects) / len(customer_projects)
    else:
        avg_budget = 0

    recommendations = []

    for service, rate in services.items():
        if service not in used_services:
            # Recommend based on budget range
            if avg_budget >= 12000 and rate >= 150:
                recommendations.append(service)
            elif avg_budget < 12000 and rate < 200:
                recommendations.append(service)

    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)

for cust_id in customers.keys():
    recommendations = recommend_services(cust_id, customers, projects, services)
    print(f"{cust_id}: {recommendations}")