# Digital Book Archive

# Initial book records
catalog = [
    {
        "title": "Java Fundamentals",
        "author": "Robert Taylor",
        "year": 2020,
        "category": "Software Development"
    },
    {
        "title": "Machine Learning Guide",
        "author": "Emma Davis",
        "year": 2023,
        "category": "Artificial Intelligence"
    },
    {
        "title": "Network Architecture",
        "author": "Michael Clark",
        "year": 2019,
        "category": "Networking"
    },
    {
        "title": "Database Management",
        "author": "Sarah Miller",
        "year": 2024,
        "category": "Databases"
    }
]

# Reader wishlist
reader_wishlist = set()

# Display menu
def show_menu():
    print("\nSelect an action:")
    print("1. View Archived Books")
    print("2. Add New Book Entry")
    print("3. View Unique Archive Categories")
    print("4. Add Category to Reader Wishlist")
    print("5. Run Topic Gap Analysis")
    print("6. Exit")


# Option 1: View books
def show_books():
    print("\n=== ARCHIVED BOOKS ===")

    if not catalog:
        print("No books found.")
        return

    for idx, entry in enumerate(catalog, start=1):
        print(f"\nEntry {idx}")
        print("Title:", entry["title"])
        print("Author:", entry["author"])
        print("Year:", entry["year"])
        print("Category:", entry["category"])

    print("\nTotal entries:", len(catalog))


# Option 2: Add a new book
def insert_book():
    print("\n=== ADD NEW ENTRY ===")

    book_title = input("Enter book title: ").strip()
    book_author = input("Enter author name: ").strip()

    try:
        pub_year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid year. Please enter a number.")
        return

    book_category = input("Enter book category: ").strip()

    if not book_title or not book_author or not book_category:
        print("All fields are required.")
        return

    new_entry = {
        "title": book_title,
        "author": book_author,
        "year": pub_year,
        "category": book_category
    }

    catalog.append(new_entry)
    print(f'Success! "{book_title}" added to the archive.')


# Option 3: View unique categories
def show_categories():
    unique_topics = {entry["category"] for entry in catalog}

    print("\n=== UNIQUE ARCHIVE CATEGORIES ===")

    for topic in sorted(unique_topics):
        print("-", topic)

    print("Total unique categories:", len(unique_topics))


# Option 4: Add category to wishlist
def add_wishlist_topic():
    print("\n=== ADD TO READER WISHLIST ===")

    topic = input("Enter requested category: ").strip()

    if not topic:
        print("Category cannot be empty.")
        return

    reader_wishlist.add(topic)
    print(f'Success! "{topic}" added to reader wishlist.')


# Option 5: Category gap analysis
def run_gap_analysis():
    archive_topics = {
        entry["category"] for entry in catalog
    }

    print("\n" + "=" * 18 + " TOPIC GAP ANALYSIS " + "=" * 18)

    print("\nArchive Holdings (Set):")
    print(archive_topics)

    print("\nReader Wishlist (Set):")
    print(reader_wishlist)

    # Categories available in both
    common_topics = archive_topics & reader_wishlist

    # Categories readers want but archive lacks
    missing_topics = reader_wishlist - archive_topics

    # All categories combined
    all_topics = archive_topics | reader_wishlist

    print("\n1. Already in Archive (Intersection):")
    print(common_topics if common_topics else "None")

    print("\n2. Acquisition Needed (Difference):")
    print(missing_topics if missing_topics else "None")

    print("\n3. Full Combined Topic Coverage (Union):")
    print(all_topics)

    print("\n" + "=" * 56)


# Main program loop
while True:
    show_menu()

    option = input("Enter your choice (1-6): ").strip()

    if option == "1":
        show_books()

    elif option == "2":
        insert_book()

    elif option == "3":
        show_categories()

    elif option == "4":
        add_wishlist_topic()

    elif option == "5":
        run_gap_analysis()

    elif option == "6":
        print("Thank you for using Digital Book Archive!")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
