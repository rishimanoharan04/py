import numpy as np
import pandas as pd
import collections
import matplotlib.pyplot as plt
from pandas.plotting import table
import dataframe_image as dfi


def project(filename):
    # read in
    df = pd.read_csv(filename)
    df2 = df.fillna(0)
    arr = df2.to_numpy()
    vendors = df2[df2.columns[0:1]].to_numpy()

    df3 = pd.read_csv('C:\\Users\\rishi\\Downloads\\Misc\\term.txt')
    terms = df3.to_numpy()

    # categories
    scheduling = np.array(
        ["Calendly", "Acuity Schedulin", "Wrike", "Depty", "7shifts", "10to8 Limited", "Setmore", "Appointy",
         "Google Calendar", "StormCource LLC", "QuickBooks", "Square Appointments", "Mindbody", "Smartsheet",
         "Google Workspace", "Clockify", "Paycor", "Asana"])
    sales = np.array(
        ["LAMBDA SOLUTIONS", "IRONMARK INC", "INTERCOM INC.", "HUBSPOT, INC.", "DYNADOT", "Creative Minds",
         "CopyTalk, LLC",
         "DOMAINS PRICED RIGHT - 101 domain", "THIRD AND GROVE LLC", "UNBOUNE", "Typeform", "VERIZON", "WISTIA, INC.",
         "VISUAL IMPACT", "ZENDESK", "Best Buy", "B&H Photo", "Salesforce", "Pipedrive", "HubSpot", "Zoho Corporation",
         "Salesloft", "Zendesk", "Freshsales", "Keap",
         "Insightly", "ActiveCampaign", "Nutshell", "PandaDoc", "LinkedIn", "Salesflare Freshworks", "Salesmate CRM",
         "Showpad", "ClearSlide", "Oracle", "MarketXpander Services Private Limited", "VanillaSoft",
         "Microsoft Corporation", "EngageBay Inc", "Beaver Builder"])
    crm = np.array(
        ["KEAP", "ZAPIER", "Pipedrive", "Salesforce", "HubSpot", "ZOHO CORPORATION", "SugarCRM", "Insightly",
         "Nutshell",
         "Capsule", "Really Simple Systems", "Agile CRM Inc.", "NetSuite", "Freshworks", "Creatio",
         "Less Annoying CRM", "American Solutions for Business", "Streak", "Nimble", "Apptivo", "Microsoft Corporation",
         "Agile CRM", "ActiveCampaign",
         "SuiteCRM"])
    project_management = np.array(
        ["LMS IMPLEMENTATION", "ENTERPRISE REPORTING - HOSTING", "ENTERPRISE REPORTING - SUPPORT", "Codekeeper",
         "SURVEY MONKEY", "THE FRANCHISE BUILDERS BRANDS", "Wrike", "Asana", "Trello", "ClickUp", "Microsoft Project",
         "Smartsheet", "Airtable", "Jira", "Zoho Projects",
         "Basecamp", "LiquidPlanner", "Workfront", "Notion", "Task management", "ProofHub", "GanttPRO", "Podio",
         "Freedcamp", "Celoxis Technologies Pvt. Ltd.", "Easy Projects", "Todoist", "Scoro",
         "Hive Design and Build LLC",
         "TeamGantt", "Ariba, Inc."])
    productivity = np.array(
        ["Lucid Software", "LINKEDIN CORPORATION", "Liberated Syndication", "LearnUpon", "KANON SAPP VIRTUAL ASSISTANT",
         "Jelly Comb", "INCITE AUTOMATION LLC", "Hootsuite", "Graphly", "GOTO MEETING", "GoDaddy", "Sonix.Ai",
         "Techsmith",
         "Visme", "VIMEO", "WORKZONE, LLC", "WP Search", "XMIND", "ZOOM INFORMATION, INC.",
         "ZOOM VIDEO COMMUNICATIONS INC.", "Slack", "Articulate Global, Inc.", "Microsoft Teams", "Trello",
         "Bee by Mailup",
         "Flock", "Workplace", "Notion", "Freeware", "Wimi", "Confluence",
         "Microsoft Office", "Google Suite", "Adobe", "Docusign", "Microsoft Teams", "Microsoft Visio", "Zoom",
         "AudioAcrobat"])
    cloud = np.array(
        ["LOGMEIN USA, INC", "Linode.com", "GOOGLE APPS", "GOOGLE MAPS API", "CORNERSTONE OnDEMAND, INC.", "TELESYSTEM",
         "Dropbox", "Amazon", "Microsoft Azure", "Google Cloud", "Google Drive", "Salesforce", "Amazon Web Services",
         "Adobe Creative Cloud", "Adobe Inc." "Google Workspace", "Oracle", "DigitalOcean", "Box", "IBM Cloud",
         "Alibaba Cloud", "Microsoft 365", "HubSpot", "Mailchimp", "Zendesk", "AWS Lambda", "Trello",
         "SlideRocket"])
    accounting = np.array(
        ["IRON MOUNTAIN", "CONCUR TECHNOLOGIES, INC", "VISUAL ROI", "Xero", "Authorize.net", "QuickBooks", "FreshBooks",
         "Wave", "Zoho Corporation", "NetSuite", "Sage Group", "Sage Intacct",
         "Sage 50", "FreeAgent", "GnuCash", "ZipBooks", "Acclivity Group LLC", "Tipalti", "Intuit", "AvidXchange",
         "Tally",
         "Paychex", "Odoo", "Gusto", "Microsoft Dynamics NAV", "ClearBooks", "Melio", "ZarMoney"])
    shipping = np.array(["FEDERAL EXPRESS", "Shopify", "Mimeo", "Fedex", "UPS", "USPS", "ShipBob", "ShipMonk"])
    hr = np.array(
        ["LICENSE MANAGEMENT SOFTWARE", "GROSS, MENDELSOHN & ASSOCIATES", "STERLING INFOSYSTEMS, INC.", "BAMBOO HR",
         "Zenefits", "Namely", "ADP", "Workday", "Paycom", "Gusto", "Paycor", "SAP SuccessFactors", "Rippling",
         "Paylocity", "Applicant tracking system", "Zoho Corporation", "Sage Group", "Ceridian Dayforce Corporation",
         "OrangeHRM", "Deel", "Freshteam", "Deputy", "Cezanne HR Limited", "TriNet", "Cornerstone OnDemand", "15Five",
         "CakeHR"])

    # implementation
    # services
    # support
    # hardware - sever, workstation
    # server - backup, office supplies, security services

    categories_list = ([scheduling, sales, crm, project_management, productivity, cloud, accounting, shipping, hr])

    types = np.array(
        ["scheduling", "sales", "CRM", "project management", "productivity", "cloud", "accounting", "shipping", "hr"])

    scheduling_array = [];
    sales_array = [];
    crm_array = [];
    project_management_array = [];
    productivity_array = [];
    cloud_array = [];
    accounting_array = [];
    shipping_array = [];
    hr_array = [];

    # sum calculator
    for i in range(len(vendors)):
        for j in range(10):
            test_list = arr[i][1:10]
            sum = 0.00
            for k in test_list:
                sum += k
        # print(arr[i][0] + "," + "$" + str(round(sum,2)))

    def categorization_process(category, name, append_array):
        for i in range(vendors.size):
            for j in range(category.size):
                if vendors[i].__contains__(category[j]):
                    append_array.append(vendors[i])
        return (str("$") + str(append_array))

    list_table = pd.DataFrame()
    list_table['Vendors'] = ["Scheduling", "Sales", "CRM", "Project Management", "Productivity", "Cloud", "Accounting",
                             "Shipping", "HR"]
    list_table['Sum'] = [categorization_process(scheduling, "scheduling ", scheduling_array),
                         categorization_process(sales, "sales ", sales_array),
                         categorization_process(crm, "CRM ", crm_array),
                         categorization_process(project_management, "project management ", project_management_array),
                         categorization_process(productivity, "productivity ", productivity_array),
                         categorization_process(cloud, "cloud ", cloud_array),
                         categorization_process(accounting, "accounting ", accounting_array),
                         categorization_process(shipping, "shipping ", shipping_array),
                         categorization_process(hr, "HR ", hr_array)]
    df_styled = list_table.style.background_gradient()  # adding a gradient based on values in cell

    dfi.export(
        df_styled,
        'C:\\Users\\rishi\Documents\\React\\sd\\src\\pages\\PyFiles\\list_table.png',
        table_conversion="matplotlib"
    )

    def categories_sum(array_argument):
        # sum calculator
        temp_categories_array = []
        sum_final_categories_array = []
        for i in range(len(array_argument)):
            itemindex = np.where(vendors == array_argument[i])[0][0]
            for j in range(10):
                test_list = arr[itemindex][1:10]
                sum = 0.00
                for k in test_list:
                    sum += k
            temp_categories_array.append(round(sum, 2))

        result = 0.00

        for q in range(len(temp_categories_array)):
            result = result + temp_categories_array[q]
        sum_final_categories_array.append(result)

        return round(result, 2)

    def singular_breakdown(argument):
        temp_categories_array = []
        sum_final_categories_array = []
        for i in range(len(argument)):
            itemindex = np.where(vendors == argument[i])[0][0]
            for j in range(10):
                test_list = arr[itemindex][1:10]
                sum = 0.00
                for k in test_list:
                    sum += k
            temp_categories_array.append(round(sum, 2))

        for q in range(len(temp_categories_array)):
            print(*argument[q] + "," + "$" + str(temp_categories_array[q]))

    category_table = pd.DataFrame()
    category_table['Vendors'] = ["Scheduling", "Sales", "CRM", "Project Management", "Productivity", "Cloud",
                                 "Accounting",
                                 "Shipping", "HR"]
    category_table['Sum'] = [categories_sum(scheduling_array), categories_sum(sales_array), categories_sum(crm_array),
                             categories_sum(project_management_array), categories_sum(productivity_array),
                             categories_sum(cloud_array), categories_sum(accounting_array),
                             categories_sum(shipping_array),
                             categories_sum(hr_array)]
    df_styled1 = category_table.style.background_gradient()  # adding a gradient based on values in cell
    dfi.export(
        df_styled1,
        'C:\\Users\\rishi\Documents\\React\\sd\\src\\pages\\PyFiles\\category_table.png',
        table_conversion="matplotlib"
    )

    def sum_sort(argument):
        temp_categories_array = []
        sum_final_categories_array = []
        for i in range(len(argument)):
            itemindex = np.where(vendors == argument[i])[0][0]
            for j in range(10):
                test_list = arr[itemindex][1:10]
                sum = 0.00
                for k in test_list:
                    sum += k
                temp_categories_array.append(round(sum, 2))
        index = np.argmin(temp_categories_array)

        return ((temp_categories_array[index]))

    def vendors_sort(argument):
        temp_categories_array = []
        sum_final_categories_array = []
        for i in range(len(argument)):
            itemindex = np.where(vendors == argument[i])[0][0]
            for j in range(10):
                test_list = arr[itemindex][1:10]
                sum = 0.00
                for k in test_list:
                    sum += k
            temp_categories_array.append(round(sum, 2))
        index = np.argmin(temp_categories_array)

        return (argument[index])

    pie_array = np.array([categories_sum(sales_array), categories_sum(scheduling_array), categories_sum(crm_array),
                          categories_sum(project_management_array), categories_sum(productivity_array),
                          categories_sum(cloud_array), categories_sum(accounting_array), categories_sum(shipping_array),
                          categories_sum(hr_array)])
    mylables = ["Sales", "Scheduling", "CRM", "Project Management", "Productivity", "Cloud", "Accounting", "Shipping",
                "HR"]
    myexplode = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]
    plt.pie(pie_array, labels=mylables, startangle=90, autopct='%1.2f%%', radius=1)
    plt.savefig("C:\\Users\\rishi\Documents\\React\\sd\\src\\pages\\PyFiles\\plot.png", bbox_inches='tight')
    plt.show()

    final_table = pd.DataFrame()
    final_table['Vendors'] = [*vendors_sort(sales_array), *vendors_sort(crm_array),
                              *vendors_sort(project_management_array),
                              *vendors_sort(productivity_array), *vendors_sort(cloud_array),
                              *vendors_sort(accounting_array), *vendors_sort(shipping_array), *vendors_sort(hr_array)]
    final_table['Sum'] = [sum_sort(sales_array), sum_sort(crm_array), sum_sort(project_management_array),
                          sum_sort(productivity_array), sum_sort(cloud_array), sum_sort(accounting_array),
                          sum_sort(shipping_array), sum_sort(hr_array)]
    df_styled2 = final_table.style.background_gradient()  # adding a gradient based on values in cell
    dfi.export(
        df_styled2,
        'C:\\Users\\rishi\Documents\\React\\sd\\src\\pages\\PyFiles\\final_table.png',
        table_conversion="matplotlib"
    )

    def terms_calc(argument):
        sum = 0.00
        for i in range(len(terms)):
            if terms[i] == 'Y':
                sum = sum_sort(argument)
            elif terms[i] == 'M':
                sum = (sum_sort(argument) * (9.0)) / 12.0
            elif terms[i] == 'A':
                sum = sum_sort(argument)
            elif terms[i] == 'B':
                sum = sum_sort(argument) * 2.0
        return sum

    forecast_table = pd.DataFrame()
    forecast_table['Vendors'] = [*vendors_sort(sales_array), *vendors_sort(crm_array),
                                 *vendors_sort(project_management_array), *vendors_sort(productivity_array),
                                 *vendors_sort(cloud_array), *vendors_sort(accounting_array),
                                 *vendors_sort(shipping_array),
                                 *vendors_sort(hr_array)]
    forecast_table['Forecast'] = [terms_calc(sales_array), terms_calc(crm_array), terms_calc(project_management_array),
                                  terms_calc(productivity_array), terms_calc(cloud_array), terms_calc(accounting_array),
                                  terms_calc(shipping_array), terms_calc(hr_array)]
    df_styled3 = forecast_table.style.background_gradient()  # adding a gradient based on values in cell
    dfi.export(
        df_styled1,
        'C:\\Users\\rishi\Documents\\React\\sd\\src\\pages\\PyFiles\\forecast_table.png',
        table_conversion="matplotlib"
    )


project('C:\\Users\\rishi\\Downloads\\Misc\\final.csv')
