'''
Andrew Cunningham
CSC505 - Critical Thinking Assignment 2

Implements the Cunningham waterfall model for Andrew's career transition out of the Navy in 2026
See associated word document for further discussion
'''

def display_menu():
    '''terminal outputs the menu of character inputs'''
    print("Cunningham Model:")
    print("1. Communication and Requirements")
    print("2. Design and Planning")
    print("3. Implementation")
    print("4. Testing")
    print("5. Deployment")
    print("6. Quit")
    print()

def terminal_input():
    '''Very simple terminal handler that loops until "q" is sent to terminate the program'''
    display_menu()

    while True:
        entry = input("Enter code: ").strip()

        print()

        if entry == "1":
            display_reqs()
        elif entry == "2":
            display_planning()
        elif entry == "3":
            display_implementation()
        elif entry == "4":
            display_testing()
        elif entry == "5":
            display_deployment()
        elif entry == "6":
            break
        else:
            print("Invalid Entry, please try again")

def display_reqs():
    '''terminal outputs communicaton and requirements'''
    print("---")
    print("Communication and Requirements")
    print("---")
    print("Overall objective:")
    print("- Successfully transition out of the Navy and establish life in Colorado Springs, CO")
    print()

    print("Education requirements:")
    print("- Complete master's degree in AI and ML")
    print()

    print("Timing requirements:")
    print("- Complete '25-'26 school year in Washington")
    print("- Settle in new house before the 2026 school year")
    print("- Collect first paycheck before first mortgage is due")
    print()

    print("Job requirements:")
    print("- Lead a small team of engineers developing cutting edge technology that benefits mankind")
    print("- Get hired as a software developer near Colorado Springs, CO")
    print()

    print("Housing requirements:")
    print("- Short commute to work")
    print("- Short distance from family")
    print("- Short distance to kids' schools")
    print("- Fenced in yard for the dogs")
    print("- Sun-lit backyard for Melinda's gardening")
    print()
    

def display_planning():
    '''terminal outputs design and planning'''
    print("---")
    print("Design and Planning")
    print("---")
    print("Education:")
    print("- Complete online MS in AI and ML by March, 2026")
    print("- Complete several side projects to showcase software development experience")
    print()

    print("Job Hunt:")
    print("- Begin networking in winter, 2025")
    print("- Aggressively apply for jobs starting March, 2026")
    print()

    print("House hunting:")
    print("- Survey potential neighborhoods")
    print("- Briarsgate area")
    print("- South-facing house")
    print("- 4 bedroom 3 bathroom houses for rent")
    print()

def display_implementation():
    '''terminal outputs implemenation'''
    print("---")
    print("Implementation:")
    print("---")
    print("Education:")
    print("- Began degree online in Winter 2024")
    print("- Developed degree completion plan for March 2026")
    print("- Additional coding projects starting once per month in Winter, 2024")
    print()

    print("Job Hunting:")
    print("- Update LinkedIn: 2025")
    print("- Assemble a list of potential jobs: Summer 2025")
    print("- Tailor skill development plan to meet most requirements: Summer 2025")
    print("- Network on LinkedIn and other sources: Spring 2026")
    print("- Apply for work starting Spring 2026")
    print()

    print("House Hunting:")
    print("- Travel to CO to survey neighborhoods: Winter 2024")
    print("- Create Zillow search: Winter 2024")
    print("- Review matches consistently and update requirements monthly")
    print("- Apply for leases: Spring 2026")
    print()

def display_testing():
    '''terminal outputs testing'''
    print("---")
    print("Testing:")
    print("---")
    print("Education:")
    print("- Review job postings to ensure skills plan aligns with industry trends")
    print("- Modify project plan to account for changing requirements")
    print()

    print("Job Hunting:")
    print("- Incorporate feedback into job search plan")
    print()

    print("House Hunting:")
    print("- Check new postings monthly to catch trends in variables")
    print()

def display_deployment():
    '''terminal outputs deployment'''
    print("---")
    print("Deployment:")
    print("---")
    print("Job Goals:")
    print("- Lead a small team of engineers")
    print("- Develop cutting edge AI models that solve real-world problems")
    print()

    print("House Goals:")
    print("- Home Office")
    print("- Desirable location")
    print("- Happy wife")
    print()

    print("Financial Goals:")
    print("- No debt")
    print()

    print("Timing Goals:")
    print("- Settled before the start of the 2026-2027 school year")
    print()


if __name__ == "__main__":
    terminal_input()