import os


def generate_invitations(template, attendees):

    if not isinstance(template, str) or not isinstance(attendees, list):
        raise TypeError()

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        for key, value in attendee.items():
            if value is None:
                attendee[key] = "N/A"

        letter = (
            template.replace("{name}", attendee.get("name", "N/A"))
            .replace("{event_title}", attendee.get("event_title", "N/A"))
            .replace("{event_date}", attendee.get("event_date", "N/A"))
            .replace("{event_location}", attendee.get("event_location", "N/A"))
        )
        
        print(letter)
        with open(f"output_{i}.txt", "w", encoding="utf-8") as file:
            file.write(letter)
