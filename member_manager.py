from config import MEMBER_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_member():
    members = load_data(MEMBER_FILE)

    name = input("Enter member name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name:
        print("Member name is required.")
        return

    member = {
        "id": generate_id(members, "M"),
        "name": name,
        "phone": phone,
        "email": email,
        "active": True
    }

    members.append(member)

    save_data(MEMBER_FILE, members)

    print("\nMember added successfully.")
    print(f"Member ID: {member['id']}")


def view_members():
    members = load_data(MEMBER_FILE)

    if not members:
        print("No members found.")
        return

    print("\n" + "=" * 70)
    print("MEMBER LIST")
    print("=" * 70)

    for member in members:
        status = "Active" if member["active"] else "Inactive"

        print(f"ID     : {member['id']}")
        print(f"Name   : {member['name']}")
        print(f"Phone  : {member['phone']}")
        print(f"Email  : {member['email']}")
        print(f"Status : {status}")
        print("-" * 70)


def search_members():
    members = load_data(MEMBER_FILE)

    keyword = input(
        "Enter member ID, name, phone, or email: "
    ).strip().lower()

    results = [
        member
        for member in members
        if keyword in member["id"].lower()
        or keyword in member["name"].lower()
        or keyword in member["phone"].lower()
        or keyword in member["email"].lower()
    ]

    if not results:
        print("No members found.")
        return

    for member in results:
        print(
            f"{member['id']} | "
            f"{member['name']} | "
            f"{member['phone']} | "
            f"{member['email']}"
        )


def deactivate_member():
    members = load_data(MEMBER_FILE)

    member_id = input("Enter Member ID: ").strip()

    member = find_by_id(members, member_id)

    if not member:
        print("Member not found.")
        return

    member["active"] = False

    save_data(MEMBER_FILE, members)

    print("Member deactivated successfully.")
