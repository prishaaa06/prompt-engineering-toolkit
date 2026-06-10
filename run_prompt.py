"""
Prompt Engineering Toolkit
---------------------------
A reusable library of marketing & content prompts with an interactive runner.
Author: Prisha Maheshwari
"""

import json
import os
import datetime
from prompts import PROMPT_LIBRARY


def display_banner():
    print("\n" + "=" * 55)
    print("   🧠  Prompt Engineering Toolkit  by Prisha M.")
    print("=" * 55)


def list_categories(library: dict) -> list:
    categories = sorted(set(p["category"] for p in library.values()))
    print("\n📂 Available Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"   {i}. {cat}")
    return categories


def list_prompts_by_category(library: dict, category: str) -> list:
    matches = [(key, p) for key, p in library.items() if p["category"] == category]
    print(f"\n📝 Prompts in '{category}':")
    for i, (key, p) in enumerate(matches, 1):
        print(f"   {i}. [{key}] {p['name']}")
        print(f"        → {p['description']}")
    return matches


def fill_prompt(template: str, variables: list) -> str:
    filled = template
    print("\n✏️  Fill in the variables:")
    values = {}
    for var in variables:
        value = input(f"   {var}: ").strip()
        values[var] = value
        filled = filled.replace(f"{{{var}}}", value)
    return filled, values


def save_output(prompt_name: str, filled_prompt: str, values: dict):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/{prompt_name.lower().replace(' ', '_')}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Prompt: {prompt_name}\n")
        f.write(f"Generated: {timestamp}\n")
        f.write(f"Variables used: {json.dumps(values, indent=2)}\n")
        f.write("\n--- FILLED PROMPT ---\n\n")
        f.write(filled_prompt)
    print(f"\n💾 Saved to: {filename}")


def run():
    display_banner()

    while True:
        categories = list_categories(PROMPT_LIBRARY)
        print("\n   [q] Quit")

        choice = input("\n👉 Select a category number: ").strip().lower()
        if choice == "q":
            print("\n👋 Bye! Happy prompting.\n")
            break

        try:
            cat_index = int(choice) - 1
            selected_category = categories[cat_index]
        except (ValueError, IndexError):
            print("❌ Invalid choice. Try again.")
            continue

        prompts_in_cat = list_prompts_by_category(PROMPT_LIBRARY, selected_category)
        print("\n   [b] Back")
        prompt_choice = input("\n👉 Select a prompt number: ").strip().lower()

        if prompt_choice == "b":
            continue

        try:
            p_index = int(prompt_choice) - 1
            key, prompt_data = prompts_in_cat[p_index]
        except (ValueError, IndexError):
            print("❌ Invalid choice.")
            continue

        print(f"\n📌 Selected: {prompt_data['name']}")
        print(f"   {prompt_data['description']}\n")
        print("--- Template Preview ---")
        print(prompt_data["template"])
        print("------------------------")

        filled, values = fill_prompt(prompt_data["template"], prompt_data["variables"])

        print("\n✅ Your filled prompt:\n")
        print("━" * 55)
        print(filled)
        print("━" * 55)

        save = input("\n💾 Save this prompt? (y/n): ").strip().lower()
        if save == "y":
            save_output(prompt_data["name"], filled, values)

        again = input("\n🔁 Use another prompt? (y/n): ").strip().lower()
        if again != "y":
            print("\n👋 Bye! Happy prompting.\n")
            break


if __name__ == "__main__":
    run()
